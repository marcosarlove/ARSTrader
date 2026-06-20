"""
ARSTrader - Abstract Base Module Contract (base_module.py)
===========================================================
Infraestrutura comum para processos filhos de estratégia.

Esta classe não implementa lógica de trading. Ela padroniza lifecycle,
comunicação IPC com o Core, heartbeats, envio de ordens e encerramento limpo.
"""

from __future__ import annotations

import asyncio
import json
import logging
import logging.handlers
import os
import queue
import signal
import time
import uuid
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Awaitable, Dict, List, Optional, Set


logger = logging.getLogger("ARSTrader.Module")


class CoreTransportError(Exception):
    """Erro de transporte IPC com o Core."""


class CoreConnectionClosed(CoreTransportError):
    """O Core fechou o socket IPC antes de responder."""


class CoreOrderResponseTimeout(CoreTransportError):
    """O Core não respondeu uma ordem dentro do timeout local configurado."""


class CoreProtocolError(CoreTransportError):
    """O Core respondeu com payload ilegível ou fora do protocolo esperado."""


class BaseStrategyModule(ABC):
    """
    Contrato abstrato para estratégias isoladas.

    O Core continua sendo dono de carteira, risco e execução. A estratégia só
    envia sinais e consome respostas explícitas do Core.
    """

    def __init__(
        self,
        *,
        name: str,
        core_host: str,
        core_port: int,
        heartbeat_interval: float,
        order_response_timeout: float = 300.0,
        log_level: int = logging.INFO,
        log_max_bytes: int = 50 * 1024 * 1024,
        log_backup_count: int = 5,
    ):
        if heartbeat_interval <= 0:
            raise ValueError("heartbeat_interval deve ser maior que zero.")
        if order_response_timeout <= 0:
            raise ValueError("order_response_timeout deve ser maior que zero.")

        self.name = name.strip().lower()
        self.core_host = core_host
        self.core_port = int(core_port)
        self.heartbeat_interval = float(heartbeat_interval)
        self.order_response_timeout = float(order_response_timeout)
        self.pid = os.getpid()
        self.module_dir = Path("modules") / self.name
        self.log_file = self.module_dir / "logs" / f"{self.name}.log"

        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._reader_task: Optional[asyncio.Task] = None
        self._is_running = False
        self._ready = False
        self._on_start_completed = False
        self._fatal_error_sent = False
        self._shutdown_event = asyncio.Event()
        self._write_lock = asyncio.Lock()
        self._order_lock = asyncio.Lock()
        self._pending_order_futures: Dict[str, asyncio.Future] = {}
        self._background_tasks: Set[asyncio.Task] = set()
        self._log_queue: Optional[queue.Queue] = None
        self._log_listener: Optional[logging.handlers.QueueListener] = None
        self._log_queue_handler: Optional[logging.handlers.QueueHandler] = None
        self.logger = self._setup_module_logger(
            level=log_level,
            max_bytes=log_max_bytes,
            backup_count=log_backup_count,
        )

    async def on_start(self) -> None:
        """Hook opcional chamado depois de BOOT e antes de READY."""

    async def on_stop(self) -> None:
        """Hook opcional chamado durante shutdown normal."""

    @abstractmethod
    async def run_strategy(self) -> None:
        """Loop principal da estratégia concreta."""

    async def start(self) -> int:
        """Executa o ciclo de vida completo do subprocesso de estratégia."""
        self._install_signal_handlers()
        self._is_running = True

        try:
            await self._connect()
            await self._send_control("BOOT", "process booted")
            await self.on_start()
            self._on_start_completed = True
            self._ready = True
            await self._send_control("READY", "strategy ready")
            self.create_background_task(self._heartbeat_loop(), name="heartbeat", critical=True)
            await self.run_strategy()
            if not self._shutdown_event.is_set():
                self.logger.warning(
                    "[%s] run_strategy terminou sem pedido explícito de shutdown; aguardando encerramento.",
                    self.name,
                )
                await self._shutdown_event.wait()
            return 0
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            await self._send_fatal_error(exc)
            return 1
        finally:
            await self.shutdown()

    async def shutdown(self) -> None:
        """Encerra tasks e socket IPC. Só envia SHUTDOWN se não houve ERROR fatal."""
        if not self._is_running and self._writer is None:
            self._shutdown_module_logger()
            return

        self._is_running = False
        self._ready = False
        self._shutdown_event.set()

        for task in list(self._background_tasks):
            task.cancel()
        if self._background_tasks:
            await asyncio.gather(*self._background_tasks, return_exceptions=True)
        self._background_tasks.clear()

        if self._on_start_completed:
            try:
                await asyncio.wait_for(self.on_stop(), timeout=5.0)
            except asyncio.TimeoutError:
                self.logger.error("[%s] timeout estourado no hook on_stop.", self.name)
            except Exception as exc:
                self.logger.error("[%s] erro em on_stop: %s", self.name, exc)
            finally:
                self._on_start_completed = False

        if not self._fatal_error_sent:
            try:
                await asyncio.wait_for(
                    self._send_control("SHUTDOWN", "normal shutdown"),
                    timeout=2.0,
                )
            except Exception:
                pass

        await self._close_writer()
        self._shutdown_module_logger()

    def request_shutdown(self) -> None:
        """Solicita encerramento normal do módulo sem bloquear o loop."""
        self._is_running = False
        self._ready = False
        self._shutdown_event.set()

    def create_background_task(
        self,
        coro: Awaitable[Any],
        *,
        name: str,
        critical: bool = True,
    ) -> asyncio.Task:
        """Cria task em background com política explícita de criticidade."""
        task = asyncio.create_task(coro, name=f"{self.name}:{name}")
        task._arstrader_critical = critical  # type: ignore[attr-defined]
        self._background_tasks.add(task)
        task.add_done_callback(self._handle_background_task_done)
        return task

    async def open_order(
        self,
        *,
        symbol: str,
        exchange: str,
        operation: str,
        price: float,
        market: str = "FUTURES",
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        ignore_fields: Optional[List[str]] = None,
        guid: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Envia sinal de abertura para o Core."""
        return await self.send_order(
            guid=guid or str(uuid.uuid4()),
            symbol=symbol,
            exchange=exchange,
            operation=operation,
            price=price,
            market=market,
            stop_loss=stop_loss,
            take_profit=take_profit,
            target_guid=None,
            ignore_fields=ignore_fields,
        )

    async def close_order(
        self,
        *,
        target_guid: str,
        symbol: str,
        exchange: str,
        operation: str,
        price: float,
        market: str = "FUTURES",
        guid: Optional[str] = None,
        ignore_fields: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Envia sinal de fechamento dinâmico para o Core."""
        return await self.send_order(
            guid=guid or str(uuid.uuid4()),
            target_guid=target_guid,
            symbol=symbol,
            exchange=exchange,
            operation=operation,
            price=price,
            market=market,
            ignore_fields=ignore_fields or ["stop_loss", "take_profit"],
        )

    async def send_order(
        self,
        *,
        guid: str,
        symbol: str,
        exchange: str,
        operation: str,
        price: float,
        market: str = "FUTURES",
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        target_guid: Optional[str] = None,
        ignore_fields: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Envia ORDER e retorna exatamente a resposta do Core."""
        self._ensure_connected()
        operation = operation.strip().upper()
        payload = self._build_order_payload(
            guid=guid,
            target_guid=target_guid,
            symbol=symbol,
            exchange=exchange,
            operation=operation,
            market=market,
            price=price,
            stop_loss=stop_loss,
            take_profit=take_profit,
            ignore_fields=ignore_fields,
        )

        loop = asyncio.get_running_loop()
        response_future = loop.create_future()
        if guid in self._pending_order_futures:
            raise ValueError(f"guid duplicado pendente: {guid}")
        self._pending_order_futures[guid] = response_future

        try:
            await self._send_json(payload)
            try:
                return await asyncio.wait_for(
                    response_future,
                    timeout=self.order_response_timeout,
                )
            except asyncio.TimeoutError as exc:
                if self._pending_order_futures.pop(guid, None) is response_future:
                    response_future.cancel()
                raise CoreOrderResponseTimeout(
                    f"Core não respondeu a ordem {guid} em {self.order_response_timeout:.1f}s"
                ) from exc
        except Exception:
            if self._pending_order_futures.get(guid) is response_future:
                self._pending_order_futures.pop(guid, None)
            raise

    def _build_order_payload(
        self,
        *,
        guid: str,
        target_guid: Optional[str],
        symbol: str,
        exchange: str,
        operation: str,
        market: str,
        price: float,
        stop_loss: Optional[float],
        take_profit: Optional[float],
        ignore_fields: Optional[List[str]],
    ) -> Dict[str, Any]:
        if not guid:
            raise ValueError("guid obrigatório.")
        if not symbol:
            raise ValueError("symbol obrigatório.")
        if not exchange:
            raise ValueError("exchange obrigatória.")
        if operation not in {"BUY", "SELL"}:
            raise ValueError("operation deve ser BUY ou SELL.")
        if float(price) <= 0:
            raise ValueError("price deve ser maior que zero.")

        fields_to_ignore = ignore_fields or []
        if not isinstance(fields_to_ignore, list):
            raise ValueError("ignore_fields deve ser uma lista.")

        payload: Dict[str, Any] = {
            "type": "ORDER",
            "guid": str(guid),
            "strategy_name": self.name,
            "symbol": str(symbol).upper(),
            "exchange": str(exchange).lower(),
            "operation": operation,
            "market": str(market).upper(),
            "price": float(price),
            "timestamp": time.time(),
            "ignore_fields": fields_to_ignore,
        }
        if target_guid:
            payload["target_guid"] = str(target_guid)
        if stop_loss is not None:
            payload["stop_loss"] = float(stop_loss)
        if take_profit is not None:
            payload["take_profit"] = float(take_profit)
        return payload

    async def _connect(self) -> None:
        self._reader, self._writer = await asyncio.open_connection(
            self.core_host,
            self.core_port,
        )
        self._reader_task = asyncio.create_task(
            self._reader_loop(self._reader),
            name=f"{self.name}:ipc-reader",
        )

    def _ensure_connected(self) -> None:
        if self._reader is None or self._writer is None or self._writer.is_closing():
            raise CoreConnectionClosed("Socket IPC com o Core não está conectado.")
        if self._reader_task is not None and self._reader_task.done():
            raise CoreConnectionClosed("Leitor IPC com o Core não está ativo.")

    async def _send_control(self, action: str, details: str = "") -> None:
        payload = {
            "type": "CONTROL",
            "action": action.strip().upper(),
            "strategy_name": self.name,
            "pid": self.pid,
            "details": details,
        }
        await self._send_json(payload)

    async def _send_json(self, payload: Dict[str, Any]) -> None:
        self._ensure_connected()
        assert self._writer is not None
        encoded = json.dumps(payload, separators=(",", ":")).encode("utf-8") + b"\n"
        async with self._write_lock:
            self._writer.write(encoded)
            await self._writer.drain()

    async def _heartbeat_loop(self) -> None:
        while self._is_running and self._ready:
            await self._send_control("HEARTBEAT")
            await asyncio.sleep(self.heartbeat_interval)

    async def _reader_loop(self, reader: asyncio.StreamReader) -> None:
        """Consome respostas do Core e entrega cada payload à Future da ordem."""
        try:
            while True:
                line = await reader.readline()
                if not line:
                    raise CoreConnectionClosed("Core fechou o socket IPC.")

                try:
                    response = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError as exc:
                    raise CoreProtocolError("Resposta do Core não é JSON válido.") from exc

                if not isinstance(response, dict):
                    raise CoreProtocolError("Resposta do Core não é um objeto JSON.")

                self._resolve_order_response(response)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            self._fail_pending_orders(exc)
            if self._is_running:
                self.logger.error("[%s] leitor IPC falhou: %s", self.name, exc)

    def _resolve_order_response(self, response: Dict[str, Any]) -> None:
        guid = response.get("guid")
        future: Optional[asyncio.Future] = None

        if guid is not None:
            future = self._pending_order_futures.pop(str(guid), None)

        if future is None:
            self.logger.warning("[%s] resposta IPC sem ordem pendente: %s", self.name, response)
            return
        if not future.done():
            future.set_result(response)

    def _fail_pending_orders(self, exc: BaseException) -> None:
        for future in self._pending_order_futures.values():
            if not future.done():
                future.set_exception(exc)
        self._pending_order_futures.clear()

    def _handle_background_task_done(self, task: asyncio.Task) -> None:
        self._background_tasks.discard(task)
        if task.cancelled():
            return

        exc = task.exception()
        if exc is None:
            return

        critical = bool(getattr(task, "_arstrader_critical", True))
        self.logger.error("[%s] task %s falhou: %s", self.name, task.get_name(), exc)
        if critical and self._is_running:
            asyncio.create_task(self._handle_fatal_background_error(exc))

    async def _handle_fatal_background_error(self, exc: BaseException) -> None:
        await self._send_fatal_error(exc)
        self._is_running = False
        self._shutdown_event.set()

    async def _send_fatal_error(self, exc: BaseException) -> None:
        if self._fatal_error_sent:
            return
        self._fatal_error_sent = True
        try:
            await self._send_control("ERROR", f"{exc.__class__.__name__}: {exc}")
        except Exception:
            pass

    async def _close_writer(self) -> None:
        self._fail_pending_orders(CoreConnectionClosed("Socket IPC encerrado."))
        reader_task = self._reader_task
        self._reader_task = None
        if reader_task and not reader_task.done():
            reader_task.cancel()
            try:
                await asyncio.wait_for(
                    asyncio.gather(reader_task, return_exceptions=True),
                    timeout=1.0,
                )
            except asyncio.TimeoutError:
                pass

        if self._writer is None:
            self._reader = None
            return
        writer = self._writer
        self._writer = None
        self._reader = None
        try:
            if not writer.is_closing():
                writer.close()
            await asyncio.wait_for(writer.wait_closed(), timeout=2.0)
        except Exception:
            pass

    def _install_signal_handlers(self) -> None:
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self.request_shutdown)
            except (NotImplementedError, RuntimeError):
                pass

    def _setup_module_logger(
        self,
        *,
        level: int,
        max_bytes: int,
        backup_count: int,
    ) -> logging.Logger:
        """Inicializa logger não-bloqueante e isolado dentro do diretório do módulo."""
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        module_logger = logging.getLogger(f"ARSTrader.{self.name}")
        module_logger.setLevel(logging.DEBUG)
        module_logger.propagate = False
        module_logger.disabled = False

        for handler in list(module_logger.handlers):
            module_logger.removeHandler(handler)
            handler.close()

        self._log_queue = queue.Queue()
        file_handler = logging.handlers.RotatingFileHandler(
            filename=str(self.log_file),
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

        self._log_listener = logging.handlers.QueueListener(
            self._log_queue,
            file_handler,
            respect_handler_level=True,
        )
        self._log_listener.start()

        self._log_queue_handler = logging.handlers.QueueHandler(self._log_queue)
        self._log_queue_handler.setLevel(logging.DEBUG)
        module_logger.addHandler(self._log_queue_handler)
        return module_logger

    def _shutdown_module_logger(self) -> None:
        """Escoa e fecha o logger próprio do módulo."""
        if self._log_queue_handler:
            self.logger.removeHandler(self._log_queue_handler)
            self._log_queue_handler.close()
            self._log_queue_handler = None

        if self._log_listener:
            self._log_listener.stop()
            self._log_listener = None
        self._log_queue = None

        for handler in list(self.logger.handlers):
            self.logger.removeHandler(handler)
            handler.close()
        self.logger.disabled = True
