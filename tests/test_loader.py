import asyncio
import os
import time
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from core.loader import ModuleLoader


_original_sleep = asyncio.sleep


async def mock_sleep(delay):
    """Permite ceder o controle ao laço de eventos sem travar ou introduzir atrasos reais."""
    await _original_sleep(0)


@pytest.mark.asyncio
async def test_module_loader_spawn_and_shutdown():
    """Verifica se o ModuleLoader inicia os processos habilitados e encerra todos via SIGTERM."""
    config_mock = MagicMock()
    config_mock.modules = {
        "morningstar": MagicMock(
            enabled=True,
            path="morningstar",
            class_name="MorningStar"
        ),
        "eveningstar": MagicMock(
            enabled=False,
            path="eveningstar",
            class_name="EveningStar"
        )
    }

    loader = ModuleLoader(config_mock, "127.0.0.1", 8888)

    mock_process = AsyncMock()
    mock_process.pid = 12345
    mock_process.stdout = AsyncMock()
    mock_process.stdout.readline.return_value = b""
    mock_process.stderr = AsyncMock()
    mock_process.stderr.readline.return_value = b""
    mock_process.terminate = MagicMock()
    mock_process.kill = MagicMock()
    mock_process.returncode = None  # Em execução

    with patch("os.path.exists", return_value=True), \
         patch("asyncio.create_subprocess_exec", return_value=mock_process) as mock_exec:
        
        try:
            await loader.start_modules()

            # Deve levantar o morningstar mas ignorar eveningstar (desabilitado)
            mock_exec.assert_called_once()
            assert "morningstar" in loader._processes
            assert loader._processes["morningstar"] == mock_process
            assert "eveningstar" not in loader._processes

            # Garante que as informações foram registradas no storage
            from core import storage
            assert "morningstar" in storage.loader
            assert storage.loader["morningstar"].status == "SPAWNING"
            assert storage.loader["morningstar"].pid == 12345
        finally:
            # Desliga o loader (garante liberação de recursos em caso de falha de asserts)
            await loader.shutdown()

        # Garante que mandou sinal de término para o processo ativo
        mock_process.terminate.assert_called_once()
        mock_process.wait.assert_called_once()

        # Garante que o status no storage foi atualizado para OFF
        from core import storage
        assert storage.loader["morningstar"].status == "OFF"
        assert storage.loader["morningstar"].pid == 0


@pytest.mark.asyncio
async def test_module_loader_watchdog_physical_recovery():
    """Verifica se o watchdog reinicia um processo que encerrou fisicamente no sistema operacional."""
    config_mock = MagicMock()
    config_mock.modules = {
        "morningstar": MagicMock(
            enabled=True,
            path="morningstar",
            class_name="MorningStar"
        )
    }

    loader = ModuleLoader(config_mock, "127.0.0.1", 8888)

    # O primeiro processo retorna código 0 (encerrado)
    proc1 = AsyncMock()
    proc1.pid = 11111
    proc1.stdout = AsyncMock()
    proc1.stdout.readline.return_value = b""
    proc1.stderr = AsyncMock()
    proc1.stderr.readline.return_value = b""
    proc1.terminate = MagicMock()
    proc1.kill = MagicMock()
    proc1.returncode = 0

    # O processo recuperado permanece ativo para evitar loop infinito
    proc2 = AsyncMock()
    proc2.pid = 22222
    proc2.stdout = AsyncMock()
    proc2.stdout.readline.return_value = b""
    proc2.stderr = AsyncMock()
    proc2.stderr.readline.return_value = b""
    proc2.terminate = MagicMock()
    proc2.kill = MagicMock()
    proc2.returncode = None

    spawn_count = 0
    async def mock_spawn(*args, **kwargs):
        nonlocal spawn_count
        spawn_count += 1
        return proc1 if spawn_count == 1 else proc2

    with patch("os.path.exists", return_value=True), \
         patch("asyncio.create_subprocess_exec", side_effect=mock_spawn), \
         patch("asyncio.sleep", side_effect=mock_sleep):
        
        try:
            await loader.start_modules()

            # Permite que o monitor execute um passo e ceda controle para o loop
            await asyncio.sleep(0.02)

            # Deve ter spawnado o primeiro processo e depois a versão recuperada (total 2)
            assert spawn_count == 2
            assert loader._processes["morningstar"] == proc2

            # Garante que as informações foram registradas/atualizadas no storage
            from core import storage
            assert storage.loader["morningstar"].status == "SPAWNING"
            assert storage.loader["morningstar"].pid == 22222
        finally:
            await loader.shutdown()


@pytest.mark.asyncio
async def test_module_loader_watchdog_logical_timeout():
    """Verifica se o watchdog elimina e reinicia uma estratégia travada (sem enviar heartbeats)."""
    config_mock = MagicMock()
    config_mock.modules = {
        "morningstar": MagicMock(
            enabled=True,
            path="morningstar",
            class_name="MorningStar"
        )
    }

    loader = ModuleLoader(config_mock, "127.0.0.1", 8888)
    # Configura um tempo limite de heartbeat extremamente baixo
    loader._heartbeat_timeout = 0.05

    proc1 = AsyncMock()
    proc1.pid = 33333
    proc1.stdout = AsyncMock()
    proc1.stdout.readline.return_value = b""
    proc1.stderr = AsyncMock()
    proc1.stderr.readline.return_value = b""
    proc1.terminate = MagicMock()
    proc1.kill = MagicMock()
    proc1.returncode = None  # Rodando fisicamente sob o OS

    proc2 = AsyncMock()
    proc2.pid = 44444
    proc2.stdout = AsyncMock()
    proc2.stdout.readline.return_value = b""
    proc2.stderr = AsyncMock()
    proc2.stderr.readline.return_value = b""
    proc2.terminate = MagicMock()
    proc2.kill = MagicMock()
    proc2.returncode = None

    spawn_count = 0
    async def mock_spawn(*args, **kwargs):
        nonlocal spawn_count
        spawn_count += 1
        return proc1 if spawn_count == 1 else proc2

    with patch("os.path.exists", return_value=True), \
         patch("asyncio.create_subprocess_exec", side_effect=mock_spawn), \
         patch("asyncio.sleep", side_effect=mock_sleep):
        
        try:
            await loader.start_modules()

            # Envelhece o último heartbeat artificialmente para estourar o limite
            loader._last_heartbeats["morningstar"] = time.time() - 10.0

            # Permite o processamento e cede controle ao monitor
            await asyncio.sleep(0.02)

            # O processo travado (proc1) deve ter sofrido kill
            proc1.kill.assert_called_once()
            proc1.wait.assert_called_once()

            # O processo secundário (proc2) deve ter sido iniciado como recuperação
            assert spawn_count == 2
            assert loader._processes["morningstar"] == proc2

            from core import storage
            assert storage.loader["morningstar"].status == "SPAWNING"
            assert storage.loader["morningstar"].pid == 44444
        finally:
            await loader.shutdown()


@pytest.mark.asyncio
async def test_module_loader_register_heartbeat():
    """Verifica se o registro de pulso atualiza o carimbo de tempo na memória RAM."""
    from core import storage
    storage.register_module("morningstar")

    config_mock = MagicMock()
    loader = ModuleLoader(config_mock, "127.0.0.1", 8888)
    
    agora = time.time()
    await loader.handle_control_signal({
        "type": "CONTROL",
        "action": "HEARTBEAT",
        "strategy_name": "morningstar",
        "pid": 12345,
        "details": ""
    })
    
    assert "morningstar" in loader._last_heartbeats
    assert loader._last_heartbeats["morningstar"] >= agora

    # Valida no storage
    assert storage.loader["morningstar"].last_heartbeat >= agora



def test_module_loader_heartbeat_timeout_config():
    """Verifica se o loader resolve corretamente o heartbeat_timeout a partir do system config, caindo para o padrão 15.0."""
    # Caso 1: Sem config.system -> cai para 15.0
    config_mock_none = MagicMock()
    config_mock_none.system = None
    loader_none = ModuleLoader(config_mock_none, "127.0.0.1", 8888)
    assert loader_none._heartbeat_timeout == 15.0

    # Caso 2: Com config.system com valor válido -> usa o valor do config
    config_mock_val = MagicMock()
    config_mock_val.system = MagicMock()
    config_mock_val.system.heartbeat_timeout = 8
    loader_val = ModuleLoader(config_mock_val, "127.0.0.1", 8888)
    assert loader_val._heartbeat_timeout == 8.0

    # Caso 3: Com config.system com string numérica -> converte para float
    config_mock_str = MagicMock()
    config_mock_str.system = MagicMock()
    config_mock_str.system.heartbeat_timeout = "12"
    loader_str = ModuleLoader(config_mock_str, "127.0.0.1", 8888)
    assert loader_str._heartbeat_timeout == 12.0

    # Caso 4: Com config.system com valor inválido -> cai para 15.0
    config_mock_invalid = MagicMock()
    config_mock_invalid.system = MagicMock()
    config_mock_invalid.system.heartbeat_timeout = "nao_sou_numero"
    loader_invalid = ModuleLoader(config_mock_invalid, "127.0.0.1", 8888)
    assert loader_invalid._heartbeat_timeout == 15.0
