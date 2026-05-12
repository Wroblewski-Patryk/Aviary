# Task

## Header
- ID: PRJ-813
- Title: Add fail-closed connector confirmation submit path
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-812
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 813
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-812 persisted bounded pending connector confirmation evidence in the
episode payload. The app still has no dedicated submission path for connector
confirmation. A safe first path must verify server-side evidence and fail
closed while replay plan snapshots are not yet persisted.

## Goal
Add an app-authenticated connector confirmation submission endpoint that checks
server-side pending confirmation evidence and refuses execution unless a future
replay contract is available.

## Success Signal
- User or operator problem: confirmation attempts are routed through a bounded
  server-side verification path instead of generic chat text.
- Expected product or reliability outcome: client-echoed confirmation payloads
  cannot authorize provider mutation.
- How success will be observed: focused API tests prove user-scope,
  mismatch, freshness, and replay-unavailable fail-closed behavior.
- Post-launch learning needed: no

## Deliverable For This Stage
Fail-closed API path and focused tests; no provider mutation execution.

## Scope
- `backend/app/api/schemas.py`
- `backend/app/api/routes.py`
- `backend/app/memory/repository.py`
- `backend/tests/test_api_routes.py`
- docs/context/state files for this task

## Implementation Plan
1. Add request/response schemas for app connector confirmation.
2. Add repository lookup for a single user-owned episode by source event id.
3. Add app route that requires auth, loads pending confirmation evidence, and
   checks trace, connector kind, provider, operation, mode, candidate summary,
   source reference, and freshness.
4. Return fail-closed `409` when replay execution evidence is unavailable.
5. Add focused API tests for accepted evidence lookup, mismatch, stale
   evidence, and user isolation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not execute provider mutation or create an allowed confirmation gate

## Acceptance Criteria
- [ ] Endpoint requires app authentication.
- [x] Endpoint requires app authentication.
- [x] Endpoint loads evidence only from the authenticated user's episode.
- [x] Endpoint rejects missing, stale, or drifted evidence fail-closed.
- [x] Endpoint rejects valid evidence with replay-unavailable until replay
  plan snapshots exist.
- [x] No provider mutation path is executed.

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
- provider mutation execution from confirmation submit

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
    -> `8 passed, 121 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py -k "episode_by_user_and_event_id or structured_episode_payload" --basetemp ..\.codex\tmp\pytest-prj813; Pop-Location`
    -> `2 passed, 64 deselected`
  - final focused regression:
    `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py tests/test_memory_repository.py -k "connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj813-combined; Pop-Location`
    -> `9 passed, 186 deselected`
- Manual checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Screenshots/logs: not applicable
- High-risk checks:
  - endpoint always returns fail-closed before provider mutation because
    `connector_confirmation_replay` is not persisted yet
  - cross-user evidence lookup returns `404`
  - candidate drift and stale evidence return `409`
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
- Rollback note: revert PRJ-813 route/schema/repository/test edits.
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
- Task summary: Added a dedicated app connector confirmation route that
  verifies persisted pending evidence and fails closed without replay.
- Files changed: API schemas/routes, memory repository lookup, API and memory
  repository tests, docs/context/state.
- How tested: focused API/repository tests and diff hygiene.
- What is incomplete: confirmed action replay is intentionally not enabled.
- Next steps: persist a replay-safe typed plan snapshot for connector
  confirmation.
- Decisions made: valid evidence returns `confirmation_replay_unavailable`
  until replay evidence exists.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: app chat can expose pending confirmation and episodes persist
  bounded evidence, but there is no app submit path.
- Gaps: stored evidence does not yet include a replayable typed plan snapshot.
- Inconsistencies: generic chat text must not authorize mutation.
- Architecture constraints: action owns side effects; connector permission
  gates own authorization; confirmation must fail closed on drift.

### 2. Select One Priority Task
- Selected task: PRJ-813.
- Priority rationale: confirmation submission is the next blocker after
  persisted evidence.
- Why other candidates were deferred: broader loop extension would increase
  risk before the confirmation boundary is explicit.

### 3. Plan Implementation
- Files or surfaces to modify: API schemas/routes, memory lookup, focused
  route tests, docs/context.
- Logic: verify submitted payload against authenticated user's server-side
  pending evidence, then stop with replay-unavailable until a later slice
  persists replay snapshots.
- Edge cases: unauthenticated user, missing evidence, user mismatch, stale
  evidence, drifted candidate fields.

### 4. Execute Implementation
- Implementation notes: added `/app/connectors/confirm`, user-scoped episode
  lookup, freshness/candidate checks, and fail-closed replay-unavailable
  response.

### 5. Verify and Test
- Validation performed: focused API tests, repository lookup tests, combined
  regression, and `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: directly allowing confirmation from submitted
  payload, rejected because it would trust client-echoed mutation evidence.
- Technical debt introduced: no
- Scalability assessment: route can enable replay once a typed snapshot is
  persisted.
- Refinements made: added real repository lookup coverage and recorded the
  pytest temp-root pitfall.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: yes.
