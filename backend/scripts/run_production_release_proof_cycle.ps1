param(
    [string]$BaseUrl = "https://aviary.luckysparrow.ch",
    [string]$Date = "",
    [string]$OutputRoot = "docs/status",
    [switch]$WaitForDeployParity,
    [int]$DeployParityMaxWaitSeconds = 300,
    [int]$DeployParityPollSeconds = 15,
    [int]$HealthRetryMaxAttempts = 3,
    [int]$HealthRetryDelaySeconds = 5
)

$ErrorActionPreference = "Stop"

if (-not $Date) {
    $Date = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
}

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"
$captureScript = Join-Path $PSScriptRoot "run_production_release_evidence_capture.ps1"
$syncScript = Join-Path $PSScriptRoot "sync_release_evidence_index_from_latest_summary.py"

& $captureScript `
    -BaseUrl $BaseUrl `
    -OutputRoot $OutputRoot `
    -WaitForDeployParity:$WaitForDeployParity `
    -DeployParityMaxWaitSeconds $DeployParityMaxWaitSeconds `
    -DeployParityPollSeconds $DeployParityPollSeconds `
    -HealthRetryMaxAttempts $HealthRetryMaxAttempts `
    -HealthRetryDelaySeconds $HealthRetryDelaySeconds
if ($LASTEXITCODE -ne 0) {
    throw "Production release evidence capture failed with exit code $LASTEXITCODE."
}

& $pythonExe $syncScript --date $Date
if ($LASTEXITCODE -ne 0) {
    throw "Release evidence index sync failed with exit code $LASTEXITCODE."
}
