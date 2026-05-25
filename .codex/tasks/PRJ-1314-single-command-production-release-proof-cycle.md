# Task

## Header
- ID: PRJ-1314
- Title: Single-command production release proof cycle
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1313
- Priority: P1
- Mission ID: PRJ-1314-single-command-production-release-proof-cycle
- Mission Status: VERIFIED

## Goal
Create one command that runs full production proof cycle: evidence capture + release-index sync.

## Definition of Done
- [x] orchestrator script added
- [x] script executed against production
- [x] release index synced from newly generated summary

## Validation Evidence
- command:
  - `./backend/scripts/run_production_release_proof_cycle.ps1 -BaseUrl "https://aviary.luckysparrow.ch"`
- outputs:
  - `docs/status/20260524T173208Z_production-release-evidence/...`
  - `docs/status/release-smoke-20260524T173208Z.json`
  - `docs/status/production-release-evidence-summary-20260524T173208Z.json`
  - auto-sync report for `docs/operations/release-evidence-index.md`
- result:
  - PASS (`health_status=ok`, `release_ready=true`, `release_violations=[]`)
