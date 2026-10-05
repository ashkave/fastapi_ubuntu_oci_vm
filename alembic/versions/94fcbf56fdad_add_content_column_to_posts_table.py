"""add content column to posts table

Revision ID: 94fcbf56fdad
Revises: b0a6adda9326
Create Date: 2026-09-30 12:11:43.991683

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94fcbf56fdad'
down_revision: Union[str, Sequence[str], None] = 'b0a6adda9326'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts_alembic', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts_alembic', 'content')
    pass
