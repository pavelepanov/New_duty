"""Data base creation

Revision ID: febbd48869bf
Revises: 
Create Date: 2023-05-10 23:20:43.037588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'febbd48869bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('defectiontype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('defection_type', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('letter', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=50), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('defection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('defection_time', sa.DateTime(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('reason', sa.String(length=300), nullable=False),
    sa.Column('defection_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['defection_type_id'], ['defectiontype.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('defection')
    op.drop_table('student')
    op.drop_table('group')
    op.drop_table('defectiontype')
    # ### end Alembic commands ###