"""db created

Revision ID: 4a2fb4d6e441
Revises: fed82238cdea
Create Date: 2023-03-05 20:10:33.730789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a2fb4d6e441'
down_revision = 'fed82238cdea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('emoji', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.Text(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('emoji', sa.String(length=30), nullable=True),
    sa.Column('background', sa.String(length=7), nullable=True),
    sa.Column('days', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_user', sa.Integer(), nullable=True),
    sa.Column('second_user', sa.Integer(), nullable=True),
    sa.Column('streak_days', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['first_user'], ['user.id'], ),
    sa.ForeignKeyConstraint(['second_user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('reciever_id', sa.Integer(), nullable=True),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['reciever_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_daily_mood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('mood', sa.Integer(), nullable=True),
    sa.Column('thankful_for', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_daily_mood')
    op.drop_table('messages')
    op.drop_table('match')
    op.drop_table('goals')
    op.drop_table('questions')
    op.drop_table('interests')
    # ### end Alembic commands ###