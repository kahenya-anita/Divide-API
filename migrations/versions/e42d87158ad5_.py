"""empty message

Revision ID: e42d87158ad5
Revises: f528e59dcd1a
Create Date: 2024-07-02 20:19:51.135915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e42d87158ad5'
down_revision = 'f528e59dcd1a'
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
