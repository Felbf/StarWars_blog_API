"""empty message

Revision ID: fa5fc4f751ca
Revises: 15791a4b1d49
Create Date: 2021-12-12 22:35:34.548567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa5fc4f751ca'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=False),
    sa.Column('eye_color', sa.String(length=80), nullable=False),
    sa.Column('birth_year', sa.String(length=80), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('skin_color', sa.String(length=80), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=80), nullable=False),
    sa.Column('climate', sa.String(length=80), nullable=False),
    sa.Column('orbital_period', sa.Float(), nullable=False),
    sa.Column('rotation_period', sa.Float(), nullable=False),
    sa.Column('diameter', sa.Float(), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('favorite_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('username', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    op.drop_table('favorite')
    op.drop_table('planet')
    op.drop_table('character')
    # ### end Alembic commands ###
