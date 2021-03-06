"""empty message

Revision ID: de41bffc4830
Revises: c61a3c33adb5
Create Date: 2017-06-20 11:04:16.344382

"""

# revision identifiers, used by Alembic.
revision = 'de41bffc4830'
down_revision = 'c61a3c33adb5'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event_invoices', sa.Column('invoice_pdf_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event_invoices', 'invoice_pdf_url')
    # ### end Alembic commands ###
