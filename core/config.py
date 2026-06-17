"""
ARSTrader - Config Manager (config.py)
=====================================
Responsável exclusivo por carregar, tipar e distribuir as variáveis contidas no arquivo 'global_config.yaml'.

Regras Operacionais:
1. Executa a leitura do arquivo YAML via thread pool dedicada para não bloquear o loop de eventos assíncrono.
2. Atua como um Singleton imutável em memória após o boot: fornece dados estruturados (Read-Only)
   para o restante do sistema.
"""

import asyncio
import os
from typing import Dict, Any, Optional, Union, List
from dataclasses import dataclass, field
import yaml


@dataclass(frozen=True)
class SystemConfig:
    environment: str
    heartbeat_timeout: int
    max_signal_latency_ms: int


@dataclass(frozen=True)
class WebServerConfig:
    host: str
    port: int


@dataclass(frozen=True)
class ExchangeConfig:
    enabled: bool
    api_key: str
    secret: str
    password: Optional[str]
    options: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class GlobalRiskConfig:
    execution_exchange: str
    max_daily_loss_pct: float
    max_simultaneous_trades: int
    default_stop_loss_pct: float
    default_take_profit_pct: float


@dataclass(frozen=True)
class ModuleRestrictionsConfig:
    target_markets: Union[str, List[str]]
    allowed_exchanges: Union[str, List[str]]
    activation_time: Optional[str]
    standby_time: Optional[str]


@dataclass(frozen=True)
class ModuleConfig:
    enabled: bool
    path: str
    class_name: str
    heartbeat_interval: Optional[int] = None
    restrictions: Optional[ModuleRestrictionsConfig] = None


class ConfigManager:
    def __init__(self, config_path: str = "global_config.yaml"):
        self.config_path = config_path

        # Atributos tipados que serão expostos publicamente como Read-Only
        self.system: Optional[SystemConfig] = None
        self.exchanges: Dict[str, ExchangeConfig] = {}
        self.global_risk: Optional[GlobalRiskConfig] = None
        self.modules: Dict[str, ModuleConfig] = {}
        self.web_server: Optional[WebServerConfig] = None

    async def load(self) -> "ConfigManager":
        """
        Ponto de entrada assíncrono para inicialização do arquivo de configuração.
        Delega a leitura do disco para um executor em thread separada.
        """
        loop = asyncio.get_running_loop()
        raw_dict = await loop.run_in_executor(None, self._read_yaml)
        self._parse_and_bind(raw_dict)
        return self

    def _read_yaml(self) -> Dict[str, Any]:
        """Executa a leitura física e síncrona do arquivo YAML."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"[Config] Arquivo de configuração não encontrado em: {self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as f:
            # SafeLoader garante proteção contra injeção de objetos arbitrários
            data = yaml.load(f, Loader=yaml.SafeLoader)
            if not data:
                raise ValueError(
                    f"[Config] O arquivo {self.config_path} está vazio ou corrompido."
                )
            return data

    def _parse_and_bind(self, raw: Dict[str, Any]) -> None:
        """
        Varre o dicionário bruto gerado pelo PyYAML e constrói a árvore de objetos tipados,
        tratando nulos e strings/curingas nativamente.
        """
        try:
            # 1. Parsing do bloco 'system'
            sys_data = raw["system"]
            self.__dict__["system"] = SystemConfig(
                environment=str(sys_data["environment"]),
                heartbeat_timeout=int(sys_data["heartbeat_timeout"]),
                max_signal_latency_ms=int(sys_data["max_signal_latency_ms"]),
            )

            # 2. Parsing do dicionário de 'exchanges'
            exchanges_dict = {}
            for name, ex_data in raw.get("exchanges", {}).items():
                exchanges_dict[name] = ExchangeConfig(
                    enabled=bool(ex_data.get("enabled", False)),
                    api_key=str(ex_data.get("api_key", "")),
                    secret=str(ex_data.get("secret", "")),
                    password=ex_data.get("password"),  # Mantém None se for null no YAML
                    options=dict(ex_data.get("options", {})),
                )
            self.__dict__["exchanges"] = exchanges_dict

            # 3. Parsing do bloco 'global_risk'
            risk_data = raw["global_risk"]
            self.__dict__["global_risk"] = GlobalRiskConfig(
                execution_exchange=str(risk_data["execution_exchange"]),
                max_daily_loss_pct=float(risk_data["max_daily_loss_pct"]),
                max_simultaneous_trades=int(risk_data["max_simultaneous_trades"]),
                default_stop_loss_pct=float(risk_data["default_stop_loss_pct"]),
                default_take_profit_pct=float(risk_data["default_take_profit_pct"]),
            )

            # 4. Parsing dinâmico do bloco 'modules'
            modules_dict = {}
            for mod_name, mod_data in raw.get("modules", {}).items():
                # Monta as restrições específicas se existirem no nó do módulo
                rest_config = None
                if "restrictions" in mod_data and mod_data["restrictions"]:
                    r_data = mod_data["restrictions"]
                    rest_config = ModuleRestrictionsConfig(
                        target_markets=r_data.get("target_markets", "*"),
                        allowed_exchanges=r_data.get("allowed_exchanges", "*"),
                        activation_time=r_data.get("activation_time"),
                        standby_time=r_data.get("standby_time"),
                    )

                modules_dict[mod_name] = ModuleConfig(
                    enabled=bool(mod_data.get("enabled", False)),
                    path=str(mod_data["path"]),
                    class_name=str(mod_data["class_name"]),
                    heartbeat_interval=mod_data.get("heartbeat_interval"),
                    restrictions=rest_config,
                )
            self.__dict__["modules"] = modules_dict

            # Sincroniza configurações com o storage de telemetria
            from core import storage

            if self.system:
                storage.config.environment = self.system.environment
                storage.config.heartbeat_timeout = float(self.system.heartbeat_timeout)

            # 5. Parsing do bloco 'web_server'
            web_data = raw.get("web_server", {})
            if web_data:
                self.__dict__["web_server"] = WebServerConfig(
                    host=str(web_data.get("host", "127.0.0.1")),
                    port=int(web_data.get("port", 8080))
                )
            else:
                self.__dict__["web_server"] = None

        except KeyError as e:
            raise KeyError(
                f"[Config] Chave obrigatória ausente no YAML durante o mapeamento estrutural: {e}"
            )
        except Exception as e:
            raise ValueError(
                f"[Config] Erro crítico na conversão de tipos das configurações: {e}"
            )
