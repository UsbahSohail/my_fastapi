"""empty message

Revision ID: 1c5da46a15cf
Revises: a12fb80febe3
Create Date: 2025-03-20 19:55:34.569851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c5da46a15cf'
down_revision: Union[str, None] = 'a12fb80febe3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
