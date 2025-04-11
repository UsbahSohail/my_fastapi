"""create post table

Revision ID: 12f94e3a9d30
Revises: 
Create Date: 2025-03-20 00:51:22.034224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12f94e3a9d30'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable=False),
                  #  sa.Column('body', sa.Text(), nullable=False),
                   # sa.Column('owner_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE')),
                    #sa.Column('created_at', sa.DateTime(), server_default=sa.func.now(), nullable=False)
                    )
    pass
    


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table('posts')
    pass
