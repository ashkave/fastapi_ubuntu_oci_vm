"""adding additional columns to posts_alembic table

Revision ID: 33c5df4585fb
Revises: d06b7a4c29a9
Create Date: 2026-09-30 12:36:00.851218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33c5df4585fb'
down_revision: Union[str, Sequence[str], None] = 'd06b7a4c29a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts_alembic', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE')
    )
    op.add_column('posts_alembic', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()'))
    )

def downgrade():
    op.drop_column('posts_alembic', 'published')
    op.drop_column('posts_alembic', 'created_at')
