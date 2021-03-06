"""init admin

Revision ID: 46569c0d4d7b
Revises: b3435cda41c5
Create Date: 2017-06-22 13:14:12.981000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46569c0d4d7b'
down_revision = 'b3435cda41c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=120), nullable=True))
    op.add_column('users', sa.Column('nickname', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_unique_constraint(None, 'users', ['nickname'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password')
    op.drop_column('users', 'nickname')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
