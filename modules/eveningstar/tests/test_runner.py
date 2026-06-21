import argparse

import pytest

from modules.eveningstar.runner import (
    build_fetcher_config,
    build_filters_config,
    build_strategy_kwargs,
    expand_env_vars,
    load_module_config,
)


def _args(**overrides):
    defaults = {
        "assets": None,
        "timeframe": None,
        "check_interval": None,
        "exchange": None,
        "market": None,
        "core_host": "127.0.0.1",
        "core_port": 8888,
        "heartbeat_interval": 5.0,
    }
    defaults.update(overrides)
    return argparse.Namespace(**defaults)


def test_runner_builds_strategy_kwargs_from_local_config():
    config = {
        "assets": ["BTC/USDT", "ETH/USDT"],
        "timeframe": "4h",
        "check_interval": 30,
        "exchange": "binance",
        "market": "FUTURES",
        "order_response_timeout": 120,
        "reward_risk_ratio": 2.0,
        "resistance_tolerance_pct": 0.005,
        "stop_buffer_pct": 0.001,
        "long_body_ratio": 1.2,
        "star_body_ratio": 0.35,
        "candle_limit": 100,
        "filters": {"volume": {"enabled": True}},
    }

    kwargs = build_strategy_kwargs(_args(), config)

    assert kwargs["assets"] == ["BTC/USDT", "ETH/USDT"]
    assert kwargs["timeframe"] == "4h"
    assert kwargs["check_interval"] == 30.0
    assert kwargs["exchange"] == "binance"
    assert kwargs["market"] == "FUTURES"
    assert kwargs["core_host"] == "127.0.0.1"
    assert kwargs["core_port"] == 8888
    assert kwargs["heartbeat_interval"] == 5.0
    assert kwargs["order_response_timeout"] == 120.0
    assert kwargs["candle_limit"] == 100
    assert kwargs["filters"] == {"volume": {"enabled": True}}


def test_runner_cli_args_override_local_config():
    config = {
        "assets": ["BTC/USDT"],
        "timeframe": "4h",
        "check_interval": 60,
        "exchange": "binance",
        "market": "FUTURES",
        "order_response_timeout": 120,
        "reward_risk_ratio": 2.0,
        "resistance_tolerance_pct": 0.005,
        "stop_buffer_pct": 0.001,
        "long_body_ratio": 1.2,
        "star_body_ratio": 0.35,
        "candle_limit": 100,
    }

    kwargs = build_strategy_kwargs(
        _args(
            assets=["SOL/USDT"],
            timeframe="1h",
            check_interval=10,
            exchange="binanceusdm",
            market="FUTURES",
        ),
        config,
    )

    assert kwargs["assets"] == ["SOL/USDT"]
    assert kwargs["timeframe"] == "1h"
    assert kwargs["check_interval"] == 10.0
    assert kwargs["exchange"] == "binanceusdm"


def test_runner_requires_assets():
    with pytest.raises(ValueError, match="assets"):
        build_strategy_kwargs(_args(), {})


def test_runner_expands_env_values_from_module_env(tmp_path):
    env_path = tmp_path / ".env"
    config_path = tmp_path / "config.yaml"
    env_path.write_text(
        "EVENINGSTAR_BINANCE_API_KEY=key-123\n"
        "EVENINGSTAR_BINANCE_SECRET=secret-456\n",
        encoding="utf-8",
    )
    config_path.write_text(
        "assets:\n"
        "  - BTC/USDT\n"
        "fetcher:\n"
        "  exchange_options:\n"
        "    apiKey: ${EVENINGSTAR_BINANCE_API_KEY:}\n"
        "    secret: ${EVENINGSTAR_BINANCE_SECRET:}\n",
        encoding="utf-8",
    )

    config = load_module_config(str(config_path), str(env_path))

    assert config["fetcher"]["exchange_options"]["apiKey"] == "key-123"
    assert config["fetcher"]["exchange_options"]["secret"] == "secret-456"


def test_runner_expands_default_env_value(monkeypatch):
    monkeypatch.delenv("EVENINGSTAR_MISSING_VALUE", raising=False)

    expanded = expand_env_vars({"value": "${EVENINGSTAR_MISSING_VALUE:fallback}"})

    assert expanded == {"value": "fallback"}


def test_runner_validates_fetcher_config_shape():
    with pytest.raises(ValueError, match="fetcher"):
        build_fetcher_config({"fetcher": []})


def test_runner_validates_filters_config_shape():
    with pytest.raises(ValueError, match="filters"):
        build_filters_config({"filters": []})
