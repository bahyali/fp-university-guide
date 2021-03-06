"""Initial migration

Revision ID: 570edac5669c
Revises: 
Create Date: 2021-05-11 15:24:38.776570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '570edac5669c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('university',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('logo', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('locations', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=1000), nullable=True),
    sa.Column('last_name', sa.String(length=1000), nullable=True),
    sa.Column('grade', sa.String(length=1000), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('campus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('university_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('university_id', sa.Integer(), nullable=False),
    sa.Column('method', sa.String(length=100), nullable=False),
    sa.Column('value', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('program',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('university_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('facility',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campus_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['campus_id'], ['campus.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scholarship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['program_id'], ['program.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scholarship')
    op.drop_table('facility')
    op.drop_table('program')
    op.drop_table('contact_info')
    op.drop_table('campus')
    op.drop_table('user')
    op.drop_table('university')
    # ### end Alembic commands ###
