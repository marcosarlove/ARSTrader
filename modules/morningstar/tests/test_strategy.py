import asyncio
from typing import Any, Dict, List

import pytest

from modules.morningstar.strategy import MorningStarStrategy


class ProbeMorningStarStrategy(MorningStarStrategy):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.orders: List[Dict[str, Any]] = []
        self.response_status = "EXECUTED"

    async def open_order(self, **kwargs: Any) -> Dict[str, Any]:
        self.orders.append(kwargs)
        return {"status": self.response_status, "guid": kwargs["guid"]}


def _base_kwargs() -> Dict[str, Any]:
    return {
        "core_host": "127.0.0.1",
        "core_port": 9999,
        "heartbeat_interval": 1.0,
        "exchange": "binance",
        "market": "FUTURES",
        "reward_risk_ratio": 2.0,
        "support_tolerance_pct": 0.005,
        "stop_buffer_pct": 0.001,
        "long_body_ratio": 1.2,
        "star_body_ratio": 0.35,
        "candle_limit": 100,
    }


def _kwargs_with_filters(filters: Dict[str, Any]) -> Dict[str, Any]:
    kwargs = _base_kwargs()
    kwargs["filters"] = filters
    return kwargs


def _neutral_candle(index: int) -> Dict[str, Any]:
    return {
        "timestamp": float(index),
        "open": 101.0,
        "high": 101.5,
        "low": 100.5,
        "close": 101.2,
        "volume": 10.0,
        "closed": True,
    }


def _morning_star_candles(timestamp_offset: int = 0) -> List[Dict[str, Any]]:
    candles = [_neutral_candle(index) for index in range(97)]
    candles.extend(
        [
            {
                "timestamp": 97.0 + timestamp_offset,
                "open": 105.0,
                "high": 106.0,
                "low": 99.5,
                "close": 100.0,
                "volume": 12.0,
                "closed": True,
            },
            {
                "timestamp": 98.0 + timestamp_offset,
                "open": 99.5,
                "high": 99.8,
                "low": 98.0,
                "close": 99.4,
                "volume": 9.0,
                "closed": True,
            },
            {
                "timestamp": 99.0 + timestamp_offset,
                "open": 99.7,
                "high": 103.5,
                "low": 98.8,
                "close": 103.0,
                "volume": 15.0,
                "closed": True,
            },
        ]
    )
    return candles


@pytest.mark.parametrize(
    "filters",
    [
        {"volume": {"enabled": True, "lookback": 20, "recovery_min_ratio": 2.0}},
        {"volatility": {"enabled": True, "atr_period": 14, "max_atr_pct": 0.001}},
        {"trend": {"enabled": True, "ema_fast": 20, "ema_slow": 50}},
        {"momentum": {"enabled": True, "rsi_period": 14, "max_rsi": -1}},
        {"risk": {"enabled": True, "max_signal_risk_pct": 0.01}},
    ],
)
@pytest.mark.asyncio
async def test_morningstar_confirmation_filters_can_block_signal(
    filters,
    tmp_path,
    monkeypatch,
):
    monkeypatch.chdir(tmp_path)

    async def fetcher(asset: str, timeframe: str, limit: int):
        return _morning_star_candles()

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_kwargs_with_filters(filters),
    )

    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert strategy.orders == []


@pytest.mark.asyncio
async def test_morningstar_cooldown_filter_blocks_until_enough_new_candles(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    calls = 0

    async def fetcher(asset: str, timeframe: str, limit: int):
        nonlocal calls
        calls += 1
        if calls == 1:
            return _morning_star_candles()
        if calls == 2:
            return _morning_star_candles(timestamp_offset=1)
        return _morning_star_candles(timestamp_offset=3)

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_kwargs_with_filters({"cooldown": {"enabled": True, "candles": 3}}),
    )

    await strategy._process_asset("BTC/USDT")
    await strategy._process_asset("BTC/USDT")
    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 2


@pytest.mark.asyncio
async def test_morningstar_emits_order_with_dynamic_sl_tp(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def fetcher(asset: str, timeframe: str, limit: int):
        assert asset == "BTC/USDT"
        assert timeframe == "4H"
        assert limit == 100
        return _morning_star_candles()

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_base_kwargs(),
    )

    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 1
    order = strategy.orders[0]
    assert order["symbol"] == "BTC/USDT"
    assert order["exchange"] == "binance"
    assert order["operation"] == "BUY"
    assert order["price"] == 103.0
    assert order["stop_loss"] == pytest.approx(97.902)
    assert order["take_profit"] == pytest.approx(113.196)
    assert strategy.market_state["BTC/USDT"].open_position is True


@pytest.mark.asyncio
async def test_morningstar_consumes_executed_trigger_and_waits_for_next_pattern(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    calls = 0

    async def fetcher(asset: str, timeframe: str, limit: int):
        nonlocal calls
        calls += 1
        if calls < 3:
            return _morning_star_candles()
        return _morning_star_candles(timestamp_offset=3)

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_base_kwargs(),
    )

    await strategy._process_asset("BTC/USDT")
    await strategy._process_asset("BTC/USDT")
    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 2


@pytest.mark.asyncio
async def test_morningstar_consumes_ignored_trigger(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def fetcher(asset: str, timeframe: str, limit: int):
        return _morning_star_candles()

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_base_kwargs(),
    )
    strategy.response_status = "IGNORED"

    await strategy._process_asset("BTC/USDT")
    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 1
    assert strategy.market_state["BTC/USDT"].open_position is False


@pytest.mark.asyncio
async def test_morningstar_ignores_open_candle_and_keeps_fixed_buffer(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def fetcher(asset: str, timeframe: str, limit: int):
        candles = [_neutral_candle(index) for index in range(101)]
        candles.append(
            {
                "timestamp": 102.0,
                "open": 1.0,
                "high": 1.0,
                "low": 1.0,
                "close": 1.0,
                "closed": False,
            }
        )
        return candles

    strategy = ProbeMorningStarStrategy(
        assets=["ETH/USDT"],
        timeframe="1H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_base_kwargs(),
    )

    await strategy._refresh_candles("ETH/USDT", strategy.market_state["ETH/USDT"])
    await strategy.shutdown()

    candles = strategy.market_state["ETH/USDT"].candles
    assert len(candles) == 100
    assert candles[-1].timestamp == 100.0


@pytest.mark.asyncio
async def test_morningstar_keeps_market_state_isolated(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    async def fetcher(asset: str, timeframe: str, limit: int):
        if asset == "BTC/USDT":
            return _morning_star_candles()
        return [_neutral_candle(index) for index in range(100)]

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT", "ETH/USDT"],
        timeframe="4H",
        check_interval=60,
        ohlcv_fetcher=fetcher,
        **_base_kwargs(),
    )

    await asyncio.gather(
        strategy._process_asset("BTC/USDT"),
        strategy._process_asset("ETH/USDT"),
    )
    await strategy.shutdown()

    assert len(strategy.orders) == 1
    assert strategy.orders[0]["symbol"] == "BTC/USDT"
    assert strategy.market_state["BTC/USDT"].open_position is True
    assert strategy.market_state["ETH/USDT"].open_position is False
