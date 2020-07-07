"""empty message

Revision ID: 090b489f0256
Revises: 552b12fe3ebc
Create Date: 2020-07-07 16:50:24.684236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '090b489f0256'
down_revision = '552b12fe3ebc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('question')
    op.drop_table('answer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('answer', sa.VARCHAR(length=20), nullable=False),
    sa.Column('isCorrect', sa.BOOLEAN(), nullable=True),
    sa.Column('questions', sa.INTEGER(), nullable=False),
    sa.CheckConstraint('"isCorrect" IN (0, 1)'),
    sa.ForeignKeyConstraint(['questions'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=30), nullable=True),
    sa.Column('email', sa.VARCHAR(length=40), nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
