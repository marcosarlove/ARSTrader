import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from decimal import Decimal
from datetime import datetime, timezone

from core.orchestrator import GlobalOrchestrator
from core.models import OperationModel, TradeResultModel
from core import storage


class DummyWallet:
    def __init__(self, payloads_closed=None):
        self._is_running = False
        self.payloads_closed = payloads_closed or []
        self.initialize_and_sync = AsyncMock(side_effect=self._init_sync)
        self.execute_order = AsyncMock()

    @property
    def daily_loss_counter(self) -> float:
        return storage.wallet.daily_loss_counter

    @daily_loss_counter.setter
    def daily_loss_counter(self, val: float):
        storage.wallet.daily_loss_counter = val

    @property
    def balance(self) -> float:
        return storage.wallet.balance

    @balance.setter
    def balance(self, val: float):
        storage.wallet.balance = val

    @property
    def active_positions(self) -> dict:
        return storage.wallet.active_positions

    async def _init_sync(self, open_operations_db, current_daily_loss):
        storage.wallet.daily_loss_counter = current_daily_loss
        return self.payloads_closed



@pytest.fixture(autouse=True)
def reset_storage():
    """Reseta o estado do storage global para cada caso de teste."""
    storage.wallet.balance = 1000.0
    storage.wallet.balance_breakdown = []
    storage.wallet.daily_loss_counter = 0.0
    storage.wallet.simultaneous_trades = 0
    storage.wallet.active_locks.clear()
    storage.wallet.active_positions.clear()
    yield


@pytest.mark.asyncio
async def test_orchestrator_boot_reconciliation():
    """Verifica o fluxo de boot e reconciliação com o banco de dados e wallet."""
    config_mock = MagicMock()
    config_mock.global_risk.execution_exchange = "binance"
    config_mock.exchanges = {"binance": MagicMock(enabled=True)}
    config_mock.system.environment = "demo"
    config_mock.system.max_signal_latency_ms = 50.0
    config_mock.web_server = None

    # Mock do DatabaseManager
    db_mock = MagicMock()
    db_mock.start = AsyncMock()
    db_mock.get_daily_loss = AsyncMock(return_value=25.0)  # Perda diária já realizada
    
    open_ops = [
        {
            "guid": "g-open-1",
            "symbol": "BTC/USDT",
            "operation": "BUY",
            "amount": 0.01,
            "current_price": 50000.0
        }
    ]
    db_mock.get_open_operations = AsyncMock(return_value=open_ops)
    
    # Simula que a ordem g-open-1 fechou offline com perda de -5.0 USDT
    payloads_closed = [
        {
            "guid": "g-open-1",
            "status": "closed",
            "close_price": 49500.0,
            "close_timestamp": 123456789.0,
            "realized_pnl": -5.0,
            "reason": "EXTERNAL_CLOSE"
        }
    ]
    
    # Mock do WalletController usando DummyWallet
    wallet_mock = DummyWallet(payloads_closed)
    
    # Mock da exchange e outros managers
    exchange_mock = MagicMock()
    server_mock = MagicMock()
    server_mock.start = AsyncMock()
    loader_mock = MagicMock()
    loader_mock.start_modules = AsyncMock()

    # Mock da query de operação por guid
    mock_op_db = MagicMock(id=42, current_price=50000.0, amount=0.01)
    db_mock.get_operation_by_guid = AsyncMock(return_value=mock_op_db)

    orchestrator = GlobalOrchestrator(
        config=config_mock,
        db=db_mock,
        wallet=wallet_mock,
        exchange=exchange_mock,
        server=server_mock,
        loader=loader_mock
    )

    await orchestrator.start()

    # 1. Deve buscar ordens abertas e perda diária inicial
    db_mock.get_daily_loss.assert_called_once()
    db_mock.get_open_operations.assert_called_once()

    # 2. Deve inicializar wallet com os dados da db
    wallet_mock.initialize_and_sync.assert_called_once_with(
        open_operations_db=open_ops,
        current_daily_loss=25.0
    )

    # 3. Deve instanciar o TradeResultModel para a ordem fechada offline e enfileirar no banco
    db_mock.enqueue_save.assert_called_once()
    saved_model = db_mock.enqueue_save.call_args[0][0]
    assert isinstance(saved_model, TradeResultModel)
    assert saved_model.operation_id == 42
    assert float(saved_model.realized_pnl) == -5.0
    assert float(saved_model.pnl_percentage) == pytest.approx(-1.0)
    assert saved_model.outcome == "LOSS"

    # 4. Deve iniciar o servidor IPC e o Loader de processos
    server_mock.start.assert_called_once()
    loader_mock.start_modules.assert_called_once()

    # 5. O storage deve conter o drawdown diário consolidado (25.0 iniciais + 5.0 offline = 30.0)
    assert storage.wallet.daily_loss_counter == 30.0


@pytest.mark.asyncio
async def test_orchestrator_applies_demo_environment():
    config_mock = MagicMock()
    config_mock.system.environment = "demo"
    exchange_mock = MagicMock()

    orchestrator = GlobalOrchestrator(config=config_mock, exchange=exchange_mock)

    await orchestrator._apply_exchange_environment()

    exchange_mock.enable_demo_trading.assert_called_once_with(True)


@pytest.mark.asyncio
async def test_orchestrator_keeps_production_environment_untouched():
    config_mock = MagicMock()
    config_mock.system.environment = "production"
    exchange_mock = MagicMock()

    orchestrator = GlobalOrchestrator(config=config_mock, exchange=exchange_mock)

    await orchestrator._apply_exchange_environment()

    exchange_mock.enable_demo_trading.assert_not_called()


@pytest.mark.asyncio
async def test_orchestrator_rejects_invalid_environment():
    config_mock = MagicMock()
    config_mock.system.environment = "sandbox"
    exchange_mock = MagicMock()

    orchestrator = GlobalOrchestrator(
        config=config_mock,
        exchange=exchange_mock,
    )

    with pytest.raises(ValueError, match="Ambiente inválido"):
        await orchestrator._apply_exchange_environment()


@pytest.mark.asyncio
async def test_orchestrator_on_order_received_success():
    """Valida o roteamento e processamento de um sinal válido de abertura de ordem."""
    db_mock = MagicMock()
    wallet_mock = MagicMock()
    
    # Mock da execução do wallet retornando sucesso
    wallet_mock.execute_order = AsyncMock(return_value={
        "guid": "g-new",
        "status": "EXECUTED",
        "amount": 0.02,
        "price": 50000.0,
        "exchange_order_id": "ord-exchange-1"
    })

    orchestrator = GlobalOrchestrator(
        db=db_mock,
        wallet=wallet_mock
    )

    signal = {
        "guid": "g-new",
        "strategy_name": "morningstar",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "market": "SPOT",
        "exchange": "binance",
        "current_price": 50000.0
    }
    
    loop = asyncio.get_running_loop()
    promise = loop.create_future()

    await orchestrator.on_order_received(signal, promise)

    # A promise IPC deve ter sido resolvida com o status executado
    res = await promise
    assert res["status"] == "EXECUTED"
    assert res["amount"] == 0.02

    # Verifica se a operação foi salva na DB inicialmente (status PENDING) e no sucesso (EXECUTED)
    assert db_mock.enqueue_save.call_count == 2
    
    first_save = db_mock.enqueue_save.call_args_list[0][0][0]
    assert isinstance(first_save, OperationModel)
    assert first_save.guid == "g-new"
    # O status PENDING foi modificado in-place para EXECUTED, por isso não validamos status aqui.

    second_save = db_mock.enqueue_save.call_args_list[1][0][0]
    assert isinstance(second_save, OperationModel)
    assert second_save.status == "EXECUTED"
    assert float(second_save.amount) == 0.02
    assert second_save.exchange_order_id == "ord-exchange-1"


@pytest.mark.asyncio
async def test_orchestrator_counts_wallet_ignored_order_as_dropped_signal():
    db_mock = MagicMock()
    wallet_mock = MagicMock()
    wallet_mock.execute_order = AsyncMock(return_value={
        "guid": "g-ignored",
        "status": "IGNORED",
        "reason": "STOP_LOSS_EXCEEDS_MAX_RISK",
    })

    orchestrator = GlobalOrchestrator(db=db_mock, wallet=wallet_mock)

    signal = {
        "guid": "g-ignored",
        "strategy_name": "morningstar",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "market": "FUTURES",
        "exchange": "binance",
        "current_price": 50000.0,
        "stop_loss": 45000.0,
        "take_profit": 51000.0,
    }
    loop = asyncio.get_running_loop()
    promise = loop.create_future()

    await orchestrator.on_order_received(signal, promise)

    res = await promise
    assert res["status"] == "IGNORED"
    assert storage.comms.signals_dropped == 1


@pytest.mark.asyncio
async def test_orchestrator_on_order_rejected():
    """Valida a persistência de auditoria de sinais rejeitados pelo pre-routing do servidor."""
    db_mock = MagicMock()
    orchestrator = GlobalOrchestrator(db=db_mock)
    
    payload = {
        "guid": "g-rejected",
        "strategy_name": "eveningstar",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0
    }

    await orchestrator.on_order_rejected(payload, "SIGNAL_OBSOLETE")

    # Deve salvar o log com status IGNORED
    db_mock.enqueue_save.assert_called_once()
    saved = db_mock.enqueue_save.call_args[0][0]
    assert isinstance(saved, OperationModel)
    assert saved.guid == "g-rejected"
    assert saved.status == "IGNORED"
    assert saved.reason == "SIGNAL_OBSOLETE"


@pytest.mark.asyncio
async def test_orchestrator_on_order_closed():
    """Valida a persistência do TradeResult quando o WebSocket confirma o fechamento de uma posição."""
    db_mock = MagicMock()
    
    # Mock do banco retornando a operação original de abertura correspondente
    mock_op = MagicMock(id=99, current_price=100.0, amount=0.1)
    db_mock.get_operation_by_guid = AsyncMock(return_value=mock_op)

    orchestrator = GlobalOrchestrator(db=db_mock)

    closed_payload = {
        "guid": "g-open",
        "status": "closed",
        "close_price": 105.0,  # Ganho de 5 USDT (105 - 100) * 0.1 = +0.5 USDT
        "close_timestamp": 123456789.0,
        "realized_pnl": 0.5
    }

    await orchestrator.on_order_closed(closed_payload)

    db_mock.get_operation_by_guid.assert_called_once_with("g-open")
    db_mock.enqueue_save.assert_called_once()

    result = db_mock.enqueue_save.call_args[0][0]
    assert isinstance(result, TradeResultModel)
    assert result.operation_id == 99
    assert float(result.realized_pnl) == 0.5
    assert float(result.pnl_percentage) == pytest.approx(5.0)  # +5%
    assert result.outcome == "WIN"


@pytest.mark.asyncio
async def test_orchestrator_shutdown():
    """Valida a finalização limpa e encadeada de todos os subcomponentes."""
    loader_mock = AsyncMock()
    server_mock = AsyncMock()
    wallet_mock = AsyncMock()
    exchange_mock = AsyncMock()
    db_mock = AsyncMock()
    web_server_mock = AsyncMock()

    orchestrator = GlobalOrchestrator(
        loader=loader_mock,
        server=server_mock,
        wallet=wallet_mock,
        exchange=exchange_mock,
        db=db_mock,
        web_server=web_server_mock
    )

    await orchestrator.shutdown()

    # Todos os componentes devem ter tido seus métodos shutdown/close chamados
    loader_mock.shutdown.assert_called_once()
    web_server_mock.shutdown.assert_called_once()
    server_mock.shutdown.assert_called_once()
    wallet_mock.shutdown.assert_called_once()
    exchange_mock.close.assert_called_once()
    db_mock.shutdown.assert_called_once()
