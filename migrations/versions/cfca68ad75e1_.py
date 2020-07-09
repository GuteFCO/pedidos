"""empty message

Revision ID: cfca68ad75e1
Revises: cd577e2a7b88
Create Date: 2020-07-09 09:03:25.803062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfca68ad75e1'
down_revision = 'cd577e2a7b88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pedido', 'creacion')
    op.drop_column('pedido', 'actualizacion')
    op.add_column('pedido', sa.Column('creacion', sa.DateTime(), nullable=False))
    op.add_column('pedido', sa.Column('actualizacion', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pedido', 'creacion',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=False)
    op.alter_column('pedido', 'actualizacion',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###