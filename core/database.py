"""
ARSTrader - Async Database Manager (database.py)
================================================
Responsável por gerenciar a conexão com o PostgreSQL usando SQLAlchemy Assíncrono
e garantir escritas não-bloqueantes através de uma fila (Worker Pattern).
"""

import os
import asyncio
import logging
from typing import Any, Optional, Tuple

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from core.models import Base
from core.logger import STATUS_LEVEL_NUM

logger = logging.getLogger("ARSTrader.Database")

class DatabaseManager:
    """
    Gerenciador de Banco de Dados com persistência desacoplada em fila.
    Garante que nenhuma operação de escrita trave o Event Loop principal de trading.
    """
    def __init__(self):
        # Recupera a URL de conexão do ambiente (Ex do .env: postgresql+asyncpg://user:pass@localhost:5432/arstrader)
        self.db_url = os.getenv("DATABASE_URL")
        if not self.db_url:
            raise ValueError("[DB] A variável DATABASE_URL não foi encontrada no ficheiro .env")

        # Configuração da Engine Assíncrona do SQLAlchemy
        self.engine = create_async_engine(
            self.db_url,
            echo=False,                  # Define como True para debugar SQL gerado (não usar em prod)
            pool_size=5,                 # Mantém conexões prontas no pool
            max_overflow=10,
            pool_timeout=30.0
        )
        
        # Fábrica de sessões assíncronas
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

        # Fila interna para buffering de dados (RAM)
        self._queue: asyncio.Queue[Tuple[str, Any]] = asyncio.Queue()
        self._worker_task: Optional[asyncio.Task] = None
        self._is_running = False

    async def start(self) -> None:
        """Inicializa o banco de dados, cria as tabelas e liga o worker em background."""
        logger.log(STATUS_LEVEL_NUM, "[DB] A inicializar o motor de banco de dados assíncrono...")
        
        # Cria as tabelas se elas não existirem no PostgreSQL
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        
        # Inicia o worker assíncrono em segundo plano
        self._is_running = True
        self._worker_task = asyncio.create_task(self._persistence_worker())
        logger.log(STATUS_LEVEL_NUM, "[DB] Worker de persistência não-bloqueante iniciado com sucesso.")

    async def get_open_operations(self) -> list:
        """
        Busca todas as operações que foram executadas mas ainda não possuem 
        um registro correspondente em trade_results (estão abertas).
        """
        from sqlalchemy import select
        from core.models import OperationModel, TradeResultModel
        
        async with self.session_factory() as session:
            stmt = select(OperationModel).outerjoin(TradeResultModel).where(
                OperationModel.status == "EXECUTED",
                TradeResultModel.id == None
            )
            result = await session.execute(stmt)
            ops = result.scalars().all()
            return [
                {
                    "guid": op.guid,
                    "symbol": op.symbol,
                    "operation": op.operation,
                    "amount": float(op.amount) if op.amount is not None else 0.0,
                    "current_price": float(op.current_price),
                    "stop_loss": float(op.stop_loss) if op.stop_loss is not None else None,
                    "take_profit": float(op.take_profit) if op.take_profit is not None else None,
                }
                for op in ops
            ]

    async def get_daily_loss(self) -> float:
        """
        Busca todos os resultados de trade ocorridos no dia de hoje (UTC)
        e soma os prejuízos realizados.
        """
        from datetime import datetime, time, timezone
        from sqlalchemy import select
        from core.models import TradeResultModel
        
        start_of_today = datetime.combine(datetime.utcnow().date(), time.min).replace(tzinfo=timezone.utc)
        
        async with self.session_factory() as session:
            stmt = select(TradeResultModel).where(
                TradeResultModel.close_timestamp >= start_of_today
            )
            result = await session.execute(stmt)
            trades = result.scalars().all()
            return sum(abs(float(t.realized_pnl)) for t in trades if t.realized_pnl < 0)

    async def get_operation_by_guid(self, guid: str) -> Optional[Any]:
        """Busca um OperationModel na base de dados a partir do seu GUID único."""
        from sqlalchemy import select
        from core.models import OperationModel
        
        async with self.session_factory() as session:
            stmt = select(OperationModel).where(OperationModel.guid == guid)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    def enqueue_save(self, model_instance: Base) -> None:
        """
        Método não-bloqueante principal. 
        Recebe qualquer instância de modelo (OperationModel ou TradeResultModel) 
        e insere imediatamente na fila para salvamento assíncrono.
        """
        try:
            self._queue.put_nowait(("SAVE", model_instance))
        except asyncio.QueueFull:
            # Em último caso, se a fila saturar por pane total no banco, logamos o erro crítico
            logger.error("[DB] Fila de persistência cheia! Risco de perda de dados de auditoria.")

    async def _persistence_worker(self) -> None:
        """Worker que consome a fila em background e executa os commits no Postgres."""
        while self._is_running or not self._queue.empty():
            try:
                # Aguarda até que surja um item na fila de forma eficiente (sem polling)
                action, model_instance = await self._queue.get()
                
                if action == "SAVE":
                    await self._execute_save(model_instance)
                
                # Sinaliza que a tarefa da fila foi processada
                self._queue.task_done()

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"[DB] Erro crítico no loop do worker de persistência: {e}")
                await asyncio.sleep(1) # Proteção contra loops de erro infinitos se o banco cair

    async def _execute_save(self, model_instance: Base) -> None:
        """Abre uma sessão isolada, adiciona o objeto à árvore do ORM e consolida no banco."""
        async with self.session_factory() as session:
            async with session.begin():
                try:
                    session.add(model_instance)
                    # O commit é feito automaticamente ao sair do bloco context manager session.begin()
                except Exception as e:
                    logger.error(f"[DB] Falha ao persistir objeto {model_instance.__class__.__name__} no banco: {e}")
                    # Como a sessão sofre rollback automático no erro do bloco, o sistema continua íntegro

    async def shutdown(self) -> None:
        """Desliga o gerenciador de forma limpa, garantindo o escoamento da fila."""
        logger.log(STATUS_LEVEL_NUM, "[DB] A encerrar o gerenciador de banco de dados... A escoar fila de escrita.")
        self._is_running = False
        
        # Aguarda até 5 segundos para que as escritas pendentes na fila terminem
        timeout = 5.0
        start_time = asyncio.get_running_loop().time()
        while not self._queue.empty():
            if (asyncio.get_running_loop().time() - start_time) > timeout:
                logger.warning(f"[DB] Shutdown timeout atingido. {self._queue.qsize()} registros não foram salvos.")
                break
            await asyncio.sleep(0.1)

        # Cancela a task do worker em background
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass

        # Fecha todas as conexões físicas do Pool do SQLAlchemy
        await self.engine.dispose()
        logger.log(STATUS_LEVEL_NUM, "[DB] Conexões com o banco de dados encerradas.")
