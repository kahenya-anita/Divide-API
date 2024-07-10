"""empty message

Revision ID: f5e80235534d
Revises: c0faf5664e25
Create Date: 2024-07-10 17:13:25.658697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5e80235534d'
down_revision = 'c0faf5664e25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divide',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('a', sa.Integer(), nullable=False),
    sa.Column('b', sa.Integer(), nullable=False),
    sa.Column('result', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('divide')
    # ### end Alembic commands ###
