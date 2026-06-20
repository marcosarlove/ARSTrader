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


@pytest.mark.asyncio
async def test_web_server_security_and_config():
    """Valida fluxos de login, sessao e edicao de configuracao com mock do orchestrator."""
    from unittest.mock import AsyncMock, MagicMock
    from aiohttp import ClientSession
    import bcrypt

    mock_db = MagicMock()
    # Mocking the session factory query for UserModel
    mock_db.session_factory = MagicMock()
    mock_session = AsyncMock()
    
    mock_session_ctx = AsyncMock()
    mock_session_ctx.__aenter__.return_value = mock_session
    mock_db.session_factory.return_value = mock_session_ctx

    # Mock user object returning from session.execute
    mock_user = MagicMock()
    mock_user.username = "admin"
    mock_user.password_hash = bcrypt.hashpw(b"adminpass", bcrypt.gensalt()).decode('utf-8')
    
    mock_result = MagicMock()
    mock_result.scalar_one_or_none.return_value = mock_user
    mock_session.execute.return_value = mock_result

    # Mock ConfigManager
    mock_config = MagicMock()
    mock_config.yaml_data = {
        "system": {"environment": "sandbox", "heartbeat_timeout": 5, "max_signal_latency_ms": 50},
        "web_server": {"host": "127.0.0.1", "port": 8080},
        "global_risk": {"execution_exchange": "binance", "max_daily_loss_pct": 2.0, "max_daily_loss_limit": 100.0, "max_simultaneous_trades": 3, "trade_risk_percentage": 0.1, "default_stop_loss_pct": 1.5, "default_take_profit_pct": 3.0, "default_safety_stop_loss_pct": 5.0},
        "exchanges": {"binance": {"enabled": True, "api_key": "key", "secret": "sec"}},
        "modules": {"morningstar": {"enabled": True, "path": "path", "class_name": "class"}}
    }
    mock_config.global_risk.execution_exchange = "binance"
    mock_config.save = AsyncMock()

    # Mock Orchestrator
    mock_orch = MagicMock()
    mock_orch.db = mock_db
    mock_orch.config = mock_config
    mock_orch.wallet = MagicMock()
    mock_orch.wallet.active_positions = {}
    mock_orch.loader = AsyncMock()
    mock_orch.safe_reload = AsyncMock()

    server = TelemetryWebServer(host="127.0.0.1", port=0, orchestrator=mock_orch)
    await server.start()
    
    port = server.runner.addresses[0][1]
    url = f"http://127.0.0.1:{port}"

    async with ClientSession() as session:
        # 1. Login com credenciais incorretas
        async with session.post(f"{url}/login", data={"username": "admin", "password": "wrongpassword"}) as resp:
            content = await resp.text()
            assert "Usuário ou senha incorretos" in content
            
        # 2. Login com credenciais corretas
        async with session.post(f"{url}/login", data={"username": "admin", "password": "adminpass"}) as resp:
            assert resp.status == 200
            # Deve estar na pagina index apos login
            html = await resp.text()
            assert "activity" in html

        # 3. GET /config deve trazer a tela de edicao
        async with session.get(f"{url}/config") as resp:
            assert resp.status == 200
            html = await resp.text()
            assert "Configurações do Robô" in html

        # 4. POST /config com senha errada deve falhar
        post_data = {
            "system.environment": "production",
            "system.heartbeat_timeout": "10",
            "system.max_signal_latency_ms": "100",
            "web_server.host": "127.0.0.1",
            "web_server.port": "8080",
            "global_risk.execution_exchange": "binance",
            "global_risk.max_daily_loss_pct": "3.0",
            "sudo_password": "wrongpassword"
        }
        async with session.post(f"{url}/config", data=post_data) as resp:
            html = await resp.text()
            assert "Senha de confirmação inválida!" in html
            assert not mock_config.save.called

        # 5. POST /config com senha correta e sem mudança de exchange
        post_data["sudo_password"] = "adminpass"
        async with session.post(f"{url}/config", data=post_data) as resp:
            assert resp.status == 200
            html = await resp.text()
            assert "Configurações gravadas e aplicadas" in html
            assert mock_config.save.called
            assert mock_config.update_from_dict.called
            assert mock_orch.loader.sync_modules.called

        # 6. POST /config tentando desativar estratégia com ordem de fecho dinâmico aberta deve falhar
        mock_orch.wallet.active_positions = {
            "some-guid-123": {
                "guid": "some-guid-123",
                "symbol": "BTC/USDT",
                "amount": 0.1,
                "price": 50000.0,
                "operation": "BUY",
                "stop_loss": None,
                "take_profit": None,
                "strategy_name": "morningstar"
            }
        }
        post_data_disable = {
            "system.environment": "sandbox",
            "system.heartbeat_timeout": "5",
            "system.max_signal_latency_ms": "50",
            "web_server.host": "127.0.0.1",
            "web_server.port": "8080",
            "global_risk.execution_exchange": "binance",
            "global_risk.max_daily_loss_pct": "2.0",
            "sudo_password": "adminpass"
        }
        # Note: por não enviar "modules.morningstar.enabled" no post, simulamos a desativação dela
        async with session.post(f"{url}/config", data=post_data_disable) as resp:
            assert resp.status == 200
            html = await resp.text()
            assert "Impossível desativar a estratégia" in html
            assert "morningstar" in html

    await server.shutdown()

