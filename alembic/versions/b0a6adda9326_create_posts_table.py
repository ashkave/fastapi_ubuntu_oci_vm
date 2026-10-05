"""create posts table

Revision ID: b0a6adda9326
Revises: 
Create Date: 2026-09-30 12:02:40.078792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0a6adda9326'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      op.create_table(
        'posts_alembic',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('posts_alembic')

