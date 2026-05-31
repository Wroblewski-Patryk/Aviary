# Task

## Header
- ID: LUC-945
- Title: [Aviary][QA+Ops] Add public-entry and internal health smoke guard (P2)
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: LUC-944
- Priority: P2
- Iteration: 2
- Operation Mode: BUILDER
- Mission ID: LUC-945-public-entry-health-smoke-guard
- Mission Status: VERIFIED

## Context
From LUC-939 coverage map, this lane needed a non-prod guard for:
- `GET /health`
- `GET /internal/state/inspect`
- `POST /event`
- `POST /event/debug`
- `GET /`
- `GET /{frontend_path:path}`

## Goal
Deliver a replayable smoke script that validates the public-entry + internal-health contract with expected debug/auth posture and stable machine-readable output.

## Implementation Plan
1. Add a dedicated non-prod smoke script with explicit checks for all required endpoints.
2. Handle both debug ingress modes (`compatibility` and `break_glass_only`).
3. Add focused tests on a stub HTTP server for deterministic proof.

## Acceptance Criteria
- Script verifies all required routes and fails fast on contract drift.
- `/event/debug` behavior is validated for both compatibility and break-glass posture.
- Script returns machine-readable JSON report on success.
- Focused regression tests pass.

## Definition of Done
- [x] `backend/scripts/run_nonprod_entry_health_smoke.py` added.
- [x] `backend/tests/test_nonprod_entry_health_smoke_script.py` added.
- [x] Focused test pack passed locally.

## Validation Evidence
- Tests:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_nonprod_entry_health_smoke_script.py; $code=$LASTEXITCODE; Pop-Location; exit $code`
  - result: `2 passed in 1.13s`
- Reality status: verified

## Deployment / Ops Evidence
- Deploy impact: low
- Smoke steps updated: yes (new dedicated non-prod smoke script)
- Rollback note: remove script + test pair if this lane is reverted.

## Result Report
- Task summary:
  - implemented dedicated QA+Ops non-prod smoke guard for public-entry and internal health surfaces.
  - added debug-mode-aware assertions for `/event/debug` with break-glass fallback verification.
- Files changed:
  - `backend/scripts/run_nonprod_entry_health_smoke.py`
  - `backend/tests/test_nonprod_entry_health_smoke_script.py`
- What is incomplete:
  - no additional docs wiring into ops runbook in this slice.
- Next steps:
  - optionally wire this script into a broader release/non-prod gate wrapper.
