# Task

## Header
- ID: PRJ-1311
- Title: Single-command production release evidence capture
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1310
- Priority: P1
- Mission ID: PRJ-1311-single-command-production-release-evidence-capture
- Mission Status: VERIFIED

## Goal
Provide one command that exports incident evidence and runs production smoke with bundle verification, then stores durable status artifacts.

## Definition of Done
- [x] script created in `backend/scripts`
- [x] script verified against production URL
- [x] runbook updated with canonical command

## Validation Evidence
- command:
  - `./backend/scripts/run_production_release_evidence_capture.ps1 -BaseUrl "https://aviary.luckysparrow.ch"`
- result:
  - PASS (`health_status=ok`, `release_ready=true`, `release_violations=[]`)
- generated artifacts:
  - `docs/status/20260524T172730Z_production-release-evidence/20260524T172730Z_incident-bundle-20260524T172730Z/*`
  - `docs/status/release-smoke-20260524T172730Z.json`
  - `docs/status/production-release-evidence-summary-20260524T172730Z.json`
