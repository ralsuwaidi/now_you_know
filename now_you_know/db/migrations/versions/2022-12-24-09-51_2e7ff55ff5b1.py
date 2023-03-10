"""empty message

Revision ID: 2e7ff55ff5b1
Revises: 0558822762a8
Create Date: 2022-12-24 09:51:27.747753

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2e7ff55ff5b1"
down_revision = "0558822762a8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_model",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=True),
        sa.Column("full_name", sa.String(length=200), nullable=True),
        sa.Column("disabled", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user_model")
    # ### end Alembic commands ###
