"""Add title and final_message fields

Revision ID: 54c6488c59cc
Revises: 415099a58080
Create Date: 2022-11-13 22:05:13.341858

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '54c6488c59cc'
down_revision = '415099a58080'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shifts', sa.Column('title', sa.String(length=100), nullable=True))
    op.execute("UPDATE shifts SET title = ''")
    op.alter_column('shifts', 'title', nullable=False)
    op.add_column('shifts', sa.Column('final_message', sa.String(length=150), nullable=True))
    op.execute("UPDATE shifts SET final_message = ''")
    op.alter_column('shifts', 'final_message', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('shifts', 'final_message')
    op.drop_column('shifts', 'title')
    # ### end Alembic commands ###