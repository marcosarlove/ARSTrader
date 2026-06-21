"""
ARSTrader - Evening Star Strategy
=================================
Estratégia concreta multimercado baseada no padrão Evening Star em resistência.
"""

from __future__ import annotations

import asyncio
import inspect
import uuid
from typing import Any, Awaitable, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Union

from modules.base_module import BaseStrategyModule
from modules.eveningstar.indicators import (
    atr_pct,
    average_volume,
    is_ema_uptrend,
    is_valid_evening_star,
    map_resistance_zone,
    price_is_on_resistance,
    rsi,
)
from modules.eveningstar.state import Candle, MarketState


RawCandle = Union[Dict[str, Any], Sequence[Any]]
OhlcvFetcher = Callable[[str, str, int], Union[Iterable[RawCandle], Awaitable[Iterable[RawCandle]]]]


class EveningStarStrategy(BaseStrategyModule):
    """
    Estratégia multimercado Evening Star.

    A estratégia identifica reversão bearish em resistência, calcula SL/TP para
    uma venda e envia o sinal ao Core via contrato IPC herdado.
    """

    def __init__(
        self,
        *,
        assets: List[str],
        timeframe: str,
        check_interval: float,
        exchange: str,
        market: str,
        reward_risk_ratio: float,
        resistance_tolerance_pct: float,
        stop_buffer_pct: float,
        long_body_ratio: float,
        star_body_ratio: float,
        candle_limit: int,
        filters: Optional[Dict[str, Any]] = None,
        ohlcv_fetcher: Optional[OhlcvFetcher] = None,
        **base_kwargs: Any,
    ) -> None:
        super().__init__(name="eveningstar", **base_kwargs)

        if not assets:
            raise ValueError("assets deve conter ao menos um ativo.")
        if check_interval <= 0:
            raise ValueError("check_interval deve ser maior que zero.")
        if reward_risk_ratio <= 0:
            raise ValueError("reward_risk_ratio deve ser maior que zero.")
        if resistance_tolerance_pct <= 0:
            raise ValueError("resistance_tolerance_pct deve ser maior que zero.")
        if stop_buffer_pct < 0:
            raise ValueError("stop_buffer_pct não pode ser negativo.")
        if candle_limit <= 0 or candle_limit > 100:
            raise ValueError("candle_limit deve estar entre 1 e 100.")

        self.assets = [asset.strip().upper() for asset in assets if asset.strip()]
        self.timeframe = timeframe.strip()
        self.check_interval = float(check_interval)
        self.ohlcv_fetcher = ohlcv_fetcher
        self.exchange = exchange.strip().lower()
        self.market = market.strip().upper()
        self.reward_risk_ratio = float(reward_risk_ratio)
        self.resistance_tolerance_pct = float(resistance_tolerance_pct)
        self.stop_buffer_pct = float(stop_buffer_pct)
        self.long_body_ratio = float(long_body_ratio)
        self.star_body_ratio = float(star_body_ratio)
        self.candle_limit = int(candle_limit)
        self.filters = filters or {}
        self.market_state: Dict[str, MarketState] = {
            asset: MarketState() for asset in self.assets
        }
        enabled_filters = sorted(
            name
            for name, config in self.filters.items()
            if isinstance(config, dict) and config.get("enabled")
        )
        self.logger.info(
            "[%s] configurada: assets=%s timeframe=%s check_interval=%.2fs candle_limit=%d filters=%s",
            self.name,
            ",".join(self.assets),
            self.timeframe,
            self.check_interval,
            self.candle_limit,
            enabled_filters or "none",
        )

    async def run_strategy(self) -> None:
        """Dispara um worker independente por ativo e aguarda shutdown."""
        for asset in self.assets:
            self.create_background_task(
                self._asset_worker(asset),
                name=f"worker:{asset}",
                critical=False,
            )
        await self._shutdown_event.wait()

    async def _asset_worker(self, asset: str) -> None:
        """Loop operacional isolado para um único ativo."""
        while self._is_running:
            try:
                await self._process_asset(asset)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.logger.error("[%s] erro no worker %s: %s", self.name, asset, exc)
            await asyncio.sleep(self.check_interval)

    async def _process_asset(self, asset: str) -> None:
        state = self.market_state[asset]
        await self._refresh_candles(asset, state)
        if len(state.candles) < 20:
            self.logger.info(
                "[%s] %s ignorado: candles fechados insuficientes (%d/20)",
                self.name,
                asset,
                len(state.candles),
            )
            return

        if not is_valid_evening_star(
            state.candles,
            long_body_ratio=self.long_body_ratio,
            star_body_ratio=self.star_body_ratio,
        ):
            self.logger.info(
                "[%s] %s sem sinal: padrão Evening Star inválido últimos3=%s",
                self.name,
                asset,
                self._format_candles(list(state.candles)[-3:]),
            )
            return

        state.resistance = map_resistance_zone(
            state.candles,
            resistance_tolerance_pct=self.resistance_tolerance_pct,
        )
        if state.resistance is None:
            self.logger.info("[%s] %s ignorado: resistência não encontrada", self.name, asset)
            return

        latest_candle = state.candles[-1]
        if not price_is_on_resistance(latest_candle, state.resistance):
            self.logger.info(
                "[%s] %s sem sinal: Evening Star válido, mas preço fora da resistência close=%.8f high=%.8f resistance=[%.8f, %.8f]",
                self.name,
                asset,
                latest_candle.close,
                latest_candle.high,
                state.resistance.lower,
                state.resistance.upper,
            )
            return

        signal_key = self._build_signal_key(list(state.candles)[-3:])
        if state.pending_order:
            self.logger.info("[%s] %s ignorado: ordem pendente para gatilho atual", self.name, asset)
            return
        if state.last_consumed_signal_key == signal_key:
            self.logger.info("[%s] %s ignorado: gatilho Evening Star já consumido", self.name, asset)
            return
        passed_filters, filter_reason = self._confirmation_filter_verdict(state, signal_key)
        if not passed_filters:
            self.logger.info("[%s] %s bloqueado por filtro: %s", self.name, asset, filter_reason)
            return

        self.logger.info(
            "[%s] %s sinal Evening Star aprovado: entry=%.8f resistance=[%.8f, %.8f] signal_key=%s",
            self.name,
            asset,
            latest_candle.close,
            state.resistance.lower,
            state.resistance.upper,
            signal_key,
        )
        await self._emit_open_order(asset, state, signal_key)

    async def _refresh_candles(self, asset: str, state: MarketState) -> None:
        raw_candles = await self._fetch_ohlcv(asset, limit=self.candle_limit)
        closed_candles = [
            self._normalize_candle(raw)
            for raw in raw_candles
            if self._is_closed_candle(raw)
        ]
        state.candles.clear()
        state.candles.extend(closed_candles[-self.candle_limit:])
        latest_ts = state.candles[-1].timestamp if state.candles else None
        self.logger.info(
            "[%s] %s candles atualizados: raw=%d closed=%d stored=%d latest_ts=%s",
            self.name,
            asset,
            len(raw_candles) if hasattr(raw_candles, "__len__") else -1,
            len(closed_candles),
            len(state.candles),
            latest_ts,
        )

    async def _fetch_ohlcv(self, asset: str, *, limit: int) -> Iterable[RawCandle]:
        if self.ohlcv_fetcher is None:
            raise NotImplementedError("Nenhum ohlcv_fetcher foi configurado para a estratégia.")

        result = self.ohlcv_fetcher(asset, self.timeframe, limit)
        if inspect.isawaitable(result):
            return await result
        return result

    async def _emit_open_order(
        self,
        asset: str,
        state: MarketState,
        signal_key: Tuple[Any, ...],
    ) -> None:
        star = state.candles[-2]
        entry = state.candles[-1].close
        stop_loss = self._calculate_stop_loss(star)
        take_profit = self._calculate_take_profit(entry, stop_loss)
        guid = str(uuid.uuid4())

        state.pending_order = True
        state.last_signal_guid = guid
        try:
            self.logger.info(
                "[%s] %s enviando ordem SELL: guid=%s entry=%.8f stop_loss=%.8f take_profit=%.8f market=%s exchange=%s",
                self.name,
                asset,
                guid,
                entry,
                stop_loss,
                take_profit,
                self.market,
                self.exchange,
            )
            response = await self.open_order(
                guid=guid,
                symbol=asset,
                exchange=self.exchange,
                operation="SELL",
                price=entry,
                market=self.market,
                stop_loss=stop_loss,
                take_profit=take_profit,
            )
            state.last_order_response = response
            state.open_position = response.get("status") == "EXECUTED"
            if response.get("status") in {"EXECUTED", "IGNORED"}:
                state.last_consumed_signal_key = signal_key
            self.logger.info(
                "[%s] %s resposta do Core: guid=%s status=%s reason=%s consumed=%s",
                self.name,
                asset,
                guid,
                response.get("status"),
                response.get("reason"),
                state.last_consumed_signal_key == signal_key,
            )
        finally:
            state.pending_order = False

    def _build_signal_key(self, candles: Sequence[Candle]) -> Tuple[Any, ...]:
        key = []
        for candle in candles:
            key.append(
                candle.timestamp
                if candle.timestamp is not None
                else (candle.open, candle.high, candle.low, candle.close)
            )
        return tuple(key)

    def _format_candles(self, candles: Sequence[Candle]) -> str:
        return ";".join(
            (
                f"ts={candle.timestamp},"
                f"o={candle.open:.8f},h={candle.high:.8f},"
                f"l={candle.low:.8f},c={candle.close:.8f}"
            )
            for candle in candles
        )

    def _passes_confirmation_filters(
        self,
        state: MarketState,
        signal_key: Tuple[Any, ...],
    ) -> bool:
        passed, _reason = self._confirmation_filter_verdict(state, signal_key)
        return passed

    def _confirmation_filter_verdict(
        self,
        state: MarketState,
        signal_key: Tuple[Any, ...],
    ) -> Tuple[bool, str]:
        candle_list = list(state.candles)
        checks = (
            ("volume", self._passes_volume_filter(candle_list)),
            ("volatility", self._passes_volatility_filter(candle_list)),
            ("trend", self._passes_trend_filter(candle_list)),
            ("momentum", self._passes_momentum_filter(candle_list)),
            ("risk", self._passes_risk_filter(candle_list)),
            ("cooldown", self._passes_cooldown_filter(candle_list, signal_key, state)),
        )
        for name, passed in checks:
            if not passed:
                return False, name
        return True, "passed"

    def _filter_config(self, name: str) -> Dict[str, Any]:
        config = self.filters.get(name, {})
        return config if isinstance(config, dict) else {}

    def _filter_enabled(self, name: str) -> bool:
        return bool(self._filter_config(name).get("enabled", False))

    def _passes_volume_filter(self, candles: Sequence[Candle]) -> bool:
        if not self._filter_enabled("volume"):
            return True

        config = self._filter_config("volume")
        lookback = int(config.get("lookback", 20))
        min_ratio = float(config.get("reversal_min_ratio", 1.2))
        reversal = candles[-1]
        if reversal.volume is None:
            return False

        baseline = average_volume(candles[:-1], period=lookback)
        return baseline is not None and reversal.volume >= baseline * min_ratio

    def _passes_volatility_filter(self, candles: Sequence[Candle]) -> bool:
        if not self._filter_enabled("volatility"):
            return True

        config = self._filter_config("volatility")
        period = int(config.get("atr_period", 14))
        max_pct = float(config.get("max_atr_pct", 0.03))
        current_atr_pct = atr_pct(candles, period=period)
        return current_atr_pct is not None and current_atr_pct <= max_pct

    def _passes_trend_filter(self, candles: Sequence[Candle]) -> bool:
        if not self._filter_enabled("trend"):
            return True

        config = self._filter_config("trend")
        if not bool(config.get("require_prior_uptrend", True)):
            return True

        fast_period = int(config.get("ema_fast", 20))
        slow_period = int(config.get("ema_slow", 50))
        return is_ema_uptrend(
            candles[:-3],
            fast_period=fast_period,
            slow_period=slow_period,
        )

    def _passes_momentum_filter(self, candles: Sequence[Candle]) -> bool:
        if not self._filter_enabled("momentum"):
            return True

        config = self._filter_config("momentum")
        period = int(config.get("rsi_period", 14))
        min_rsi = float(config.get("min_rsi", 55.0))
        closes_through_star = [candle.close for candle in candles[:-1]]
        current_rsi = rsi(closes_through_star, period=period)
        return current_rsi is not None and current_rsi >= min_rsi

    def _passes_risk_filter(self, candles: Sequence[Candle]) -> bool:
        if not self._filter_enabled("risk"):
            return True

        config = self._filter_config("risk")
        max_signal_risk_pct = float(config.get("max_signal_risk_pct", 0.02))
        star = candles[-2]
        entry = candles[-1].close
        stop_loss = self._calculate_stop_loss(star)
        risk = stop_loss - entry
        return entry > 0 and risk > 0 and risk <= entry * max_signal_risk_pct

    def _passes_cooldown_filter(
        self,
        candles: Sequence[Candle],
        signal_key: Tuple[Any, ...],
        state: MarketState,
    ) -> bool:
        if not self._filter_enabled("cooldown"):
            return True
        if state.last_consumed_signal_key is None:
            return True

        config = self._filter_config("cooldown")
        cooldown_candles = int(config.get("candles", 3))
        if cooldown_candles <= 0:
            return True

        last_consumed_reversal_key = state.last_consumed_signal_key[-1]
        if last_consumed_reversal_key == signal_key[-1]:
            return False

        for index, candle in enumerate(candles):
            candle_key = (
                candle.timestamp
                if candle.timestamp is not None
                else (candle.open, candle.high, candle.low, candle.close)
            )
            if candle_key == last_consumed_reversal_key:
                candles_after = len(candles) - 1 - index
                return candles_after >= cooldown_candles

        current_reversal_key = signal_key[-1]
        if isinstance(last_consumed_reversal_key, (int, float)) and isinstance(
            current_reversal_key,
            (int, float),
        ):
            return (current_reversal_key - last_consumed_reversal_key) >= cooldown_candles

        return True

    def _calculate_stop_loss(self, star: Candle) -> float:
        return star.high * (1.0 + self.stop_buffer_pct)

    def _calculate_take_profit(self, entry: float, stop_loss: float) -> float:
        risk = stop_loss - entry
        return entry - (risk * self.reward_risk_ratio)

    def _normalize_candle(self, raw: RawCandle) -> Candle:
        if isinstance(raw, dict):
            return Candle(
                timestamp=self._optional_float(raw.get("timestamp") or raw.get("time")),
                open=float(raw["open"]),
                high=float(raw["high"]),
                low=float(raw["low"]),
                close=float(raw["close"]),
                volume=self._optional_float(raw.get("volume")),
                closed=bool(raw.get("closed", True)),
            )

        if len(raw) < 5:
            raise ValueError("Candle OHLCV sequencial deve ter ao menos 5 campos.")

        return Candle(
            timestamp=self._optional_float(raw[0]),
            open=float(raw[1]),
            high=float(raw[2]),
            low=float(raw[3]),
            close=float(raw[4]),
            volume=self._optional_float(raw[5]) if len(raw) > 5 else None,
            closed=True,
        )

    def _is_closed_candle(self, raw: RawCandle) -> bool:
        if isinstance(raw, dict):
            return bool(raw.get("closed", True))
        return True

    def _optional_float(self, value: Any) -> Optional[float]:
        if value is None:
            return None
        return float(value)
