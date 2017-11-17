"""add channel id column

Revision ID: 082165b5a4a3
Revises: cb9769f37d27
Create Date: 2017-11-16 18:17:21.075903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '082165b5a4a3'
down_revision = 'cb9769f37d27'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('booths', sa.Column('channel_id', sa.String(100)))


def downgrade():
    op.drop_column('booths', 'channel_id')
