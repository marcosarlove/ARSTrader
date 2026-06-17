"""
ARSTrader - Async Socket Signal Server (server.py)
==================================================
Servidor local TCP assíncrono encarregado de ouvir os subprocessos (estratégias).
Recebe pacotes JSON unificados contendo HEARTBEATS ou ORDENS e despacha-os
através de Callbacks
"""

import asyncio
import inspect
import logging
import json
from typing import Callable, Coroutine, Any, Optional

# Garante que o nível de log STATUS esteja registrado
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Server")


class SignalServer:
    """
    Servidor de Sockets TCP para Comunicação Inter-Processos (IPC).
    Funciona no modelo Push-Only (as estratégias enviam dados e o Core processa).
    """

    def __init__(
        self,
        host: str,
        port: int,
        on_heartbeat_cb: Callable[[str, int], Any],
        on_order_cb: Callable[[dict], Coroutine[Any, Any, None]],
    ):
        """
        :param host: Endereço IP onde o servidor vai escutar (ex: '127.0.0.1')
        :param port: Porta numérica para o socket TCP (ex: 8888)
        :param on_heartbeat_cb: Função no Loader para registar o pulso (recebe strategy_name, pid)
        :param on_order_cb: Corrotina (função async) no Core para processar a ordem de trading
        """
        self.host = host
        self.port = port

        # Callbacks de Inversão de Controlo
        self.on_heartbeat = on_heartbeat_cb
        self.on_order = on_order_cb

        self._server: Optional[asyncio.Server] = None
        self._is_running = False
        self._active_connections = set()

    async def start(self) -> None:
        """Inicializa o servidor TCP e coloca-o à escuta na rede local."""
        if self._is_running:
            return

        try:
            # Inicia o servidor assíncrono nativo do asyncio
            self._server = await asyncio.start_server(
                self._handle_client, self.host, self.port
            )
            self._is_running = True

            logger.log(
                STATUS_LEVEL_NUM,
                f"[Server] Servidor de Sinais IPC online em {self.host}:{self.port}",
            )

            # Executa o servidor em background sem bloquear quem chamou o start()
            asyncio.create_task(self._server.serve_forever())

        except Exception as e:
            logger.error(
                f"[Server] Falha crítica ao levantar o servidor de sockets: {e}"
            )
            raise e

    async def _handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        """Gerencia a conexão persistente (Keep-Alive) de uma estratégia específica."""
        client_address = writer.get_extra_info("peername")
        logger.debug(f"[Server] Nova conexão estabelecida vinda de {client_address}")

        self._active_connections.add(writer)

        try:
            # Mantém o canal aberto para ler múltiplas mensagens consecutivas pela mesma conexão
            while self._is_running:
                # Lê os dados até encontrar a quebra de linha (padrão de terminação da mensagem)
                data = await reader.readline()

                # Se não houver dados, o cliente desconectou
                if not data:
                    break

                # Decodifica a linha recebida de forma ultrarrápida
                message_str = data.decode("utf-8").strip()
                if not message_str:
                    continue

                # Dispara o processamento da mensagem de forma assíncrona
                asyncio.create_task(self._process_message(message_str))

        except asyncio.CancelledError:
            pass
        except Exception as e:
            logger.debug(
                f"[Server] Exceção na conexão do cliente {client_address}: {e}"
            )
        finally:
            # Fecha o socket de forma limpa quando o subprocesso cai ou desliga
            self._active_connections.discard(writer)
            writer.close()
            try:
                await writer.wait_closed()
            except Exception:
                pass
            logger.debug(f"[Server] Conexão encerrada para {client_address}")

    async def _process_message(self, message_str: str) -> None:
        """Faz o parse do JSON em microssegundos e distribui para o callback correto."""
        try:
            # Parse nativo (leva ~1-3 microssegundos)
            payload = json.loads(message_str)
            msg_type = payload.get("type")
            strategy_name = payload.get("strategy_name")

            if not msg_type or not strategy_name:
                logger.warning(
                    f"[Server] Mensagem inválida rejeitada (Falta type ou strategy_name): {message_str}"
                )
                return

            # Roteamento direto por String
            if msg_type == "HEARTBEAT":
                pid = payload.get("pid", 0)
                # Chama o callback do Loader (síncrono ou disparado imediatamente)
                if inspect.iscoroutinefunction(self.on_heartbeat):
                    await self.on_heartbeat(strategy_name, pid)
                else:
                    self.on_heartbeat(strategy_name, pid)

            elif msg_type == "ORDER":
                logger.log(
                    STATUS_LEVEL_NUM,
                    f"[Server] Sinal de OPERAÇÃO recebido da estratégia '{strategy_name.upper()}'",
                )
                # Dispara o callback assíncrono do Core/Risco para processar e enviar à Exchange
                await self.on_order(payload)

            else:
                logger.warning(f"[Server] Tipo de mensagem desconhecido: '{msg_type}'")

        except json.JSONDecodeError:
            logger.error(
                f"[Server] Falha ao fazer parse de JSON corrompido: {message_str}"
            )
        except Exception as e:
            logger.error(f"[Server] Erro ao processar payload do sinal: {e}")

    async def shutdown(self) -> None:
        """Desliga o servidor de sockets fechando a porta local e conexões ativas."""
        if not self._is_running:
            return

        logger.log(STATUS_LEVEL_NUM, "[Server] A encerrar o servidor de sinais TCP...")
        self._is_running = False

        # Fecha conexões de clientes remanescentes
        for writer in list(self._active_connections):
            writer.close()
            try:
                await writer.wait_closed()
            except Exception:
                pass

        if self._server:
            self._server.close()
            await self._server.wait_closed()

        logger.log(
            STATUS_LEVEL_NUM, "[Server] Servidor de Sinais TCP finalizado com sucesso."
        )
