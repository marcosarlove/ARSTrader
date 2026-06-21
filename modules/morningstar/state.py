"""
ARSTrader - Local Market Memory Manager (state.py)
==================================================
Estruturas de estado locais da estratégia Morning Star.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Any, Deque, Dict, Optional, Tuple


@dataclass(frozen=True)
class Candle:
    """Representa uma vela fechada normalizada para análise estrutural."""

    timestamp: Optional[float]
    open: float
    high: float
    low: float
    close: float
    volume: Optional[float] = None
    closed: bool = True

    @property
    def body(self) -> float:
        return abs(self.close - self.open)

    @property
    def is_bearish(self) -> bool:
        return self.close < self.open

    @property
    def is_bullish(self) -> bool:
        return self.close > self.open

    @property
    def body_midpoint(self) -> float:
        return min(self.open, self.close) + (self.body / 2.0)


@dataclass(frozen=True)
class SupportZone:
    """Faixa de suporte calculada a partir de pivôs/fundos recentes."""

    center: float
    lower: float
    upper: float


@dataclass
class MarketState:
    """Estado isolado por ativo monitorado."""

    candles: Deque[Candle] = field(default_factory=lambda: deque(maxlen=100))
    support: Optional[SupportZone] = None
    pending_order: bool = False
    open_position: bool = False
    last_consumed_signal_key: Optional[Tuple[Any, ...]] = None
    last_signal_guid: Optional[str] = None
    last_order_response: Optional[Dict[str, Any]] = None
