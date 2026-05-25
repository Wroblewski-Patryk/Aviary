param(
    [string]$BaseUrl = "https://aviary.luckysparrow.ch",
    [string]$OutputRoot = "docs/status",
    [switch]$WaitForDeployParity,
    [int]$DeployParityMaxWaitSeconds = 300,
    [int]$DeployParityPollSeconds = 15,
    [int]$HealthRetryMaxAttempts = 3,
    [int]$HealthRetryDelaySeconds = 5
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

function Get-UtcStamp {
    return (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
}

function Ensure-Directory {
    param([Parameter(Mandatory = $true)][string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$backendRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$pythonExe = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $pythonExe)) {
    throw "Python virtualenv executable not found at '$pythonExe'."
}

$resolvedOutputRoot = if ([System.IO.Path]::IsPathRooted($OutputRoot)) {
    $OutputRoot
} else {
    Join-Path $repoRoot $OutputRoot
}
Ensure-Directory -Path $resolvedOutputRoot

$stamp = Get-UtcStamp
$bundleDirName = "${stamp}_production-release-evidence"
$bundleDir = Join-Path $resolvedOutputRoot $bundleDirName
Ensure-Directory -Path $bundleDir

$releaseSmokeJson = Join-Path $resolvedOutputRoot "release-smoke-$stamp.json"
$summaryJson = Join-Path $resolvedOutputRoot "production-release-evidence-summary-$stamp.json"

Push-Location $backendRoot
try {
    & $pythonExe ".\scripts\export_incident_evidence_bundle.py" `
        --base-url $BaseUrl `
        --output-root $bundleDir `
        --capture-mode release_smoke
    if ($LASTEXITCODE -ne 0) {
        throw "Incident evidence export failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

$generatedBundleDirs = @(Get-ChildItem -LiteralPath $bundleDir -Directory)
if ($generatedBundleDirs.Count -ne 1) {
    throw "Expected exactly one incident bundle directory under '$bundleDir'."
}
$finalBundleDir = $generatedBundleDirs[0].FullName

$smokeParams = @{
    BaseUrl = $BaseUrl
    IncidentEvidenceBundlePath = $finalBundleDir
    HealthRetryMaxAttempts = $HealthRetryMaxAttempts
    HealthRetryDelaySeconds = $HealthRetryDelaySeconds
}
if ($WaitForDeployParity.IsPresent) {
    $smokeParams.WaitForDeployParity = $true
    $smokeParams.DeployParityMaxWaitSeconds = $DeployParityMaxWaitSeconds
    $smokeParams.DeployParityPollSeconds = $DeployParityPollSeconds
}

$smokeResult = & (Join-Path $backendRoot "scripts\run_release_smoke.ps1") @smokeParams
if ($LASTEXITCODE -ne 0) {
    throw "Release smoke failed with exit code $LASTEXITCODE."
}
$smokeResult | Out-File -LiteralPath $releaseSmokeJson -Encoding utf8

$smokeJson = Get-Content -LiteralPath $releaseSmokeJson -Raw -Encoding UTF8 | ConvertFrom-Json
$summary = [ordered]@{
    kind = "production_release_evidence_capture"
    generated_at = (Get-Date).ToUniversalTime().ToString("o")
    base_url = $BaseUrl
    bundle_directory = $finalBundleDir
    release_smoke_report = $releaseSmokeJson
    health_status = $smokeJson.health_status
    release_ready = $smokeJson.release_ready
    release_violations = @($smokeJson.release_violations)
    runtime_build_revision = $smokeJson.deployment_runtime_build_revision
    web_shell_build_revision = $smokeJson.web_shell_build_revision
}
$summary | ConvertTo-Json -Depth 6 | Out-File -LiteralPath $summaryJson -Encoding utf8
$summary | ConvertTo-Json -Depth 6
