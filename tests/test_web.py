import asyncio
import pytest
from aiohttp import ClientSession
from core.web import TelemetryWebServer
from core.storage import storage


@pytest.fixture(autouse=True)
def reset_storage():
    """Reseta o estado do storage global para cada caso de teste."""
    storage.wallet.balance = 1000.0
    storage.wallet.daily_loss_counter = 0.0
    storage.wallet.simultaneous_trades = 0
    storage.wallet.active_locks.clear()
    storage.wallet.active_positions.clear()
    yield


@pytest.mark.asyncio
async def test_web_server_endpoints():
    """Valida que o servidor web inicializa, serve a página index e envia telemetria via WebSocket."""
    # Inicia o servidor web na porta 0 (porta efêmera livre no SO)
    server = TelemetryWebServer(host="127.0.0.1", port=0)
    await server.start()

    # Obtém a porta dinâmica alocada
    assert server.runner is not None
    port = server.runner.addresses[0][1]
    
    url = f"http://127.0.0.1:{port}"
    ws_url = f"ws://127.0.0.1:{port}/ws"

    async with ClientSession() as session:
        # 1. Testa a rota Index (HTTP /)
        async with session.get(url) as resp:
            assert resp.status == 200
            html_content = await resp.text()
            assert "ARSTrader" in html_content
            assert "Terminal de Telemetria" in html_content

        # 2. Testa a rota do WebSocket (/ws)
        async with session.ws_connect(ws_url) as ws:
            # Recebe o estado inicial
            msg = await ws.receive_json()
            assert msg["type"] == "state"
            assert "wallet" in msg["data"]
            assert msg["data"]["wallet"]["balance"] == 1000.0

            # Modifica um valor no storage para testar a notificação assíncrona
            storage.wallet.balance = 1500.50

            # O WebSocket deve receber a atualização em tempo real
            msg_update = await ws.receive_json()
            assert msg_update["type"] == "update"
            assert msg_update["path"] == "wallet.balance"
            assert msg_update["value"] == 1500.50

            # Mais uma modificação (locks de ativos)
            storage.wallet.active_locks["ETH/USDT"] = True

            msg_lock = await ws.receive_json()
            assert msg_lock["type"] == "update"
            assert msg_lock["path"] == "wallet.active_locks.ETH/USDT"
            assert msg_lock["value"] is True

    # Desliga o servidor
    await server.shutdown()
