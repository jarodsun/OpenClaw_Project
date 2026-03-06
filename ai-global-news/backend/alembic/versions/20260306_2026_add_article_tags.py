"""add article tags

Revision ID: 20260306_2026
Revises: 20260306_1758
Create Date: 2026-03-06 20:26:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '20260306_2026'
down_revision: Union[str, Sequence[str], None] = '20260306_1758'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('articles', sa.Column('tags', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('articles', 'tags')
