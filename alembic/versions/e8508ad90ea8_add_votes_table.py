"""add votes table

Revision ID: e8508ad90ea8
Revises: 33c5df4585fb
Create Date: 2026-10-01 23:59:59.546200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8508ad90ea8'
down_revision: Union[str, Sequence[str], None] = '33c5df4585fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    
    op.create_table('votes_alembic',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts_alembic.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users_alembic.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###

def downgrade():
    
    op.drop_table('votes_alembic')
    # ### end Alembic commands ###