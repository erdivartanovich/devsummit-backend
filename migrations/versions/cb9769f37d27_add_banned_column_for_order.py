"""add-banned-column-for-order

Revision ID: cb9769f37d27
Revises: 3888358e1e87
Create Date: 2017-11-15 12:41:37.664913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb9769f37d27'
down_revision = '3888358e1e87'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('banned', sa.Boolean(), server_default=sa.schema.DefaultClause("0")))


def downgrade():
    op.drop_column('orders', 'banned')
