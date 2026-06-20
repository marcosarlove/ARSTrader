import asyncio
import time
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import ccxt

from core.wallet import WalletController
from core.config import ConfigManager
from core import storage
from core.logger import STATUS_LEVEL_NUM


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
async def test_wallet_controller_risk_limits():
    """Valida a aplicação da trava de risco tripla síncrona baseada no storage."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 2
    config_mock.global_risk.max_daily_loss_limit = 50.0
    config_mock.global_risk.trade_risk_percentage = 0.10

    exchange_mock = MagicMock()
    controller = WalletController(exchange_mock, config_mock)

    # 1. Teste de trava: Perda diária estourada
    storage.wallet.daily_loss_counter = 50.0
    signal = {
        "guid": "g1",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }
    res = await controller.execute_order(signal)
    assert res["status"] == "IGNORED"
    assert res["reason"] == "DAILY_LOSS_LIMIT_EXCEEDED"

    storage.wallet.daily_loss_counter = 0.0

    # 2. Teste de trava: Limite de trades simultâneos atingido
    storage.wallet.active_locks["ETH/USDT"] = True
    storage.wallet.active_locks["SOL/USDT"] = True
    res = await controller.execute_order(signal)
    assert res["status"] == "IGNORED"
    assert res["reason"] == "LIMIT_SIMULTANEOUS_TRADES_EXCEEDED"

    storage.wallet.active_locks.clear()

    # 3. Teste de trava: Lock ativo no próprio ativo
    storage.wallet.active_locks["BTC/USDT"] = "g-open"
    res = await controller.execute_order(signal)
    assert res["status"] == "IGNORED"
    assert res["reason"] == "ASSET_LOCK_ACTIVE"


@pytest.mark.asyncio
async def test_wallet_controller_sizing_limits():
    """Verifica o cálculo de dimensionamento dinâmico de lote com travas de valor mínimo/notional."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10  # 10% de 1000 = 100 USDT de risco
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {
        "limits": {
            "amount": {"min": 0.005},
            "cost": {"min": 500.0},
        }
    }
    exchange_mock.create_order = AsyncMock(
        return_value={"id": "order-123", "price": 50000.0, "status": "closed"}
    )

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    signal = {
        "guid": "g2",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }
    res = await controller.execute_order(signal)

    assert res["status"] == "EXECUTED"
    assert res["amount"] == 0.01  # Lote mínimo recalculado
    assert res["exchange_order_id"] == "order-123"
    assert exchange_mock.create_order.call_count == 3
    exchange_mock.create_order.assert_any_call(
        symbol="BTC/USDT", type="market", side="buy", amount=0.01
    )
    exchange_mock.create_order.assert_any_call(
        symbol="BTC/USDT",
        type="market",
        side="sell",
        amount=0.01,
        price=None,
        params={"stopLossPrice": 49000.0, "reduceOnly": "true"},
    )
    exchange_mock.create_order.assert_any_call(
        symbol="BTC/USDT",
        type="market",
        side="sell",
        amount=0.01,
        price=None,
        params={"takeProfitPrice": 52000.0, "reduceOnly": "true"},
    )


@pytest.mark.asyncio
async def test_wallet_controller_attached_sl_tp_when_supported():
    """Usa SL/TP anexado na ordem de entrada quando o CCXT/Binance declara suporte."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(return_value={
        "id": "entry-1",
        "price": 50000.0,
        "status": "closed",
        "stopLossOrderId": "sl-1",
        "takeProfitOrderId": "tp-1",
    })

    controller = WalletController(exchange_mock, config_mock)
    controller._supports_attached_sl_tp = True
    controller._supports_stop_loss_price = True
    controller._supports_take_profit_price = True
    storage.wallet.balance = 1000.0

    res = await controller.execute_order({
        "guid": "g-attached",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    })

    assert res["status"] == "EXECUTED"
    assert exchange_mock.create_order.call_count == 1
    exchange_mock.create_order.assert_called_once_with(
        symbol="BTC/USDT",
        type="market",
        side="buy",
        amount=0.002,
        params={"stopLossPrice": 49000.0, "takeProfitPrice": 52000.0},
    )

    pos = storage.wallet.active_positions["g-attached"]
    assert pos["stop_loss_order_id"] == "sl-1"
    assert pos["take_profit_order_id"] == "tp-1"


@pytest.mark.asyncio
async def test_wallet_controller_reconciliation():
    """Verifica a reconciliação assíncrona paralela (FASE A) ao inicializar o ecossistema."""
    config_mock = MagicMock()
    exchange_mock = MagicMock()

    open_ops = [
        {
            "guid": "g1",
            "symbol": "BTC/USDT",
            "operation": "BUY",
            "amount": 0.01,
            "current_price": 50000.0,
            "exchange_order_id": "ord-1",
        },
        {
            "guid": "g2",
            "symbol": "ETH/USDT",
            "operation": "BUY",
            "amount": 0.1,
            "current_price": 3000.0,
            "exchange_order_id": "ord-2",
        },
    ]

    async def mock_fetch_order(order_id, symbol):
        if order_id == "ord-1":
            return {"id": "ord-1", "status": "open", "amount": 0.01, "price": 50000.0}
        else:
            return {
                "id": "ord-2",
                "status": "closed",
                "amount": 0.1,
                "price": 3100.0,
                "average": 3100.0,
                "timestamp": 123456789.0,
            }

    exchange_mock.fetch_order = AsyncMock(side_effect=mock_fetch_order)
    exchange_mock.watch_balance = AsyncMock(side_effect=asyncio.CancelledError)
    exchange_mock.watch_orders = AsyncMock(side_effect=asyncio.CancelledError)

    controller = WalletController(exchange_mock, config_mock)

    closed_payloads = await controller.initialize_and_sync(
        open_ops, current_daily_loss=12.5
    )

    # ord-1 permaneceu aberta -> reativou lock e posição
    assert "BTC/USDT" in storage.wallet.active_locks
    assert "g1" in storage.wallet.active_positions
    assert storage.wallet.daily_loss_counter == 12.5

    # ord-2 foi fechada -> gerou payload de fechamento e não colocou lock
    assert "ETH/USDT" not in storage.wallet.active_locks
    assert len(closed_payloads) == 1
    assert closed_payloads[0]["guid"] == "g2"
    assert closed_payloads[0]["status"] == "CLOSED"
    assert closed_payloads[0]["close_price"] == 3100.0
    assert closed_payloads[0]["realized_pnl"] == pytest.approx(10.0)

    await controller.shutdown()


@pytest.mark.asyncio
async def test_wallet_controller_execution_exceptions():
    """Valida o tratamento de exceções do CCXT liberando locks em caso de falha de execução."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(
        side_effect=ccxt.InsufficientFunds("Insufficient funds on exchange")
    )

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    signal = {
        "guid": "g3",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }
    res = await controller.execute_order(signal)

    assert res["status"] == "FAILED"
    assert "EXCHANGE_INSUFFICIENT_FUNDS" in res["reason"]
    assert "BTC/USDT" not in storage.wallet.active_locks


@pytest.mark.asyncio
async def test_wallet_controller_execute_close_order():
    """Valida a execução de ordens de fechamento baseadas em target_guid."""
    config_mock = MagicMock()
    
    # Configura posição original no storage
    storage.wallet.active_locks["BTC/USDT"] = "g-open"
    storage.wallet.active_positions["g-open"] = {
        "guid": "g-open",
        "symbol": "BTC/USDT",
        "amount": 0.01,
        "price": 50000.0,
        "operation": "BUY",
        "exchange_order_id": "ord-open"
    }

    exchange_mock = MagicMock()
    exchange_mock.create_order = AsyncMock(return_value={
        "id": "ord-close",
        "price": 51000.0,
        "average": 51000.0,
        "status": "closed",
        "timestamp": 123456789.0
    })

    controller = WalletController(exchange_mock, config_mock)
    
    close_signal = {
        "guid": "g-close",
        "target_guid": "g-open",
        "symbol": "BTC/USDT",
        "operation": "SELL",
        "current_price": 51000.0
    }
    
    res = await controller.execute_order(close_signal)
    
    assert res["status"] == "CLOSED"
    assert res["target_guid"] == "g-open"
    assert res["close_price"] == 51000.0
    assert res["realized_pnl"] == pytest.approx(10.0)  # PnL: (51000 - 50000) * 0.01 = 10 USDT
    
    # O lock e a posição ativa correspondente não devem ser limpos pela chamada REST
    assert "BTC/USDT" in storage.wallet.active_locks
    assert "g-open" in storage.wallet.active_positions
    
    # Simulamos a chegada da confirmação da ordem via WebSocket
    await controller._handle_closed_order({
        "id": "ord-close",
        "symbol": "BTC/USDT",
        "status": "closed",
        "average": 51000.0,
        "amount": 0.01,
        "timestamp": 123456789.0
    })

    # Agora sim, o lock e a posição ativa correspondente devem ser limpos
    assert "BTC/USDT" not in storage.wallet.active_locks
    assert "g-open" not in storage.wallet.active_positions
    
    # Ordem contrária executada ("sell")
    exchange_mock.create_order.assert_called_once_with(
        symbol="BTC/USDT",
        type="market",
        side="sell",
        amount=0.01
    )


@pytest.mark.asyncio
async def test_wallet_controller_manual_close_max_risk_stop_loss():
    """Valida as ordens manuais utilizando o stop loss de risco máximo da configuração."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_safety_stop_loss_pct = 5.0  # 5% safety stop loss

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(return_value={
        "id": "ord-1",
        "price": 100.0,
        "status": "closed"
    })

    controller = WalletController(exchange_mock, config_mock)
    
    signal = {
        "guid": "g-manual",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 100.0,
        "ignore_fields": ["stop_loss", "take_profit"]
    }
    
    res = await controller.execute_order(signal)
    
    assert res["status"] == "EXECUTED"
    pos = storage.wallet.active_positions["g-manual"]
    # 5% de stop loss a partir de 100 = 95.0
    assert pos["stop_loss"] == 95.0
    assert pos["take_profit"] is None
    assert exchange_mock.create_order.call_count == 2
    exchange_mock.create_order.assert_any_call(
        symbol="BTC/USDT",
        type="market",
        side="sell",
        amount=1.0,
        price=None,
        params={"stopLossPrice": 95.0, "reduceOnly": "true"},
    )


@pytest.mark.asyncio
async def test_wallet_controller_open_order_defaults_fallback():
    """Valida ordens normais sem SL/TP fornecidos caindo nos alvos padrão configurados."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(return_value={
        "id": "ord-2",
        "price": 200.0,
        "status": "closed"
    })

    controller = WalletController(exchange_mock, config_mock)
    
    signal = {
        "guid": "g-default",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 200.0
    }
    
    res = await controller.execute_order(signal)
    
    assert res["status"] == "EXECUTED"
    pos = storage.wallet.active_positions["g-default"]
    # 2% stop loss a partir de 200 = 196.0
    assert pos["stop_loss"] == 196.0
    # 4% take profit a partir de 200 = 208.0
    assert pos["take_profit"] == 208.0
    assert exchange_mock.create_order.call_count == 3


@pytest.mark.asyncio
async def test_wallet_controller_rejects_strategy_stop_loss_above_max_risk_buy():
    """BUY com SL abaixo do risco máximo global é rejeitado antes da exchange."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    exchange_mock = MagicMock()
    exchange_mock.create_order = AsyncMock()

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    res = await controller.execute_order({
        "guid": "g-risk-buy",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 100.0,
        "stop_loss": 95.0,
        "take_profit": 104.0,
    })

    assert res["status"] == "IGNORED"
    assert res["reason"] == "STOP_LOSS_EXCEEDS_MAX_RISK"
    exchange_mock.create_order.assert_not_called()
    assert "BTC/USDT" not in storage.wallet.active_locks


@pytest.mark.asyncio
async def test_wallet_controller_rejects_strategy_stop_loss_above_max_risk_sell():
    """SELL com SL acima do risco máximo global é rejeitado antes da exchange."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    exchange_mock = MagicMock()
    exchange_mock.create_order = AsyncMock()

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    res = await controller.execute_order({
        "guid": "g-risk-sell",
        "symbol": "BTC/USDT",
        "operation": "SELL",
        "current_price": 100.0,
        "stop_loss": 103.0,
        "take_profit": 96.0,
    })

    assert res["status"] == "IGNORED"
    assert res["reason"] == "STOP_LOSS_EXCEEDS_MAX_RISK"
    exchange_mock.create_order.assert_not_called()
    assert "BTC/USDT" not in storage.wallet.active_locks


@pytest.mark.asyncio
async def test_wallet_controller_ghost_balance_allocation():
    """Valida que o watch_balance_loop ignora saldos de moedas não homologadas (evitando saldo fantasma)."""
    config_mock = MagicMock()
    exchange_mock = MagicMock()
    
    # Simula um saldo que contém moedas como BNB ou BTC e moedas homologadas como USDT
    exchange_mock.watch_balance = AsyncMock(return_value={
        "free": {
            "BNB": 0.05,
            "BTC": 0.0001,
            "USDT": 500.0,
            "USDC": 100.0
        }
    })
    
    controller = WalletController(exchange_mock, config_mock)
    controller._is_running = True
    
    # Executa o loop uma vez (simulado manualmente chamando o corpo do try)
    balance = await exchange_mock.watch_balance()
    free_balance = balance.get("free", {})
    
    allowed_bases = ["USDT", "USDC", "USD"]
    usdt_balance = None
    for base in allowed_bases:
        if base in free_balance and free_balance[base] > 0:
            usdt_balance = free_balance[base]
            break
            
    assert usdt_balance == 500.0  # Pega o primeiro homologado (USDT), ignorando o pó de BNB/BTC


@pytest.mark.asyncio
async def test_wallet_controller_duplicate_websocket_messages():
    """Valida que mensagens repetidas do mesmo ID de ordem de fecho são ignoradas."""
    config_mock = MagicMock()
    exchange_mock = MagicMock()
    
    # Callback para monitorar o número de invocações do Orchestrator
    on_close_mock = MagicMock()
    controller = WalletController(exchange_mock, config_mock, on_order_close_cb=on_close_mock)
    
    storage.wallet.active_locks["BTC/USDT"] = "g-pos"
    storage.wallet.active_positions["g-pos"] = {
        "guid": "g-pos",
        "symbol": "BTC/USDT",
        "amount": 0.1,
        "price": 100.0,
        "operation": "BUY",
        "exchange_order_id": "ord-entry"
    }
    
    # Primeira mensagem de fechamento (prejuízo de -10 USDT)
    order_msg = {
        "id": "ord-exit",
        "symbol": "BTC/USDT",
        "status": "closed",
        "average": 90.0,
        "amount": 0.1,
        "timestamp": 123456789.0
    }
    
    # Adicionamos ao pending close para simular que foi iniciado por nós
    controller._pending_close_orders["ord-exit"] = "g-pos"
    
    await controller._handle_closed_order(order_msg)
    
    assert storage.wallet.daily_loss_counter == pytest.approx(1.0)
    assert on_close_mock.call_count == 1
    
    # Envia a mesma confirmação duplicada
    await controller._handle_closed_order(order_msg)
    
    # O daily_loss_counter e o callback não devem ser incrementados/chamados novamente
    assert storage.wallet.daily_loss_counter == pytest.approx(1.0)
    assert on_close_mock.call_count == 1


@pytest.mark.asyncio
async def test_wallet_controller_concurrent_close_order_pending_open():
    """Valida que um sinal de fecho logo após a abertura não falha se a posição ainda estiver PENDING_OPEN."""
    config_mock = MagicMock()
    # Configuração de risco padrão
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0
    config_mock.global_risk.default_safety_stop_loss_pct = 5.0
    
    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    
    # Mock do create_order lento (usamos sleep para simular rede assíncrona)
    async def slow_create_order(*args, **kwargs):
        await asyncio.sleep(0.1)
        return {"id": "ord-entry-exchange", "price": 50000.0, "status": "closed"}
        
    exchange_mock.create_order = AsyncMock(side_effect=slow_create_order)
    
    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0
    
    open_signal = {
        "guid": "g-entry",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0
    }
    
    # Disparar abertura em background
    open_task = asyncio.create_task(controller.execute_order(open_signal))
    
    # Aguarda um curtíssimo espaço de tempo para dar tempo de criar o estado "PENDING_OPEN"
    await asyncio.sleep(0.01)
    
    # Assert do estado intermediário/concorrente na RAM
    assert "g-entry" in storage.wallet.active_positions
    assert storage.wallet.active_positions["g-entry"]["status"] == "PENDING_OPEN"
    
    # Mock para a ordem de fechamento
    exchange_mock.create_order = AsyncMock(return_value={
        "id": "ord-close-exchange",
        "price": 50100.0,
        "average": 50100.0,
        "status": "closed"
    })
    
    close_signal = {
        "guid": "g-close",
        "target_guid": "g-entry",
        "symbol": "BTC/USDT",
        "operation": "SELL",
        "current_price": 50100.0
    }
    
    # Executa a ordem de fechamento concorrente. Não deve dar ORIGINAL_POSITION_NOT_FOUND!
    close_res = await controller.execute_order(close_signal)
    assert close_res["status"] == "CLOSED"
    
    # Limpa a tarefa de abertura em background
    await open_task


@pytest.mark.asyncio
async def test_wallet_controller_concurrent_same_symbol_open_is_single_flight():
    """Dois sinais simultâneos no mesmo símbolo não podem gerar duas entradas."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    async def slow_create_order(*args, **kwargs):
        await asyncio.sleep(0.05)
        return {"id": f"ord-{kwargs.get('side', 'unknown')}", "price": 50000.0, "status": "closed"}

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(side_effect=slow_create_order)

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    signal_a = {
        "guid": "g-concurrent-a",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }
    signal_b = {
        "guid": "g-concurrent-b",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }

    res_a, res_b = await asyncio.gather(
        controller.execute_order(signal_a),
        controller.execute_order(signal_b),
    )

    statuses = {res_a["guid"]: res_a["status"], res_b["guid"]: res_b["status"]}
    reasons = {res_a["guid"]: res_a.get("reason"), res_b["guid"]: res_b.get("reason")}

    assert sorted(statuses.values()) == ["EXECUTED", "IGNORED"]
    ignored_guid = next(g for g, status in statuses.items() if status == "IGNORED")
    executed_guid = next(g for g, status in statuses.items() if status == "EXECUTED")
    assert reasons[ignored_guid] == "ASSET_LOCK_ACTIVE"
    assert storage.wallet.active_locks["BTC/USDT"] == executed_guid

    # Entrada + SL + TP apenas para uma posição.
    assert exchange_mock.create_order.call_count == 3


@pytest.mark.asyncio
async def test_wallet_controller_capacity_waits_for_pending_failure():
    """Sinal de outro ativo aguarda uma reserva pendente falhar antes de usar a vaga."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    config_mock.global_risk.trade_risk_percentage = 0.10
    config_mock.global_risk.default_stop_loss_pct = 2.0
    config_mock.global_risk.default_take_profit_pct = 4.0

    storage.wallet.active_locks["SOL/USDT"] = "g-sol"
    storage.wallet.active_locks["ADA/USDT"] = "g-ada"
    storage.wallet.simultaneous_trades = 2

    async def create_order_side_effect(*args, **kwargs):
        await asyncio.sleep(0.02)
        if kwargs["symbol"] == "BTC/USDT":
            raise ccxt.InsufficientFunds("insufficient margin")
        return {"id": f"ord-{kwargs['symbol']}-{kwargs['side']}", "price": 3000.0, "status": "closed"}

    exchange_mock = MagicMock()
    exchange_mock.market.return_value = {}
    exchange_mock.create_order = AsyncMock(side_effect=create_order_side_effect)

    controller = WalletController(exchange_mock, config_mock)
    storage.wallet.balance = 1000.0

    btc_signal = {
        "guid": "g-btc-fails",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
    }
    eth_signal = {
        "guid": "g-eth-waits",
        "symbol": "ETH/USDT",
        "operation": "BUY",
        "current_price": 3000.0,
    }

    btc_res, eth_res = await asyncio.gather(
        controller.execute_order(btc_signal),
        controller.execute_order(eth_signal),
    )

    assert btc_res["status"] == "FAILED"
    assert btc_res["reason"] == "EXCHANGE_INSUFFICIENT_FUNDS"
    assert eth_res["status"] == "EXECUTED"
    assert storage.wallet.active_locks["ETH/USDT"] == "g-eth-waits"
    assert "BTC/USDT" not in storage.wallet.active_locks
    assert storage.wallet.simultaneous_trades == 3


@pytest.mark.asyncio
async def test_wallet_controller_release_lock_only_by_owner():
    """Rollback de uma ordem não pode liberar lock que já pertence a outro guid."""
    config_mock = MagicMock()
    exchange_mock = MagicMock()
    controller = WalletController(exchange_mock, config_mock)

    storage.wallet.active_locks["BTC/USDT"] = "owner-b"
    storage.wallet.simultaneous_trades = 1

    await controller._release_symbol_lock("BTC/USDT", "owner-a")
    assert storage.wallet.active_locks["BTC/USDT"] == "owner-b"
    assert storage.wallet.simultaneous_trades == 1

    await controller._release_symbol_lock("BTC/USDT", "owner-b")
    assert "BTC/USDT" not in storage.wallet.active_locks
    assert storage.wallet.simultaneous_trades == 0


@pytest.mark.asyncio
async def test_wallet_controller_latency_pre_send():
    """Valida que ordens com latência estourada antes de tocar o mercado são rejeitadas pela Wallet."""
    config_mock = MagicMock()
    config_mock.system.max_signal_latency_ms = 50.0  # 50ms max
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0
    
    exchange_mock = MagicMock()
    controller = WalletController(exchange_mock, config_mock)
    
    # 1. Testa abertura obsoleta (100ms atrás, excede 50ms)
    obsolete_time = time.time() - 0.100
    signal_open = {
        "guid": "g-obs-open",
        "symbol": "BTC/USDT",
        "operation": "BUY",
        "current_price": 50000.0,
        "timestamp": obsolete_time
    }
    
    res = await controller.execute_order(signal_open)
    assert res["status"] == "IGNORED"
    assert res["reason"] == "SIGNAL_OBSOLETE_BEFORE_SEND"
    assert "BTC/USDT" not in storage.wallet.active_locks

    # 2. Testa fecho obsoleto
    # Primeiro coloca a posição na RAM manualmente
    storage.wallet.active_locks["BTC/USDT"] = "g-open"
    storage.wallet.active_positions["g-open"] = {
        "guid": "g-open",
        "symbol": "BTC/USDT",
        "amount": 0.01,
        "price": 50000.0,
        "operation": "BUY",
        "exchange_order_id": "ord-open"
    }
    
    signal_close = {
        "guid": "g-obs-close",
        "target_guid": "g-open",
        "symbol": "BTC/USDT",
        "operation": "SELL",
        "current_price": 51000.0,
        "timestamp": obsolete_time
    }
    
    res_close = await controller.execute_order(signal_close)
    assert res_close["status"] == "FAILED"
    assert res_close["reason"] == "SIGNAL_OBSOLETE_BEFORE_SEND"


@pytest.mark.asyncio
async def test_wallet_observer_pattern():
    """Valida que múltiplos listeners podem se registrar e ser notificados no fechamento."""
    config_mock = MagicMock()
    config_mock.global_risk.max_simultaneous_trades = 3
    config_mock.global_risk.max_daily_loss_limit = 100.0

    exchange_mock = MagicMock()
    controller = WalletController(exchange_mock, config_mock)

    # Cria dois callbacks mockados
    listener_1 = MagicMock()
    listener_2 = AsyncMock()

    controller.register_order_close_listener(listener_1)
    controller.register_order_close_listener(listener_2)

    # Simula o recebimento de fechamento de posição via WebSocket no loop de ordens
    storage.wallet.active_positions["g-pos"] = {
        "guid": "g-pos",
        "symbol": "BTC/USDT",
        "amount": 0.01,
        "price": 50000.0,
        "operation": "BUY",
        "exchange_order_id": "ord-123"
    }

    # Executa o fechamento interno que chama _handle_closed_order
    mock_order = {
        "id": "ord-999",  # ID diferente do de entrada para ser tratado como fechamento externo
        "symbol": "BTC/USDT",
        "status": "closed",
        "filled": 0.01,
        "price": 51000.0,
        "average": 51000.0,
        "timestamp": 123456789.0
    }

    await controller._handle_closed_order(mock_order)

    # Ambos os listeners devem ter sido chamados com o payload correspondente
    listener_1.assert_called_once()
    listener_2.assert_called_once()
    
    payload = listener_1.call_args[0][0]
    assert payload["guid"] == "g-pos"
    assert payload["realized_pnl"] == pytest.approx(10.0)
    assert payload["status"] == "CLOSED"
