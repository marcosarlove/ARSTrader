import asyncio
import json
import socket
import pytest
from unittest.mock import AsyncMock, MagicMock
from core.server import SignalServer


@pytest.fixture
def unused_port():
    """Retorna uma porta TCP livre local para os testes do servidor."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    port = s.getsockname()[1]
    s.close()
    return port


@pytest.mark.asyncio
async def test_signal_server_start_and_shutdown(unused_port):
    """Verifica se o servidor inicia e para de forma limpa, fechando conexões."""
    control_mock = MagicMock()
    order_mock = AsyncMock()

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    await server.start()
    assert server._is_running is True

    # Tenta conectar um cliente
    reader, writer = await asyncio.open_connection("127.0.0.1", unused_port)
    assert len(server._active_connections) == 1

    # Desliga o servidor
    await server.shutdown()
    assert server._is_running is False
    assert len(server._active_connections) == 0

    # Tenta fechar o escritor do cliente se ainda estiver aberto
    writer.close()
    try:
        await writer.wait_closed()
    except Exception:
        pass


@pytest.mark.asyncio
async def test_signal_server_control_sync_callback(unused_port):
    """Testa o disparo correto do callback síncrono de controle."""
    control_mock = MagicMock()
    order_mock = AsyncMock()

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    await server.start()

    reader, writer = await asyncio.open_connection("127.0.0.1", unused_port)
    
    # Envia payload de CONTROL (HEARTBEAT)
    payload = {
        "type": "CONTROL",
        "action": "HEARTBEAT",
        "strategy_name": "morningstar",
        "pid": 9999,
        "details": "heartbeat normal"
    }
    writer.write(f"{json.dumps(payload)}\n".encode('utf-8'))
    await writer.drain()

    # Aguarda o processamento da mensagem
    await asyncio.sleep(0.05)

    control_mock.assert_called_once_with({
        "type": "CONTROL",
        "action": "HEARTBEAT",
        "strategy_name": "morningstar",
        "pid": 9999,
        "details": "heartbeat normal"
    })

    writer.close()
    await writer.wait_closed()
    await server.shutdown()


@pytest.mark.asyncio
async def test_signal_server_control_async_callback(unused_port):
    """Testa o disparo correto do callback assíncrono de controle."""
    control_mock = AsyncMock()
    order_mock = AsyncMock()

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    await server.start()

    reader, writer = await asyncio.open_connection("127.0.0.1", unused_port)
    
    payload = {
        "type": "CONTROL",
        "action": "READY",
        "strategy_name": "eveningstar",
        "pid": 8888,
        "details": "tudo pronto"
    }
    writer.write(f"{json.dumps(payload)}\n".encode('utf-8'))
    await writer.drain()

    await asyncio.sleep(0.05)

    control_mock.assert_called_once_with({
        "type": "CONTROL",
        "action": "READY",
        "strategy_name": "eveningstar",
        "pid": 8888,
        "details": "tudo pronto"
    })

    writer.close()
    await writer.wait_closed()
    await server.shutdown()


@pytest.mark.asyncio
async def test_signal_server_order_callback(unused_port):
    """Testa o disparo correto do callback de ordem (assíncrono por design)."""
    control_mock = MagicMock()
    
    async def mock_on_order(payload, promise):
        promise.set_result({"status": "SUCCESS"})
        
    order_mock = AsyncMock(side_effect=mock_on_order)

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    await server.start()

    reader, writer = await asyncio.open_connection("127.0.0.1", unused_port)
    
    import time
    payload = {
        "type": "ORDER",
        "guid": "test-guid-123",
        "strategy_name": "morningstar",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "market": "FUTURES",
        "exchange": "binance",
        "price": 68000.0,
        "timestamp": time.time(),
        "amount": 0.01,
        "wallet_balance_before": 1000.0
    }
    writer.write(f"{json.dumps(payload)}\n".encode('utf-8'))
    await writer.drain()

    await asyncio.sleep(0.05)

    order_mock.assert_called_once()
    called_args = order_mock.call_args[0]
    assert called_args[0]["guid"] == payload["guid"]
    assert called_args[0]["current_price"] == payload["price"]
    assert called_args[0]["operation"] == payload["operation"]
    assert isinstance(called_args[1], asyncio.Future)

    writer.close()
    await writer.wait_closed()
    await server.shutdown()


@pytest.mark.asyncio
async def test_signal_server_invalid_payloads(unused_port):
    """Verifica se payloads malformados ou tipos desconhecidos são tratados sem quebrar o servidor."""
    control_mock = MagicMock()
    order_mock = AsyncMock()

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    await server.start()

    reader, writer = await asyncio.open_connection("127.0.0.1", unused_port)
    
    # 1. Envia JSON corrompido
    writer.write(b"corrupted json string \n")
    # 2. Envia payload sem campos obrigatórios (Falta tipo e estratégia)
    writer.write(b'{"some_key": "some_value"}\n')
    # 3. Envia tipo de mensagem desconhecido
    writer.write(b'{"type": "UNKNOWN_ACTION", "strategy_name": "morningstar"}\n')
    await writer.drain()

    await asyncio.sleep(0.05)

    # Nenhum callback deve ter sido chamado
    control_mock.assert_not_called()
    order_mock.assert_not_called()

    writer.close()
    await writer.wait_closed()
    await server.shutdown()


@pytest.mark.asyncio
async def test_signal_server_bind_failure(unused_port):
    """Verifica se tentar rodar o servidor em uma porta já ocupada lança erro apropriado."""
    control_mock = MagicMock()
    order_mock = AsyncMock()

    # Ocupa a porta abrindo um socket TCP
    occupier = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    occupier.bind(('127.0.0.1', unused_port))
    occupier.listen(1)

    server = SignalServer(
        host="127.0.0.1",
        port=unused_port,
        on_control_cb=control_mock,
        on_order_cb=order_mock
    )

    with pytest.raises(Exception):
        await server.start()

    occupier.close()
