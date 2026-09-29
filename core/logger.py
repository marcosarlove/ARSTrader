"""
ARSTrader - Non-Blocking Central Logger (logger.py)
===================================================
Responsável por centralizar o fluxo de logs da aplicação de forma assíncrona,
evitando travar o Event Loop de trading. Utiliza fila em memória (QueueHandler)
e o handler de arquivo rotativo nativo (RotatingFileHandler) para boot instantâneo.
"""

import os
import sys
import queue
import logging
import logging.handlers
from typing import Any, Optional
from dotenv import load_dotenv

# Carrega as variáveis do ficheiro .env
load_dotenv()

# Nível customizado para logs de status/visualização
STATUS_LEVEL_NUM = 25
logging.addLevelName(STATUS_LEVEL_NUM, "STATUS")


def status(self, message, *args, **kws):
    """Método helper para registrar logs no nível STATUS."""
    if self.isEnabledFor(STATUS_LEVEL_NUM):
        self._log(STATUS_LEVEL_NUM, message, args, **kws)


logging.Logger.status = status


def log_status(message, *args, **kws):
    """Função global helper no módulo logging para o nível STATUS."""
    logging.log(STATUS_LEVEL_NUM, message, *args, **kws)


logging.status = log_status

# Determina o diretório raiz do projeto para calcular caminhos relativos
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_relative_path(pathname: str) -> str:
    """Retorna o caminho relativo do arquivo de origem a partir da raiz do projeto."""
    try:
        return os.path.relpath(pathname, PROJECT_ROOT)
    except Exception:
        return os.path.basename(pathname)


class ContextFilter(logging.Filter):
    """
    Filtro do logging encarregado de adicionar metadados detalhados de contexto ao LogRecord.
    Desta vez, sem varredura de pilha de frames para máxima performance e compatibilidade com asyncio.
    """
    def filter(self, record: logging.LogRecord) -> bool:
        # Adiciona o caminho relativo do arquivo emissor (operação ultrarrápida de string)
        record.relpath = get_relative_path(record.pathname)
        return True


class ThirdPartyNoiseFilter(logging.Filter):
    """Bloqueia logs volumosos de bibliotecas externas no arquivo central."""
    noisy_prefixes = (
        "ccxt",
        "aiohttp.access",
        "websockets",
        "asyncio",
    )

    def filter(self, record: logging.LogRecord) -> bool:
        return not record.name.startswith(self.noisy_prefixes)


class LogManager:
    """
    Gerenciador do ecossistema de logs da aplicação.
    Configura fila em memória e despacha eventos assincronamente em segundo plano.
    Utiliza o RotatingFileHandler nativo para evitar processamento no boot.
    """
    def __init__(
        self,
        log_file: Optional[str] = None,
        max_bytes: Optional[int] = None,
        backup_count: int = 5,
        console_level: int = logging.INFO,
        file_level: Optional[int] = None
    ):
        self.log_file = log_file or os.getenv("LOG_FILE", "logs/arstrader.log")
        
        env_max_bytes = os.getenv("LOG_MAX_BYTES")
        self.max_bytes = max_bytes or (int(env_max_bytes) if env_max_bytes else 150 * 1024 * 1024)
        
        self.backup_count = backup_count
        self.console_level = console_level
        env_file_level = os.getenv("LOG_FILE_LEVEL", "INFO").upper()
        self.file_level = file_level if file_level is not None else getattr(logging, env_file_level, logging.INFO)
        
        self._queue: Optional[queue.Queue] = None
        self._listener: Optional[logging.handlers.QueueListener] = None
        self._queue_handler: Optional[logging.handlers.QueueHandler] = None
        self._is_running = False

    def start(self) -> None:
        """Inicializa o motor de logs não-bloqueante de forma síncrona e instantânea."""
        if self._is_running:
            return

        # Garante a existência do diretório para evitar erros de I/O
        os.makedirs(os.path.dirname(os.path.abspath(self.log_file)), exist_ok=True)

        # 1. Instancia a fila thread-safe em memória
        self._queue = queue.Queue()

        # 2. Define o padrão de formatação detalhado nativo (ultrarrápido, sem inspeção de frames)
        # Formato: timestamp | LEVEL | arquivo:linha | função | mensagem
        format_str = "%(asctime)s | %(levelname)-8s | %(relpath)s:%(lineno)d | %(funcName)s | %(message)s"
        formatter = logging.Formatter(format_str, datefmt="%Y-%m-%d %H:%M:%S")

        # 3. Handler de arquivo nativo
        file_handler = logging.handlers.RotatingFileHandler(
            filename=self.log_file,
            maxBytes=self.max_bytes,
            backupCount=self.backup_count,
            encoding='utf-8'
        )
        file_handler.setLevel(self.file_level)
        file_handler.setFormatter(formatter)
        if os.getenv("LOG_THIRD_PARTY_DEBUG", "0").lower() not in {"1", "true", "yes"}:
            file_handler.addFilter(ThirdPartyNoiseFilter())

        # 4. Handler de console (Apenas status/visualização, >= INFO)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(self.console_level)
        console_handler.setFormatter(formatter)

        # 5. Inicializa o QueueListener que roda em segundo plano consumindo a fila
        self._listener = logging.handlers.QueueListener(
            self._queue,
            file_handler,
            console_handler,
            respect_handler_level=True
        )
        self._listener.start()

        # 6. Captura o Logger Raiz (Root)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)

        # Limpa eventuais handlers pré-configurados para evitar duplicações
        for h in root_logger.handlers[:]:
            root_logger.removeHandler(h)

        # 7. Associa o QueueHandler ao logger root
        self._queue_handler = logging.handlers.QueueHandler(self._queue)
        
        # Filtro de contexto executa no envio do log para popular os metadados de caminho relativo
        context_filter = ContextFilter()
        self._queue_handler.addFilter(context_filter)
        
        root_logger.addHandler(self._queue_handler)
        self._quiet_noisy_loggers()

        self._is_running = True
        
        # Log inaugural no sistema não-bloqueante
        logging.getLogger("ARSTrader.Logger").info(
            f"[Logger] Inicializado sistema não-bloqueante nativo. Arquivo: {self.log_file} (Máx Bytes: {self.max_bytes}, File Level: {logging.getLevelName(self.file_level)})"
        )

    def _quiet_noisy_loggers(self) -> None:
        """Reduz verbosidade de bibliotecas que despejam payloads HTTP grandes."""
        if os.getenv("LOG_THIRD_PARTY_DEBUG", "0").lower() in {"1", "true", "yes"}:
            return

        for logger_name in (
            "ccxt",
            "ccxt.base.exchange",
            "ccxt.async_support.base.exchange",
            "aiohttp.access",
            "websockets",
            "asyncio",
        ):
            logging.getLogger(logger_name).setLevel(logging.WARNING)

    def shutdown(self) -> None:
        """Desliga o sistema de logs de forma limpa escoando a fila restante."""
        if not self._is_running:
            return

        logging.getLogger("ARSTrader.Logger").info("[Logger] A encerrar o gerenciador de logs... A escoar fila.")
        
        # Remove o handler da fila do logger root para evitar novas postagens
        root_logger = logging.getLogger()
        if self._queue_handler:
            root_logger.removeHandler(self._queue_handler)
            self._queue_handler.close()

        # Para o listener (aguarda o escoamento completo da fila)
        if self._listener:
            self._listener.stop()

        self._is_running = False
