"""add is_up_to_date to Document

Revision ID: d2381b16c65a
Revises: 03616a9c6d1a
Create Date: 2024-12-12 20:07:50.990991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2381b16c65a'
down_revision = '03616a9c6d1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('is_up_to_date', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('document', 'is_up_to_date')
    # ### end Alembic commands ###
