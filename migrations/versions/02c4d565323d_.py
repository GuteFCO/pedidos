"""empty message

Revision ID: 02c4d565323d
Revises: 37a79d6d0c63
Create Date: 2020-07-09 09:27:34.895415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02c4d565323d'
down_revision = '37a79d6d0c63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pedido', sa.Column('usuario_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pedido', 'usuario_id')
    # ### end Alembic commands ###
