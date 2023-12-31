"""Initial migration.

Revision ID: ecd96fee43d8
Revises: 
Create Date: 2023-08-02 21:35:28.815062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecd96fee43d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('follow',
    sa.Column('id_follow', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_follower', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_follower'], ['users.id_user'], ),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], ),
    sa.PrimaryKeyConstraint('id_follow')
    )
    op.create_table('posts',
    sa.Column('id_post', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users.id_user'], ),
    sa.PrimaryKeyConstraint('id_post')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('follow')
    op.drop_table('users')
    # ### end Alembic commands ###
