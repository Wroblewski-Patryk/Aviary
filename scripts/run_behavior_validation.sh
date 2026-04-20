#!/usr/bin/env bash
set -euo pipefail

if [[ -x "./.venv/bin/python" ]]; then
  PYTHON_BIN="./.venv/bin/python"
elif [[ -x "./.venv/Scripts/python" ]]; then
  PYTHON_BIN="./.venv/Scripts/python"
else
  PYTHON_BIN="python3"
fi

"$PYTHON_BIN" -m pytest -q tests/test_api_routes.py tests/test_runtime_pipeline.py -k "system_debug_behavior_contract or system_debug_surface or behavior_harness_outputs_structured_contract_results or runtime_behavior_"
