param(
    [string]$PythonExe = ".\.venv\Scripts\python",
    [string]$ArtifactPath = "artifacts/behavior_validation/report.json",
    [switch]$PrintArtifactJson
)

$ErrorActionPreference = "Stop"

$args = @(
    ".\scripts\run_behavior_validation.py",
    "--python-exe", $PythonExe,
    "--artifact-path", $ArtifactPath
)
if ($PrintArtifactJson) {
    $args += "--print-artifact-json"
}

& $PythonExe @args
