from __future__ import annotations

import inspect
import random
from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Sequence, Union


RawCandle = Union[Dict[str, Any], Sequence[Any]]
OhlcvFetcher = Callable[[str, str, int], Union[Iterable[RawCandle], Awaitable[Iterable[RawCandle]]]]


class MorningStarScenarioOhlcvWrapper:
    """Wrapper local de OHLCV para ensaios Morning Star em demo."""

    def __init__(self, fetcher: OhlcvFetcher, config: Optional[Dict[str, Any]] = None) -> None:
        self.fetcher = fetcher
        self.config = config or {}
        self.random = random.Random(self.config.get("seed"))
        self.cooldowns: Dict[str, int] = {}
        self.sequence_by_asset: Dict[str, int] = {}

    async def __call__(self, asset: str, timeframe: str, limit: int) -> List[Dict[str, Any]]:
        try:
            result = self.fetcher(asset, timeframe, limit)
            if inspect.isawaitable(result):
                result = await result
            candles = [self._to_dict(raw) for raw in result]
        except Exception:
            candles = self._generate_fallback_candles(limit)

        if len(candles) < 20:
            return candles

        if self._consume_cooldown(asset):
            return candles

        probability = float(self.config.get("probability", 1.0))
        if self.random.random() > probability:
            return candles

        scenario = self._choose_scenario()
        if scenario == "no_signal":
            transformed = self._build_no_signal(candles)
        else:
            transformed = self._build_morning_star(candles, scenario)
            self._stamp_synthetic_trigger(asset, transformed)

        self.cooldowns[asset] = int(self.config.get("cooldown_cycles", 2))
        return transformed[-limit:]

    def _consume_cooldown(self, asset: str) -> bool:
        remaining = self.cooldowns.get(asset, 0)
        if remaining <= 0:
            return False
        self.cooldowns[asset] = remaining - 1
        return True

    def _choose_scenario(self) -> str:
        scenarios = self.config.get("scenarios") or {}
        if not isinstance(scenarios, dict):
            scenarios = {}
        if not scenarios:
            scenarios = {
                "valid_signal": {"weight": 4},
                "excessive_risk": {"weight": 1},
                "low_volume": {"weight": 1},
                "high_volatility": {"weight": 1},
                "no_signal": {"weight": 2},
            }

        names: List[str] = []
        weights: List[float] = []
        for name, cfg in scenarios.items():
            if isinstance(cfg, dict) and cfg.get("enabled", True) is False:
                continue
            names.append(str(name))
            weights.append(float(cfg.get("weight", 1.0)) if isinstance(cfg, dict) else 1.0)
        return self.random.choices(names, weights=weights, k=1)[0] if names else "valid_signal"

    def _scenario_config(self, name: str) -> Dict[str, Any]:
        scenarios = self.config.get("scenarios") or {}
        cfg = scenarios.get(name, {}) if isinstance(scenarios, dict) else {}
        return cfg if isinstance(cfg, dict) else {}

    def _range_pct(self, scenario: str, key: str, default: Sequence[float]) -> float:
        raw = self._scenario_config(scenario).get(key, default)
        if not isinstance(raw, Sequence) or isinstance(raw, str) or len(raw) < 2:
            raw = default
        return self.random.uniform(float(raw[0]), float(raw[1])) / 100.0

    def _build_morning_star(self, candles: List[Dict[str, Any]], scenario: str) -> List[Dict[str, Any]]:
        output = [dict(candle) for candle in candles]
        entry = float(output[-1]["close"])
        risk_pct = self._range_pct(
            scenario,
            "stop_distance_pct",
            [3.5, 6.0] if scenario == "excessive_risk" else [0.12, 0.28],
        )
        volatility_pct = self._range_pct(
            scenario,
            "candle_range_pct",
            [4.0, 8.0] if scenario == "high_volatility" else [0.35, 0.9],
        )

        base_volume = self._average_volume(output[:-3]) or 100.0
        if scenario == "low_volume":
            recovery_volume = base_volume * self.random.uniform(0.05, 0.25)
        else:
            recovery_volume = base_volume * self.random.uniform(1.4, 2.2)

        self._shape_prior_downtrend(output, entry)

        first_open = entry * (1.0 + risk_pct * 1.2)
        first_close = entry * (1.0 - risk_pct * 1.25)
        star_low = entry * (1.0 - risk_pct * 1.4)
        star_open = entry * (1.0 - risk_pct * 1.34)
        star_close = entry * (1.0 - risk_pct * 1.30)
        recovery_open = entry * (1.0 - risk_pct * 0.70)

        output[-3].update(
            open=first_open,
            high=max(first_open, first_close) * (1.0 + volatility_pct * 0.25),
            low=min(first_open, first_close) * (1.0 - volatility_pct * 0.25),
            close=first_close,
            volume=base_volume * self.random.uniform(1.0, 1.4),
            closed=True,
        )
        output[-2].update(
            open=star_open,
            high=max(star_open, star_close) * (1.0 + volatility_pct * 0.08),
            low=star_low,
            close=star_close,
            volume=base_volume * self.random.uniform(0.6, 1.0),
            closed=True,
        )
        output[-1].update(
            open=recovery_open,
            high=entry * (1.0 + volatility_pct * 0.35),
            low=min(star_low * (1.0 + risk_pct * 0.1), recovery_open),
            close=entry,
            volume=recovery_volume,
            closed=True,
        )
        return output

    def _stamp_synthetic_trigger(self, asset: str, candles: List[Dict[str, Any]]) -> None:
        sequence = self.sequence_by_asset.get(asset, 0) + 1
        self.sequence_by_asset[asset] = sequence
        offset = sequence / 1000.0
        for index, candle in enumerate(candles[-3:], start=1):
            timestamp = candle.get("timestamp")
            if isinstance(timestamp, (int, float)):
                candle["timestamp"] = float(timestamp) + offset + (index / 100000.0)

    def _shape_prior_downtrend(self, candles: List[Dict[str, Any]], entry: float) -> None:
        start = 0
        end = len(candles) - 3
        count = max(1, end - start)
        high_anchor = entry * self.random.uniform(1.08, 1.16)
        low_anchor = entry * self.random.uniform(1.015, 1.035)
        for offset, index in enumerate(range(start, end)):
            progress = offset / max(1, count - 1)
            close = high_anchor + (low_anchor - high_anchor) * progress
            body = close * self.random.uniform(0.0015, 0.004)
            candles[index].update(
                open=close + body,
                high=close + body * 1.8,
                low=close - body * 1.6,
                close=close,
                volume=float(candles[index].get("volume") or 100.0),
                closed=True,
            )

    def _build_no_signal(self, candles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        output = [dict(candle) for candle in candles]
        entry = float(output[-1]["close"])
        for index in range(max(0, len(output) - 6), len(output)):
            drift = self.random.uniform(-0.002, 0.002)
            close = entry * (1.0 + drift)
            body = close * self.random.uniform(0.0008, 0.002)
            output[index].update(
                open=close - body,
                high=close + body * 1.5,
                low=close - body * 1.5,
                close=entry if index == len(output) - 1 else close,
                closed=True,
            )
        return output

    def _average_volume(self, candles: List[Dict[str, Any]]) -> Optional[float]:
        sample = [float(candle.get("volume") or 0.0) for candle in candles[-20:]]
        sample = [value for value in sample if value > 0]
        return sum(sample) / len(sample) if sample else None

    def _generate_fallback_candles(self, limit: int) -> List[Dict[str, Any]]:
        import time
        candles = []
        now_ms = int(time.time() * 1000)
        step_ms = 14400000  # 4h default
        start_ts = now_ms - (limit * step_ms)
        for index in range(limit):
            close = 60000.0
            candles.append({
                "timestamp": float(start_ts + index * step_ms),
                "open": close,
                "high": close,
                "low": close,
                "close": close,
                "volume": 100.0,
                "closed": True,
            })
        return candles

    def _to_dict(self, raw: RawCandle) -> Dict[str, Any]:
        if isinstance(raw, dict):
            return dict(raw)
        if len(raw) < 5:
            raise ValueError("Candle OHLCV sequencial deve ter ao menos 5 campos.")
        return {
            "timestamp": raw[0],
            "open": raw[1],
            "high": raw[2],
            "low": raw[3],
            "close": raw[4],
            "volume": raw[5] if len(raw) > 5 else None,
            "closed": True,
        }
