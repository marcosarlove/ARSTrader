"""
ARSTrader - Global Orchestrator / Sovereign Engine (orchestrator.py)
=====================================================================
Dono único da instância de conexão ativa com a API da Exchange via CCXT Pro
e comandante supremo do fluxo macro do robô.
"""

import asyncio
import logging
import time
import inspect
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
from decimal import Decimal

from core.config import ConfigManager
from core.database import DatabaseManager
from core.wallet import WalletController
from core.server import SignalServer
from core.loader import ModuleLoader
from core.models import OperationModel, TradeResultModel
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Orchestrator")


class GlobalOrchestrator:
    """
    Comandante supremo do ARSTrader.
    Orquestra o ciclo de vida dos módulos, a rede TCP IPC de sinais e a execução de ordens na exchange,
    garantindo reconciliação e integridade de limites de risco.
    """

    def __init__(
        self,
        config_path: str = "global_config.yaml",
        ipc_host: str = "127.0.0.1",
        ipc_port: int = 8888,
        exchange: Optional[Any] = None,
        config: Optional[ConfigManager] = None,
        db: Optional[DatabaseManager] = None,
        wallet: Optional[WalletController] = None,
        server: Optional[SignalServer] = None,
        loader: Optional[ModuleLoader] = None,
        web_server: Optional[Any] = None,
    ):
        """
        :param config_path: Caminho para o ficheiro global_config.yaml.
        :param ipc_host: Endereço IP local onde o servidor de sockets escuta.
        :param ipc_port: Porta numérica para o servidor de sockets.
        :param exchange: Instância CCXT Pro opcional (injeção para testes).
        :param config: ConfigManager opcional (injeção para testes).
        :param db: DatabaseManager opcional (injeção para testes).
        :param wallet: WalletController opcional (injeção para testes).
        :param server: SignalServer opcional (injeção para testes).
        :param loader: ModuleLoader opcional (injeção para testes).
        :param web_server: TelemetryWebServer opcional (injeção para testes).
        """
        self.config_path = config_path
        self.ipc_host = ipc_host
        self.ipc_port = ipc_port
        self.exchange = exchange
        self.config = config
        self.db = db
        self.wallet = wallet
        self.server = server
        self.loader = loader
        self.web_server = web_server

        self._is_running = False

    async def start(self) -> None:
        """Inicializa todo o sistema e reconcilia o estado antes de iniciar as estratégias."""
        logger.log(STATUS_LEVEL_NUM, "[Orchestrator] Inicializando o Sovereign Engine...")
        self._is_running = True

        # 1. Carrega as configurações se não injetadas
        if not self.config:
            self.config = ConfigManager(self.config_path)
            await self.config.load()

        # 2. Inicializa o Database se não injetado
        if not self.db:
            self.db = DatabaseManager()
            await self.db.start()

        # 3. Inicializa o CCXT Pro Exchange se não injetado
        if not self.exchange:
            exchange_name = self.config.global_risk.execution_exchange
            ex_config = self.config.exchanges.get(exchange_name)
            if not ex_config or not ex_config.enabled:
                raise ValueError(f"[Orchestrator] Exchange {exchange_name} indisponível ou desativada.")

            options = {
                'apiKey': ex_config.api_key,
                'secret': ex_config.secret,
                'password': ex_config.password,
                'enableRateLimit': True,
                'options': ex_config.options,
            }
            self.exchange = self.create_exchange(exchange_name, options)
            if self.config.system.environment == "sandbox":
                try:
                    res = self.exchange.set_sandbox_mode(True)
                    if inspect.iscoroutine(res):
                        await res
                except Exception as e:
                    logger.warning(f"[Orchestrator] Falha ao definir modo sandbox na exchange: {e}")

        # 4. Reconciliação no Boot (Reconciliation Loop)
        await self._reconcile_and_boot_wallet()

        # 5. Inicializa o SignalServer se não injetado
        if not self.server:
            self.server = SignalServer(
                host=self.ipc_host,
                port=self.ipc_port,
                on_heartbeat_cb=self.on_heartbeat,
                on_order_cb=self.on_order_received,
                on_rejected_order_cb=self.on_order_rejected,
                max_latency_seconds=self.config.system.max_signal_latency_ms / 1000.0
            )
            await self.server.start()
        else:
            if hasattr(self.server, "start"):
                await self.server.start()

        # 6. Inicializa o ModuleLoader se não injetado
        if not self.loader:
            self.loader = ModuleLoader(
                config_manager=self.config,
                server_host=self.ipc_host,
                server_port=self.ipc_port
            )
            await self.loader.start_modules()
        else:
            if hasattr(self.loader, "start_modules"):
                await self.loader.start_modules()

        # 7. Inicializa o TelemetryWebServer se não injetado e configurado
        if not self.web_server and self.config and self.config.web_server:
            from core.web import TelemetryWebServer
            self.web_server = TelemetryWebServer(
                host=self.config.web_server.host,
                port=self.config.web_server.port
            )
            await self.web_server.start()
        elif self.web_server:
            if hasattr(self.web_server, "start"):
                await self.web_server.start()

        logger.log(STATUS_LEVEL_NUM, "[Orchestrator] Sovereign Engine totalmente operacional.")

    def create_exchange(self, exchange_name: str, options: dict) -> Any:
        """Cria a instância da Exchange usando CCXT Pro por padrão (pode ser sobreposta)."""
        import ccxt.pro as ccxtpro
        exchange_class = getattr(ccxtpro, exchange_name)
        return exchange_class(options)

    def _get_wallet_balance(self) -> float:
        """Retorna o saldo da carteira com segurança se estiver disponível."""
        if not self.wallet:
            return 0.0
        val = getattr(self.wallet, "balance", 0.0)
        try:
            return float(val)
        except Exception:
            return 0.0

    async def _reconcile_and_boot_wallet(self) -> None:
        """
        Executa as queries na db, calcula o drawdown diário acumulado
        e sincroniza o estado da Wallet antes de habilitar as estratégias.
        """
        logger.log(STATUS_LEVEL_NUM, "[Orchestrator] A iniciar reconciliação de estado com a base de dados...")

        # Busca perdas do dia e ordens abertas da base de dados usando os helpers assíncronos
        daily_loss = await self.db.get_daily_loss()
        open_ops = await self.db.get_open_operations()

        logger.info(f"[Orchestrator] Drawdown diário já acumulado hoje: {daily_loss:.4f} USDT")
        logger.info(f"[Orchestrator] {len(open_ops)} ordens encontradas em aberto na base de dados para sincronização.")

        # Inicializa o WalletController se não injetado
        if not self.wallet:
            self.wallet = WalletController(
                exchange=self.exchange,
                config=self.config,
                on_order_close_cb=self.on_order_closed
            )

        # Registra o callback do Orchestrator na wallet usando o padrão Observer
        if hasattr(self.wallet, "register_order_close_listener"):
            self.wallet.register_order_close_listener(self.on_order_closed)

        # Sempre executa initialize_and_sync no boot para reconciliação correta
        # de perdas e ordens fechadas externamente
        closed_payloads = await self.wallet.initialize_and_sync(
            open_operations_db=open_ops,
            current_daily_loss=daily_loss
        )

        # Trata ordens que foram fechadas externamente enquanto estávamos offline
        for payload in closed_payloads:
            guid = payload["guid"]
            op_db = await self.db.get_operation_by_guid(guid)
            if op_db:
                # Calcula a variação percentual do PnL
                entry_price = float(op_db.current_price)
                realized_pnl = float(payload["realized_pnl"])
                amount = float(op_db.amount) if op_db.amount is not None else 0.0

                pnl_pct = 0.0
                if entry_price > 0 and amount > 0:
                    pnl_pct = (realized_pnl / (entry_price * amount)) * 100.0

                result_model = TradeResultModel(
                    operation_id=op_db.id,
                    close_timestamp=datetime.fromtimestamp(payload["close_timestamp"] / 1000.0, tz=timezone.utc),
                    close_price=Decimal(str(payload["close_price"])),
                    realized_pnl=Decimal(str(realized_pnl)),
                    pnl_percentage=Decimal(str(pnl_pct)),
                    outcome="WIN" if realized_pnl > 0 else ("LOSS" if realized_pnl < 0 else "BREAKEVEN")
                )
                self.db.enqueue_save(result_model)

                # Se a ordem fechada offline causou prejuízo, atualiza o drawdown diário na RAM
                if realized_pnl < 0:
                    if hasattr(self.wallet, "daily_loss_counter"):
                        try:
                            self.wallet.daily_loss_counter += abs(realized_pnl)
                        except TypeError:
                            self.wallet.daily_loss_counter = abs(realized_pnl)
                    else:
                        self.wallet.daily_loss_counter = abs(realized_pnl)

        current_loss = 0.0
        if self.wallet and hasattr(self.wallet, "daily_loss_counter"):
            try:
                current_loss = float(self.wallet.daily_loss_counter)
            except Exception:
                current_loss = 0.0
        logger.log(STATUS_LEVEL_NUM, f"[Orchestrator] Reconciliação concluída. Drawdown diário ajustado: {current_loss:.4f} USDT")

    async def on_heartbeat(self, strategy_name: str, pid: int) -> None:
        """Callback de heartbeat recebido pelo SignalServer, encaminhado ao Loader."""
        if self.loader:
            self.loader.register_heartbeat(strategy_name, pid)

    async def on_order_received(self, message_str: str, promise: asyncio.Future) -> None:
        """
        Callback principal (on_order_cb) do SignalServer para sinais válidos.
        Registra a operação como PENDING e executa-a via WalletController.
        """
        import json
        try:
            signal = json.loads(message_str)
        except Exception as e:
            logger.error(f"[Orchestrator] Falha grave ao ler sinal validado: {e}")
            promise.set_result({"status": "FAILED", "reason": "DECODE_ERROR"})
            return

        guid = signal.get("guid")
        symbol = signal.get("symbol")
        operation = signal.get("operation")
        strategy_name = signal.get("strategy_name")
        current_price = signal.get("current_price")

        # 1. Cria e registra a OperationModel inicial na base de dados
        op_model = OperationModel(
            guid=guid,
            target_guid=signal.get("target_guid"),
            symbol=symbol,
            operation=operation,
            market=signal.get("market", "SPOT"),
            exchange=signal.get("exchange", "unknown"),
            strategy_name=strategy_name,
            current_price=Decimal(str(current_price)),
            stop_loss=Decimal(str(signal.get("stop_loss"))) if signal.get("stop_loss") is not None else None,
            take_profit=Decimal(str(signal.get("take_profit"))) if signal.get("take_profit") is not None else None,
            wallet_balance_before=Decimal(str(self._get_wallet_balance())),
            status="PENDING",
            reason="A aguardar processamento"
        )
        self.db.enqueue_save(op_model)

        # 2. Executa a ordem de fato no WalletController
        try:
            res = await self.wallet.execute_order(signal)

            # 3. Atualiza os dados finais de execução da OperationModel na base de dados
            op_model.status = res.get("status", "FAILED")
            op_model.reason = res.get("reason") or "Sucesso"
            if "amount" in res:
                op_model.amount = Decimal(str(res["amount"]))
            if "price" in res:
                op_model.current_price = Decimal(str(res["price"]))

            # Recupera stop_loss e take_profit calculados dinamicamente na wallet para auditoria
            if self.wallet and hasattr(self.wallet, "active_positions"):
                try:
                    positions = self.wallet.active_positions
                    if guid in positions:
                        pos_ram = positions[guid]
                        if pos_ram.get("stop_loss"):
                            op_model.stop_loss = Decimal(str(pos_ram["stop_loss"]))
                        if pos_ram.get("take_profit"):
                            op_model.take_profit = Decimal(str(pos_ram["take_profit"]))
                except Exception:
                    pass

            self.db.enqueue_save(op_model)

            # 4. Resolve a promise da rede IPC
            promise.set_result(res)

        except Exception as e:
            logger.error(f"[Orchestrator] Erro interno durante a execução de {guid}: {e}")
            op_model.status = "FAILED"
            op_model.reason = f"INTERNAL_ERROR: {e}"
            self.db.enqueue_save(op_model)
            promise.set_result({"status": "FAILED", "reason": f"INTERNAL_ERROR: {e}"})

    async def on_order_rejected(self, payload: dict, verdict: str) -> None:
        """
        Callback de ordens rejeitadas pré-envio (por exemplo, por latência estourada).
        Apenas gera o registro OperationModel de auditoria como IGNORED na base de dados.
        """
        guid = payload.get("guid") or f"rejected-{int(time.time()*1000)}"
        op_model = OperationModel(
            guid=guid,
            target_guid=payload.get("target_guid"),
            symbol=payload.get("symbol", "UNKNOWN"),
            operation=payload.get("operation", "BUY"),
            market=payload.get("market", "SPOT"),
            exchange=payload.get("exchange", "unknown"),
            strategy_name=payload.get("strategy_name", "unknown"),
            current_price=Decimal(str(payload.get("current_price") or payload.get("price") or 0.0)),
            wallet_balance_before=Decimal(str(self._get_wallet_balance())),
            status="IGNORED",
            reason=verdict
        )
        self.db.enqueue_save(op_model)

    async def on_order_closed(self, payload: dict) -> None:
        """
        Callback acionado assíncronamente via WebSocket do Wallet quando uma ordem é fechada.
        Registra o TradeResultModel na base de dados de forma não-bloqueante.
        """
        guid = payload["guid"]
        realized_pnl = payload["realized_pnl"]
        close_price = payload["close_price"]
        close_timestamp = payload["close_timestamp"]

        # Busca a operação original
        op_db = await self.db.get_operation_by_guid(guid)
        if not op_db:
            logger.warning(f"[Orchestrator] Impossível persistir TradeResult: Operação {guid} não encontrada na base de dados.")
            return

        entry_price = float(op_db.current_price)
        amount = float(op_db.amount) if op_db.amount is not None else 0.0

        pnl_pct = 0.0
        if entry_price > 0 and amount > 0:
            pnl_pct = (realized_pnl / (entry_price * amount)) * 100.0

        result_model = TradeResultModel(
            operation_id=op_db.id,
            close_timestamp=datetime.fromtimestamp(close_timestamp / 1000.0, tz=timezone.utc),
            close_price=Decimal(str(close_price)),
            realized_pnl=Decimal(str(realized_pnl)),
            pnl_percentage=Decimal(str(pnl_pct)),
            outcome="WIN" if realized_pnl > 0 else ("LOSS" if realized_pnl < 0 else "BREAKEVEN")
        )
        self.db.enqueue_save(result_model)

        logger.info(
            f"[Orchestrator] Auditoria do encerramento de {guid} gravada na DB. Outcome: {result_model.outcome} (PnL: {realized_pnl:.4f})"
        )

    async def shutdown(self) -> None:
        """Desliga ordenadamente todos os subprocessos e conexões físicas do Core."""
        logger.log(STATUS_LEVEL_NUM, "[Orchestrator] Iniciando encerramento ordenado...")
        self._is_running = False

        # 1. Desliga o ModuleLoader (mata estratégias filhas)
        if self.loader:
            try:
                await self.loader.shutdown()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao encerrar ModuleLoader: {e}")

        # 1.5 Desliga o TelemetryWebServer
        if self.web_server:
            try:
                await self.web_server.shutdown()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao encerrar TelemetryWebServer: {e}")

        # 2. Desliga o SignalServer (fecha porta TCP local)
        if self.server:
            try:
                await self.server.shutdown()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao encerrar SignalServer: {e}")

        # 3. Desliga o WalletController (cancela loops de WebSocket da exchange)
        if self.wallet:
            try:
                await self.wallet.shutdown()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao encerrar WalletController: {e}")

        # 4. Desliga conexões físicas da Exchange se necessário
        if self.exchange:
            try:
                await self.exchange.close()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao fechar conexão com a exchange: {e}")

        # 5. Desliga o banco de dados (escoa fila de persistência do worker)
        if self.db:
            try:
                await self.db.shutdown()
            except Exception as e:
                logger.error(f"[Orchestrator] Erro ao encerrar DatabaseManager: {e}")

        logger.log(STATUS_LEVEL_NUM, "[Orchestrator] Sovereign Engine desligado com sucesso.")
