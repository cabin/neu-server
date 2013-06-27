"""Create prospect

Revision ID: 51d5a2c7b782
Revises: None
Create Date: 2013-06-27 13:15:49.815141
"""

# Revision identifiers, used by Alembic.
revision = '51d5a2c7b782'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'prospect',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=256), nullable=False),
        sa.Column('email', sa.Unicode(length=256), nullable=False),
        sa.Column('zipcode', sa.String(length=16), nullable=True),
        sa.Column('note', sa.Text(), nullable=True),
        sa.Column('ip_address', sa.String(length=16), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        mysql_engine='InnoDB',
        mysql_charset='utf8',
    )


def downgrade():
    op.drop_table('prospect')
