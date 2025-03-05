"""change table name

Revision ID: 058c93f82e9a
Revises: e5fdf372a418
Create Date: 2025-03-05 10:58:32.386786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '058c93f82e9a'
down_revision = 'e5fdf372a418'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('student', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'student')
