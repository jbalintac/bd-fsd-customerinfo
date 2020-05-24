"""initial database migration

Revision ID: 5f62b64a1ded
Revises: 
Create Date: 2020-05-24 20:03:56.164393

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5f62b64a1ded'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('contact', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('prospective', 'current', 'nonActive', name='status'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('note',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('customer_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('note')
    op.drop_table('customer')
    # ### end Alembic commands ###
