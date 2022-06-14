"""create foreign key

Revision ID: 4103b8b6ea63
Revises: ec6d40534c42
Create Date: 2022-06-14 11:31:24.701048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4103b8b6ea63'
down_revision = 'ec6d40534c42'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")

    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
