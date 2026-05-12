# Task

## Header
- ID: PRJ-814
- Title: Persist connector confirmation replay snapshot
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-813
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 814
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-813 added a fail-closed app confirmation submit route. It can validate
server-side pending evidence, but it still returns
`confirmation_replay_unavailable` because the episode does not persist a
replay-safe typed connector intent snapshot.

## Goal
Persist a bounded connector confirmation replay snapshot next to pending
confirmation evidence without enabling confirmed action execution.

## Success Signal
- User or operator problem: valid confirmation evidence has enough server-side
  typed intent and gate context for a later replay slice.
- Expected product or reliability outcome: future replay can be built without
  trusting client-echoed operation details.
- How success will be observed: action persistence and app confirmation tests
  pass.
- Post-launch learning needed: no

## Deliverable For This Stage
Replay snapshot persistence and fail-closed API recognition.

## Scope
- `backend/app/core/connector_confirmation.py`
- `backend/app/core/action.py`
- `backend/tests/test_action_executor.py`
- `backend/tests/test_api_routes.py`
- docs/context/state files for this task

## Implementation Plan
1. Add a helper that builds `connector_confirmation_replay` only when a
   pending confirmation payload exists.
2. Include the matching typed domain intent, matching not-yet-allowed
   permission gate, and bounded observation evidence.
3. Persist the replay snapshot in episode payload.
4. Add tests that prove snapshot persistence and API recognition while still
   failing closed before mutation.
5. Run focused regression and diff hygiene.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not execute provider mutation or create an allowed confirmation gate

## Acceptance Criteria
- [x] Replay snapshot is persisted only with valid pending confirmation.
- [x] Snapshot contains typed intent, matching gate, and bounded observation.
- [x] App confirmation reaches `confirmation_replay_not_implemented` when the
  snapshot exists.
- [x] No provider mutation or allowed gate is executed.

## Definition of Done
- [x] Focused action/API tests pass.
- [x] Context and task state are updated.
- [x] Diff hygiene passes.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping
- provider mutation execution from confirmation submit

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "pending_connector_confirmation"; Pop-Location`
    -> `1 passed, 51 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
    -> `9 passed, 121 deselected`
  - final focused regression:
    `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_memory_repository.py -k "pending_connector_confirmation or connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj814-combined; Pop-Location`
    -> `11 passed, 237 deselected`
- Manual checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Screenshots/logs: not applicable
- High-risk checks:
  - replay snapshot records `execution_allowed=false`
  - endpoint still returns `confirmation_replay_not_implemented` before any
    provider mutation path
  - no allowed connector permission gate is created
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/skill-guided-bounded-action-loop-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: planning/context sync only.

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert PRJ-814 helper and episode payload edits.
- Observability or alerting impact: none
- Staged rollout or feature flag: no

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
- Task summary: Persisted replay-safe connector confirmation evidence without
  enabling mutation.
- Files changed: connector confirmation helper, action persistence, action/API
  tests, docs/context/state.
- How tested: focused action/API/repository regressions and diff hygiene.
- What is incomplete: confirmed action replay remains intentionally blocked.
- Next steps: implement confirmed replay execution from persisted snapshot with
  full drift and freshness checks.
- Decisions made: replay snapshot records `execution_allowed=false` and API
  continues to fail closed.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: confirmation submit validates pending evidence but lacks replay
  evidence.
- Gaps: future action replay would otherwise need to reconstruct typed intent
  from client data or unrelated runtime state.
- Inconsistencies: pending evidence and typed replay evidence must be generated
  from the same server-side turn.
- Architecture constraints: action owns side effects; confirmation submit must
  not create an allowed gate until replay is explicitly implemented.

### 2. Select One Priority Task
- Selected task: PRJ-814.
- Priority rationale: typed replay evidence is the prerequisite to any safe
  confirmed action replay.
- Why other candidates were deferred: executing confirmed mutation is still
  unsafe without persisted replay context.

### 3. Plan Implementation
- Files or surfaces to modify: connector confirmation helper, action
  persistence, focused tests, docs/context.
- Logic: persist replay evidence only when pending confirmation exists and a
  matching typed connector intent and not-yet-allowed confirmation gate exist.
- Edge cases: missing observation, missing gate, missing intent, provider drift,
  raw provider payload exclusion.

### 4. Execute Implementation
- Implementation notes: added a replay snapshot builder and persisted
  `connector_confirmation_replay` beside pending confirmation evidence.

### 5. Verify and Test
- Validation performed: focused action/API tests, final combined regression,
  and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: letting the submit endpoint reconstruct intent
  from submitted fields, rejected because it would trust client data.
- Technical debt introduced: no
- Scalability assessment: snapshot supports later connector families through
  typed domain intent serialization.
- Refinements made: API now has a separate test for replay-present
  fail-closed behavior.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: not applicable.
