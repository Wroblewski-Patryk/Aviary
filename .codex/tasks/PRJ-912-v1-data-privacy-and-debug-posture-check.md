# Task

## Header
- ID: PRJ-912
- Title: V1 Data Privacy And Debug Posture Check
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Security
- Depends on: PRJ-911, PRJ-923
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 912
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
Core no-UI v1 is accepted and rollback posture is documented. The remaining
P0 hardening gate is to verify debug, auth, reset, and payload exposure
boundaries before moving toward launch-channel and security hardening tasks.

## Goal
Verify v1 data privacy and debug posture using production health evidence and
focused regression tests.

## Scope
- `docs/planning/v1-data-privacy-and-debug-posture-check.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-912-v1-data-privacy-and-debug-posture-check.md`

## Success Signal
- User or operator problem: release owner can distinguish safe core posture
  from remaining public-launch hardening.
- Expected product or reliability outcome: debug and data exposure boundaries
  are explicit and tested.
- How success will be observed: focused tests pass and production health
  exposes safe policy posture without secret values.
- Post-launch learning needed: no

## Deliverable For This Stage
Privacy/debug posture document and context updates.

## Constraints
- do not enable production debug payload access
- do not commit generated health snapshots
- do not claim AI red-team or cross-user audit completion
- keep provider secret values out of docs

## Implementation Plan
1. Capture production health snapshot locally.
2. Run focused auth/debug/reset/transcript tests.
3. Scan the health snapshot for secret-value risk indicators.
4. Document GO/HOLD posture.
5. Update release plan and context.

## Acceptance Criteria
- Debug disabled posture is recorded.
- Auth and reset boundaries are backed by tests.
- Raw/provider payload exposure boundaries are recorded.
- Remaining AI/security hardening is explicitly queued.

## Definition of Done
- [x] Production health snapshot captured locally.
- [x] Focused regression tests passed.
- [x] Secret-value scan completed.
- [x] Privacy/debug posture doc created.
- [x] Context docs updated.
- [x] `git diff --check` passed.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "debug_payload or internal_state_inspection or app_reset_data or app_me_requires_authenticated_session or app_chat_history_excludes_unlinked_telegram_turns or app_personality_overview_uses_authenticated_user or app_tools_overview_requires_authenticated_session"; Pop-Location`
  - result: `23 passed, 96 deselected`
- Manual checks:
  - production health snapshot captured at
    `.codex/artifacts/prj912-health-snapshot.json`
  - snapshot reports `event_debug_enabled=false`
  - snapshot reports `event_debug_query_compat_enabled=false`
  - snapshot reports `raw_payload_storage_allowed=false`
  - snapshot scan found setting names and policy hints, not secret values
- Screenshots/logs: not applicable
- High-risk checks: no production env change; no debug payload enabled
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/security/secure-development-lifecycle.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: no runtime change
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report

- Task summary: verified v1 privacy/debug posture.
- Files changed:
  - `docs/planning/v1-data-privacy-and-debug-posture-check.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-912-v1-data-privacy-and-debug-posture-check.md`
- How tested: focused pytest, production health review, secret-value scan.
- What is incomplete: AI red-team, cross-user audit, and provider payload
  leakage audit remain queued.
- Next steps: PRJ-909 or PRJ-931 depending on launch-channel priority.
- Decisions made: core no-UI v1 privacy/debug posture is GO; public-launch
  security hardening remains HOLD.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: privacy/debug posture needed one release-readable artifact.
- Gaps: AI red-team and deeper cross-user audit remain queued.
- Inconsistencies: none.
- Architecture constraints: no production debug payload exposure.

### 2. Select One Priority Task
- Selected task: PRJ-912 V1 Data Privacy And Debug Posture Check.
- Priority rationale: final P0 hardening gate before launch-channel/security
  tasks.
- Why other candidates were deferred: Telegram smoke may need operator chat
  preconditions; this task is locally and production-observable.

### 3. Plan Implementation
- Files or surfaces to modify: planning doc, release plan, context docs.
- Logic: document evidence; do not alter runtime.
- Edge cases: setting names in health are acceptable, secret values are not.
- Validation: focused tests and health snapshot scan.

### 4. Execute Implementation
- Captured production health snapshot.
- Ran focused regression suite.
- Documented posture and remaining holds.

### 5. Verify And Test
- Focused tests passed.
- Health snapshot shows debug disabled and safe payload boundaries.
- `git diff --check` passed.

### 6. Self-Review
- Architecture alignment: yes.
- Existing system reuse: tests, health, release docs.
- Workaround check: no bypass introduced.
- Duplication check: no new privacy system created.

### 7. Update Documentation And Knowledge
- Updated task board, project state, and release plan.
- Learning journal update: not required.
