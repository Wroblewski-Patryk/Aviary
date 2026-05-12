# Task

## Header
- ID: PRJ-812
- Title: Persist pending connector confirmation evidence
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-811
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 812
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-811 exposed a bounded `pending_confirmation` response to app chat. A
future confirmation submission still needs server-side evidence from the
original turn, otherwise the backend would have to trust a client-echoed
candidate.

## Goal
Persist the bounded pending connector confirmation evidence in the episode and
reuse one helper for API projection and memory persistence.

## Success Signal
- User or operator problem: future confirmation submission can verify against
  server-side evidence instead of trusting a client payload.
- Expected product or reliability outcome: pending confirmation stays bounded,
  reusable, and action-owned.
- How success will be observed: focused action, API, and runtime tests pass.
- Post-launch learning needed: no

## Deliverable For This Stage
Shared pending-confirmation builder plus persisted episode evidence.

## Scope
- `backend/app/core/connector_confirmation.py`
- `backend/app/api/routes.py`
- `backend/app/core/action.py`
- `backend/tests/test_action_executor.py`
- `backend/tests/test_api_routes.py`
- `backend/tests/test_runtime_pipeline.py`
- docs/context/state files for this task

## Implementation Plan
1. Extract the pending-confirmation projection into one core helper.
2. Reuse the helper from app chat API.
3. Store the same bounded payload in episode payload as
   `pending_connector_confirmation`.
4. Add action and runtime assertions for persisted evidence.
5. Run focused regression and diff hygiene.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not add confirmation submission or provider mutation execution

## Acceptance Criteria
- [x] API and persistence use one pending-confirmation builder.
- [x] Episode payload stores bounded pending-confirmation evidence when action
  stops on confirmation-required connector mutation.
- [x] Missing observation or missing not-yet-allowed gate still yields no
  pending confirmation.
- [x] Runtime ClickUp triage records the persisted evidence.

## Definition of Done
- [x] Focused action/API/runtime tests pass.
- [x] Context and task state are updated.
- [x] Diff hygiene passes.

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
- confirmation submission endpoint or provider mutation execution

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_message"; Pop-Location`
    -> `3 passed, 121 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "pending_connector_confirmation or clickup"; Pop-Location`
    -> `8 passed, 44 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "clickup_task_update_until_confirmation"; Pop-Location`
    -> `1 passed, 109 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py -k "pending_connector_confirmation or app_chat_message"; Pop-Location`
    -> `4 passed, 172 deselected`
  - final focused regression:
    `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_runtime_pipeline.py -k "pending_connector_confirmation or app_chat_message or clickup_task_update_until_confirmation"; Pop-Location`
    -> `6 passed, 280 deselected`
- Manual checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Screenshots/logs: not applicable.
- High-risk checks: no confirmation submission or provider mutation added.
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
- Follow-up architecture doc updates: not required beyond plan/context sync.

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert PRJ-812 helper and episode payload edits.
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

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: bounded connector operation metadata and candidate
  summary.
- Trust boundaries: runtime result, action observations, connector permission
  gates, episode memory.
- Permission or ownership checks: persisted evidence is generated server-side
  from the current action result.
- Abuse cases: client-echoed confirmation candidate is not trusted by this
  slice.
- Secret handling: no changes.
- Security tests or scans: focused regressions.
- Fail-closed behavior: helper returns no payload without both observation and
  not-yet-allowed confirmation gate.
- Residual risk: future submit endpoint must still enforce replay, freshness,
  user-scope, and candidate-drift checks.

## Result Report
- Task summary: Persisted bounded pending connector confirmation evidence.
- Files changed: core helper, app route, action persistence, tests,
  docs/context/state.
- How tested: focused API/action/runtime tests and diff hygiene.
- What is incomplete: no confirmation submission endpoint.
- Next steps: implement dedicated confirmation submission with replay,
  freshness, and user-scope checks.
- Decisions made: episode payload is the server-side evidence anchor for a
  future confirmation path.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: app response exposed pending confirmation, but no durable evidence
  was recorded for future confirmation.
- Gaps: future submit would otherwise need to trust client-echoed candidate
  data.
- Inconsistencies: API and memory projection needed one shared helper.
- Architecture constraints: action owns side effects and permission gates own
  authorization.

### 2. Select One Priority Task
- Selected task: PRJ-812.
- Priority rationale: server-side evidence is prerequisite to safe
  confirmation submission.
- Why other candidates were deferred: actual mutation confirmation endpoint is
  higher risk without this evidence anchor.

### 3. Plan Implementation
- Files or surfaces to modify: core helper, API route, action persistence,
  focused tests.
- Logic: build bounded payload only from `confirmation_required` observation
  plus not-yet-allowed confirmation gate.
- Edge cases: missing observation, missing gate, raw payload exclusion.

### 4. Execute Implementation
- Implementation notes: extracted helper and stored
  `pending_connector_confirmation` in episode payload.

### 5. Verify and Test
- Validation performed: focused API, action, runtime tests and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: duplicate the API helper in action persistence.
- Technical debt introduced: no
- Scalability assessment: shared helper can support later connector families.
- Refinements made: runtime test now asserts persisted ClickUp evidence.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: not applicable.
