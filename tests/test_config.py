import pytest
import os
import yaml
from core.config import ConfigManager, SystemConfig, ExchangeConfig, GlobalRiskConfig, ModuleConfig, ModuleRestrictionsConfig

@pytest.fixture
def valid_yaml_content():
    """Retorna uma estrutura de dicionário contendo um arquivo YAML de configuração válido."""
    return {
        "system": {
            "environment": "sandbox",
            "heartbeat_timeout": 5,
            "max_signal_latency_ms": 50
        },
        "exchanges": {
            "binance": {
                "enabled": True,
                "api_key": "API_KEY_BINANCE",
                "secret": "SECRET_BINANCE",
                "password": None,
                "options": {
                    "defaultType": "future",
                    "adjustForTimeDifference": True
                }
            },
            "bybit": {
                "enabled": False,
                "api_key": "API_KEY_BYBIT",
                "secret": "SECRET_BYBIT",
                "password": "some_password",
                "options": {
                    "defaultType": "linear"
                }
            }
        },
        "global_risk": {
            "execution_exchange": "binance",
            "max_daily_loss_pct": 2.0,
            "max_simultaneous_trades": 3,
            "default_stop_loss_pct": 1.5,
            "default_take_profit_pct": 3.0
        },
        "modules": {
            "dashboard": {
                "enabled": True,
                "path": "dashboard",
                "class_name": "DashboardServer",
                "port": 8000,
                "host": "127.0.0.1"
            },
            "morningstar": {
                "enabled": True,
                "path": "morningstar",
                "class_name": "MorningStar",
                "heartbeat_interval": 2,
                "restrictions": {
                    "target_markets": "*/USDT",
                    "allowed_exchanges": "*",
                    "activation_time": "07:00:00",
                    "standby_time": None
                }
            }
        }
    }

def create_temp_yaml(directory, content) -> str:
    """Helper para persistir o dicionário em um arquivo YAML temporário gerenciado pelo pytest."""
    file_path = directory / "config.yaml"
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(content, f, default_flow_style=False)
    return str(file_path)

@pytest.mark.asyncio
async def test_load_valid_config(tmp_path, valid_yaml_content):
    """Testa se um arquivo YAML válido é carregado e convertido corretamente para as instâncias tipadas."""
    temp_path = create_temp_yaml(tmp_path, valid_yaml_content)
    manager = ConfigManager(config_path=temp_path)
    
    await manager.load()

    # 1. Validações do bloco 'system'
    assert manager.system is not None
    assert isinstance(manager.system, SystemConfig)
    assert manager.system.environment == "sandbox"
    assert manager.system.heartbeat_timeout == 5
    assert manager.system.max_signal_latency_ms == 50

    # 2. Validações de 'exchanges'
    assert "binance" in manager.exchanges
    assert "bybit" in manager.exchanges
    
    binance = manager.exchanges["binance"]
    assert isinstance(binance, ExchangeConfig)
    assert binance.enabled is True
    assert binance.api_key == "API_KEY_BINANCE"
    assert binance.secret == "SECRET_BINANCE"
    assert binance.password is None
    assert binance.options["defaultType"] == "future"
    assert binance.options["adjustForTimeDifference"] is True

    bybit = manager.exchanges["bybit"]
    assert bybit.enabled is False
    assert bybit.api_key == "API_KEY_BYBIT"
    assert bybit.secret == "SECRET_BYBIT"
    assert bybit.password == "some_password"

    # 3. Validações de 'global_risk'
    assert manager.global_risk is not None
    assert isinstance(manager.global_risk, GlobalRiskConfig)
    assert manager.global_risk.execution_exchange == "binance"
    assert manager.global_risk.max_daily_loss_pct == 2.0
    assert manager.global_risk.max_simultaneous_trades == 3
    assert manager.global_risk.default_stop_loss_pct == 1.5
    assert manager.global_risk.default_take_profit_pct == 3.0

    # 4. Validações de 'modules'
    assert "dashboard" in manager.modules
    assert "morningstar" in manager.modules

    dashboard = manager.modules["dashboard"]
    assert isinstance(dashboard, ModuleConfig)
    assert dashboard.enabled is True
    assert dashboard.path == "dashboard"
    assert dashboard.class_name == "DashboardServer"
    assert dashboard.port == 8000
    assert dashboard.host == "127.0.0.1"
    assert dashboard.restrictions is None

    morningstar = manager.modules["morningstar"]
    assert isinstance(morningstar, ModuleConfig)
    assert morningstar.enabled is True
    assert morningstar.heartbeat_interval == 2
    assert morningstar.restrictions is not None
    
    rest = morningstar.restrictions
    assert isinstance(rest, ModuleRestrictionsConfig)
    assert rest.target_markets == "*/USDT"
    assert rest.allowed_exchanges == "*"
    assert rest.activation_time == "07:00:00"
    assert rest.standby_time is None

    # 5. Validações da integração com o storage global
    from core import storage
    assert storage.config.environment == "sandbox"
    assert storage.config.heartbeat_timeout == 5.0

@pytest.mark.asyncio
async def test_load_file_not_found(tmp_path):
    """Testa se um FileNotFoundError é lançado ao tentar carregar um arquivo inexistente."""
    non_existent_path = str(tmp_path / "does_not_exist.yaml")
    manager = ConfigManager(config_path=non_existent_path)
    
    with pytest.raises(FileNotFoundError) as exc_info:
        await manager.load()
    assert "Arquivo de configuração não encontrado" in str(exc_info.value)

@pytest.mark.asyncio
async def test_load_empty_file(tmp_path):
    """Testa se um ValueError é lançado ao tentar carregar um arquivo vazio."""
    temp_path = tmp_path / "empty.yaml"
    temp_path.write_text("")  # Cria o arquivo vazio

    manager = ConfigManager(config_path=str(temp_path))
    with pytest.raises(ValueError) as exc_info:
        await manager.load()
    assert "está vazio ou corrompido" in str(exc_info.value)

@pytest.mark.asyncio
async def test_load_missing_required_key(tmp_path, valid_yaml_content):
    """Testa se KeyError é lançado ao faltar uma seção obrigatória (ex: 'system')."""
    invalid_content = valid_yaml_content.copy()
    del invalid_content["system"]
    
    temp_path = create_temp_yaml(tmp_path, invalid_content)
    manager = ConfigManager(config_path=temp_path)
    
    with pytest.raises(KeyError) as exc_info:
        await manager.load()
    assert "Chave obrigatória ausente no YAML" in str(exc_info.value)
    assert "system" in str(exc_info.value)

@pytest.mark.asyncio
async def test_load_invalid_value_type(tmp_path, valid_yaml_content):
    """Testa se ValueError é lançado quando um tipo de dado é incompatível (ex: heartbeat_timeout como string não numérica)."""
    invalid_content = valid_yaml_content.copy()
    invalid_content["system"] = {
        "environment": "sandbox",
        "heartbeat_timeout": "nao_sou_um_numero",
        "max_signal_latency_ms": 50
    }
    
    temp_path = create_temp_yaml(tmp_path, invalid_content)
    manager = ConfigManager(config_path=temp_path)
    
    with pytest.raises(ValueError) as exc_info:
        await manager.load()
    assert "Erro crítico na conversão de tipos" in str(exc_info.value)
