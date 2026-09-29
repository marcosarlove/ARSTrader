from typing import Any, Dict, List

import pytest

from modules.morningstar.strategy import MorningStarStrategy
from modules.morningstar.tests.test_strategy import ProbeMorningStarStrategy, _base_kwargs
from modules.morningstar.utils.scenario_ohlcv_wrapper import MorningStarScenarioOhlcvWrapper


def _raw_candles() -> List[Dict[str, Any]]:
    candles = []
    for index in range(100):
        close = 100.0 + (index * 0.01)
        candles.append({
            "timestamp": float(index),
            "open": close - 0.05,
            "high": close + 0.10,
            "low": close - 0.10,
            "close": close,
            "volume": 100.0,
            "closed": True,
        })
    return candles


@pytest.mark.asyncio
async def test_morningstar_wrapper_preserves_latest_real_close_and_generates_signal(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    raw = _raw_candles()
    real_close = raw[-1]["close"]

    async def fetcher(asset: str, timeframe: str, limit: int):
        return raw

    wrapper = MorningStarScenarioOhlcvWrapper(
        fetcher,
        {
            "enabled": True,
            "seed": 7,
            "cooldown_cycles": 0,
            "scenarios": {"valid_signal": {"weight": 1, "stop_distance_pct": [0.2, 0.2]}},
        },
    )

    candles = await wrapper("BTC/USDT", "4h", 100)

    assert candles[-1]["close"] == real_close

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4h",
        check_interval=60,
        ohlcv_fetcher=lambda asset, timeframe, limit: candles,
        **_base_kwargs(),
    )

    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 1
    assert strategy.orders[0]["operation"] == "BUY"
    assert strategy.orders[0]["price"] == real_close
    risk_pct = (real_close - strategy.orders[0]["stop_loss"]) / real_close
    assert risk_pct < 0.03


@pytest.mark.asyncio
async def test_morningstar_wrapper_renews_signal_key_each_cycle(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    raw = _raw_candles()

    async def fetcher(asset: str, timeframe: str, limit: int):
        return raw

    wrapper = MorningStarScenarioOhlcvWrapper(
        fetcher,
        {
            "enabled": True,
            "seed": 7,
            "cooldown_cycles": 0,
            "scenarios": {"valid_signal": {"weight": 1, "stop_distance_pct": [0.2, 0.2]}},
        },
    )

    first = await wrapper("BTC/USDT", "4h", 100)
    second = await wrapper("BTC/USDT", "4h", 100)

    strategy = ProbeMorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4h",
        check_interval=60,
        ohlcv_fetcher=lambda asset, timeframe, limit: first,
        **_base_kwargs(),
    )
    await strategy._process_asset("BTC/USDT")
    strategy.ohlcv_fetcher = lambda asset, timeframe, limit: second
    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert len(strategy.orders) == 2


@pytest.mark.asyncio
async def test_morningstar_wrapper_can_generate_excessive_risk_signal(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    raw = _raw_candles()

    async def fetcher(asset: str, timeframe: str, limit: int):
        return raw

    wrapper = MorningStarScenarioOhlcvWrapper(
        fetcher,
        {
            "enabled": True,
            "seed": 11,
            "cooldown_cycles": 0,
            "scenarios": {"excessive_risk": {"weight": 1, "stop_distance_pct": [5.0, 5.0]}},
        },
    )
    candles = await wrapper("BTC/USDT", "4h", 100)

    strategy = MorningStarStrategy(
        assets=["BTC/USDT"],
        timeframe="4h",
        check_interval=60,
        ohlcv_fetcher=lambda asset, timeframe, limit: candles,
        **{
            **_base_kwargs(),
            "filters": {"risk": {"enabled": True, "max_signal_risk_pct": 0.02}},
        },
    )

    await strategy._process_asset("BTC/USDT")
    await strategy.shutdown()

    assert strategy.market_state["BTC/USDT"].last_order_response is None
