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


async def create_user_cli(username: str, password: str) -> int:
    """Cria ou atualiza um utilizador administrador via CLI com a password hashed via bcrypt."""
    import bcrypt
    from core.database import DatabaseManager
    from core.models import UserModel
    from sqlalchemy import select

    db = DatabaseManager()
    print(f"A criar/atualizar o utilizador '{username}'...")
    try:
        async with db.session_factory() as session:
            async with session.begin():
                stmt = select(UserModel).where(UserModel.username == username)
                result = await session.execute(stmt)
                existing_user = result.scalar_one_or_none()
                
                hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                if existing_user:
                    print(f"Utilizador '{username}' já existe. A atualizar a password...")
                    existing_user.password_hash = hashed_pw
                else:
                    new_user = UserModel(username=username, password_hash=hashed_pw)
                    session.add(new_user)
        await db.engine.dispose()
        print(f"Utilizador '{username}' criado/atualizado com sucesso!")
        return 0
    except Exception as e:
        print(f"Erro ao criar/atualizar utilizador: {e}")
        print("Confirme que as migrations foram aplicadas com: alembic upgrade head")
        await db.engine.dispose()
        return 1


async def delete_user_cli(username: str) -> int:
    """Apaga um utilizador administrador existente via CLI."""
    from core.database import DatabaseManager
    from core.models import UserModel
    from sqlalchemy import select

    db = DatabaseManager()
    print(f"A apagar o utilizador '{username}'...")
    try:
        async with db.session_factory() as session:
            async with session.begin():
                stmt = select(UserModel).where(UserModel.username == username)
                result = await session.execute(stmt)
                existing_user = result.scalar_one_or_none()
                
                if existing_user:
                    await session.delete(existing_user)
                    print(f"Utilizador '{username}' apagado com sucesso!")
                    success = True
                else:
                    print(f"Erro: Utilizador '{username}' não encontrado na base de dados.")
                    success = False
        await db.engine.dispose()
        return 0 if success else 1
    except Exception as e:
        print(f"Erro ao apagar utilizador: {e}")
        await db.engine.dispose()
        return 1


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
    parser.add_argument(
        "--create-user",
        action="store_true",
        help="Criar um novo usuário administrador para o Dashboard e sair."
    )
    parser.add_argument(
        "--username",
        type=str,
        help="Nome de usuário para o novo administrador"
    )
    parser.add_argument(
        "--password",
        type=str,
        help="Senha para o novo administrador"
    )
    parser.add_argument(
        "--delete-user",
        action="store_true",
        help="Apagar um usuário administrador existente do Dashboard e sair."
    )
    args = parser.parse_args()

    # 3. Validação prévia de existência da URL do Banco de Dados
    if not os.getenv("DATABASE_URL"):
        print("[ERRO CRÍTICO] A variável de ambiente DATABASE_URL não está configurada no seu .env!")
        print("Por favor, crie um arquivo .env na raiz do projeto com o seguinte padrão:")
        print("DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco")
        sys.exit(1)

    # 3.1. Execução rápida se a intenção for a criação de usuário administrador
    if args.create_user:
        if not args.username or not args.password:
            print("[ERRO CRÍTICO] Para criar um utilizador, deve fornecer --username e --password.")
            sys.exit(1)
        exit_code = asyncio.run(create_user_cli(args.username, args.password))
        sys.exit(exit_code)

    # 3.2. Execução rápida se a intenção for a exclusão de usuário administrador
    if args.delete_user:
        if not args.username:
            print("[ERRO CRÍTICO] Para apagar um utilizador, deve fornecer --username.")
            sys.exit(1)
        exit_code = asyncio.run(delete_user_cli(args.username))
        sys.exit(exit_code)

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
