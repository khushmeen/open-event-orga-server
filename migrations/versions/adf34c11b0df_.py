"""empty message

Revision ID: adf34c11b0df
Revises: 47e818661817
Create Date: 2016-06-19 15:12:13.886000

"""

# revision identifiers, used by Alembic.
revision = 'adf34c11b0df'
down_revision = '47e818661817'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('schedule_published_on', sa.DateTime()))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'schedule_published_on')
    ### end Alembic commands ###
