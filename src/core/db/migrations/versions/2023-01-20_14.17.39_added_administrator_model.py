"""added administrator model

Revision ID: cf3ecbc0aacc
Revises: a6d858f5a96e
Create Date: 2023-01-20 14:17:39.683984

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cf3ecbc0aacc'
down_revision = 'a6d858f5a96e'
branch_labels = None
depends_on = None


ROLE_ENUM = sa.Enum('administrator', 'psychologist', name='administrator_role')
ROLE_ENUM_POSTGRES = postgresql.ENUM('administrator', 'psychologist', name='administrator_role', create_type=False)
ROLE_ENUM.with_variant(ROLE_ENUM_POSTGRES, 'postgresql')

STATUS_ENUM = sa.Enum('active', 'blocked', name='administrator_status')
STATUS_ENUM_POSTGRES = postgresql.ENUM('active', 'blocked', name='administrator_status', create_type=False)
STATUS_ENUM.with_variant(STATUS_ENUM_POSTGRES, 'postgresql')


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrators',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=70), nullable=False),
    sa.Column('role', ROLE_ENUM, nullable=False),
    sa.Column('last_login_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('status', STATUS_ENUM, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administrators')
    ROLE_ENUM.drop(op.get_bind(), checkfirst=True)
    STATUS_ENUM.drop(op.get_bind(), checkfirst=True)

    # ### end Alembic commands ###