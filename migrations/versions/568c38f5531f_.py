"""empty message

Revision ID: 568c38f5531f
Revises: 090b489f0256
Create Date: 2020-07-07 18:05:32.186009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '568c38f5531f'
down_revision = '090b489f0256'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.String(length=20), nullable=False),
    sa.Column('isCorrect', sa.Boolean(), nullable=True),
    sa.Column('questions', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['questions'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('user')
    op.drop_table('question')
    # ### end Alembic commands ###
