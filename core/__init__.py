"""
ARSTrader - Core Package Initializer
====================================
Transforma o diretório 'core' em um pacote Python herdável.
Expõe de forma limpa as classes principais para o ponto de entrada global (main.py),
garantindo que a inicialização do ecossistema ocorra sem caminhos de importação redundantes.
"""

from core.config import ConfigManager
from core.database import DatabaseManager
from core.logger import LogManager
from core.server import SignalServer
from core.loader import ModuleLoader
from core.storage import GlobalStorage, storage
from core.wallet import WalletController
from core.orchestrator import GlobalOrchestrator
from core.web import TelemetryWebServer

__all__ = [
    "ConfigManager",
    "DatabaseManager",
    "LogManager",
    "SignalServer",
    "ModuleLoader",
    "GlobalStorage",
    "storage",
    "WalletController",
    "GlobalOrchestrator",
    "TelemetryWebServer",
]
