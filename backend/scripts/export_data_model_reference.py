from __future__ import annotations

import argparse
from pathlib import Path
import sys

from sqlalchemy import UniqueConstraint

_BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))

from app.memory.models import Base


def _column_type(column) -> str:
    return column.type.compile(dialect=None)


def _column_default(column) -> str:
    if column.default is None:
        return ""
    if column.default.is_callable:
        return "callable"
    return str(column.default.arg)


def _unique_constraints(table) -> list[str]:
    names: list[str] = []
    for constraint in table.constraints:
        if isinstance(constraint, UniqueConstraint):
            cols = ", ".join(column.name for column in constraint.columns)
            names.append(f"{constraint.name or 'unnamed'}({cols})")
    return sorted(names)


def export_columns(output_path: Path) -> None:
    lines: list[str] = [
        "# Column Model Reference",
        "",
        "Generated from `backend/app/memory/models.py` via `Base.metadata`.",
        "Do not edit table details by hand; regenerate this file after model changes.",
        "",
        "Regeneration command:",
        "",
        "```powershell",
        "Push-Location .\\backend",
        "..\\.venv\\Scripts\\python .\\scripts\\export_data_model_reference.py --columns-output ..\\docs\\data\\columns.md --erd-output ..\\docs\\data\\erd.mmd",
        "Pop-Location",
        "```",
        "",
    ]
    for table in sorted(Base.metadata.sorted_tables, key=lambda item: item.name):
        model_name = next(iter(table.info.get("models", [])), "UNVERIFIED")
        primary_key = ", ".join(column.name for column in table.primary_key.columns)
        lines.extend(
            [
                f"## `{table.name}`",
                "",
                f"- ORM model: `{model_name}`",
                f"- Primary key: `{primary_key}`",
                f"- Unique constraints: {', '.join(_unique_constraints(table)) or 'none'}",
                "",
                "| Column | Type | Nullable | Indexed | Default |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for column in table.columns:
            default = _column_default(column)
            lines.append(
                f"| `{column.name}` | `{_column_type(column)}` | "
                f"{'yes' if column.nullable else 'no'} | "
                f"{'yes' if column.index else 'no'} | "
                f"{default or 'none'} |"
            )
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def export_erd(output_path: Path) -> None:
    lines: list[str] = ["erDiagram"]
    for table in sorted(Base.metadata.sorted_tables, key=lambda item: item.name):
        lines.append(f"  {table.name} {{")
        for column in table.columns:
            type_name = _column_type(column).replace(" ", "_").replace("(", "_").replace(")", "")
            markers: list[str] = []
            if column.primary_key:
                markers.append("PK")
            if column.index:
                markers.append("IDX")
            marker_text = f" \"{', '.join(markers)}\"" if markers else ""
            lines.append(f"    {type_name} {column.name}{marker_text}")
        lines.append("  }")

    lines.extend(
        [
            "  %% Logical application-level links, not inspected ForeignKey constraints:",
            "  %% aion_auth_session.user_id -> aion_auth_user.id",
            "  %% aion_profile.user_id -> user identity",
            "  %% user_id columns scope most runtime tables to one user",
            "  %% aion_task.goal_id -> aion_goal.id when present",
            "  %% source_event_id/supporting_event_id/event_id fields link back to runtime events",
        ]
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export SQLAlchemy metadata as column reference and Mermaid ERD.",
    )
    parser.add_argument("--columns-output", default="../docs/data/columns.md")
    parser.add_argument("--erd-output", default="../docs/data/erd.mmd")
    args = parser.parse_args()

    model_names = {mapper.local_table.name: mapper.class_.__name__ for mapper in Base.registry.mappers}
    for table in Base.metadata.tables.values():
        table.info.setdefault("models", []).append(model_names.get(table.name, "UNVERIFIED"))

    export_columns(Path(args.columns_output))
    export_erd(Path(args.erd_output))


if __name__ == "__main__":
    main()
