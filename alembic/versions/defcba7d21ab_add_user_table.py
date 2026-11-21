"""add user table

Revision ID: defcba7d21ab
Revises: 589808bc1752
Create Date: 2026-11-21 23:01:08.094991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'defcba7d21ab'
down_revision: Union[str, None] = '589808bc1752'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id",sa.Integer,primary_key=True,nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column("password",sa.String(),nullable=False),
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )



def downgrade():
    op.drop_table("users")
