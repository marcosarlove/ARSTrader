"""
ARSTrader - Wallet & Risk Manager (wallet.py)
=============================================
Detém o monopólio absoluto sobre os dados privados da conta e cálculos de tamanho de posição.

Regras Operacionais:
1. Sincroniza e armazena localmente o saldo real e as posições abertas na Exchange.
2. Valida se o sinal entrante viola os limites globais e estritos: teto de perda diária (Daily Drawdown) e limite de ordens simultâneas.
3. Executa a inteligência de Sizing: calcula o lote exato a ser boletado e determina os alvos de Stop Loss e Take Profit se a estratégia não fornecer-los ou fornecer inválidos.
4. Se o sinal falhar em qualquer validação matemática deste módulo, a operação é abortada.
"""

import asyncio
import logging
import time
import inspect
from typing import Any, Callable, Coroutine, Dict, List, Optional, Tuple

import ccxt
from core.config import ConfigManager
from core.logger import STATUS_LEVEL_NUM
from core import storage

logger = logging.getLogger("ARSTrader.Wallet")


class WalletController:
    """
    Gerenciador financeiro e controlador de risco do ARSTrader.
    Interage com o CCXT Pro para sincronizar saldo, monitorar execuções via WebSockets
    e executar ordens de mercado respeitando limites de risco estritos na velocidade da RAM.
    """

    def __init__(
        self,
        exchange: Any,
        config: ConfigManager,
        on_order_close_cb: Optional[Callable[[dict], Any]] = None,
    ):
        """
        :param exchange: Instância de conexão ativa com a API da Exchange (CCXT Pro).
        :param config: Instância do gerenciador de configurações.
        :param on_order_close_cb: Callback assíncrono para notificar o Orchestrator sobre fechamentos.
        """
        self.exchange = exchange
        self.config = config
        self.on_order_close_cb = on_order_close_cb

        # Lista de listeners para eventos de fechamento de ordem (Padrão Observer)
        self._order_close_listeners: List[Callable[[dict], Any]] = []
        if on_order_close_cb:
            self._order_close_listeners.append(on_order_close_cb)

        # Referências para tarefas rodando em background
        self._balance_task: Optional[asyncio.Task] = None
        self._orders_task: Optional[asyncio.Task] = None
        self._is_running = False

        # Registro temporário das ordens de fecho disparadas via REST
        self._pending_close_orders: Dict[str, str] = {}

        # Set para evitar processamento de mensagens duplicadas da Exchange
        self._processed_order_ids = set()

        # Protege transições críticas de estado em RAM: risk-check + claim
        # do símbolo + rollback por dono do lock.
        self._state_lock = asyncio.Lock()
        self._symbol_locks: Dict[str, asyncio.Lock] = {}
        self._capacity_condition = asyncio.Condition()
        self._pending_open_guids = set()

        # Capabilities de proteção detectadas no boot. O fallback conservador é
        # usar ordens separadas, pois attached SL/TP não é universal.
        self._supports_attached_sl_tp = False
        self._supports_stop_loss_price = False
        self._supports_take_profit_price = False

    def register_order_close_listener(self, listener: Callable[[dict], Any]) -> None:
        """Adiciona um listener para receber atualizações de fechamento de ordens."""
        if not any(id(x) == id(listener) for x in self._order_close_listeners):
            self._order_close_listeners.append(listener)

    @property
    def daily_loss_counter(self) -> float:
        return float(storage.wallet.daily_loss_counter)

    @daily_loss_counter.setter
    def daily_loss_counter(self, value: float) -> None:
        storage.wallet.daily_loss_counter = float(value)

    @property
    def balance(self) -> float:
        return float(storage.wallet.balance)

    @balance.setter
    def balance(self, value: float) -> None:
        storage.wallet.balance = float(value)

    @property
    def active_positions(self) -> dict:
        return storage.wallet.active_positions

    def _lock_owner(self, symbol: str) -> Optional[str]:
        owner = storage.wallet.active_locks.get(symbol)
        return str(owner) if owner is not None else None

    async def _get_symbol_lock(self, symbol: str) -> asyncio.Lock:
        async with self._state_lock:
            if symbol not in self._symbol_locks:
                self._symbol_locks[symbol] = asyncio.Lock()
            return self._symbol_locks[symbol]

    async def _reserve_open_slot(self, symbol: str, guid: str, max_simultaneous: int, max_loss: float) -> Optional[str]:
        """Reserva capacidade global sem publicar estado fantasma em active_locks."""
        async with self._capacity_condition:
            while True:
                if storage.wallet.daily_loss_counter >= max_loss:
                    return "DAILY_LOSS_LIMIT_EXCEEDED"

                if symbol in storage.wallet.active_locks:
                    return "ASSET_LOCK_ACTIVE"

                active_count = len(storage.wallet.active_locks)
                if active_count >= max_simultaneous:
                    return "LIMIT_SIMULTANEOUS_TRADES_EXCEEDED"

                if active_count + len(self._pending_open_guids) < max_simultaneous:
                    self._pending_open_guids.add(guid)
                    return None

                await self._capacity_condition.wait()

    async def _release_open_slot(self, guid: str) -> None:
        async with self._capacity_condition:
            self._pending_open_guids.discard(guid)
            self._capacity_condition.notify_all()

    async def _mark_position_open(self, symbol: str, guid: str) -> None:
        async with self._state_lock:
            storage.wallet.active_locks[symbol] = guid
            storage.wallet.simultaneous_trades = len(storage.wallet.active_locks)
        async with self._capacity_condition:
            self._capacity_condition.notify_all()

    async def _release_symbol_lock(self, symbol: str, owner_guid: str) -> None:
        """Libera um lock apenas se quem está liberando ainda for o dono."""
        async with self._state_lock:
            owner = storage.wallet.active_locks.get(symbol)
            if owner == owner_guid:
                storage.wallet.active_locks.pop(symbol, None)
                storage.wallet.simultaneous_trades = len(storage.wallet.active_locks)
        async with self._capacity_condition:
            self._capacity_condition.notify_all()

    async def _ensure_position_lock(self, symbol: str, owner_guid: str) -> None:
        """Garante lock para posição reconciliada/aberta sem sobrescrever outro dono."""
        async with self._state_lock:
            if symbol not in storage.wallet.active_locks:
                storage.wallet.active_locks[symbol] = owner_guid
                storage.wallet.simultaneous_trades = len(storage.wallet.active_locks)

    def _risk_float(self, name: str, default: float) -> float:
        """Lê um valor numérico da configuração de risco com fallback defensivo."""
        try:
            return float(getattr(self.config.global_risk, name))
        except Exception:
            return default

    async def _maybe_load_markets(self) -> None:
        """Carrega mercados se a exchange expõe essa chamada."""
        load_markets = getattr(self.exchange, "load_markets", None)
        if not load_markets:
            return
        res = load_markets()
        if inspect.iscoroutine(res):
            await res

    def _feature_value(self, symbol: str, method: str, feature: str) -> bool:
        """Consulta suporte de feature no CCXT quando disponível."""
        feature_value = getattr(self.exchange, "feature_value", None)
        if not feature_value:
            return False
        try:
            return bool(feature_value(symbol, method, feature))
        except Exception as e:
            logger.debug(f"[Wallet] Feature CCXT indisponível para {symbol}/{method}/{feature}: {e}")
            return False

    def _detect_protection_capabilities(self, symbol: Optional[str] = None) -> None:
        """Detecta se a exchange suporta SL/TP anexado e parâmetros unificados de proteção."""
        probe_symbol = symbol or "BTC/USDT:USDT"
        self._supports_attached_sl_tp = self._feature_value(
            probe_symbol, "createOrder", "attachedStopLossTakeProfit"
        )
        self._supports_stop_loss_price = self._feature_value(
            probe_symbol, "createOrder", "stopLossPrice"
        )
        self._supports_take_profit_price = self._feature_value(
            probe_symbol, "createOrder", "takeProfitPrice"
        )
        logger.info(
            "[Wallet] Capabilities SL/TP detectadas para %s: attached=%s, stopLossPrice=%s, takeProfitPrice=%s",
            probe_symbol,
            self._supports_attached_sl_tp,
            self._supports_stop_loss_price,
            self._supports_take_profit_price,
        )

    async def initialize_and_sync(
        self, open_operations_db: List[dict], current_daily_loss: float
    ) -> List[dict]:
        """
        FASE A: Inicialização e Sincronização Assíncrona (Reconciliation Loop)
        Consulta o estado real de todas as operações abertas em paralelo na Exchange.
        """
        logger.log(
            STATUS_LEVEL_NUM,
            "[Wallet] A iniciar reconciliação de estado com a Exchange...",
        )
        self._is_running = True

        # Valida credenciais com a Exchange na inicialização (falha alto se incorretas)
        from unittest.mock import Mock
        if not isinstance(self.exchange, Mock):
            try:
                logger.info("[Wallet] Validando credenciais com a Exchange via REST API...")
                await self._maybe_load_markets()
                self._detect_protection_capabilities()
                balance_data = await self.exchange.fetch_balance()
                free_balance = balance_data.get("free", {})
                allowed_bases = ["USDT", "USDC", "USD"]
                usdt_balance = 0.0
                for base in allowed_bases:
                    if base in free_balance and free_balance[base] > 0:
                        usdt_balance = free_balance[base]
                        break
                storage.wallet.balance = float(usdt_balance)
            except ccxt.AuthenticationError as e:
                logger.critical(f"[Wallet] Falha crítica de autenticação na Exchange (API Keys inválidas): {e}")
                raise e
        else:
            self._detect_protection_capabilities()

        # Inicializa o contador diário de perda e limite na RAM para telemetria
        storage.wallet.daily_loss_counter = current_daily_loss
        storage.wallet.max_daily_loss_limit = float(self.config.global_risk.max_daily_loss_limit)

        # Consulta simultânea via REST
        tasks = [self._sync_order(op) for op in open_operations_db]
        results = await asyncio.gather(*tasks)

        # Filtra os payloads das ordens que foram fechadas enquanto estávamos offline
        closed_payloads = [res for res in results if res is not None]

        logger.log(
            STATUS_LEVEL_NUM,
            f"[Wallet] Reconciliação concluída. {len(closed_payloads)} ordens fechadas externamente.",
        )

        # Inicializa os loops de WebSocket para monitoramento contínuo se ainda não estiverem ativos
        if self._balance_task is None or self._balance_task.done():
            self._balance_task = asyncio.create_task(self._watch_balance_loop())
        if self._orders_task is None or self._orders_task.done():
            self._orders_task = asyncio.create_task(self._watch_orders_loop())

        return closed_payloads

    async def _sync_order(self, op: dict) -> Optional[dict]:
        """Sincroniza uma única ordem aberta consultando a API REST da Exchange."""
        guid = op.get("guid")
        symbol = op.get("symbol")
        order_id = op.get("exchange_order_id") or guid

        try:
            logger.debug(f"[Wallet] Verificando status na exchange para a ordem {order_id}...")
            order = await self.exchange.fetch_order(order_id, symbol)
            status = order.get("status")

            if status == "open":
                # Ordem continua aberta: reativa imediatamente lock e posição na RAM
                await self._ensure_position_lock(symbol, guid)
                storage.wallet.active_positions[guid] = {
                    "guid": guid,
                    "symbol": symbol,
                    "amount": float(order.get("amount") or op.get("amount", 0.0)),
                    "price": float(order.get("price") or op.get("current_price", 0.0)),
                    "operation": op.get("operation", "BUY"),
                    "exchange_order_id": order_id,
                    "stop_loss": op.get("stop_loss"),
                    "take_profit": op.get("take_profit"),
                    "strategy_name": op.get("strategy_name"),
                }
                return None
            else:
                # Ordem foi fechada ou cancelada externamente
                close_price = order.get("average") or order.get("price") or float(op.get("current_price", 0.0))
                close_ts = order.get("timestamp") or (time.time() * 1000.0)

                # Calcula PnL provisório para auditoria
                entry_price = float(op.get("current_price", 0.0))
                amount = float(order.get("amount") or op.get("amount", 0.0))
                operation = op.get("operation", "BUY")

                pnl = 0.0
                if operation == "BUY":
                    pnl = (close_price - entry_price) * amount
                else:
                    pnl = (entry_price - close_price) * amount

                return {
                    "guid": guid,
                    "status": "CLOSED" if status == "closed" else "CANCELED",
                    "close_price": close_price,
                    "close_timestamp": close_ts,
                    "realized_pnl": pnl,
                    "reason": "EXTERNAL_CLOSE",
                }

        except ccxt.OrderNotFound:
            logger.warning(
                f"[Wallet] Ordem {order_id} não encontrada na exchange. Tratando como cancelada externamente."
            )
            return {
                "guid": guid,
                "status": "CANCELED",
                "close_price": float(op.get("current_price", 0.0)),
                "close_timestamp": time.time() * 1000.0,
                "realized_pnl": 0.0,
                "reason": "EXTERNAL_CLOSE_NOT_FOUND",
            }
        except Exception as e:
            logger.error(
                f"[Wallet] Erro crítico ao buscar ordem {order_id} na exchange: {e}. Mantendo como aberta por segurança."
            )
            # Para evitar sobreexposição de risco, mantemos o lock na RAM ativo
            await self._ensure_position_lock(symbol, guid)
            storage.wallet.active_positions[guid] = {
                "guid": guid,
                "symbol": symbol,
                "amount": float(op.get("amount", 0.0)),
                "price": float(op.get("current_price", 0.0)),
                "operation": op.get("operation", "BUY"),
                "exchange_order_id": order_id,
                "stop_loss": op.get("stop_loss"),
                "take_profit": op.get("take_profit"),
                "strategy_name": op.get("strategy_name"),
            }
            return None

    async def _watch_balance_loop(self) -> None:
        """Loop perpétuo de WebSocket para monitorar o saldo da conta."""
        logger.info("[Wallet] Loop watch_balance iniciado.")
        while self._is_running:
            try:
                balance = await self.exchange.watch_balance()
                free_balance = balance.get("free", {})
                
                # Busca apenas pelas moedas base homologadas para evitar "saldo fantasma" (restos de outras moedas)
                allowed_bases = ["USDT", "USDC", "USD"]
                usdt_balance = None
                for base in allowed_bases:
                    if base in free_balance and free_balance[base] > 0:
                        usdt_balance = free_balance[base]
                        break
                            
                if usdt_balance is not None:
                    storage.wallet.balance = float(usdt_balance)
            except ccxt.NetworkError as e:
                logger.warning(f"[Wallet] Erro de rede no WebSocket watch_balance: {e}")
                await asyncio.sleep(5)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"[Wallet] Erro no loop watch_balance: {e}")
                await asyncio.sleep(5)

    async def _handle_closed_order(self, order: dict) -> None:
        """
        Processa uma ordem fechada ou cancelada recebida via WebSocket:
        1. Filtra contra mensagens duplicadas.
        2. Identifica se a ordem corresponde a uma entrada (abertura) ou saída (fechamento) de posição.
        3. Se for entrada e cancelada, limpa locks/posições. Se for fechada (filled), apenas confirma abertura.
        4. Se for saída (fechada/cancelada), limpa locks/posições e atualiza a perda diária.
        """
        status = order.get("status")
        if status not in ["closed", "canceled"]:
            return

        order_id = order.get("id")
        client_order_id = order.get("clientOrderId")
        symbol = order.get("symbol")

        # Filtro de duplicidade de mensagens
        if (order_id and order_id in self._processed_order_ids) or (client_order_id and client_order_id in self._processed_order_ids):
            logger.debug(f"[Wallet] Ordem {order_id}/{client_order_id} já processada. Ignorando mensagem duplicada.")
            return

        # Busca a posição ativa na RAM para determinar o tipo de fluxo
        guid = None
        is_entry_order = False

        # Tenta identificar se o evento é da própria ordem de abertura (entry)
        for g, pos in list(storage.wallet.active_positions.items()):
            if g == client_order_id or pos.get("exchange_order_id") == order_id or (client_order_id and pos.get("exchange_order_id") == client_order_id):
                guid = g
                is_entry_order = True
                break

        # Se não for de abertura, tenta encontrar se é uma ordem de fecho (exit)
        if not guid:
            # 1. Tenta por ID de ordem pendente de fecho (mapeada no REST)
            if client_order_id and client_order_id in self._pending_close_orders:
                guid = self._pending_close_orders.get(client_order_id)
            elif order_id and order_id in self._pending_close_orders:
                guid = self._pending_close_orders.get(order_id)
            else:
                # 2. Tenta varrer active_positions por símbolo para fecho externo (ex: Stop Loss/Take Profit da exchange)
                for g, pos in list(storage.wallet.active_positions.items()):
                    if pos.get("symbol") == symbol:
                        guid = g
                        break

        # Se não encontramos nenhuma posição correspondente, não há o que processar
        if not guid or guid not in storage.wallet.active_positions:
            return

        pos = storage.wallet.active_positions[guid]
        symbol = pos["symbol"]

        if is_entry_order:
            # Se for a ordem de entrada:
            # - Se status for "closed" (filled): a posição abriu com sucesso. Não limpamos nada da RAM.
            # - Se status for "canceled": a abertura falhou ou foi cancelada, então limpamos tudo da RAM.
            if status == "closed":
                logger.info(f"[Wallet] Confirmação de abertura de posição para {symbol} (GUID: {guid}) via WebSocket.")
                if order_id:
                    self._processed_order_ids.add(order_id)
                if client_order_id:
                    self._processed_order_ids.add(client_order_id)
                return
            else:
                # CANCELED
                logger.warning(f"[Wallet] Abertura de posição para {symbol} (GUID: {guid}) foi cancelada na exchange.")

        # Fluxo de limpeza e encerramento de posição (para ordens de saída ou aberturas canceladas)
        if client_order_id:
            self._pending_close_orders.pop(client_order_id, None)
        if order_id:
            self._pending_close_orders.pop(order_id, None)

        # Registra nos processados para evitar reprocessamento
        if order_id:
            self._processed_order_ids.add(order_id)
        if client_order_id:
            self._processed_order_ids.add(client_order_id)

        # Limpa locks e posições ativas da RAM na hora
        await self._release_symbol_lock(symbol, guid)
        storage.wallet.active_positions.pop(guid, None)

        # Se uma ordem protetiva disparou, cancela a contraparte remanescente
        # para evitar ordens reduce-only órfãs depois do fechamento da posição.
        protection_order_ids = {
            "stop_loss_order_id": pos.get("stop_loss_order_id"),
            "take_profit_order_id": pos.get("take_profit_order_id"),
        }
        for key, protection_id in list(protection_order_ids.items()):
            if protection_id in {order_id, client_order_id}:
                protection_order_ids[key] = None
        await self._cancel_protection_orders(symbol, protection_order_ids)

        # Limita o tamanho do histórico de processados para evitar leak
        if len(self._processed_order_ids) > 10000:
            self._processed_order_ids.clear()

        # Calcula PnL definitivo
        entry_price = float(pos.get("price", 0.0))
        close_price = order.get("average") or order.get("price") or entry_price
        amount = float(order.get("amount") or pos.get("amount", 0.0))
        operation = pos.get("operation", "BUY")

        pnl = 0.0
        # Se a abertura foi cancelada, o PnL é 0
        if not is_entry_order or status != "canceled":
            if operation == "BUY":
                pnl = (close_price - entry_price) * amount
            else:
                pnl = (entry_price - close_price) * amount

        # Se for negativo, contabiliza a perda diária
        if pnl < 0:
            storage.wallet.daily_loss_counter += abs(pnl)

        logger.log(
            STATUS_LEVEL_NUM,
            f"[Wallet] Posição [{guid}] encerrada. Status: {status.upper()}. PnL: {pnl:.4f}",
        )

        payload = {
            "guid": guid,
            "status": "CLOSED" if status == "closed" else "CANCELED",
            "close_price": close_price,
            "close_timestamp": order.get("timestamp") or (time.time() * 1000.0),
            "realized_pnl": pnl,
            "reason": "TAKE_PROFIT" if pnl > 0 else "STOP_LOSS",
        }

        # Notifica todos os listeners registrados (Padrão Observer)
        for listener in self._order_close_listeners:
            try:
                if inspect.iscoroutinefunction(listener):
                    await listener(payload)
                else:
                    listener(payload)
            except Exception as cb_err:
                logger.error(
                    f"[Wallet] Erro ao disparar listener de fechamento de ordem: {cb_err}"
                )

    async def _watch_orders_loop(self) -> None:
        """Loop perpétuo de WebSocket para rastrear o fechamento de ordens."""
        logger.info("[Wallet] Loop watch_orders iniciado.")
        while self._is_running:
            try:
                orders = await self.exchange.watch_orders()
                for order in orders:
                    await self._handle_closed_order(order)
            except ccxt.NetworkError as e:
                logger.warning(f"[Wallet] Erro de rede no WebSocket watch_orders: {e}")
                await asyncio.sleep(5)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"[Wallet] Erro no loop watch_orders: {e}")
                await asyncio.sleep(5)

    async def execute_order(self, signal: dict) -> dict:
        """
        FASE B: Operação Ativa e Verificação de Risco
        Roteia o sinal (abertura ou fechamento) e executa o processamento correspondente.
        """
        target_guid = signal.get("target_guid")
        if target_guid:
            return await self._execute_close_order(signal)
        else:
            return await self._execute_open_order(signal)

    async def _execute_close_order(self, signal: dict) -> dict:
        """Processa e executa o sinal de fechamento de uma ordem/posição ativa."""
        guid = signal["guid"]
        target_guid = signal["target_guid"]

        # Busca a posição ativa na memória RAM
        pos = storage.wallet.active_positions.get(target_guid)
        if not pos:
            logger.warning(f"[Wallet] Solicitação de fecho rejeitada: posição {target_guid} não localizada na RAM.")
            return {
                "guid": guid,
                "status": "FAILED",
                "reason": "ORIGINAL_POSITION_NOT_FOUND",
            }

        symbol = pos["symbol"]
        amount = pos["amount"]
        operation = pos["operation"]

        # Define operação oposta para fechamento de posição
        close_side = "sell" if operation == "BUY" else "buy"

        # A posição original continua dona do lock durante o fechamento.
        await self._ensure_position_lock(symbol, target_guid)

        logger.info(
            f"[Wallet] Executando fecho de posição para {symbol} ({close_side.upper()}) - Qtd: {amount}"
        )

        try:
            # Verificação de latência de segurança na Wallet antes de fechar a ordem
            signal_timestamp = signal.get("timestamp")
            if signal_timestamp:
                max_latency_ms = self.config.system.max_signal_latency_ms
                latency_seconds = time.time() - float(signal_timestamp)
                if (latency_seconds * 1000.0) > max_latency_ms:
                    logger.error(
                        f"[Wallet] Ordem de fecho [{guid}] abortada: latência do sinal ({latency_seconds * 1000.0:.2f}ms) "
                        f"excede o limite de {max_latency_ms}ms antes do envio."
                    )
                    return {
                        "guid": guid,
                        "status": "FAILED",
                        "reason": "SIGNAL_OBSOLETE_BEFORE_SEND",
                    }

            order = await self.exchange.create_order(
                symbol=symbol,
                type="market",
                side=close_side,
                amount=amount,
            )

            order_id = order.get("id")
            # Mapeia o ID da ordem de fecho para que o WebSocket a reconcilie
            self._pending_close_orders[order_id] = target_guid
            if order.get("clientOrderId"):
                self._pending_close_orders[order.get("clientOrderId")] = target_guid

            # Calcula PnL provisório para o retorno imediato da API REST
            entry_price = float(pos.get("price", 0.0))
            close_price = float(order.get("price") or order.get("average") or signal["current_price"])

            pnl = 0.0
            if operation == "BUY":
                pnl = (close_price - entry_price) * amount
            else:
                pnl = (entry_price - close_price) * amount

            logger.log(
                STATUS_LEVEL_NUM,
                f"[Wallet] Ordem de fecho [{target_guid}] enviada com sucesso à Exchange. ID: {order_id}",
            )

            # Nota: a limpeza final dos locks/active_positions e incremento do drawdown diário
            # será feita de forma assíncrona pelo WebSocket (_watch_orders_loop) para evitar duplicidade.
            return {
                "guid": guid,
                "target_guid": target_guid,
                "status": "CLOSED",
                "close_price": close_price,
                "close_timestamp": order.get("timestamp") or (time.time() * 1000.0),
                "realized_pnl": pnl,
                "reason": "CLOSED_BY_SIGNAL",
            }

        except Exception as e:
            logger.error(f"[Wallet] Erro na exchange ao fechar posição {target_guid}: {e}")
            return {
                "guid": guid,
                "status": "FAILED",
                "reason": f"EXCHANGE_CLOSE_ERROR: {e}",
            }

    async def _create_protection_orders(
        self,
        guid: str,
        symbol: str,
        operation: str,
        amount: float,
        stop_loss: Optional[float],
        take_profit: Optional[float],
    ) -> Dict[str, Optional[str]]:
        """Cria ordens protetivas reduce-only para a posição recém-aberta."""
        close_side = "sell" if operation == "BUY" else "buy"
        protection_order_ids: Dict[str, Optional[str]] = {
            "stop_loss_order_id": None,
            "take_profit_order_id": None,
        }

        if stop_loss is None or float(stop_loss) <= 0:
            raise ValueError("STOP_LOSS_REQUIRED")

        try:
            sl_order = await self.exchange.create_order(
                symbol=symbol,
                type="market",
                side=close_side,
                amount=amount,
                price=None,
                params={
                    "stopLossPrice": float(stop_loss),
                    "reduceOnly": "true",
                },
            )
            protection_order_ids["stop_loss_order_id"] = sl_order.get("id")

            if take_profit is not None and float(take_profit) > 0:
                tp_order = await self.exchange.create_order(
                    symbol=symbol,
                    type="market",
                    side=close_side,
                    amount=amount,
                    price=None,
                    params={
                        "takeProfitPrice": float(take_profit),
                        "reduceOnly": "true",
                    },
                )
                protection_order_ids["take_profit_order_id"] = tp_order.get("id")
        except Exception:
            await self._cancel_protection_orders(symbol, protection_order_ids)
            raise

        return protection_order_ids

    async def _cancel_protection_orders(self, symbol: str, protection_order_ids: Dict[str, Optional[str]]) -> None:
        """Cancela ordens protetivas já criadas durante rollback de proteção."""
        for order_id in protection_order_ids.values():
            if not order_id:
                continue
            try:
                await self.exchange.cancel_order(order_id, symbol)
            except Exception as e:
                logger.warning(f"[Wallet] Falha ao cancelar ordem protetiva {order_id}: {e}")

    async def _emergency_close_unprotected_position(
        self,
        guid: str,
        symbol: str,
        operation: str,
        amount: float,
    ) -> None:
        """Fecha a mercado uma posição cuja criação de SL/TP falhou."""
        close_side = "sell" if operation == "BUY" else "buy"
        await self.exchange.create_order(
            symbol=symbol,
            type="market",
            side=close_side,
            amount=amount,
            params={"reduceOnly": "true"},
        )
        await self._release_symbol_lock(symbol, guid)
        storage.wallet.active_positions.pop(guid, None)

    def _build_attached_protection_params(
        self,
        stop_loss: Optional[float],
        take_profit: Optional[float],
    ) -> Dict[str, float]:
        """Monta os parâmetros de proteção anexada para create_order."""
        if stop_loss is None or float(stop_loss) <= 0:
            raise ValueError("STOP_LOSS_REQUIRED")

        params: Dict[str, float] = {"stopLossPrice": float(stop_loss)}
        if take_profit is not None and float(take_profit) > 0:
            params["takeProfitPrice"] = float(take_profit)
        return params

    def _extract_attached_protection_ids(self, order: dict) -> Dict[str, Optional[str]]:
        """Extrai IDs de SL/TP anexados quando a exchange os retorna no order payload."""
        stop_loss_payload = order.get("stopLoss")
        take_profit_payload = order.get("takeProfit")
        return {
            "stop_loss_order_id": order.get("stopLossOrderId") or (
                stop_loss_payload.get("id") if isinstance(stop_loss_payload, dict) else None
            ),
            "take_profit_order_id": order.get("takeProfitOrderId") or (
                take_profit_payload.get("id") if isinstance(take_profit_payload, dict) else None
            ),
        }

    def _stop_loss_exceeds_max_risk(
        self,
        operation: str,
        current_price: float,
        stop_loss: Optional[float],
    ) -> bool:
        """Valida se o SL informado implica risco maior que o máximo global."""
        if stop_loss is None or stop_loss <= 0 or current_price <= 0:
            return True

        max_sl_pct = self._risk_float("default_stop_loss_pct", 1.5)
        if operation == "BUY":
            max_allowed_sl = current_price * (1.0 - max_sl_pct / 100.0)
            return stop_loss < max_allowed_sl

        max_allowed_sl = current_price * (1.0 + max_sl_pct / 100.0)
        return stop_loss > max_allowed_sl

    async def _execute_open_order(self, signal: dict) -> dict:
        symbol = signal["symbol"]
        symbol_lock = await self._get_symbol_lock(symbol)
        async with symbol_lock:
            return await self._execute_open_order_locked(signal)

    async def _execute_open_order_locked(self, signal: dict) -> dict:
        """Processa e executa a abertura de uma nova ordem."""
        guid = signal["guid"]
        symbol = signal["symbol"]
        operation = str(signal["operation"]).upper()

        max_sim = self.config.global_risk.max_simultaneous_trades
        max_loss = self.config.global_risk.max_daily_loss_limit

        # 1. Trava de risco tripla + reserva de capacidade global.
        rejection_reason = await self._reserve_open_slot(symbol, guid, max_sim, max_loss)
        if rejection_reason:
            if rejection_reason == "LIMIT_SIMULTANEOUS_TRADES_EXCEEDED":
                logger.warning(
                    f"[Wallet] Ordem [{guid}] ignorada: limite de trades simultâneos ({max_sim}) atingido."
                )
            elif rejection_reason == "DAILY_LOSS_LIMIT_EXCEEDED":
                logger.warning(
                    f"[Wallet] Ordem [{guid}] ignorada: limite de perda diária ({max_loss}) excedido."
                )
            elif rejection_reason == "ASSET_LOCK_ACTIVE":
                logger.warning(
                    f"[Wallet] Ordem [{guid}] ignorada: lock ativo já existente para o símbolo {symbol}."
                )
            return {
                "guid": guid,
                "status": "IGNORED",
                "reason": rejection_reason,
            }

        try:
            # Verificação de latência de segurança na Wallet antes de processar/enviar a ordem
            signal_timestamp = signal.get("timestamp")
            if signal_timestamp:
                max_latency_ms = self.config.system.max_signal_latency_ms
                latency_seconds = time.time() - float(signal_timestamp)
                if (latency_seconds * 1000.0) > max_latency_ms:
                    logger.error(
                        f"[Wallet] Ordem [{guid}] abortada: latência do sinal ({latency_seconds * 1000.0:.2f}ms) "
                        f"excede o limite de {max_latency_ms}ms antes do envio."
                    )
                    await self._release_symbol_lock(symbol, guid)
                    return {
                        "guid": guid,
                        "status": "IGNORED",
                        "reason": "SIGNAL_OBSOLETE_BEFORE_SEND",
                    }

            # 2. Definição do Stop Loss e Take Profit
            current_price = float(signal["current_price"])
            ignore_fields = signal.get("ignore_fields", [])
            strategy_provided_stop_loss = False
            
            # Caso 1: Fechamento Manual (ignore_fields contendo stop_loss e take_profit)
            if "stop_loss" in ignore_fields and "take_profit" in ignore_fields:
                safety_pct = self._risk_float("default_safety_stop_loss_pct", 5.0)
                if operation == "BUY":
                    stop_loss = current_price * (1.0 - safety_pct / 100.0)
                else:
                    stop_loss = current_price * (1.0 + safety_pct / 100.0)
                take_profit = None
                logger.debug(f"[Wallet] Ordem manual configurada com Stop Loss de risco máximo: {stop_loss}")
            else:
                # Caso 2: Ordem normal (gerencia risco utilizando alvos informados ou padrão)
                sl_val = signal.get("stop_loss")
                if sl_val is not None and float(sl_val) > 0:
                    strategy_provided_stop_loss = True
                    stop_loss = float(sl_val)
                else:
                    # Target padrão
                    sl_pct = self._risk_float("default_stop_loss_pct", 1.5)
                    if operation == "BUY":
                        stop_loss = current_price * (1.0 - sl_pct / 100.0)
                    else:
                        stop_loss = current_price * (1.0 + sl_pct / 100.0)

                tp_val = signal.get("take_profit")
                if tp_val is not None and float(tp_val) > 0:
                    take_profit = float(tp_val)
                else:
                    # Target padrão
                    tp_pct = self._risk_float("default_take_profit_pct", 3.0)
                    if operation == "BUY":
                        take_profit = current_price * (1.0 + tp_pct / 100.0)
                    else:
                        take_profit = current_price * (1.0 - tp_pct / 100.0)

            if strategy_provided_stop_loss and self._stop_loss_exceeds_max_risk(operation, current_price, stop_loss):
                logger.warning(
                    f"[Wallet] Ordem [{guid}] ignorada: stop loss excede o risco máximo permitido."
                )
                await self._release_symbol_lock(symbol, guid)
                return {
                    "guid": guid,
                    "status": "IGNORED",
                    "reason": "STOP_LOSS_EXCEEDS_MAX_RISK",
                }

            # 3. Dimensionamento de Lote Dinâmico (Sizing)
            available_balance = storage.wallet.balance
            risk_pct = self.config.global_risk.trade_risk_percentage
            trade_value = available_balance * risk_pct

            if current_price <= 0:
                await self._release_symbol_lock(symbol, guid)
                return {
                    "guid": guid,
                    "status": "FAILED",
                    "reason": "INVALID_PRICE",
                }

            amount = trade_value / current_price

            # Valida contra os limites da Exchange
            try:
                market = self.exchange.market(symbol)
                min_amount = market.get("limits", {}).get("amount", {}).get("min") or 0.0
                min_cost = market.get("limits", {}).get("cost", {}).get("min") or 0.0
            except Exception:
                min_amount = 0.0
                min_cost = 0.0

            if amount < min_amount:
                amount = min_amount

            cost = amount * current_price
            if cost < min_cost:
                amount = min_cost / current_price

            # Checagem final de fundos
            if amount * current_price > available_balance:
                logger.warning(
                    f"[Wallet] Ordem [{guid}] ignorada: saldo insuficiente para atender lote mínimo. "
                    f"Saldo: {available_balance}, Requerido: {amount * current_price}"
                )
                await self._release_symbol_lock(symbol, guid)
                return {
                    "guid": guid,
                    "status": "IGNORED",
                    "reason": "INSUFFICIENT_BALANCE_FOR_MIN_NOTIONAL",
                }

            # Gravamos o estado temporário como "PENDING_OPEN" antes da execução na Exchange para
            # evitar ORIGINAL_POSITION_NOT_FOUND em caso de ordem de fechamento concorrente/muito rápida.
            storage.wallet.active_positions[guid] = {
                "guid": guid,
                "symbol": symbol,
                "amount": amount,
                "price": current_price,
                "operation": operation,
                "exchange_order_id": None,
                "status": "PENDING_OPEN",
                "stop_loss": stop_loss,
                "take_profit": take_profit,
                "strategy_name": signal.get("strategy_name"),
            }

            logger.info(
                f"[Wallet] Disparando ordem de mercado para {symbol} ({operation}) - Quantidade: {amount:.6f}"
            )

            use_attached_protection = (
                self._supports_attached_sl_tp
                and self._supports_stop_loss_price
                and (take_profit is None or self._supports_take_profit_price)
            )

            entry_params = {}
            if use_attached_protection:
                entry_params = self._build_attached_protection_params(stop_loss, take_profit)

            entry_kwargs = {
                "symbol": symbol,
                "type": "market",
                "side": operation.lower(),
                "amount": amount,
            }
            if entry_params:
                entry_kwargs["params"] = entry_params

            order = await self.exchange.create_order(**entry_kwargs)

            order_id = order.get("id")
            exec_price = order.get("price") or order.get("average") or current_price

            protection_order_ids: Dict[str, Optional[str]] = {
                "stop_loss_order_id": None,
                "take_profit_order_id": None,
            }

            if use_attached_protection:
                protection_order_ids = self._extract_attached_protection_ids(order)
                logger.info(f"[Wallet] Ordem [{guid}] aberta com SL/TP anexado na requisição de entrada.")
            else:
                try:
                    protection_order_ids = await self._create_protection_orders(
                        guid=guid,
                        symbol=symbol,
                        operation=operation,
                        amount=amount,
                        stop_loss=stop_loss,
                        take_profit=take_profit,
                    )
                except Exception as protection_err:
                    logger.critical(
                        f"[Wallet] Falha ao criar SL/TP para {guid}. Fechando posição desprotegida: {protection_err}"
                    )
                    await self._cancel_protection_orders(symbol, protection_order_ids)
                    try:
                        await self._emergency_close_unprotected_position(guid, symbol, operation, amount)
                    except Exception as close_err:
                        logger.critical(
                            f"[Wallet] Falha ao fechar posição desprotegida {guid}: {close_err}"
                        )
                        return {
                            "guid": guid,
                            "status": "FAILED",
                            "amount": amount,
                            "price": exec_price,
                            "exchange_order_id": order_id,
                            "reason": f"PROTECTION_ORDER_FAILED_EMERGENCY_CLOSE_FAILED: {protection_err}; {close_err}",
                        }
                    return {
                        "guid": guid,
                        "status": "FAILED",
                        "amount": amount,
                        "price": exec_price,
                        "exchange_order_id": order_id,
                        "reason": f"PROTECTION_ORDER_FAILED_POSITION_CLOSED: {protection_err}",
                    }

            # Atualiza no storage com os dados consolidados da Exchange
            storage.wallet.active_positions[guid].update({
                "amount": amount,
                "price": exec_price,
                "exchange_order_id": order_id,
                "status": "OPEN",
                **protection_order_ids,
            })
            await self._mark_position_open(symbol, guid)

            logger.log(
                STATUS_LEVEL_NUM,
                f"[Wallet] Ordem [{guid}] executada com sucesso. ID da exchange: {order_id}",
            )

            return {
                "guid": guid,
                "status": "EXECUTED",
                "amount": amount,
                "price": exec_price,
                "exchange_order_id": order_id,
                "reason": "ORDER_SUCCESS",
            }

        except ccxt.InsufficientFunds as e:
            await self._release_symbol_lock(symbol, guid)
            storage.wallet.active_positions.pop(guid, None)
            logger.error(f"[Wallet] Saldo insuficiente para {guid}: {e}")
            return {
                "guid": guid,
                "status": "FAILED",
                "reason": "EXCHANGE_INSUFFICIENT_FUNDS",
            }
        except ccxt.NetworkError as e:
            await self._release_symbol_lock(symbol, guid)
            storage.wallet.active_positions.pop(guid, None)
            logger.error(f"[Wallet] Erro de rede na execução de {guid}: {e}")
            return {
                "guid": guid,
                "status": "FAILED",
                "reason": f"NETWORK_ERROR: {e}",
            }
        except Exception as e:
            await self._release_symbol_lock(symbol, guid)
            storage.wallet.active_positions.pop(guid, None)
            logger.error(f"[Wallet] Erro na exchange ao executar {guid}: {e}")
            return {
                "guid": guid,
                "status": "FAILED",
                "reason": f"EXCHANGE_ERROR: {e}",
            }
        finally:
            await self._release_open_slot(guid)

    async def shutdown(self) -> None:
        """Encerra os loops WebSockets em background de forma limpa."""
        logger.log(STATUS_LEVEL_NUM, "[Wallet] A encerrar WalletController...")
        self._is_running = False

        if self._balance_task:
            self._balance_task.cancel()
        if self._orders_task:
            self._orders_task.cancel()

        for task in [self._balance_task, self._orders_task]:
            if task:
                try:
                    await task
                except asyncio.CancelledError:
                    pass
        logger.log(STATUS_LEVEL_NUM, "[Wallet] Loops do WalletController encerrados.")
