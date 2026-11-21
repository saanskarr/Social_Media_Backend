"""create post table

Revision ID: 33d438565740
Revises: 
Create Date: 2026-11-21 22:40:01.941826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33d438565740'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer,primary_key=True,nullable=False),sa.Column('title',sa.String(),nullable=False),)

    pass


def downgrade():
    op.drop_table('posts')
    pass
