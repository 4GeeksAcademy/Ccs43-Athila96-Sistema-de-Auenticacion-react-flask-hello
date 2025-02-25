"""empty message

Revision ID: 837732e89bf1
Revises: 
Create Date: 2023-09-12 21:47:02.228546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '837732e89bf1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('password_hash', sa.String(length=800), nullable=False),
    sa.Column('salt', sa.String(length=800), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
