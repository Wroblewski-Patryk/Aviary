# Task

## Header
- ID: PRJ-1308
- Title: Local release gate report automation
- Task Type: implementation
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1307
- Priority: P1
- Mission ID: PRJ-1308-local-release-gate-report-automation
- Mission Status: VERIFIED

## Goal
Provide one-command local release-gate execution with a machine-readable report.

## Scope
- `backend/scripts/run_architecture_graph_local_release_gate.py`
- `docs/status/architecture-graph-local-release-gate.json`

## Validation Evidence
- Script execution PASS with `overall_status=PASSED`
- Report written to `docs/status/architecture-graph-local-release-gate.json`

## Residual
Hosted CI artifact proof remains optional supplementary evidence under `DEC-005`.
