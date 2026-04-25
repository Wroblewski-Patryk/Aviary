#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
"../.venv/Scripts/python" "./scripts/run_user_data_cleanup.py" "$@"
