"""empty message

Revision ID: 7afb5e23e75f
Revises: 4505b08ab709
Create Date: 2020-07-07 16:44:13.252537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7afb5e23e75f'
down_revision = '4505b08ab709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
