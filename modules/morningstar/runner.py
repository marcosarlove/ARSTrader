"""
ARSTrader - Morning Star Process Runner
=======================================
Entrada executável do subprocesso isolado da estratégia Morning Star.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from modules.morningstar.strategy import MorningStarStrategy


DEFAULT_CONFIG_PATH = Path(__file__).with_name("config.yaml")
DEFAULT_ENV_PATH = Path(__file__).with_name(".env")


class AsyncCcxtOhlcvFetcher:
    """Adaptador assíncrono de OHLCV mantido fora da lógica da estratégia."""

    def __init__(
        self,
        *,
        exchange_id: str,
        exchange_options: Optional[Dict[str, Any]] = None,
        ohlcv_params: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.exchange_id = exchange_id
        self.exchange_options = exchange_options or {}
        self.ohlcv_params = ohlcv_params or {}
        self._exchange: Optional[Any] = None

    async def __call__(self, asset: str, timeframe: str, limit: int) -> Iterable[List[Any]]:
        exchange = await self._get_exchange()
        return await exchange.fetch_ohlcv(
            asset,
            timeframe=timeframe,
            limit=limit,
            params=self.ohlcv_params,
        )

    async def close(self) -> None:
        if self._exchange is None:
            return
        await self._exchange.close()
        self._exchange = None

    async def _get_exchange(self) -> Any:
        if self._exchange is not None:
            return self._exchange

        import ccxt.async_support as ccxt_async

        exchange_class = getattr(ccxt_async, self.exchange_id)
        self._exchange = exchange_class(
            {
                "enableRateLimit": True,
                **self.exchange_options,
            }
        )
        return self._exchange


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ARSTrader Morning Star strategy runner")
    parser.add_argument("--name", default="morningstar")
    parser.add_argument("--class", dest="class_name", default="MorningStar")
    parser.add_argument("--core-host", required=True)
    parser.add_argument("--core-port", required=True, type=int)
    parser.add_argument("--heartbeat-interval", required=True, type=float)
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--env", default=str(DEFAULT_ENV_PATH))
    parser.add_argument("--assets", nargs="*")
    parser.add_argument("--timeframe")
    parser.add_argument("--check-interval", type=float)
    parser.add_argument("--exchange")
    parser.add_argument("--market")
    return parser.parse_args()


def load_module_config(config_path: str, env_path: str = str(DEFAULT_ENV_PATH)) -> Dict[str, Any]:
    load_module_env(env_path)
    path = Path(config_path)
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file) or {}

    if not isinstance(config, dict):
        raise ValueError(f"Configuração inválida em {path}. Esperado mapa YAML.")
    return expand_env_vars(config)


def load_module_env(env_path: str) -> None:
    path = Path(env_path)
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


def expand_env_vars(value: Any) -> Any:
    pattern = re.compile(r"\$\{([A-Za-z0-9_]+)(?::([^}]*))?\}")

    def replace_env(match: re.Match[str]) -> str:
        var_name = match.group(1)
        default_value = match.group(2)
        env_value = os.environ.get(var_name)
        if env_value is not None:
            return env_value
        if default_value is not None:
            return default_value
        return ""

    if isinstance(value, str):
        return pattern.sub(replace_env, value)
    if isinstance(value, dict):
        return {key: expand_env_vars(item) for key, item in value.items()}
    if isinstance(value, list):
        return [expand_env_vars(item) for item in value]
    return value


def build_strategy_kwargs(args: argparse.Namespace, config: Dict[str, Any]) -> Dict[str, Any]:
    assets = args.assets or require_config(config, "assets")
    if not assets:
        raise ValueError("MorningStar exige ao menos um ativo em assets.")

    return {
        "assets": [str(asset).upper() for asset in assets],
        "timeframe": str(args.timeframe or require_config(config, "timeframe")),
        "check_interval": float(args.check_interval or require_config(config, "check_interval")),
        "exchange": str(args.exchange or require_config(config, "exchange")),
        "market": str(args.market or require_config(config, "market")),
        "reward_risk_ratio": float(require_config(config, "reward_risk_ratio")),
        "support_tolerance_pct": float(require_config(config, "support_tolerance_pct")),
        "stop_buffer_pct": float(require_config(config, "stop_buffer_pct")),
        "long_body_ratio": float(require_config(config, "long_body_ratio")),
        "star_body_ratio": float(require_config(config, "star_body_ratio")),
        "candle_limit": int(require_config(config, "candle_limit")),
        "filters": build_filters_config(config),
        "core_host": args.core_host,
        "core_port": args.core_port,
        "heartbeat_interval": args.heartbeat_interval,
        "order_response_timeout": float(require_config(config, "order_response_timeout")),
    }


def build_fetcher_config(config: Dict[str, Any]) -> Dict[str, Any]:
    fetcher_config = config.get("fetcher", {})
    if fetcher_config is None:
        fetcher_config = {}
    if not isinstance(fetcher_config, dict):
        raise ValueError("fetcher deve ser um mapa YAML.")
    return fetcher_config


def build_filters_config(config: Dict[str, Any]) -> Dict[str, Any]:
    filters_config = config.get("filters", {})
    if filters_config is None:
        filters_config = {}
    if not isinstance(filters_config, dict):
        raise ValueError("filters deve ser um mapa YAML.")
    return filters_config


def require_config(config: Dict[str, Any], key: str) -> Any:
    if key not in config or config[key] in (None, ""):
        raise ValueError(f"Configuração obrigatória ausente: {key}")
    return config[key]


async def amain() -> int:
    args = parse_args()
    config = load_module_config(args.config, args.env)
    strategy_kwargs = build_strategy_kwargs(args, config)
    fetcher_config = build_fetcher_config(config)

    fetcher = AsyncCcxtOhlcvFetcher(
        exchange_id=str(require_config(fetcher_config, "exchange_id")),
        exchange_options=dict(require_config(fetcher_config, "exchange_options")),
        ohlcv_params=dict(require_config(fetcher_config, "ohlcv_params")),
    )
    strategy = MorningStarStrategy(
        ohlcv_fetcher=fetcher,
        **strategy_kwargs,
    )

    try:
        return await strategy.start()
    finally:
        await fetcher.close()

def main() -> None:
    raise SystemExit(asyncio.run(amain()))


if __name__ == "__main__":
    main()
