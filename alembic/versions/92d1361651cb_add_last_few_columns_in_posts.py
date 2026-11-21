"""add last few columns in posts

Revision ID: 92d1361651cb
Revises: 5b870b5ab1f5
Create Date: 2026-11-21 23:17:33.402358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92d1361651cb'
down_revision: Union[str, None] = '5b870b5ab1f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'),)
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('NOW()'),nullable=False))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
