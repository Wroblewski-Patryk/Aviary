param(
    [string]$PythonExe = ".\.venv\Scripts\python"
)

$ErrorActionPreference = "Stop"

& $PythonExe -m pytest -q tests/test_api_routes.py tests/test_runtime_pipeline.py -k "system_debug_behavior_contract or system_debug_surface or behavior_harness_outputs_structured_contract_results or runtime_behavior_"
