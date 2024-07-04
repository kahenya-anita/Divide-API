"""empty message

Revision ID: 321e432670b8
Revises: 4e476acb2abf
Create Date: 2024-07-04 09:11:14.762989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '321e432670b8'
down_revision = '4e476acb2abf'
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
