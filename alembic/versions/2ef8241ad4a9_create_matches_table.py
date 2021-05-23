"""create matches table

Revision ID: 2ef8241ad4a9
Revises: 
Create Date: 2021-05-23 19:15:41.853333

"""

from alembic import op
import sqlalchemy as sa
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

# revision identifiers, used by Alembic.
revision = '2ef8241ad4a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    file_path = os.path.join(this_dir, "upgrade", "create_match_table.sql")

    with open(file_path, "r") as ddl:
        sql_text = ddl.read()
        alembic_op.execute(sql_text)


def downgrade():
    file_path = os.path.join(this_dir, "downgrade", "drop_match_table.sql")
    with open(file_path, "r") as ddl:
        sql_text = ddl.read()
        alembic_op.execute(sql_text)




