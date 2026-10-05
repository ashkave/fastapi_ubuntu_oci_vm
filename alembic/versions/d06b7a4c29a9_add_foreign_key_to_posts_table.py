"""add foreign key to posts table

Revision ID: d06b7a4c29a9
Revises: 7faff9b8d4c7
Create Date: 2026-09-30 12:31:28.909626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd06b7a4c29a9'
down_revision: Union[str, Sequence[str], None] = '7faff9b8d4c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts_alembic', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts_alembic", referent_table="users_alembic",
        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts_alembic")
    op.drop_column('posts_alembic', 'owner_id')