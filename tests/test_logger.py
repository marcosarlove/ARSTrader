import os
import sys
import time
import logging
import pytest
from unittest.mock import MagicMock

from core.logger import (
    LogManager, 
    ContextFilter, 
    STATUS_LEVEL_NUM
)

def test_status_level_registration():
    """Valida se o nível STATUS foi registrado corretamente no módulo logging."""
    assert logging.getLevelName(STATUS_LEVEL_NUM) == "STATUS"
    
    logger = logging.getLogger("test_status_reg")
    assert hasattr(logger, "status")
    assert hasattr(logging, "status")


def test_context_filter_injection():
    """Valida se o ContextFilter injeta relpath e funcName corretamente no LogRecord."""
    logger = logging.getLogger("test_ctx_filter")
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    
    records = []
    class MockHandler(logging.Handler):
        def emit(self, record):
            records.append(record)
            
    handler = MockHandler()
    handler.addFilter(ContextFilter())
    logger.addHandler(handler)
    
    logger.info("Mensagem de teste")
    
    assert len(records) == 1
    rec = records[0]
    assert hasattr(rec, "relpath")
    assert rec.funcName == "test_context_filter_injection"
    assert "test_logger.py" in rec.relpath


def test_log_manager_asynchronous_flow(tmp_path):
    """Valida o funcionamento integrado do LogManager de forma não-bloqueante."""
    log_file = tmp_path / "arstrader_manager_test.log"
    
    # Configura console_level alto para não poluir o stdout real dos testes
    manager = LogManager(
        log_file=str(log_file),
        max_bytes=1000,
        console_level=logging.WARNING
    )
    
    # Inicia o gerenciador de logs
    manager.start()
    
    logger = logging.getLogger("ARSTrader.TestManager")
    logger.setLevel(logging.DEBUG)
    
    # Emite logs de diferentes níveis
    logger.debug("Mensagem Debug")
    logger.info("Mensagem Info")
    logger.warning("Mensagem Warning")
    logger.status("Mensagem Status")
    
    # Pequena pausa para garantir que o QueueListener processe a fila
    time.sleep(0.1)
    
    # Encerra o gerenciador (aguarda o escoamento final)
    manager.shutdown()
    
    # Valida se os logs foram gravados fisicamente
    assert os.path.exists(str(log_file))
    with open(str(log_file), 'r', encoding='utf-8') as f:
        content = f.read()
        
    assert "Mensagem Debug" in content
    assert "Mensagem Info" in content
    assert "Mensagem Warning" in content
    assert "Mensagem Status" in content
    assert "test_log_manager_asynchronous_flow" in content
    assert "test_logger.py" in content


def test_rotating_handler_by_bytes(tmp_path):
    """Valida se a rotação por tamanho de bytes nativa funciona corretamente através do LogManager."""
    log_file = tmp_path / "bytes_rotation.log"
    
    # Limite de tamanho muito baixo para forçar a rotação imediatamente
    manager = LogManager(
        log_file=str(log_file),
        max_bytes=100,
        backup_count=2,
        console_level=logging.WARNING
    )
    
    manager.start()
    
    logger = logging.getLogger("ARSTrader.TestBytesRotation")
    logger.setLevel(logging.DEBUG)
    
    # Emite logs longos. Cada log formatado terá aproximadamente 80-90 bytes, forçando rotação.
    logger.warning("Mensagem de log que excede o limite numero um para forcar rotacao")
    logger.warning("Mensagem de log que excede o limite numero dois para forcar rotacao")
    
    # Aguarda o processamento
    time.sleep(0.1)
    
    manager.shutdown()
    
    # Verifica a existência dos arquivos rotacionados
    assert os.path.exists(str(log_file))
    assert os.path.exists(f"{log_file}.1")
