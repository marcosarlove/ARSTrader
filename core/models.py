"""
ARSTrader - Database Models (models.py)
=======================================
Mapeamento via SQLAlchemy focado em auditoria de decisões.
Registra todas as intenções de trade (executadas ou ignoradas) e o retorno financeiro final.
"""

from datetime import datetime
from typing import Optional
from decimal import Decimal
from sqlalchemy import String, Integer, Numeric, DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class OperationModel(Base):
    """
    Tabela Principal de Operações.
    Regista absolutamente tudo o que o bot pensou em fazer.
    Serve para auditar por que razão uma estratégia operou ou foi ignorada.
    """

    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )

    # Rastreabilidade Estrita via UUID/GUID
    guid: Mapped[str] = mapped_column(
        String(64), unique=True, nullable=False
    )  # GUID único gerado pela estratégia
    target_guid: Mapped[Optional[str]] = mapped_column(
        String(64), nullable=True
    )  # Aponta para o GUID de abertura caso seja um fecho dinâmico

    # Identificação do Ativo e Contexto
    symbol: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # ex: BTC/USDT, SOL/USDT
    operation: Mapped[str] = mapped_column(String(10), nullable=False)  # BUY, SELL
    market: Mapped[str] = mapped_column(String(20), nullable=False)  # SPOT, FUTURES
    exchange: Mapped[str] = mapped_column(String(30), nullable=False)  # binance, kucoin
    strategy_name: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # Módulo/Estratégia que gerou o sinal

    # Parâmetros de Preço e Alvos
    current_price: Mapped[Decimal] = mapped_column(Numeric(24, 12), nullable=False)
    amount: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(24, 12), nullable=True
    )  # NULL se rejeitado antes do Sizing no Wallet
    stop_loss: Mapped[Optional[Decimal]] = mapped_column(Numeric(24, 12), nullable=True)
    take_profit: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(24, 12), nullable=True
    )

    # Auditoria de Bancas/Saldos
    wallet_balance_before: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(24, 12), nullable=True
    )  # NULL se rejeitado antes do Wallet

    # Estado da Decisão
    status: Mapped[str] = mapped_column(
        String(20), nullable=False
    )  # EXECUTED, IGNORED, FAILED
    reason: Mapped[Optional[str]] = mapped_column(
        Text, nullable=True
    )  # ex: "SIGNAL_OBSOLETE", "ASSET_LOCK_ACTIVE", "Sucesso"

    # Relacionamento: Se foi executada, pode gerar um resultado de trade mais tarde
    result: Mapped[Optional["TradeResultModel"]] = relationship(
        back_populates="operation", cascade="all, delete-orphan"
    )

    __table_args__ = (
        Index("idx_ops_guid", "guid"),
        Index("idx_ops_target_guid", "target_guid"),
        Index("idx_ops_symbol_time", "symbol", "timestamp"),
        Index("idx_ops_status", "status"),
        Index("idx_ops_strategy", "strategy_name"),
    )


class TradeResultModel(Base):
    """
    Tabela de Resultados dos Trades.
    Armazena o desfecho financeiro exclusivo das operações que foram de facto EXECUTADAS.
    """

    __tablename__ = "trade_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Chave estrangeira ligando diretamente à operação de origem
    operation_id: Mapped[int] = mapped_column(
        ForeignKey("operations.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    operation: Mapped["OperationModel"] = relationship(back_populates="result")

    # Fechamento do Trade
    close_timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
    close_price: Mapped[Decimal] = mapped_column(Numeric(24, 12), nullable=False)

    # Métricas de Desempenho (Ganhos e Perdas)
    realized_pnl: Mapped[Decimal] = mapped_column(
        Numeric(24, 12), nullable=False
    )  # Valor nominal ganho/perdido (ex: +50.25 ou -12.10)
    pnl_percentage: Mapped[Decimal] = mapped_column(
        Numeric(6, 2), nullable=False
    )  # Lucro/Prejuízo em % (ex: 2.50 ou -1.20)
    outcome: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # WIN, LOSS, BREAKEVEN

    __table_args__ = (
        Index("idx_results_outcome", "outcome"),
        Index("idx_results_time", "close_timestamp"),
    )


class UserModel(Base):
    """
    Tabela de Usuários para autenticação no Dashboard.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        Index("idx_users_username", "username"),
    )

