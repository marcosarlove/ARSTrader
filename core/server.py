"""
ARSTrader - Async Socket Signal Server (server.py)
==================================================
Servidor local TCP assíncrono encarregado de ouvir os subprocessos (estratégias).
Recebe pacotes JSON unificados contendo HEARTBEATS ou ORDENS e despacha-os
através de Callbacks usando Promises (Futures) para respostas não-bloqueantes.
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
    Funciona no modelo Bidirecional Assíncrono via Padrão de Promessas.
    """

    def __init__(
        self,
        host: str,
        port: int,
        on_control_cb: Callable[[dict], Any],
        on_order_cb: Callable[[str, asyncio.Future], Coroutine[Any, Any, None]],
        on_rejected_order_cb: Optional[Callable[[dict, str], Coroutine[Any, Any, None]]] = None,
        max_latency_seconds: float = 2.0
    ):
        """
        :param host: Endereço IP onde o servidor vai escutar (ex: '127.0.0.1')
        :param port: Porta numérica para o socket TCP (ex: 8888)
        :param on_control_cb: Função no Orchestrator para gerenciar sinais de controle (recebe payload dict)
        :param on_order_cb: Corrotina no Orchestrator que recebe a string bruta do sinal e a Promessa
        :param on_rejected_order_cb: Callback no Orchestrator para persistir ordens rejeitadas de antemão
        """
        self.host = host
        self.port = port

        # Callbacks de Inversão de Controlo
        self.on_control = on_control_cb
        self.on_order = on_order_cb
        self.on_rejected_order = on_rejected_order_cb

        # Controlador de tráfego para validação de schema e latência
        from core.comms import TrafficController
        self.traffic_controller = TrafficController(max_latency_seconds=max_latency_seconds)

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

                # Pega o loop atual para gerar a promessa (Future) de resposta
                loop = asyncio.get_running_loop()
                promise = loop.create_future()

                # Dispara o roteamento e processamento do pacote passando a promessa junto
                # Rodamos como Task para permitir que múltiplos pacotes concorrentes usem o mesmo pipe se necessário
                asyncio.create_task(
                    self._route_and_await_signal(message_str, promise, writer)
                )

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

    async def _route_and_await_signal(
        self, message_str: str, promise: asyncio.Future, writer: asyncio.StreamWriter
    ) -> None:
        """
        Roteia o sinal para o destino correto. Se for uma ORDER, suspende a execução
        da tarefa até que o Orchestrator cumpra a promessa, enviando o resultado de volta.
        """
        try:
            # Tratamento de sinais do tipo CONTROL
            if (
                '"type": "CONTROL"' in message_str
                or '"type":"CONTROL"' in message_str
            ):
                success, payload, verdict = self.traffic_controller.process_control_packet(message_str)
                if not success:
                    logger.error(f"[Server] Sinal de controle rejeitado pelo comms: {verdict}")
                    return

                if inspect.iscoroutinefunction(self.on_control):
                    await self.on_control(payload)
                else:
                    self.on_control(payload)
                return

            # Se for uma ordem de trading, aciona o fluxo principal do Core via Orchestrator
            if '"type": "ORDER"' in message_str or '"type":"ORDER"' in message_str:
                # Executa a validação de schema e latência do TrafficController de antemão
                success, payload, verdict = self.traffic_controller.process_incoming_packet(message_str)
                
                if not success:
                    # Envia a resposta final de erro pelo socket da estratégia com terminação newline
                    response_payload = {"status": "IGNORED", "reason": verdict}
                    writer.write(json.dumps(response_payload).encode("utf-8") + b"\n")
                    await writer.drain()
                    
                    # Resolve a promessa interna para limpeza
                    promise.set_result(response_payload)
                    
                    # Notifica o callback de auditoria de rejeições se cadastrado
                    if self.on_rejected_order:
                        try:
                            if inspect.iscoroutinefunction(self.on_rejected_order):
                                await self.on_rejected_order(payload or {}, verdict)
                            else:
                                self.on_rejected_order(payload or {}, verdict)
                        except Exception as audit_err:
                            logger.error(f"[Server] Erro ao disparar auditoria de rejeição: {audit_err}")
                    return

                # Chama o Orchestrator passando a string bruta e o objeto da promessa vacante
                await self.on_order(message_str, promise)

                # A Mágica do Desacoplamento: O Server suspende aqui até a promessa ser resolvida
                response_payload = await promise

                # Envia a resposta final de volta pelo socket da estratégia com terminação newline
                writer.write(json.dumps(response_payload).encode("utf-8") + b"\n")
                await writer.drain()
            else:
                logger.warning(
                    f"[Server] Mensagem com tipo de payload desconhecido ou malformado."
                )

        except json.JSONDecodeError:
            logger.error(
                f"[Server] Falha ao fazer parse de JSON corrompido no pre-routing."
            )
        except Exception as e:
            logger.error(
                f"[Server] Erro crítico no ciclo de vida da Promise do sinal: {e}"
            )

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
