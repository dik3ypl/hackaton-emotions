"""remove interests

Revision ID: 06bbf4c7712f
Revises: 73acf1b74bfb
Create Date: 2023-03-06 04:42:32.203440

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '06bbf4c7712f'
down_revision = '73acf1b74bfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('interests')
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('receiver_id', sa.Integer(), nullable=True))
        batch_op.drop_column('reciever_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reciever_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.drop_column('receiver_id')

    op.create_table('interests',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('emoji', mysql.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
