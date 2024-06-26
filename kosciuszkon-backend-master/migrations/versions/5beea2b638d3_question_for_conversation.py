"""Question for conversation

Revision ID: 5beea2b638d3
Revises: 06bbf4c7712f
Create Date: 2023-03-06 07:09:21.670714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5beea2b638d3'
down_revision = '06bbf4c7712f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_for_conversation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('user_one_id', sa.Integer(), nullable=True),
    sa.Column('user_two_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['user_one_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_two_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_for_conversation')
    # ### end Alembic commands ###
