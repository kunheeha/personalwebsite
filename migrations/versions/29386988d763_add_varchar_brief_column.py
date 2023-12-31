"""add varchar brief column

Revision ID: 29386988d763
Revises: dbcfe9f303ad
Create Date: 2023-06-20 22:20:22.391352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29386988d763'
down_revision = 'dbcfe9f303ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brief', sa.String(), server_default='a plan for world domination', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('brief')

    # ### end Alembic commands ###
