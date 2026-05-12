# Task

## Header
- ID: PRJ-815
- Title: Execute confirmed connector replay from snapshot
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-814
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 815
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-814 persisted replay-safe connector confirmation evidence but left
`/app/connectors/confirm` fail-closed at
`confirmation_replay_not_implemented`. The next smallest slice is to execute
confirmed replay through the existing action boundary only after all stored
evidence checks pass.

## Goal
Allow app connector confirmation to re-enter action with the persisted typed
intent and a matching allowed connector permission gate.

## Success Signal
- User or operator problem: confirmed connector mutations can use the approved
  action path instead of generic chat text.
- Expected product or reliability outcome: provider mutation runs only through
  action after server-side replay evidence passes drift and freshness checks.
- How success will be observed: focused API/action tests pass.
- Post-launch learning needed: no

## Deliverable For This Stage
Confirmed replay execution from stored evidence for the existing connector
action path.

## Scope
- `backend/app/api/schemas.py`
- `backend/app/api/routes.py`
- `backend/tests/test_api_routes.py`
- docs/context/state files for this task

## Implementation Plan
1. Reconstruct a `PlanOutput` from the stored replay snapshot.
2. Validate the snapshot against pending evidence and reject drift fail-closed.
3. Convert the matching stored gate to `allowed=true` only inside the replay
   plan.
4. Build the standard action delivery envelope and call existing
   `ActionExecutor.execute`.
5. Return bounded action status, actions, notes, and pending evidence.
6. Add focused tests for successful replay and retained fail-closed behavior.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not execute provider mutation outside action

## Acceptance Criteria
- [x] Replay execution uses `ActionExecutor.execute`.
- [x] Allowed gate is created only from matching stored replay evidence.
- [x] Drifted replay evidence is rejected before action.
- [x] Successful replay returns bounded action result fields.

## Definition of Done
- [x] Focused API tests pass.
- [x] Context and task state are updated.
- [x] Diff hygiene passes.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping
- provider mutation execution outside action

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
    -> `11 passed, 121 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "clickup_update or pending_connector_confirmation"; Pop-Location`
    -> `1 passed, 51 deselected`
  - final focused regression:
    `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_memory_repository.py -k "pending_connector_confirmation or connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj815-combined; Pop-Location`
    -> `13 passed, 237 deselected`
- Manual checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Screenshots/logs: not applicable
- High-risk checks:
  - replay execution uses `ActionExecutor.execute`
  - replay drift is rejected before action
  - API route does not call provider clients directly
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
- Rollback note: revert PRJ-815 route/schema/test edits.
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
- Task summary: Enabled confirmed connector replay through action from stored
  server-side evidence.
- Files changed: API schema/route, focused API tests, docs/context/state.
- How tested: focused API/action/repository regression and diff hygiene.
- What is incomplete: app UI confirmation controls are not added yet.
- Next steps: add UI controls and execution result rendering.
- Decisions made: API route only reconstructs a plan and calls action; provider
  clients remain action-owned.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: replay evidence exists but submit still stops at
  `confirmation_replay_not_implemented`.
- Gaps: no route path turns stored replay evidence into a matching allowed gate.
- Inconsistencies: confirmed execution must use action, not route-local provider
  calls.
- Architecture constraints: side effects stay in action; client payload is only
  a selector and must not authorize mutation.

### 2. Select One Priority Task
- Selected task: PRJ-815.
- Priority rationale: confirmed replay is the next bounded connector
  confirmation slice after persisted replay evidence.
- Why other candidates were deferred: UI controls should wait until backend
  replay is verified.

### 3. Plan Implementation
- Files or surfaces to modify: API schema/route and focused API tests.
- Logic: validate evidence, rebuild plan, set matching gate allowed, execute
  through action, return bounded result.
- Edge cases: missing executor, missing replay, stale evidence, drifted gate,
  provider not ready, provider execution failure.

### 4. Execute Implementation
- Implementation notes: rebuilt replay plan from stored snapshot, converted the
  matching gate to allowed, and invoked `ActionExecutor.execute`.

### 5. Verify and Test
- Validation performed: focused API tests, action coverage selector, final
  combined regression, and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: API-local provider call, rejected because it would
  violate action ownership.
- Technical debt introduced: no
- Scalability assessment: plan reconstruction can support the existing typed
  connector intent families.
- Refinements made: added replay drift and missing-executor tests.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: not applicable.
