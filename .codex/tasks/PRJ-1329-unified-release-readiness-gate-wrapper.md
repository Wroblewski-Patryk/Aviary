# Task

## Header
- ID: PRJ-1329
- Title: Unified release readiness gate wrapper
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1328
- Priority: P1
- Iteration: 1329
- Operation Mode: ARCHITECT
- Mission ID: PRJ-1324-mystic-clean-ui-orchestration-wave-1
- Mission Status: VERIFIED

## Context
Release checks are green, but execution still spans multiple commands.

## Goal
Provide one command that runs core readiness checks in sequence and writes a summary artifact.

## Scope
- `backend/scripts/run_unified_release_readiness_gate.ps1`
- `docs/operations/runtime-ops-runbook.md`

## Definition of Done
- [x] Wrapper script created.
- [x] Script executes and writes summary artifact.
- [x] Runbook updated with usage.

## Validation Evidence
- Command:
  - `.\backend\scripts\run_unified_release_readiness_gate.ps1 -SkipProductionProof`
- Result:
  - architecture gate PASS
  - UI parity smoke PASS
  - summary artifact written: `docs/status/unified-release-readiness-20260525T033415Z.json`
- Reality status: verified
