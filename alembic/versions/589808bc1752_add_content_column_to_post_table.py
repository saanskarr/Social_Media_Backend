"""add content column to post table

Revision ID: 589808bc1752
Revises: 33d438565740
Create Date: 2026-11-21 22:48:27.929403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '589808bc1752'
down_revision: Union[str, None] = '33d438565740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False),
    )


def downgrade() :
    op.drop_column('posts','content')
    pass
