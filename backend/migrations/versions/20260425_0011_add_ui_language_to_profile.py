"""Add ui_language to aion_profile."""

from alembic import op
import sqlalchemy as sa


revision = "20260425_0011"
down_revision = "20260425_0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "aion_profile",
        sa.Column("ui_language", sa.String(length=16), nullable=False, server_default="system"),
    )


def downgrade() -> None:
    op.drop_column("aion_profile", "ui_language")
