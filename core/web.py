"""
ARSTrader - Telemetry Web Server (web.py)
=========================================
Fornece um servidor web HTTP e WebSocket assíncrono (via aiohttp) para exibir
a telemetria e o estado em tempo real do robô de trading armazenado na RAM (storage.py).
"""

import asyncio
import json
import logging
from typing import Any, Dict, Optional, Set
from decimal import Decimal

from aiohttp import web
from core.storage import storage, ModuleState
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

    def __init__(self, host: str = "127.0.0.1", port: int = 8080):
        self.host = host
        self.port = port
        self.app = web.Application()
        
        # Rotas
        self.app.router.add_get("/", self.handle_index)
        self.app.router.add_get("/ws", self.handle_ws)
        
        self.runner: Optional[web.AppRunner] = None
        self.site: Optional[web.TCPSite] = None
        self._is_running = False

        # Centralized active clients dictionary mapping each WS connection to its queue
        self._clients: Dict[web.WebSocketResponse, asyncio.Queue] = {}
        # Centralized writer tasks mapping each WS connection to its background writer
        self._writer_tasks: Dict[web.WebSocketResponse, asyncio.Task] = {}

    async def handle_index(self, request: web.Request) -> web.Response:
        """Serve a página do dashboard HTML."""
        return web.Response(text=HTML_TEMPLATE, content_type="text/html")

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


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ARSTrader | Terminal de Telemetria</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #1e1b4b 100%);
            --card-bg: rgba(17, 24, 39, 0.7);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --accent-purple: #8b5cf6;
            --accent-glow: rgba(139, 92, 246, 0.25);
            --status-green: #10b981;
            --status-red: #ef4444;
            --status-yellow: #f59e0b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background: var(--bg-gradient);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 2rem;
            overflow-x: hidden;
        }

        .glow-1 {
            position: absolute;
            top: -10%;
            left: -10%;
            width: 50vw;
            height: 50vw;
            background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
            pointer-events: none;
        }
        .glow-2 {
            position: absolute;
            bottom: -10%;
            right: -10%;
            width: 50vw;
            height: 50vw;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.08) 0%, rgba(0,0,0,0) 70%);
            z-index: -1;
            pointer-events: none;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--card-border);
        }

        .logo-container {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .logo-text {
            font-size: 1.75rem;
            font-weight: 800;
            letter-spacing: -0.5px;
            background: linear-gradient(to right, #ffffff, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .sys-badges {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .badge {
            padding: 0.4rem 0.8rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border: 1px solid var(--card-border);
        }

        .badge-env {
            background: rgba(139, 92, 246, 0.15);
            color: #c084fc;
            border-color: rgba(139, 92, 246, 0.3);
        }

        .badge-conn {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            background: rgba(17, 24, 39, 0.8);
        }

        .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--status-red);
            box-shadow: 0 0 8px var(--status-red);
        }

        .dot.online {
            background: var(--status-green);
            box-shadow: 0 0 8px var(--status-green);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            gap: 1.5rem;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 1rem;
            padding: 1.5rem;
            backdrop-filter: blur(16px);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s, border-color 0.2s;
        }

        .card:hover {
            border-color: rgba(139, 92, 246, 0.3);
        }

        .card-title {
            font-size: 0.95rem;
            color: var(--text-secondary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .card-wallet { grid-column: span 5; }
        .card-comms { grid-column: span 3; }
        .card-modules { grid-column: span 4; }
        .card-positions { grid-column: span 8; }
        .card-locks { grid-column: span 4; }

        .balance-value {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #ffffff, #c084fc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px var(--accent-glow);
        }

        .drawdown-container {
            margin-top: 1.25rem;
        }

        .drawdown-header {
            display: flex;
            justify-content: space-between;
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 0.4rem;
        }

        .progress-bar-bg {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 9999px;
            overflow: hidden;
            border: 1px solid var(--card-border);
        }

        .progress-bar-fill {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--accent-purple), #a855f7);
            border-radius: 9999px;
            transition: width 0.4s ease;
        }

        .comms-stat-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0;
            border-bottom: 1px solid var(--card-border);
        }

        .comms-stat-item:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }

        .comms-stat-label {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .comms-stat-value {
            font-size: 1rem;
            font-weight: 600;
            font-family: 'Fira Code', monospace;
        }

        .module-list {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .module-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--card-border);
            padding: 0.75rem 1rem;
            border-radius: 0.75rem;
        }

        .module-info {
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }

        .module-name {
            font-weight: 600;
            font-size: 0.9rem;
        }

        .module-meta {
            font-size: 0.75rem;
            color: var(--text-secondary);
            font-family: 'Fira Code', monospace;
        }

        .module-status {
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .status-on { background: rgba(16, 185, 129, 0.15); color: #34d399; }
        .status-off { background: rgba(239, 44, 68, 0.15); color: #f87171; }
        .status-starting { background: rgba(245, 158, 11, 0.15); color: #fbbf24; }

        table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }

        th {
            font-size: 0.8rem;
            color: var(--text-secondary);
            font-weight: 600;
            text-transform: uppercase;
            padding: 0.75rem 1rem;
            border-bottom: 1px solid var(--card-border);
        }

        td {
            padding: 1rem;
            font-size: 0.9rem;
            border-bottom: 1px solid var(--card-border);
            font-family: 'Outfit', sans-serif;
        }

        tr:last-child td {
            border-bottom: none;
        }

        .mono {
            font-family: 'Fira Code', monospace;
        }

        .badge-op {
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 700;
        }

        .badge-buy { background: rgba(16, 185, 129, 0.15); color: #34d399; }
        .badge-sell { background: rgba(239, 44, 68, 0.15); color: #f87171; }

        .no-data {
            text-align: center;
            color: var(--text-secondary);
            padding: 2.5rem 0;
            font-style: italic;
        }

        .locks-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }

        .lock-pill {
            display: flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.5rem 0.75rem;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.2);
            color: #f87171;
            border-radius: 0.5rem;
            font-weight: 600;
            font-size: 0.85rem;
        }

        .lock-pill i {
            width: 14px;
            height: 14px;
        }

        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.05);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--card-border);
            border-radius: 9999px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(139, 92, 246, 0.3);
        }
    </style>
</head>
<body>
    <div class="glow-1"></div>
    <div class="glow-2"></div>

    <header>
        <div class="logo-container">
            <i data-lucide="activity" style="color: var(--accent-purple); width: 28px; height: 28px;"></i>
            <span class="logo-text">ARSTrader</span>
        </div>
        <div class="sys-badges">
            <span class="badge badge-env" id="badge-environment">SANDBOX</span>
            <span class="badge badge-conn">
                <span class="dot" id="conn-dot"></span>
                <span id="conn-text">Desconectado</span>
            </span>
        </div>
    </header>

    <main class="grid-container">
        <section class="card card-wallet">
            <div class="card-title">
                <i data-lucide="wallet" style="width: 18px; height: 18px;"></i>
                <span>Carteira & Gestão de Risco</span>
            </div>
            <div>
                <div class="balance-value" id="wallet-balance">0.00 USDT</div>
                <div class="comms-stat-item">
                    <span class="comms-stat-label">Drawdown Diário Acumulado</span>
                    <span class="comms-stat-value" id="daily-loss-counter">0.00 USDT</span>
                </div>
                <div class="drawdown-container">
                    <div class="drawdown-header">
                        <span>Progresso do Limite de Perda</span>
                        <span id="drawdown-percentage">0.0%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" id="drawdown-fill"></div>
                    </div>
                </div>
            </div>
        </section>

        <section class="card card-comms">
            <div class="card-title">
                <i data-lucide="cpu" style="width: 18px; height: 18px;"></i>
                <span>Comunicação IPC & Latência</span>
            </div>
            <div>
                <div class="comms-stat-item">
                    <span class="comms-stat-label">Latência do Sinal</span>
                    <span class="comms-stat-value mono" id="comms-latency">0.00 ms</span>
                </div>
                <div class="comms-stat-item">
                    <span class="comms-stat-label">Sinais Processados</span>
                    <span class="comms-stat-value" id="comms-processed">0</span>
                </div>
                <div class="comms-stat-item">
                    <span class="comms-stat-label">Sinais Rejeitados</span>
                    <span class="comms-stat-value" style="color: var(--status-red);" id="comms-dropped">0</span>
                </div>
                <div class="comms-stat-item">
                    <span class="comms-stat-label">Bloqueio de Execução</span>
                    <span class="comms-stat-value" id="comms-lock">Nenhum</span>
                </div>
            </div>
        </section>

        <section class="card card-modules">
            <div class="card-title">
                <i data-lucide="layers" style="width: 18px; height: 18px;"></i>
                <span>Módulos de Estratégias</span>
            </div>
            <div class="module-list" id="modules-container">
                <div class="no-data">Nenhuma estratégia registada.</div>
            </div>
        </section>

        <section class="card card-positions">
            <div class="card-title">
                <i data-lucide="briefcase" style="width: 18px; height: 18px;"></i>
                <span>Posições Ativas na RAM</span>
            </div>
            <div style="overflow-x: auto;">
                <table>
                    <thead>
                        <tr>
                            <th>GUID</th>
                            <th>Símbolo</th>
                            <th>Lado</th>
                            <th>Quantidade</th>
                            <th>Preço Entrada</th>
                            <th>Stop Loss</th>
                            <th>Take Profit</th>
                        </tr>
                    </thead>
                    <tbody id="positions-table-body">
                        <tr>
                            <td colspan="7" class="no-data">Nenhuma posição em aberto.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <section class="card card-locks">
            <div class="card-title">
                <i data-lucide="lock" style="width: 18px; height: 18px;"></i>
                <span>Locks de Ativos (Evitar Duplicação)</span>
            </div>
            <div class="locks-container" id="locks-container">
                <div class="no-data">Nenhum lock ativo na RAM.</div>
            </div>
        </section>
    </main>

    <script>
        lucide.createIcons();

        let socket = null;
        let state = {};

        function connect() {
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${protocol}//${window.location.host}/ws`;
            
            socket = new WebSocket(wsUrl);

            socket.onopen = () => {
                document.getElementById('conn-dot').className = 'dot online';
                document.getElementById('conn-text').innerText = 'Conectado';
                console.log('Conectado ao WebSocket de Telemetria.');
            };

            socket.onclose = () => {
                document.getElementById('conn-dot').className = 'dot';
                document.getElementById('conn-text').innerText = 'Desconectado';
                console.log('Conexão encerrada. Tentando reconectar...');
                setTimeout(connect, 3000);
            };

            socket.onerror = (err) => {
                console.error('Erro no WebSocket:', err);
                socket.close();
            };

            socket.onmessage = (event) => {
                const message = JSON.parse(event.data);
                if (message.type === 'state') {
                    state = message.data;
                    renderAll();
                } else if (message.type === 'update') {
                    applyUpdate(message.path, message.value);
                    renderAll();
                }
            };
        }

        function applyUpdate(path, value) {
            if (!path) return;
            const parts = path.split('.');
            let current = state;
            
            const protectedCollections = ["active_positions", "active_locks", "loader"];

            for (let i = 0; i < parts.length - 1; i++) {
                const part = parts[i];
                if (current[part] === undefined || current[part] === null || typeof current[part] !== 'object') {
                    current[part] = {};
                }
                current = current[part];
            }
            
            const last = parts[parts.length - 1];
            
            if (value === null) {
                if (protectedCollections.includes(last)) {
                    current[last] = {};
                } else if (current && typeof current === 'object' && !Array.isArray(current)) {
                    delete current[last];
                } else if (Array.isArray(current)) {
                    const idx = current.indexOf(last);
                    if (idx > -1) current.splice(idx, 1);
                }
            } else {
                if (value !== null && typeof value === 'object' && !Array.isArray(value) && current[last] && typeof current[last] === 'object' && !Array.isArray(current[last])) {
                    current[last] = { ...current[last], ...value };
                } else {
                    current[last] = value;
                }
            }
        }

        function renderAll() {
            if (!state || Object.keys(state).length === 0) return;

            // Environment
            const envBadge = document.getElementById('badge-environment');
            if (state.config && state.config.environment) {
                envBadge.innerText = state.config.environment;
                envBadge.className = `badge badge-env ${state.config.environment.toLowerCase()}`;
            }

            // Wallet
            if (state.wallet) {
                const balance = typeof state.wallet.balance === 'number' ? state.wallet.balance : 0;
                document.getElementById('wallet-balance').innerText = `${balance.toFixed(2)} USDT`;
                
                const loss = typeof state.wallet.daily_loss_counter === 'number' ? state.wallet.daily_loss_counter : 0;
                document.getElementById('daily-loss-counter').innerText = `${loss.toFixed(2)} USDT`;

                const maxLossLimit = typeof state.wallet.max_daily_loss_limit === 'number' ? state.wallet.max_daily_loss_limit : 100;
                const percentage = Math.min((loss / maxLossLimit) * 100, 100);
                document.getElementById('drawdown-percentage').innerText = `${percentage.toFixed(1)}%`;
                document.getElementById('drawdown-fill').style.width = `${percentage}%`;
                
                if (percentage >= 100) {
                    document.getElementById('drawdown-fill').style.background = 'var(--status-red)';
                } else if (percentage >= 80) {
                    document.getElementById('drawdown-fill').style.background = 'var(--status-yellow)';
                } else {
                    document.getElementById('drawdown-fill').style.background = 'linear-gradient(90deg, var(--accent-purple), #a855f7)';
                }

                // Render positions
                const posTableBody = document.getElementById('positions-table-body');
                const positions = state.wallet.active_positions || {};
                const guidList = Object.keys(positions);

                if (guidList.length === 0) {
                    posTableBody.innerHTML = `<tr><td colspan="7" class="no-data">Nenhuma posição em aberto.</td></tr>`;
                } else {
                    posTableBody.innerHTML = guidList.map(guid => {
                        const pos = positions[guid];
                        if (!pos) return '';
                        const sideClass = pos.operation === 'BUY' ? 'badge-buy' : 'badge-sell';
                        
                        const sl = (pos.stop_loss && typeof pos.stop_loss === 'number') ? `${pos.stop_loss.toFixed(2)}` : '-';
                        const tp = (pos.take_profit && typeof pos.take_profit === 'number') ? `${pos.take_profit.toFixed(2)}` : '-';
                        const price = (pos.price && typeof pos.price === 'number') ? pos.price.toFixed(2) : '-';
                        const amount = (pos.amount && typeof pos.amount === 'number') ? pos.amount.toFixed(4) : '-';

                        return `
                            <tr>
                                <td class="mono" style="font-size: 0.8rem; max-width: 120px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${guid}</td>
                                <td style="font-weight: 600;">${pos.symbol || '-'}</td>
                                <td><span class="badge-op ${sideClass}">${pos.operation || '-'}</span></td>
                                <td class="mono">${amount}</td>
                                <td class="mono">${price}</td>
                                <td class="mono" style="color: var(--status-red);">${sl}</td>
                                <td class="mono" style="color: var(--status-green);">${tp}</td>
                            </tr>
                        `;
                    }).join('');
                }

                // Render locks
                const locksContainer = document.getElementById('locks-container');
                const activeLocks = state.wallet.active_locks || {};
                let locksList = [];
                if (Array.isArray(activeLocks)) {
                    locksList = activeLocks;
                } else if (activeLocks && typeof activeLocks === 'object') {
                    locksList = Object.keys(activeLocks);
                }

                if (locksList.length === 0) {
                    locksContainer.innerHTML = `<div class="no-data">Nenhum lock ativo na RAM.</div>`;
                } else {
                    locksContainer.innerHTML = locksList.map(sym => `
                        <div class="lock-pill">
                            <i data-lucide="lock"></i>
                            <span>${sym}</span>
                        </div>
                    `).join('');
                    lucide.createIcons();
                }
            }

            // Comms
            if (state.comms) {
                const latency = typeof state.comms.latency_ms === 'number' ? state.comms.latency_ms : 0;
                document.getElementById('comms-latency').innerText = `${latency.toFixed(2)} ms`;
                document.getElementById('comms-processed').innerText = state.comms.signals_processed || 0;
                document.getElementById('comms-dropped').innerText = state.comms.signals_dropped || 0;
                
                const lockVal = state.comms.execution_lock ? 'BLOQUEADO' : 'Livre';
                const lockElem = document.getElementById('comms-lock');
                lockElem.innerText = lockVal;
                lockElem.style.color = state.comms.execution_lock ? 'var(--status-red)' : 'var(--status-green)';
            }

            // Loader (Strategies)
            if (state.loader) {
                const modulesContainer = document.getElementById('modules-container');
                const stratNames = Object.keys(state.loader);

                if (stratNames.length === 0) {
                    modulesContainer.innerHTML = `<div class="no-data">Nenhuma estratégia registada.</div>`;
                } else {
                    modulesContainer.innerHTML = stratNames.map(name => {
                        const mod = state.loader[name];
                        if (!mod) return '';
                        const statusClass = mod.status === 'ON' ? 'status-on' : (mod.status === 'OFF' ? 'status-off' : 'status-starting');
                        const pidText = mod.pid ? `PID: ${mod.pid}` : 'Sem processo';
                        const heartbeat = mod.last_heartbeat ? new Date(mod.last_heartbeat * 1000).toLocaleTimeString() : 'Nunca';

                        return `
                            <div class="module-item">
                                <div class="module-info">
                                    <span class="module-name">${name}</span>
                                    <span class="module-meta">${pidText} | Last HB: ${heartbeat}</span>
                                </div>
                                <span class="module-status ${statusClass}">${mod.status || 'OFF'}</span>
                            </div>
                        `;
                    }).join('');
                }
            }
        }

        connect();
    </script>
</body>
</html>"""