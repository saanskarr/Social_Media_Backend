"""add foreign key to post table

Revision ID: 5b870b5ab1f5
Revises: defcba7d21ab
Create Date: 2026-11-21 23:10:37.506044

"""
from pydantic_core.core_schema import nullable_schema
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b870b5ab1f5'
down_revision: Union[str, None] = 'defcba7d21ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("owner_id", sa.Integer(), nullable=False),
    )
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )

def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")