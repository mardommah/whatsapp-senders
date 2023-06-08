"""testing migrate 3

Revision ID: 739786056cd3
Revises: 065234d489c6
Create Date: 2023-06-07 22:13:20.661031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '739786056cd3'
down_revision = '065234d489c6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARCHAR(length=50), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_info_id'), 'user_info', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_info_id'), table_name='user_info')
    op.drop_table('user_info')
    # ### end Alembic commands ###