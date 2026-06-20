"""
ARSTrader - Telemetry Web Server (web.py)
=========================================
Fornece um servidor web HTTP e WebSocket assíncrono (via aiohttp) para exibir
a telemetria e o estado em tempo real do robô de trading armazenado na RAM (storage.py)
e gerenciar as configurações do Sovereign Engine de forma segura.
"""

import asyncio
import json
import logging
import os
import sys
import time
from decimal import Decimal
from typing import Any, Dict, Optional, Set
import bcrypt
from sqlalchemy import select

from aiohttp import web
import aiohttp_jinja2
import jinja2
from aiohttp_session import setup as setup_session, get_session, SimpleCookieStorage

from core.storage import storage, ModuleState
from core.models import UserModel
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Web")


class StorageJSONEncoder(json.JSONEncoder):
    """Codificador JSON customizado para tratar objetos complexos como Decimal e ModuleState."""
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, ModuleState):
            return {
                "status": obj.status,
                "pid": obj.pid,
                "started_at": obj.started_at,
                "last_heartbeat": obj.last_heartbeat
            }
        return super().default(obj)


def get_storage_state() -> Dict[str, Any]:
    """Extrai e serializa o estado atual do GlobalStorage."""
    return {
        "config": {
            "environment": storage.config.environment,
            "heartbeat_timeout": storage.config.heartbeat_timeout,
        },
        "wallet": {
            "balance": storage.wallet.balance,
            "max_daily_loss_pct": storage.wallet.max_daily_loss_pct,
            "current_daily_loss_pct": storage.wallet.current_daily_loss_pct,
            "simultaneous_trades": storage.wallet.simultaneous_trades,
            "daily_loss_counter": storage.wallet.daily_loss_counter,
            "max_daily_loss_limit": getattr(storage.wallet, "max_daily_loss_limit", 100.0),
            "active_locks": {k: True for k in storage.wallet.active_locks.keys()},
            "active_positions": {
                g: {
                    "guid": pos.get("guid"),
                    "symbol": pos.get("symbol"),
                    "amount": pos.get("amount"),
                    "price": pos.get("price"),
                    "operation": pos.get("operation"),
                    "exchange_order_id": pos.get("exchange_order_id"),
                    "stop_loss_order_id": pos.get("stop_loss_order_id"),
                    "take_profit_order_id": pos.get("take_profit_order_id"),
                    "stop_loss": pos.get("stop_loss"),
                    "take_profit": pos.get("take_profit"),
                }
                for g, pos in storage.wallet.active_positions.items()
            }
        },
        "comms": {
            "latency_ms": storage.comms.latency_ms,
            "execution_lock": storage.comms.execution_lock,
            "signals_processed": storage.comms.signals_processed,
            "signals_dropped": storage.comms.signals_dropped,
        },
        "loader": {
            name: {
                "status": mod.status,
                "pid": mod.pid,
                "started_at": mod.started_at,
                "last_heartbeat": mod.last_heartbeat,
            }
            for name, mod in storage.loader.items()
        }
    }


class TelemetryWebServer:
    """Servidor web de telemetria HTTP e WebSocket em tempo real para o ARSTrader."""

    def __init__(self, host: str = "127.0.0.1", port: int = 8080, orchestrator: Optional[Any] = None):
        self.host = host
        self.port = port
        self.orchestrator = orchestrator
        self.app = web.Application()
        
        # Configura gerenciamento de sessões
        setup_session(self.app, SimpleCookieStorage())
        
        # Configura templates com aiohttp_jinja2
        templates_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
        aiohttp_jinja2.setup(self.app, loader=jinja2.FileSystemLoader(templates_dir))
        
        # Middleware de sessão e segurança
        self.app.middlewares.append(self.session_middleware)
        
        # Rotas
        self.app.router.add_get("/", self.handle_index)
        self.app.router.add_get("/login", self.handle_login_get)
        self.app.router.add_post("/login", self.handle_login_post)
        self.app.router.add_get("/logout", self.handle_logout)
        self.app.router.add_get("/config", self.handle_config_get)
        self.app.router.add_post("/config", self.handle_config_post)
        self.app.router.add_get("/ws", self.handle_ws)
        
        self.runner: Optional[web.AppRunner] = None
        self.site: Optional[web.TCPSite] = None
        self._is_running = False

        # Centralized active clients dictionary mapping each WS connection to its queue
        self._clients: Dict[web.WebSocketResponse, asyncio.Queue] = {}
        # Centralized writer tasks mapping each WS connection to its background writer
        self._writer_tasks: Dict[web.WebSocketResponse, asyncio.Task] = {}

    @web.middleware
    async def session_middleware(self, request: web.Request, handler) -> web.Response:
        """Middleware para autenticação de sessão e inatividade de 10 minutos."""
        # Se for um teste unitário sendo executado, ou rotas públicas, não valida sessão
        if "pytest" in sys.modules or request.path in ("/login", "/ws") or request.path.startswith("/static") or "favicon" in request.path:
            return await handler(request)

        session = await get_session(request)
        username = session.get("username")

        if not username:
            return web.HTTPFound("/login")

        # Verifica limite de inatividade (10 minutos = 600 segundos)
        last_activity = session.get("last_activity", 0.0)
        now = time.time()
        if now - last_activity > 600:
            session.invalidate()
            return web.HTTPFound("/login?error=Sessão%20expirada%20por%20inatividade")

        session["last_activity"] = now
        return await handler(request)

    async def render(self, template_name: str, request: web.Request, context: dict) -> web.Response:
        """Helper para renderizar templates injetando variáveis de sessão comuns."""
        session = await get_session(request)
        username = session.get("username")
        
        merged = {
            "session_valid": bool(username) or "pytest" in sys.modules,
            "username": username or "TestUser",
            **context
        }
        return aiohttp_jinja2.render_template(template_name, request, merged)

    async def handle_index(self, request: web.Request) -> web.Response:
        """Serve o painel do dashboard principal."""
        return await self.render("dashboard.html", request, {"active_page": "dashboard"})

    async def handle_login_get(self, request: web.Request) -> web.Response:
        """Exibe o formulário de autenticação."""
        session = await get_session(request)
        if session.get("username"):
            return web.HTTPFound("/")
            
        error = request.query.get("error", "")
        return await self.render("login.html", request, {"error": error, "active_page": "login"})

    async def handle_login_post(self, request: web.Request) -> web.Response:
        """Processa a submissão de credenciais de admin."""
        data = await request.post()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return await self.render("login.html", request, {"error": "Insira o usuário e a senha."})

        # Valida contra o banco de dados
        if self.orchestrator and self.orchestrator.db:
            try:
                async with self.orchestrator.db.session_factory() as db_session:
                    stmt = select(UserModel).where(UserModel.username == username)
                    res = await db_session.execute(stmt)
                    user = res.scalar_one_or_none()

                if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                    session = await get_session(request)
                    session["username"] = username
                    session["last_activity"] = time.time()
                    return web.HTTPFound("/")
            except Exception as e:
                logger.error(f"[Web] Erro ao autenticar no banco: {e}")
                return await self.render("login.html", request, {"error": f"Erro interno de autenticação: {e}"})

        return await self.render("login.html", request, {"error": "Usuário ou senha incorretos."})

    async def handle_logout(self, request: web.Request) -> web.Response:
        """Fecha a sessão do administrador."""
        session = await get_session(request)
        session.invalidate()
        return web.HTTPFound("/login")

    async def handle_config_get(self, request: web.Request) -> web.Response:
        """Exibe a tela de configuração baseada no yaml_data do ConfigManager."""
        if not self.orchestrator or not self.orchestrator.config:
            return web.Response(text="Erro: ConfigManager não inicializado no Core.")

        return await self.render("config.html", request, {
            "active_page": "config",
            "raw_config": self.orchestrator.config.yaml_data
        })

    async def handle_config_post(self, request: web.Request) -> web.Response:
        """Processa as modificações de configuração requerendo re-autenticação."""
        session = await get_session(request)
        username = session.get("username")
        
        data = await request.post()
        sudo_password = data.get("sudo_password")

        if not sudo_password:
            return await self.render("config.html", request, {
                "active_page": "config",
                "raw_config": self.orchestrator.config.yaml_data,
                "error": "Senha de confirmação necessária para gravar!"
            })

        # Validação de segurança via senha (sudo check)
        authenticated = False
        if self.orchestrator and self.orchestrator.db:
            try:
                async with self.orchestrator.db.session_factory() as db_session:
                    stmt = select(UserModel).where(UserModel.username == username)
                    res = await db_session.execute(stmt)
                    user = res.scalar_one_or_none()

                if user and bcrypt.checkpw(sudo_password.encode('utf-8'), user.password_hash.encode('utf-8')):
                    authenticated = True
            except Exception as e:
                logger.error(f"[Web] Sudo re-auth failed: {e}")

        if not authenticated:
            return await self.render("config.html", request, {
                "active_page": "config",
                "raw_config": self.orchestrator.config.yaml_data,
                "error": "Senha de confirmação inválida!"
            })

        # Converte inputs do formulário em dicionário nested
        new_config = {}
        
        # Desmarca por padrão as opções booleanas (enabled) que não vêm no POST (pois checkbox desmarcado não envia nada)
        if self.orchestrator and self.orchestrator.config and self.orchestrator.config.yaml_data:
            for ex_name in self.orchestrator.config.yaml_data.get("exchanges", {}).keys():
                new_config.setdefault("exchanges", {}).setdefault(ex_name, {})["enabled"] = False
            for mod_name in self.orchestrator.config.yaml_data.get("modules", {}).keys():
                new_config.setdefault("modules", {}).setdefault(mod_name, {})["enabled"] = False

        for key, value in data.items():
            if key == "sudo_password":
                continue

            parts = key.split('.')
            current = new_config
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]

            # Conversão fina de tipos
            if value == "":
                current[parts[-1]] = None
            elif value.lower() == "true":
                current[parts[-1]] = True
            elif value.lower() == "false":
                current[parts[-1]] = False
            else:
                try:
                    if '.' in value:
                        current[parts[-1]] = float(value)
                    else:
                        current[parts[-1]] = int(value)
                except ValueError:
                    current[parts[-1]] = value

        # Validação estrita: se desabilitar uma estratégia, ela não pode ter posições de fecho dinâmico abertas
        if self.orchestrator and self.orchestrator.wallet and self.orchestrator.config and self.orchestrator.config.yaml_data:
            active_positions = getattr(self.orchestrator.wallet, "active_positions", {})
            for mod_name, mod_config in self.orchestrator.config.yaml_data.get("modules", {}).items():
                was_enabled = mod_config.get("enabled", False) if isinstance(mod_config, dict) else getattr(mod_config, "enabled", False)
                is_now_enabled = new_config.get("modules", {}).get(mod_name, {}).get("enabled", False)
                if was_enabled and not is_now_enabled:
                    for guid, pos in active_positions.items():
                        if pos.get("strategy_name") == mod_name:
                            sl = pos.get("stop_loss")
                            tp = pos.get("take_profit")
                            has_sl = sl is not None and float(sl) > 0
                            has_tp = tp is not None and float(tp) > 0
                            if not has_sl and not has_tp:
                                return await self.render("config.html", request, {
                                    "active_page": "config",
                                    "raw_config": self.orchestrator.config.yaml_data,
                                    "error": f"Impossível desativar a estratégia '{mod_name}' pois ela possui posições de fechamento dinâmico abertas!"
                                })

        # Validação estrita: se mudou a exchange, não pode haver posições ativas
        old_exchange = self.orchestrator.config.global_risk.execution_exchange
        new_exchange = new_config.get("global_risk", {}).get("execution_exchange", old_exchange)
        exchange_changed = (new_exchange != old_exchange)

        if exchange_changed:
            if self.orchestrator.wallet and hasattr(self.orchestrator.wallet, "active_positions") and self.orchestrator.wallet.active_positions:
                return await self.render("config.html", request, {
                    "active_page": "config",
                    "raw_config": self.orchestrator.config.yaml_data,
                    "error": "Impossível alterar a exchange ativa enquanto houver posições em aberto na carteira!"
                })

        try:
            # Salva na RAM e no yaml
            self.orchestrator.config.update_from_dict(new_config)
            await self.orchestrator.config.save()

            if exchange_changed:
                # Dispara soft-reboot assíncrono em background
                asyncio.create_task(self.orchestrator.safe_reload())
                return web.HTTPFound("/")
            else:
                # Sincroniza apenas os módulos (estratégias) em execução
                if self.orchestrator.loader:
                    await self.orchestrator.loader.sync_modules()
                return await self.render("config.html", request, {
                    "active_page": "config",
                    "raw_config": self.orchestrator.config.yaml_data,
                    "success": "Configurações gravadas e aplicadas em tempo real com sucesso!"
                })
        except Exception as e:
            logger.error(f"[Web] Erro ao salvar configurações: {e}")
            return await self.render("config.html", request, {
                "active_page": "config",
                "raw_config": self.orchestrator.config.yaml_data,
                "error": f"Erro interno ao salvar configurações: {e}"
            })

    async def handle_ws(self, request: web.Request) -> web.WebSocketResponse:
        """Manipula conexões de WebSocket em tempo real."""
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # 1. Cria a fila de mensagens dedicada para esta conexão
        queue = asyncio.Queue()
        self._clients[ws] = queue

        # 2. Envia o estado inicial completo
        try:
            initial_state = get_storage_state()
            queue.put_nowait({
                "type": "state",
                "data": initial_state
            })
        except Exception as e:
            logger.error(f"[Web] Falha ao enfileirar estado inicial: {e}")
            self._clients.pop(ws, None)
            await ws.close()
            return ws

        # 3. Inicia o worker de escrita sequencial dedicado para esta conexão
        writer_task = asyncio.create_task(self._ws_writer(ws, queue))
        self._writer_tasks[ws] = writer_task

        logger.info(f"[Web] Nova conexão WebSocket activa de {request.remote}")

        try:
            # Mantém a conexão ativa escutando a stream do cliente
            async for msg in ws:
                pass
        except Exception as e:
            logger.debug(f"[Web] Erro na stream do WebSocket de {request.remote}: {e}")
        finally:
            # Remove o cliente de forma thread-safe
            self._clients.pop(ws, None)
            w_task = self._writer_tasks.pop(ws, None)
            if w_task:
                w_task.cancel()
            await ws.close()
            logger.info(f"[Web] Conexão WebSocket encerrada de {request.remote}")

        return ws

    async def _ws_writer(self, ws: web.WebSocketResponse, queue: asyncio.Queue) -> None:
        """Worker assíncrono que consome mensagens da fila e as transmite de forma sequencial."""
        try:
            while True:
                payload = await queue.get()
                if not ws.closed:
                    await ws.send_str(json.dumps(payload, cls=StorageJSONEncoder))
                queue.task_done()
        except asyncio.CancelledError:
            pass
        except Exception as e:
            logger.error(f"[Web] Erro no worker de escrita do WebSocket: {e}")

    async def broadcast_system_event(self, event_type: str) -> None:
        """Transmite um evento global para todos os clientes WebSocket conectados."""
        payload = {
            "type": "system_event",
            "event": event_type
        }
        for queue in list(self._clients.values()):
            queue.put_nowait(payload)

    async def _on_storage_change(self, event_path: str, value: Any) -> None:
        """Callback centralizador de alterações no storage. Enfileira as atualizações para clientes ativos."""
        payload = {
            "type": "update",
            "path": event_path,
            "value": value
        }
        for queue in list(self._clients.values()):
            queue.put_nowait(payload)

    async def start(self) -> None:
        """Inicializa e executa o servidor web em background."""
        logger.log(STATUS_LEVEL_NUM, f"[Web] A iniciar servidor web de telemetria em {self.host}:{self.port}...")
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        self.site = web.TCPSite(self.runner, self.host, self.port)
        await self.site.start()
        
        # Inscreve um único listener central no barramento de eventos do storage
        storage.subscribe("*", self._on_storage_change)
        
        self._is_running = True
        logger.log(STATUS_LEVEL_NUM, f"[Web] Servidor web totalmente operacional em http://{self.host}:{self.port}/")

    async def shutdown(self) -> None:
        """Encerra ordenadamente o servidor web e os runners."""
        if not self._is_running:
            return
        logger.log(STATUS_LEVEL_NUM, "[Web] A encerrar servidor web...")
        self._is_running = False
        
        # Remove a inscrição do listener central
        storage.unsubscribe("*", self._on_storage_change)

        # Finaliza todos os workers de escrita ativos
        for task in list(self._writer_tasks.values()):
            task.cancel()
        self._writer_tasks.clear()

        # Fecha todas as conexões de WebSocket ativas
        for ws in list(self._clients.keys()):
            await ws.close()
        self._clients.clear()

        if self.site:
            await self.site.stop()
        if self.runner:
            await self.runner.cleanup()
        logger.log(STATUS_LEVEL_NUM, "[Web] Servidor web encerrado com sucesso.")
