"""add article summary

Revision ID: 20260306_2040
Revises: 20260306_2026
Create Date: 2026-03-06 20:40:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '20260306_2040'
down_revision: Union[str, Sequence[str], None] = '20260306_2026'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('articles', sa.Column('summary', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('articles', 'summary')
