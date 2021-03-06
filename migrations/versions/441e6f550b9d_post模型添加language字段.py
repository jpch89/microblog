"""Post模型添加language字段

Revision ID: 441e6f550b9d
Revises: 0f5c218760fc
Create Date: 2018-09-07 07:27:40.316136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '441e6f550b9d'
down_revision = '0f5c218760fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
