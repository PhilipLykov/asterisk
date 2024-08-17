"""add pjsip tenantid

Revision ID: 655054a68ad5
Revises: 9f3692b1654b
Create Date: 2024-06-11 11:18:41.466929

"""

# revision identifiers, used by Alembic.
revision = '655054a68ad5'
down_revision = '9f3692b1654b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('ps_endpoints', sa.Column('tenantid', sa.String(80)))


def downgrade():
    op.drop_column('ps_endpoints', 'tenantid')
