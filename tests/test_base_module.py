import asyncio
import json
import socket
from pathlib import Path

import pytest

from modules.base_module import BaseStrategyModule, CoreOrderResponseTimeout


class DummyModule(BaseStrategyModule):
    def __init__(self, *args, run_event=None, auto_shutdown=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.run_event = run_event
        self.auto_shutdown = auto_shutdown
        self.result = None

    async def run_strategy(self) -> None:
        if self.run_event:
            await self.run_event.wait()
        if self.auto_shutdown:
            self.request_shutdown()


class OrderModule(BaseStrategyModule):
    async def run_strategy(self) -> None:
        self.result = await self.open_order(
            guid="g-open",
            symbol="BTC/USDT",
            exchange="binance",
            operation="BUY",
            price=65000.0,
            market="FUTURES",
            stop_loss=64000.0,
            take_profit=67000.0,
        )
        self.request_shutdown()


class CloseModule(BaseStrategyModule):
    async def run_strategy(self) -> None:
        self.result = await self.close_order(
            guid="g-close",
            target_guid="g-open",
            symbol="BTC/USDT",
            exchange="binance",
            operation="SELL",
            price=65100.0,
        )
        self.request_shutdown()


class FatalModule(BaseStrategyModule):
    async def run_strategy(self) -> None:
        raise RuntimeError("boom")


class StopProbeModule(BaseStrategyModule):
    def __init__(self, *args, stop_delay=0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.stop_delay = stop_delay
        self.stop_called = False

    async def on_stop(self) -> None:
        if self.stop_delay:
            await asyncio.sleep(self.stop_delay)
        self.stop_called = True

    async def run_strategy(self) -> None:
        self.request_shutdown()


@pytest.fixture
def unused_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


async def _run_ipc_server(port, received, order_response=None, stop_after=3):
    async def handle(reader, writer):
        try:
            while True:
                line = await reader.readline()
                if not line:
                    break
                payload = json.loads(line.decode("utf-8"))
                received.append(payload)
                if payload.get("type") == "ORDER" and order_response is not None:
                    writer.write(json.dumps(order_response).encode("utf-8") + b"\n")
                    await writer.drain()
                if len(received) >= stop_after:
                    break
        finally:
            writer.close()
            await writer.wait_closed()

    server = await asyncio.start_server(handle, "127.0.0.1", port)
    return server


async def _run_late_response_server(port, received):
    async def delayed_response(writer, payload):
        await asyncio.sleep(0.05)
        writer.write(
            json.dumps({"status": "LATE", "guid": payload["guid"]}).encode("utf-8") + b"\n"
        )
        await writer.drain()

    async def handle(reader, writer):
        delayed_tasks = []
        try:
            while True:
                line = await reader.readline()
                if not line:
                    break
                payload = json.loads(line.decode("utf-8"))
                received.append(payload)
                if payload.get("type") != "ORDER":
                    continue

                if payload["guid"] == "g-timeout":
                    delayed_tasks.append(asyncio.create_task(delayed_response(writer, payload)))
                    continue

                writer.write(
                    json.dumps({"status": "EXECUTED", "guid": payload["guid"]}).encode("utf-8")
                    + b"\n"
                )
                await writer.drain()
        finally:
            if delayed_tasks:
                await asyncio.gather(*delayed_tasks, return_exceptions=True)
            writer.close()
            await writer.wait_closed()

    server = await asyncio.start_server(handle, "127.0.0.1", port)
    return server


async def _run_response_without_guid_server(port, received):
    async def handle(reader, writer):
        try:
            while True:
                line = await reader.readline()
                if not line:
                    break
                payload = json.loads(line.decode("utf-8"))
                received.append(payload)
                if payload.get("type") == "ORDER":
                    writer.write(json.dumps({"status": "EXECUTED"}).encode("utf-8") + b"\n")
                    await writer.drain()
        finally:
            writer.close()
            await writer.wait_closed()

    server = await asyncio.start_server(handle, "127.0.0.1", port)
    return server


@pytest.mark.asyncio
async def test_base_module_lifecycle_starts_heartbeat_after_ready(unused_port):
    received = []
    server = await _run_ipc_server(unused_port, received, stop_after=4)
    run_event = asyncio.Event()
    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=0.01,
        run_event=run_event,
    )

    task = asyncio.create_task(module.start())
    await asyncio.sleep(0.05)
    run_event.set()
    assert await task == 0

    server.close()
    await server.wait_closed()

    actions = [p.get("action") for p in received if p.get("type") == "CONTROL"]
    assert actions[0] == "BOOT"
    assert actions[1] == "READY"
    assert "HEARTBEAT" in actions[2:]


@pytest.mark.asyncio
async def test_base_module_waits_for_shutdown_when_strategy_returns(unused_port):
    received = []
    server = await _run_ipc_server(unused_port, received, stop_after=10)
    run_event = asyncio.Event()
    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
        run_event=run_event,
        auto_shutdown=False,
    )

    task = asyncio.create_task(module.start())
    await asyncio.sleep(0.05)
    run_event.set()
    await asyncio.sleep(0.05)
    assert not task.done()

    module.request_shutdown()
    assert await asyncio.wait_for(task, timeout=1.0) == 0

    server.close()
    await server.wait_closed()

    actions = [p.get("action") for p in received if p.get("type") == "CONTROL"]
    assert "SHUTDOWN" in actions


@pytest.mark.asyncio
async def test_base_module_open_order_schema_and_response(unused_port):
    received = []
    response = {"status": "EXECUTED", "guid": "g-open", "amount": 0.01}
    server = await _run_ipc_server(unused_port, received, order_response=response, stop_after=3)

    module = OrderModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
    )

    assert await module.start() == 0
    assert module.result == response

    server.close()
    await server.wait_closed()

    order = next(p for p in received if p.get("type") == "ORDER")
    assert order["guid"] == "g-open"
    assert order["strategy_name"] == "morningstar"
    assert order["symbol"] == "BTC/USDT"
    assert order["exchange"] == "binance"
    assert order["operation"] == "BUY"
    assert order["price"] == 65000.0
    assert order["stop_loss"] == 64000.0
    assert order["take_profit"] == 67000.0
    assert "timestamp" in order


@pytest.mark.asyncio
async def test_base_module_close_order_dynamic_schema(unused_port):
    received = []
    response = {"status": "CLOSED", "guid": "g-close", "target_guid": "g-open"}
    server = await _run_ipc_server(unused_port, received, order_response=response, stop_after=3)

    module = CloseModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
    )

    assert await module.start() == 0
    assert module.result == response

    server.close()
    await server.wait_closed()

    order = next(p for p in received if p.get("type") == "ORDER")
    assert order["guid"] == "g-close"
    assert order["target_guid"] == "g-open"
    assert order["operation"] == "SELL"
    assert order["ignore_fields"] == ["stop_loss", "take_profit"]


@pytest.mark.asyncio
async def test_base_module_order_timeout_is_local_exception(unused_port):
    received = []
    server = await _run_ipc_server(unused_port, received, order_response=None, stop_after=3)

    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
        order_response_timeout=0.01,
    )
    await module._connect()

    with pytest.raises(CoreOrderResponseTimeout):
        await module.open_order(
            guid="g-timeout",
            symbol="BTC/USDT",
            exchange="binance",
            operation="BUY",
            price=65000.0,
        )

    await module.shutdown()
    server.close()
    await server.wait_closed()
    assert not any(p.get("action") == "ERROR" for p in received)


@pytest.mark.asyncio
async def test_base_module_does_not_call_on_stop_when_connect_fails(unused_port):
    module = StopProbeModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
    )

    assert await module.start() == 1
    assert module.stop_called is False


@pytest.mark.asyncio
async def test_base_module_ignores_late_timed_out_response(unused_port):
    received = []
    server = await _run_late_response_server(unused_port, received)
    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
        order_response_timeout=0.01,
    )
    await module._connect()

    with pytest.raises(CoreOrderResponseTimeout):
        await module.open_order(
            guid="g-timeout",
            symbol="BTC/USDT",
            exchange="binance",
            operation="BUY",
            price=65000.0,
        )

    await asyncio.sleep(0.08)
    module.order_response_timeout = 1.0
    response = await module.open_order(
        guid="g-next",
        symbol="ETH/USDT",
        exchange="binance",
        operation="BUY",
        price=3500.0,
    )

    await module.shutdown()
    server.close()
    await server.wait_closed()

    assert response == {"status": "EXECUTED", "guid": "g-next"}


@pytest.mark.asyncio
async def test_base_module_requires_guid_to_resolve_order_response(unused_port):
    received = []
    server = await _run_response_without_guid_server(unused_port, received)
    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
        order_response_timeout=0.01,
    )
    await module._connect()

    with pytest.raises(CoreOrderResponseTimeout):
        await module.open_order(
            guid="g-strict",
            symbol="BTC/USDT",
            exchange="binance",
            operation="BUY",
            price=65000.0,
        )

    await module.shutdown()
    server.close()
    await server.wait_closed()
    assert module._pending_order_futures == {}


@pytest.mark.asyncio
async def test_base_module_on_stop_timeout_does_not_block_shutdown(unused_port):
    received = []
    server = await _run_ipc_server(unused_port, received, stop_after=3)
    module = StopProbeModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
        stop_delay=10.0,
    )

    assert await asyncio.wait_for(module.start(), timeout=7.0) == 0

    server.close()
    await server.wait_closed()
    assert module.stop_called is False


@pytest.mark.asyncio
async def test_base_module_fatal_exception_sends_error_not_shutdown(unused_port):
    received = []
    server = await _run_ipc_server(unused_port, received, stop_after=3)

    module = FatalModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=unused_port,
        heartbeat_interval=1.0,
    )

    assert await module.start() == 1
    server.close()
    await server.wait_closed()

    actions = [p.get("action") for p in received if p.get("type") == "CONTROL"]
    assert "BOOT" in actions
    assert "READY" in actions
    assert "ERROR" in actions
    assert "SHUTDOWN" not in actions


@pytest.mark.asyncio
async def test_base_module_has_isolated_non_blocking_log_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    module = DummyModule(
        name="morningstar",
        core_host="127.0.0.1",
        core_port=9999,
        heartbeat_interval=1.0,
    )
    module.logger.info("mensagem de teste")
    await module.shutdown()

    log_file = Path("modules/morningstar/logs/morningstar.log")
    assert log_file.exists()
    assert "mensagem de teste" in log_file.read_text(encoding="utf-8")
