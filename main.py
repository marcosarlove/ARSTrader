"""
ARSTrader - Sovereign Entry Point (main.py)
===========================================
Ponto de entrada principal do robô de trading ARSTrader.
Inicializa o gerenciamento assíncrono de logs, carrega variáveis de ambiente,
valida a conexão com o banco de dados e delega a orquestração de todo o
ecossistema (estratégias, exchange, telemetria) ao GlobalOrchestrator.
"""

import argparse
import asyncio
import logging
import os
import signal
import sys
from dotenv import load_dotenv

from core.logger import LogManager
from core.orchestrator import GlobalOrchestrator


async def main_async(args: argparse.Namespace) -> int:
    """Loop assíncrono principal do motor de trading."""
    logger = logging.getLogger("ARSTrader.Main")
    
    # 1. Instanciamento do Orquestrador Geral
    orchestrator = GlobalOrchestrator(
        config_path=args.config,
        ipc_host=args.host,
        ipc_port=args.port
    )
    
    # 2. Configuração do evento de encerramento do bot
    shutdown_event = asyncio.Event()
    
    def handle_signal():
        logger.warning("Sinal de interrupção (SIGINT/SIGTERM) detectado! Iniciando desligamento gracioso...")
        shutdown_event.set()
        
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, handle_signal)
        except NotImplementedError:
            # Fallback para plataformas ou condições que não suportam add_signal_handler
            pass

    # 3. Inicialização de todo o motor Sovereign
    try:
        await orchestrator.start()
    except Exception as e:
        logger.critical(f"Falha crítica no boot do Sovereign Engine: {e}", exc_info=True)
        try:
            await orchestrator.shutdown()
        except Exception as shutdown_err:
            logger.error(f"Erro ao limpar recursos após falha no boot: {shutdown_err}")
        return 1

    # 4. Mantém o loop ativo até receber o evento de encerramento
    await shutdown_event.wait()

    # 5. Encerramento gracioso de todos os componentes
    logger.info("Desligando subcomponentes do robô...")
    try:
        await orchestrator.shutdown()
    except Exception as e:
        logger.error(f"Erro durante o desligamento do orquestrador: {e}", exc_info=True)
        return 1
        
    logger.info("Todos os componentes foram encerrados com sucesso.")
    return 0


def main():
    """Configura o ambiente inicial e o fluxo de log."""
    # 1. Carrega o arquivo .env se ele existir na pasta raiz
    load_dotenv()
    
    # 2. Configura a análise de argumentos da linha de comandos
    parser = argparse.ArgumentParser(
        description="ARSTrader - Sovereign Engine Trading Bot Entry Point"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="global_config.yaml",
        help="Caminho do ficheiro global_config.yaml (padrão: global_config.yaml)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="IP local onde o servidor IPC de sinais escuta (padrão: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8888,
        help="Porta local onde o servidor IPC de sinais escuta (padrão: 8888)"
    )
    parser.add_argument(
        "--console-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Nível mínimo de verbosidade do console (padrão: INFO)"
    )
    args = parser.parse_args()

    # 3. Validação prévia de existência da URL do Banco de Dados
    if not os.getenv("DATABASE_URL"):
        print("[ERRO CRÍTICO] A variável de ambiente DATABASE_URL não está configurada no seu .env!")
        print("Por favor, crie um arquivo .env na raiz do projeto com o seguinte padrão:")
        print("DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco")
        sys.exit(1)

    # 4. Inicializa o LogManager de forma não-bloqueante
    console_level = getattr(logging, args.console_level.upper(), logging.INFO)
    log_manager = LogManager(console_level=console_level)
    log_manager.start()

    main_logger = logging.getLogger("ARSTrader.Main")
    main_logger.info("LogManager assíncrono inicializado.")
    main_logger.info(f"Ambiente: {os.getenv('DATABASE_URL').split('@')[-1]} (URL mascarada)")

    # 5. Executa a corrotina principal no loop de eventos
    exit_code = 0
    try:
        exit_code = asyncio.run(main_async(args))
    except KeyboardInterrupt:
        main_logger.warning("Interrupção manual (KeyboardInterrupt) detectada fora do fluxo do loop.")
    finally:
        # Garante a descarga da fila de logs na persistência física
        log_manager.shutdown()
        
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
