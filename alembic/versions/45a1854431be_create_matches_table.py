"""create matches table

Revision ID: 45a1854431be
Revises: 
Create Date: 2021-05-23 18:34:22.321257

"""
from alembic import op
import sqlalchemy as sa
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

# revision identifiers, used by Alembic.
revision = "45a1854431be"
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
