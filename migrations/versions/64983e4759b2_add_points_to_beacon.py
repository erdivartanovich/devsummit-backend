"""add points to beacon

Revision ID: 64983e4759b2
Revises: 082165b5a4a3
Create Date: 2017-11-17 17:21:21.659160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64983e4759b2'
down_revision = '082165b5a4a3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('beacons', sa.Column('point', sa.Integer))


def downgrade():
    op.drop_column('beacons', 'point')
