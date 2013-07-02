"""Add type to prospect

Revision ID: 307ef18c7364
Revises: 51d5a2c7b782
Create Date: 2013-07-01 19:31:38.965346
"""

# Revision identifiers, used by Alembic.
revision = '307ef18c7364'
down_revision = '51d5a2c7b782'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('prospect', sa.Column('type', sa.String(length=16), nullable=True))


def downgrade():
    op.drop_column('prospect', 'type')
