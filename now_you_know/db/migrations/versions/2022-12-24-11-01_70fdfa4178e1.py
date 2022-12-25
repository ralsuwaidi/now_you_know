"""empty message

Revision ID: 70fdfa4178e1
Revises: 2e7ff55ff5b1
Create Date: 2022-12-24 11:01:07.937488

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "70fdfa4178e1"
down_revision = "2e7ff55ff5b1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "movie_model",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("title", sa.String(length=200), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("rating", sa.String(length=10), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.drop_table("user_model")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_model",
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("email", sa.VARCHAR(length=200), autoincrement=False, nullable=True),
        sa.Column(
            "full_name",
            sa.VARCHAR(length=200),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("disabled", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("username", name="user_model_pkey"),
    )
    op.drop_table("movie_model")
    # ### end Alembic commands ###
