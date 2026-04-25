# Task

## Header
- ID: PRJ-720
- Title: Shared Backend Cleanup Owner And Operator Script
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-719
- Priority: P1

## Context
The destructive-data lane needed one backend-owned cleanup contract that could
be reused by self-service reset and operator flows without duplicating
table-by-table delete logic across API routes or scripts.

## Goal
Implement one shared runtime-cleanup owner in the backend, expose the bounded
self-service reset endpoint through that owner, and add an operator script for
single-user reset or runtime-only cleanup while preserving auth identity and
profile state.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] `MemoryRepository` owns one shared runtime cleanup contract for single-user and runtime-only global cleanup.
- [x] `POST /app/me/reset-data` reuses that owner and revokes all sessions after reset.
- [x] operator scripts exist for bounded cleanup execution with explicit confirmations.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py tests/test_api_routes.py tests/test_runtime_pipeline.py; Pop-Location`
  - result: `273 passed`
- Manual checks:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_user_data_cleanup.py --help; Pop-Location`
- Screenshots/logs:
  - CLI help output confirmed both cleanup modes and confirmation flags.
- High-risk checks:
  - reset preserves profile/settings and managed operational preferences while revoking auth sessions
  - runtime cleanup owner is shared by repository, API route, and operator script

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/user-data-reset-and-production-cleanup-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - context and plan truth updated for `PRJ-720` completion and `PRJ-721` handoff

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
- Shared cleanup owner lives in `backend/app/memory/repository.py`.
- Self-service entrypoint lives at `POST /app/me/reset-data`.
- Operator entrypoints live in:
  - `backend/scripts/run_user_data_cleanup.py`
  - `backend/scripts/run_user_data_cleanup.ps1`
  - `backend/scripts/run_user_data_cleanup.sh`
