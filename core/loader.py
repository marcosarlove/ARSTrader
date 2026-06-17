"""
ARSTrader - Process Loader & Watchdog (loader.py)
==================================================
O Gestor de Ciclo de Vida dos Súditos.
Responsável pelo isolamento físico, inicialização e monitoramento contínuo dos processos filhos (Módulos).

Regras Operacionais:
1. Lê as diretivas de 'config.py' e instancia dinamicamente cada estratégia habilitada em seu próprio processo.
2. Mantém o registro centralizado de PIDs (Process IDs) e filas de controle.
3. Executa o Watchdog ativo: se o batimento cardíaco (heartbeat) de um módulo falhar ou expirar o tempo limite,
   este componente elimina o processo zumbi e o reinicia do zero imediatamente.
"""

import asyncio
import logging
import sys
import os
import time
from typing import Dict, Optional
from core.config import ConfigManager
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Loader")


class ModuleLoader:
    """
    Gerenciador de subprocessos para as estratégias do ARSTrader.
    Garante o isolamento de falhas: se uma estratégia morrer, o Core continua vivo.
    """

    def __init__(
        self, config_manager: ConfigManager, server_host: str, server_port: int
    ):
        """
        :param config_manager: Instância já carregada do gerenciador de configurações.
        :param server_host: IP do SignalServer para as estratégias se conectarem.
        :param server_port: Porta do SignalServer para as estratégias se conectarem.
        """
        self.config = config_manager
        self.server_host = server_host
        self.server_port = server_port

        # Armazena as referências dos subprocessos ativos {nome_do_modulo: Process}
        self._processes: Dict[str, asyncio.subprocess.Process] = {}

        # Registra o timestamp do último heartbeat recebido {nome_do_modulo: timestamp}
        self._last_heartbeats: Dict[str, float] = {}

        self._monitor_task: Optional[asyncio.Task] = None
        self._is_running = False

        # Tempo máximo permitido sem receber batimento cardíaco da estratégia (15 segundos padrão ou do config)
        self._heartbeat_timeout = 15.0
        if self.config:
            system_cfg = getattr(self.config, "system", None)
            if system_cfg:
                timeout_val = getattr(system_cfg, "heartbeat_timeout", None)
                if isinstance(timeout_val, (int, float)):
                    self._heartbeat_timeout = float(timeout_val)
                elif isinstance(timeout_val, str):
                    try:
                        self._heartbeat_timeout = float(timeout_val)
                    except ValueError:
                        pass

    async def start_modules(self) -> None:
        """Varre as configurações e inicia todos os módulos habilitados como subprocessos."""
        self._is_running = True
        modules_to_load = self.config.modules

        if not modules_to_load:
            logger.warning("[Loader] Nenhum módulo encontrado nas configurações.")
            return

        for mod_name, mod_config in modules_to_load.items():
            # Ignora o dashboard neste gerenciador (pois roda como serviço separado) ou se desativado
            if not mod_config.enabled:
                logger.info(f"[Loader] Módulo '{mod_name}' desativado).")
                continue

            # Registra o módulo no storage de telemetria
            from core import storage

            storage.register_module(mod_name)
            storage.loader[mod_name].status = "STARTING"

            await self._spawn_process(mod_name, mod_config.path, mod_config.class_name)

        # Inicia a tarefa em background que monitora a saúde física e os batimentos dos processos
        self._monitor_task = asyncio.create_task(self._monitor_processes())

    def register_heartbeat(self, strategy_name: str, pid: int) -> None:
        """
        MÉTODO CALLBACK: Invocado pelo SignalServer sempre que um pulso TCP chega.
        Atualiza o carimbo de tempo da RAM instantaneamente.
        """
        agora = time.time()
        self._last_heartbeats[strategy_name] = agora
        logger.debug(
            f"[Loader] Heartbeat recebido de '{strategy_name}' (PID registrado no sinal: {pid})"
        )

        # Sincroniza no storage de telemetria
        from core import storage

        if strategy_name in storage.loader:
            storage.loader[strategy_name].last_heartbeat = agora

    async def _spawn_process(self, name: str, path: str, class_name: str) -> None:
        """Gera um subprocesso do Linux injetando o IP e Porta do servidor central."""
        # Monta o caminho relativo da estratégia (ex: modules/morningstar/runner.py)
        runner_path = os.path.join("modules", path, "runner.py")

        if not os.path.exists(runner_path):
            logger.error(
                f"[Loader] Ficheiro de execução não encontrado para '{name}' em: {runner_path}"
            )
            return

        try:
            logger.info(
                f"[Loader] A iniciar subprocesso para a estratégia: {name.upper()}..."
            )

            # Executa o subprocesso passando os argumentos que a estratégia precisa para se sincronizar
            proc = await asyncio.create_subprocess_exec(
                sys.executable,  # Garante o uso do mesmo interpretador do ambiente virtual (venv)
                runner_path,
                "--name",
                name,
                "--class",
                class_name,
                "--core-host",
                self.server_host,
                "--core-port",
                str(self.server_port),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            self._processes[name] = proc
            # Inicializa o cronômetro de vida com o tempo atual para não ser morta no primeiro ciclo
            agora = time.time()
            self._last_heartbeats[name] = agora

            logger.log(
                STATUS_LEVEL_NUM,
                f"[Loader] Módulo '{name}' iniciado com sucesso. PID: {proc.pid}",
            )

            # Sincroniza no storage de telemetria
            from core import storage

            if name in storage.loader:
                storage.loader[name].pid = proc.pid
                storage.loader[name].started_at = agora
                storage.loader[name].status = "ON"

            # Dispara tarefas assíncronas para canalizar o stdout/stderr do processo para o logger do Core
            asyncio.create_task(self._read_stream(name, proc.stdout, "INFO"))
            asyncio.create_task(self._read_stream(name, proc.stderr, "ERROR"))

        except Exception as e:
            logger.error(
                f"[Loader] Falha crítica ao levantar o processo do módulo '{name}': {e}"
            )

    async def _read_stream(
        self, module_name: str, stream: Optional[asyncio.StreamReader], level: str
    ) -> None:
        """Lê os fluxos de texto de saída da estratégia e redireciona para o logger central."""
        if not stream:
            return

        while self._is_running:
            line = await stream.readline()
            if not line:
                break

            decoded_line = line.decode("utf-8").strip()
            if decoded_line:
                if level == "ERROR":
                    logger.error(f"[{module_name.upper()}] {decoded_line}")
                else:
                    logger.info(f"[{module_name.upper()}] {decoded_line}")

    async def _monitor_processes(self) -> None:
        """Monitor contínuo em background. Valida o encerramento do Linux e o estouro de Heartbeats."""
        logger.log(
            STATUS_LEVEL_NUM, "[Loader] Monitor de subprocessos e Heartbeats ativado."
        )

        while self._is_running:
            try:
                agora = time.time()

                for name, proc in list(self._processes.items()):
                    # 1. Verificação Física (O processo morreu no Linux?)
                    return_code = proc.returncode

                    if return_code is not None:
                        logger.error(
                            f"[Loader] Módulo '{name.upper()}' encerrou fisicamente com código: {return_code}"
                        )
                        from core import storage

                        if name in storage.loader:
                            storage.loader[name].status = "OFF"
                            storage.loader[name].pid = 0
                        await self._recover_module(name)
                        continue

                    # 2. Verificação Lógica (A estratégia travou em loop e parou de mandar heartbeats?)
                    ultimo_pulso = self._last_heartbeats.get(name, agora)
                    if (agora - ultimo_pulso) > self._heartbeat_timeout:
                        logger.error(
                            f"[Loader] Módulo '{name.upper()}' congelou! Sem heartbeats há {agora - ultimo_pulso:.1f}s."
                        )
                        from core import storage

                        if name in storage.loader:
                            storage.loader[name].status = "RECOVERING"

                        # Força a derrubada imediata para limpar o processo fantasma
                        try:
                            logger.warning(
                                f"[Loader] Forçando SIGKILL no processo travado de '{name.upper()}' (PID: {proc.pid})"
                            )
                            proc.kill()
                            await (
                                proc.wait()
                            )  # Limpa os resíduos da tabela de processos do Linux
                        except Exception:
                            pass

                        await self._recover_module(name)

                await asyncio.sleep(
                    3.0
                )  # Varre a cada 3 segundos para balancear uso de CPU

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"[Loader] Erro no loop do monitor de processos: {e}")
                await asyncio.sleep(5)

    async def _recover_module(self, name: str) -> None:
        """Remove o rastro do processo antigo e inicia uma nova instância limpa."""
        self._processes.pop(name, None)
        self._last_heartbeats.pop(name, None)

        if self._is_running:
            logger.log(
                STATUS_LEVEL_NUM,
                f"[Loader] Tentando reiniciar a estratégia '{name}' automaticamente...",
            )
            from core import storage

            if name in storage.loader:
                storage.loader[name].status = "RECOVERING"

            mod_config = self.config.modules[name]
            await self._spawn_process(name, mod_config.path, mod_config.class_name)

    async def shutdown(self) -> None:
        """Para o monitoramento e encerra todos os subprocessos de forma coordenada."""
        logger.log(
            STATUS_LEVEL_NUM,
            "[Loader] A encerrar o gerenciador de módulos... A desligar subprocessos.",
        )
        self._is_running = False

        if self._monitor_task:
            self._monitor_task.cancel()

        # Envia sinal de término limpo (SIGTERM) para os filhos ativos
        for name, proc in self._processes.items():
            try:
                logger.info(
                    f"[Loader] Enviando SIGTERM para: {name.upper()} (PID: {proc.pid})"
                )
                from core import storage

                if name in storage.loader:
                    storage.loader[name].status = "OFF"
                    storage.loader[name].pid = 0
                proc.terminate()
                # Dá até 2 segundos para o encerramento gracioso das conexões locais
                await asyncio.wait_for(proc.wait(), timeout=2.0)
            except asyncio.TimeoutError:
                logger.warning(
                    f"[Loader] Módulo '{name}' não respondeu. Aplicando SIGKILL..."
                )
                try:
                    proc.kill()
                    await proc.wait()
                except Exception:
                    pass
            except Exception as e:
                logger.error(f"[Loader] Erro ao encerrar módulo '{name}': {e}")

        self._processes.clear()
        self._last_heartbeats.clear()
        logger.log(
            STATUS_LEVEL_NUM,
            "[Loader] Todos os subprocessos de estratégias foram finalizados.",
        )
