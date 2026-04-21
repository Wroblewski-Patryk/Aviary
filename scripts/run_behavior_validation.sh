#!/usr/bin/env bash
set -euo pipefail

if [[ -x "./.venv/bin/python" ]]; then
  PYTHON_BIN="./.venv/bin/python"
elif [[ -x "./.venv/Scripts/python" ]]; then
  PYTHON_BIN="./.venv/Scripts/python"
else
  PYTHON_BIN="python3"
fi

ARTIFACT_PATH="artifacts/behavior_validation/report.json"
PRINT_ARTIFACT_JSON="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --artifact-path)
      ARTIFACT_PATH="${2:-$ARTIFACT_PATH}"
      shift 2
      ;;
    --print-artifact-json)
      PRINT_ARTIFACT_JSON="true"
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

ARGS=(
  "./scripts/run_behavior_validation.py"
  "--python-exe" "$PYTHON_BIN"
  "--artifact-path" "$ARTIFACT_PATH"
)
if [[ "$PRINT_ARTIFACT_JSON" == "true" ]]; then
  ARGS+=("--print-artifact-json")
fi

"$PYTHON_BIN" "${ARGS[@]}"
