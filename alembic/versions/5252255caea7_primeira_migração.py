"""primeira migração

Revision ID: 5252255caea7
Revises: 
Create Date: 2026-06-19 00:10:16.103742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5252255caea7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
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
    op.create_index('idx_ops_symbol_time', 'operations', ['symbol', 'timestamp'], unique=False)
    op.create_index('idx_ops_status', 'operations', ['status'], unique=False)
    op.create_index('idx_ops_strategy', 'operations', ['strategy_name'], unique=False)

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
    op.drop_index('idx_results_time', table_name='trade_results')
    op.drop_index('idx_results_outcome', table_name='trade_results')
    op.drop_table('trade_results')
    op.drop_index('idx_ops_strategy', table_name='operations')
    op.drop_index('idx_ops_status', table_name='operations')
    op.drop_index('idx_ops_symbol_time', table_name='operations')
    op.drop_index('idx_ops_target_guid', table_name='operations')
    op.drop_index('idx_ops_guid', table_name='operations')
    op.drop_table('operations')
