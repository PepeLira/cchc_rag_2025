"""add timestamps to document model

Revision ID: 03616a9c6d1a
Revises: 964ddacf18d3
Create Date: 2024-12-11 17:04:07.078859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03616a9c6d1a'
down_revision = '964ddacf18d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('document', sa.Column('uploaded_at', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_document_updated_at'), 'document', ['updated_at'], unique=False)
    op.create_index(op.f('ix_document_uploaded_at'), 'document', ['uploaded_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_document_uploaded_at'), table_name='document')
    op.drop_index(op.f('ix_document_updated_at'), table_name='document')
    op.drop_column('document', 'uploaded_at')
    op.drop_column('document', 'updated_at')
    # ### end Alembic commands ###
