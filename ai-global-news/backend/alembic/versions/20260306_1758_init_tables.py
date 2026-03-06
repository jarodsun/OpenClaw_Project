"""init tables

Revision ID: 20260306_1758
Revises: 
Create Date: 2026-03-06 17:58:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '20260306_1758'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('source_name', sa.String(length=120), nullable=False),
        sa.Column('title', sa.String(length=512), nullable=False),
        sa.Column('url', sa.String(length=1024), nullable=False),
        sa.Column('author', sa.String(length=120), nullable=True),
        sa.Column('language', sa.String(length=16), nullable=True),
        sa.Column('content_raw', sa.Text(), nullable=True),
        sa.Column('published_at', sa.DateTime(), nullable=True),
        sa.Column('ingested_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('url'),
    )
    op.create_index('idx_articles_source_ingested_at', 'articles', ['source_name', 'ingested_at'], unique=False)

    op.create_table(
        'sources',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=120), nullable=False),
        sa.Column('category', sa.String(length=64), nullable=False),
        sa.Column('homepage_url', sa.String(length=512), nullable=False),
        sa.Column('feed_url', sa.String(length=512), nullable=True),
        sa.Column('enabled', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('note', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )


def downgrade() -> None:
    op.drop_table('sources')
    op.drop_index('idx_articles_source_ingested_at', table_name='articles')
    op.drop_table('articles')
