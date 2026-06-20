"""add_exchange_order_id

Revision ID: 9b7c2e4f1a6b
Revises: 60c4776d2005
Create Date: 2026-06-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9b7c2e4f1a6b'
down_revision: Union[str, Sequence[str], None] = '60c4776d2005'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    table_names = inspector.get_table_names()

    if 'operations' not in table_names:
        op.create_table(
            'operations',
            sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
            sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
            sa.Column('guid', sa.String(length=64), nullable=False),
            sa.Column('target_guid', sa.String(length=64), nullable=True),
            sa.Column('symbol', sa.String(length=20), nullable=False),
            sa.Column('operation', sa.String(length=10), nullable=False),
            sa.Column('market', sa.String(length=20), nullable=False),
            sa.Column('exchange', sa.String(length=30), nullable=False),
            sa.Column('strategy_name', sa.String(length=50), nullable=False),
            sa.Column('current_price', sa.Numeric(precision=24, scale=12), nullable=False),
            sa.Column('amount', sa.Numeric(precision=24, scale=12), nullable=True),
            sa.Column('exchange_order_id', sa.String(length=128), nullable=True),
            sa.Column('stop_loss', sa.Numeric(precision=24, scale=12), nullable=True),
            sa.Column('take_profit', sa.Numeric(precision=24, scale=12), nullable=True),
            sa.Column('wallet_balance_before', sa.Numeric(precision=24, scale=12), nullable=True),
            sa.Column('status', sa.String(length=20), nullable=False),
            sa.Column('reason', sa.Text(), nullable=True),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('guid')
        )
        op.create_index('idx_ops_guid', 'operations', ['guid'], unique=False)
        op.create_index('idx_ops_target_guid', 'operations', ['target_guid'], unique=False)
        op.create_index('idx_ops_exchange_order_id', 'operations', ['exchange_order_id'], unique=False)
        op.create_index('idx_ops_symbol_time', 'operations', ['symbol', 'timestamp'], unique=False)
        op.create_index('idx_ops_status', 'operations', ['status'], unique=False)
        op.create_index('idx_ops_strategy', 'operations', ['strategy_name'], unique=False)
    else:
        columns = {col['name'] for col in inspector.get_columns('operations')}
        indexes = {idx['name'] for idx in inspector.get_indexes('operations')}
        if 'exchange_order_id' not in columns:
            op.add_column('operations', sa.Column('exchange_order_id', sa.String(length=128), nullable=True))
        if 'idx_ops_exchange_order_id' not in indexes:
            op.create_index('idx_ops_exchange_order_id', 'operations', ['exchange_order_id'], unique=False)

    if 'trade_results' not in table_names:
        op.create_table(
            'trade_results',
            sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
            sa.Column('operation_id', sa.Integer(), nullable=False),
            sa.Column('close_timestamp', sa.DateTime(timezone=True), nullable=False),
            sa.Column('close_price', sa.Numeric(precision=24, scale=12), nullable=False),
            sa.Column('realized_pnl', sa.Numeric(precision=24, scale=12), nullable=False),
            sa.Column('pnl_percentage', sa.Numeric(precision=6, scale=2), nullable=False),
            sa.Column('outcome', sa.String(length=10), nullable=False),
            sa.ForeignKeyConstraint(['operation_id'], ['operations.id'], ondelete='CASCADE'),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('operation_id')
        )
        op.create_index('idx_results_outcome', 'trade_results', ['outcome'], unique=False)
        op.create_index('idx_results_time', 'trade_results', ['close_timestamp'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if 'operations' not in inspector.get_table_names():
        return

    indexes = {idx['name'] for idx in inspector.get_indexes('operations')}
    columns = {col['name'] for col in inspector.get_columns('operations')}
    if 'idx_ops_exchange_order_id' in indexes:
        op.drop_index('idx_ops_exchange_order_id', table_name='operations')
    if 'exchange_order_id' in columns:
        op.drop_column('operations', 'exchange_order_id')
