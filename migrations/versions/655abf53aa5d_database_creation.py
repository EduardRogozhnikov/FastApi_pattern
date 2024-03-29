"""Database creation

Revision ID: 655abf53aa5d
Revises: 
Create Date: 2024-02-02 13:18:34.140112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '655abf53aa5d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('permission', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.Column('username', sa.String(length=255), nullable=False),
                    sa.Column('password', sa.String(length=255), nullable=False),
                    sa.Column('registrated_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
