param(
    [string]$BaseUrl = "https://aviary.luckysparrow.ch",
    [switch]$SkipProductionProof
)

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$statusDir = Join-Path $repoRoot "docs\status"
$timestamp = Get-Date -Format "yyyyMMddTHHmmssZ"
$summaryPath = Join-Path $statusDir "unified-release-readiness-$timestamp.json"

Push-Location $repoRoot
try {
    $steps = @()

    Write-Host "[1/3] Architecture local release gate..."
    Push-Location "backend"
    & "..\.venv\Scripts\python" ".\scripts\run_architecture_graph_local_release_gate.py"
    $archExit = $LASTEXITCODE
    Pop-Location
    $steps += @{
        step = "architecture_local_release_gate"
        ok = ($archExit -eq 0)
        exit_code = $archExit
    }
    if ($archExit -ne 0) { throw "Architecture local gate failed." }

    Write-Host "[2/3] UI parity smoke gate..."
    Push-Location "web"
    & "node" ".\scripts\route-smoke.mjs" `
        --screenshots "docs/status/ui-parity-wave5" `
        --screenshot-routes "/dashboard,/chat,/personality" `
        --viewports "desktop,tablet,mobile" `
        --navigation-proof `
        --account-proof `
        --fail-on-ui-findings `
        --report "docs/status/ui-parity-wave5-report.json"
    $uiExit = $LASTEXITCODE
    Pop-Location
    $steps += @{
        step = "ui_parity_smoke_gate"
        ok = ($uiExit -eq 0)
        exit_code = $uiExit
    }
    if ($uiExit -ne 0) { throw "UI parity smoke gate failed." }

    if (-not $SkipProductionProof) {
        Write-Host "[3/3] Production release proof cycle..."
        & ".\backend\scripts\run_production_release_proof_cycle.ps1" -BaseUrl $BaseUrl
        $prodExit = $LASTEXITCODE
        $steps += @{
            step = "production_release_proof_cycle"
            ok = ($prodExit -eq 0)
            exit_code = $prodExit
            base_url = $BaseUrl
        }
        if ($prodExit -ne 0) { throw "Production proof cycle failed." }
    } else {
        $steps += @{
            step = "production_release_proof_cycle"
            ok = $true
            skipped = $true
            reason = "SkipProductionProof switch used"
        }
    }

    $report = @{
        kind = "unified_release_readiness_gate"
        generated_at = (Get-Date).ToUniversalTime().ToString("o")
        base_url = $BaseUrl
        skip_production_proof = [bool]$SkipProductionProof
        status = "ok"
        steps = $steps
    }
    $report | ConvertTo-Json -Depth 6 | Set-Content -Path $summaryPath -Encoding utf8
    Write-Host "summary=$summaryPath"
}
catch {
    $report = @{
        kind = "unified_release_readiness_gate"
        generated_at = (Get-Date).ToUniversalTime().ToString("o")
        base_url = $BaseUrl
        skip_production_proof = [bool]$SkipProductionProof
        status = "failed"
        error = $_.Exception.Message
        steps = $steps
    }
    $report | ConvertTo-Json -Depth 6 | Set-Content -Path $summaryPath -Encoding utf8
    Write-Host "summary=$summaryPath"
    throw
}
finally {
    Pop-Location
}
