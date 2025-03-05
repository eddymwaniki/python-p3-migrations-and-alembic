"""change date enrolled

Revision ID: 3c80dce1444a
Revises: 058c93f82e9a
Create Date: 2025-03-05 11:07:52.344360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c80dce1444a'
down_revision = '058c93f82e9a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars' ,'date_enrolled',new_column_name = 'date_joined')


def downgrade() -> None:
    op.alter_column('scholars','date_joined',new_column_name = 'date_enrolled')
