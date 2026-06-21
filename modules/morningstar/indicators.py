"""
ARSTrader - Mathematical & Technical Analysis (indicators.py)
=============================================================
Funções stateless de suporte e validação do padrão Morning Star.
"""

from __future__ import annotations

from typing import Deque, Iterable, List, Optional

from modules.morningstar.state import Candle, SupportZone


def map_support_zone(
    candles: Deque[Candle],
    *,
    support_tolerance_pct: float,
) -> Optional[SupportZone]:
    lows: List[float] = []
    candle_list = list(candles)
    if not candle_list:
        return None

    for index in range(1, len(candle_list) - 1):
        previous_candle = candle_list[index - 1]
        current_candle = candle_list[index]
        next_candle = candle_list[index + 1]
        if current_candle.low <= previous_candle.low and current_candle.low <= next_candle.low:
            lows.append(current_candle.low)

    if not lows:
        lows.append(min(candle.low for candle in candle_list))

    current_price = candle_list[-1].close
    support_price = min(lows, key=lambda low: abs(current_price - low))
    tolerance = support_price * support_tolerance_pct
    return SupportZone(
        center=support_price,
        lower=support_price - tolerance,
        upper=support_price + tolerance,
    )


def price_is_on_support(candle: Candle, support: SupportZone) -> bool:
    return candle.low <= support.upper and candle.close >= support.lower


def is_valid_morning_star(
    candles: Deque[Candle],
    *,
    long_body_ratio: float,
    star_body_ratio: float,
) -> bool:
    if len(candles) < 3:
        return False

    candle_a, candle_b, candle_c = list(candles)[-3:]
    average_body = average_body_size(candles, exclude_last=3)
    if average_body <= 0:
        average_body = candle_a.body

    return (
        is_long_bearish(candle_a, average_body, long_body_ratio)
        and is_small_star_below_previous_body(candle_a, candle_b, star_body_ratio)
        and is_strong_bullish_recovery(candle_a, candle_c)
    )


def is_long_bearish(candle: Candle, average_body: float, long_body_ratio: float) -> bool:
    return candle.is_bearish and candle.body >= average_body * long_body_ratio


def is_small_star_below_previous_body(
    previous: Candle,
    star: Candle,
    star_body_ratio: float,
) -> bool:
    previous_body_bottom = min(previous.open, previous.close)
    star_body_top = max(star.open, star.close)
    return star.body <= previous.body * star_body_ratio and star_body_top <= previous_body_bottom


def is_strong_bullish_recovery(first: Candle, recovery: Candle) -> bool:
    return recovery.is_bullish and recovery.close > first.body_midpoint


def average_body_size(candles: Deque[Candle], *, exclude_last: int) -> float:
    sample = list(candles)[:-exclude_last]
    if not sample:
        return 0.0
    return sum(candle.body for candle in sample) / len(sample)


def average_volume(candles: Iterable[Candle], *, period: int) -> Optional[float]:
    sample = [candle.volume for candle in list(candles)[-period:] if candle.volume is not None]
    if len(sample) < period:
        return None
    return sum(sample) / len(sample)


def true_range(current: Candle, previous: Candle) -> float:
    return max(
        current.high - current.low,
        abs(current.high - previous.close),
        abs(current.low - previous.close),
    )


def atr(candles: Iterable[Candle], *, period: int) -> Optional[float]:
    candle_list = list(candles)
    if len(candle_list) < period + 1:
        return None

    ranges = [
        true_range(candle_list[index], candle_list[index - 1])
        for index in range(1, len(candle_list))
    ]
    sample = ranges[-period:]
    return sum(sample) / len(sample)


def atr_pct(candles: Iterable[Candle], *, period: int) -> Optional[float]:
    candle_list = list(candles)
    if not candle_list or candle_list[-1].close <= 0:
        return None

    value = atr(candle_list, period=period)
    if value is None:
        return None
    return value / candle_list[-1].close


def ema(values: Iterable[float], *, period: int) -> Optional[float]:
    value_list = list(values)
    if len(value_list) < period or period <= 0:
        return None

    multiplier = 2.0 / (period + 1.0)
    current = sum(value_list[:period]) / period
    for value in value_list[period:]:
        current = (value * multiplier) + (current * (1.0 - multiplier))
    return current


def rsi(values: Iterable[float], *, period: int) -> Optional[float]:
    value_list = list(values)
    if len(value_list) < period + 1 or period <= 0:
        return None

    gains: List[float] = []
    losses: List[float] = []
    for previous, current in zip(value_list[-period - 1 : -1], value_list[-period:]):
        change = current - previous
        gains.append(max(change, 0.0))
        losses.append(max(-change, 0.0))

    average_gain = sum(gains) / period
    average_loss = sum(losses) / period
    if average_loss == 0:
        return 100.0

    relative_strength = average_gain / average_loss
    return 100.0 - (100.0 / (1.0 + relative_strength))


def is_ema_downtrend(
    candles: Iterable[Candle],
    *,
    fast_period: int,
    slow_period: int,
) -> bool:
    closes = [candle.close for candle in candles]
    fast = ema(closes, period=fast_period)
    slow = ema(closes, period=slow_period)
    if fast is None or slow is None:
        return False
    return fast < slow and closes[-1] < fast
