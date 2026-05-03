param(
    [string]$BaseUrl = "https://aviary.luckysparrow.ch",
    [string]$SelectedSha = "",
    [string]$SelectedTag = "",
    [switch]$MonitorMode,
    [switch]$SkipSmoke,
    [switch]$EnforceLocalHeadParity,
    [int]$TimeoutSeconds = 20,
    [int]$DeployParityMaxWaitSeconds = 300,
    [int]$DeployParityPollSeconds = 15,
    [int]$HealthRetryMaxAttempts = 5,
    [int]$HealthRetryDelaySeconds = 5,
    [string]$Output = ""
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)

if (Test-Path (Join-Path $repoRoot ".venv\Scripts\python.exe")) {
    $pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonExe = "python"
}
else {
    throw "Python executable not found. Install Python or activate .venv."
}

$args = @(
    (Join-Path $PSScriptRoot "run_release_go_no_go.py"),
    "--base-url", $BaseUrl,
    "--timeout-seconds", ([string]$TimeoutSeconds),
    "--deploy-parity-max-wait-seconds", ([string]$DeployParityMaxWaitSeconds),
    "--deploy-parity-poll-seconds", ([string]$DeployParityPollSeconds),
    "--health-retry-max-attempts", ([string]$HealthRetryMaxAttempts),
    "--health-retry-delay-seconds", ([string]$HealthRetryDelaySeconds)
)

if ($SelectedSha) {
    $args += @("--selected-sha", $SelectedSha)
}
if ($SelectedTag) {
    $args += @("--selected-tag", $SelectedTag)
}
if ($MonitorMode) {
    $args += "--monitor-mode"
}
if ($SkipSmoke) {
    $args += "--skip-smoke"
}
if ($EnforceLocalHeadParity) {
    $args += "--enforce-local-head-parity"
}
if ($Output) {
    $args += @("--output", $Output)
}

Push-Location $repoRoot
try {
    & $pythonExe @args
}
finally {
    Pop-Location
}
