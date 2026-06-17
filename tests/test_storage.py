import asyncio
import time
import pytest
from unittest.mock import AsyncMock, MagicMock
from core.storage import GlobalStorage


def test_storage_basic_properties_triggers_events():
    """Valida se alterar uma propriedade simples no storage dispara os callbacks correspondentes."""
    storage = GlobalStorage()
    
    events = []
    def callback(event_path, value):
        events.append((event_path, value))

    # Subscreve para alterações na carteira
    storage.subscribe("wallet.balance", callback)
    
    # Faz alteração
    storage.wallet.balance = 5000.50
    
    # Verifica disparo
    assert len(events) == 1
    assert events[0] == ("wallet.balance", 5000.50)

    # Nova alteração para o mesmo valor não deve disparar (reduz ruído)
    storage.wallet.balance = 5000.50
    assert len(events) == 1

    # Nova alteração com valor diferente dispara
    storage.wallet.balance = 4500.00
    assert len(events) == 2
    assert events[1] == ("wallet.balance", 4500.00)


def test_storage_wildcard_subscriptions():
    """Valida se inscrições com caracteres coringa (glob) funcionam corretamente."""
    storage = GlobalStorage()
    
    events_wildcard = []
    events_exact = []
    
    storage.subscribe("loader.*.status", lambda p, v: events_wildcard.append((p, v)))
    storage.subscribe("loader.morningstar.status", lambda p, v: events_exact.append((p, v)))
    
    # Registra módulos (gera inicialização com status "OFF" que dispara eventos)
    storage.register_module("morningstar")
    storage.register_module("eveningstar")
    
    # Limpa as coletas iniciais para testar apenas as modificações subsequentes
    events_wildcard.clear()
    events_exact.clear()
    
    storage.loader["morningstar"].status = "ON"
    storage.loader["eveningstar"].status = "STARTING"
    
    # loader.*.status deve ter capturado os dois estados
    assert len(events_wildcard) == 2
    assert ("loader.morningstar.status", "ON") in events_wildcard
    assert ("loader.eveningstar.status", "STARTING") in events_wildcard
    
    # loader.morningstar.status exato deve capturar apenas o do morningstar
    assert len(events_exact) == 1
    assert events_exact[0] == ("loader.morningstar.status", "ON")


def test_storage_unsubscribe():
    """Valida se descadastrar um ouvinte para de notificá-lo."""
    storage = GlobalStorage()
    
    events = []
    cb = lambda p, v: events.append((p, v))
    
    storage.subscribe("config.environment", cb)
    storage.config.environment = "production"
    assert len(events) == 1
    
    # Cancela inscrição
    storage.unsubscribe("config.environment", cb)
    storage.config.environment = "sandbox"
    
    # Não deve ter novos disparos
    assert len(events) == 1


@pytest.mark.asyncio
async def test_storage_async_callback_execution():
    """Valida se callbacks assíncronos (async def) são disparados em segundo plano via create_task."""
    storage = GlobalStorage()
    
    async_events = []
    async def async_cb(event_path, value):
        await asyncio.sleep(0.01)  # Simula pequeno I/O (ex: transmissão WebSocket)
        async_events.append((event_path, value))

    storage.subscribe("comms.latency_ms", async_cb)
    
    # Altera propriedade
    storage.comms.latency_ms = 12.5
    
    # Como o callback executa em background, async_events deve estar vazio inicialmente
    assert len(async_events) == 0
    
    # Cede o laço de eventos para a microtarefa executar
    await asyncio.sleep(0.02)
    
    # Agora deve estar populado
    assert len(async_events) == 1
    assert async_events[0] == ("comms.latency_ms", 12.5)


@pytest.mark.asyncio
async def test_storage_sync_callback_in_executor():
    """Valida se callbacks síncronos ordinários são jogados para o executor de threads se houver loop."""
    storage = GlobalStorage()
    
    events = []
    def slow_sync_cb(event_path, value):
        time.sleep(0.01)  # Simula bloqueio de I/O
        events.append((event_path, value))
        
    storage.subscribe("wallet.balance", slow_sync_cb)
    
    # Altera propriedade
    storage.wallet.balance = 100.0
    
    # O loop principal continua rodando sem travar
    assert len(events) == 0
    
    # Cede controle para permitir a thread rodar e sinalizar o loop
    await asyncio.sleep(0.02)
    
    assert len(events) == 1
    assert events[0] == ("wallet.balance", 100.0)


def test_storage_error_resilience():
    """Garante que se um callback quebrar, não impede a alteração de dados nem afeta outros ouvintes."""
    storage = GlobalStorage()
    
    events_success = []
    def broken_cb(p, v):
        raise ValueError("Simulated handler crash")
        
    def success_cb(p, v):
        events_success.append((p, v))

    storage.subscribe("wallet.simultaneous_trades", broken_cb)
    storage.subscribe("wallet.simultaneous_trades", success_cb)
    
    # Alteração deve ocorrer sem levantar exceção para o chamador
    storage.wallet.simultaneous_trades = 2
    
    # O valor mudou com sucesso
    assert storage.wallet.simultaneous_trades == 2
    
    # O ouvinte saudável recebeu a mensagem com sucesso
    assert len(events_success) == 1
    assert events_success[0] == ("wallet.simultaneous_trades", 2)


def test_storage_list_mutability_notification():
    """Verifica se a reatribuição de listas (mutáveis) aciona corretamente o gatilho de eventos."""
    storage = GlobalStorage()
    
    events = []
    storage.subscribe("wallet.positions", lambda p, v: events.append((p, v)))
    
    # Modificar inplace não aciona (__setattr__ não roda)
    storage.wallet.positions.append("BTC/USDT")
    assert len(events) == 0
    
    # Reatribuir um novo valor diferente aciona corretamente
    storage.wallet.positions = storage.wallet.positions + ["ETH/USDT"]
    assert len(events) == 1
    assert events[0] == ("wallet.positions", ["BTC/USDT", "ETH/USDT"])
