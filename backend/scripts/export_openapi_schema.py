from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

_BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))

from app.main import app


def export_openapi_schema(output_path: Path) -> None:
    schema = app.openapi()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(schema, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export the FastAPI OpenAPI schema without starting the server.",
    )
    parser.add_argument(
        "--output",
        default="../docs/api/openapi.json",
        help="Output JSON path, relative to the current working directory.",
    )
    args = parser.parse_args()
    export_openapi_schema(Path(args.output))


if __name__ == "__main__":
    main()
