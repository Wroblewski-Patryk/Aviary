# Task

## Header
- ID: PRJ-808
- Title: Extend loop to ClickUp read and confirmation-gated mutation
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-807
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 808
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The ClickUp action path already had provider-backed `create_task`,
`list_tasks`, and `update_task` operations plus connector policy metadata.
However, mutating ClickUp operations could still execute directly when a
`mutate_with_confirmation` intent reached action, even though the shared
connector policy marks those operations as blocked until explicit confirmation.

## Goal
Make the ClickUp slice follow the bounded action-loop contract: read-only task
triage can execute, provider blockers are observable, and create/update
mutations require an explicitly allowed confirmation gate before execution.

## Success Signal
- User or operator problem: ClickUp updates are no longer silently executed from
  a confirmation-required intent.
- Expected product or reliability outcome: runtime can inspect ClickUp tasks in
  a turn, identify update candidates, and ask for confirmation before mutation.
- How success will be observed: action/runtime tests show `clickup_list_tasks`
  for triage, no `clickup_update_task` until confirmation, and bounded blocker
  observations.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified backend slice with action confirmation enforcement, ClickUp
read/triage evidence, runtime scenario updates, and source-of-truth sync.

## Scope
- `backend/app/core/action.py`
- `backend/tests/test_action_executor.py`
- `backend/tests/test_runtime_pipeline.py`
- source-of-truth docs and agent state files

## Implementation Plan
1. Reuse existing connector permission gates and action delivery envelopes.
2. Treat `ConnectorPermissionGateOutput(allowed=True, requires_confirmation=True)`
   as the explicit confirmation signal for mutating ClickUp operations.
3. Block unconfirmed `create_task` before provider mutation and emit a bounded
   confirmation-required observation.
4. For unconfirmed `update_task`, run read-only task lookup, expose the matched
   candidate if available, and stop before mutation.
5. Emit a provider-blocker observation when ClickUp is requested but the client
   is not ready.
6. Update unit/runtime tests and repository truth.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- skills remain metadata-only
- no mutation without an explicitly allowed confirmation gate
- no DB schema, auth, env, secret, deployment, or provider-family change

## Acceptance Criteria
- [x] `list_tasks` remains read-only and provider-backed when ready.
- [x] `create_task` is blocked until a matching confirmation gate is allowed.
- [x] `update_task` performs read-only candidate triage, then stops until
  confirmation.
- [x] confirmed `create_task` and `update_task` still execute when a matching
  allowed gate is present.
- [x] ClickUp provider-not-ready state is observable as a blocker.
- [x] Runtime behavior scenarios expect confirmation gating instead of direct
  mutation.

## Definition of Done
- [x] Implementation is narrowly scoped to ClickUp action execution.
- [x] Relevant action, connector policy, and runtime tests pass.
- [x] Source-of-truth docs and state are updated.
- [x] `DEFINITION_OF_DONE.md` requirements were considered for this runtime
  slice.

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
- executing ClickUp create/update without explicit confirmation

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k clickup; Pop-Location`
    -> `6 passed, 44 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py; Pop-Location`
    -> `51 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "clickup or role_governed_tool_usage or work_partner_scenarios"; Pop-Location`
    -> `4 passed, 106 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_connector_policy.py; Pop-Location`
    -> `6 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_connector_policy.py; Pop-Location`
    -> `57 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_connector_policy.py tests/test_runtime_pipeline.py -k "clickup or role_governed_tool_usage or work_partner_scenarios or connector_operation"; Pop-Location`
    -> `13 passed, 154 deselected`
  - `git diff --check`
    -> passed with LF/CRLF warnings only
- Manual checks: action-boundary review against connector policy.
- Screenshots/logs: not applicable.
- High-risk checks: confirmation gate, provider blocker, no raw payloads,
  no mutation without `allowed=True`.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/skill-guided-bounded-action-loop-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: yes, action executed ClickUp mutations from
  confirmation-required intents without checking an allowed confirmation gate.
- Decision required from user: no, the existing architecture and policy already
  require confirmation.
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: planning/context/state truth updated.

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert PRJ-808 action/test changes to restore prior direct
  ClickUp mutation behavior.
- Observability or alerting impact: action observations now expose
  `confirmation_required` and `clickup_client_not_ready` blockers.
- Staged rollout or feature flag: existing connector/provider readiness gates.

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
- Data classification: bounded ClickUp task names/status summaries.
- Trust boundaries: action owns provider calls; connector gates own
  confirmation posture.
- Permission or ownership checks: matching `task_system/clickup/operation`
  gate must be `allowed=True` for mutation.
- Abuse cases: accidental task creation/update without confirmation.
- Secret handling: no secret changes.
- Fail-closed behavior: unconfirmed mutation stops before provider mutation.
- Residual risk: the repo still needs a broader UX/API confirmation flow before
  normal planner output can produce `allowed=True` gates.

## Result Report
- Task summary: ClickUp read remains provider-backed; create/update now require
  an explicit allowed confirmation gate; update requests can perform read-only
  candidate triage before asking for confirmation.
- Files changed:
  - `backend/app/core/action.py`
  - `backend/tests/test_action_executor.py`
  - `backend/tests/test_runtime_pipeline.py`
  - task/context/planning/state docs
- How tested: focused action, runtime, and connector policy pytest commands.
- What is incomplete: full user-facing confirmation UX/API remains outside this
  slice.
- Next steps: PRJ-809 docs/ops/behavior evidence sync.
- Decisions made: `allowed=True` on the matching connector permission gate is
  the explicit confirmation signal for action execution.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: ClickUp mutate intents were marked confirmation-required but action
  did not enforce allowed confirmation before provider mutation.
- Gaps: no observable provider-not-ready blocker for ClickUp intent execution.
- Inconsistencies: runtime behavior scenarios expected direct ClickUp update.
- Architecture constraints: action owns execution, connector policy owns
  confirmation posture, skills are metadata-only.

### 2. Select One Priority Task
- Selected task: PRJ-808.
- Priority rationale: it closes the mutation side of the bounded action-loop
  rollout after PRJ-807 proved read-only multi-step behavior.
- Why other candidates were deferred: broader docs/ops sync belongs to PRJ-809.

### 3. Plan Implementation
- Files or surfaces to modify: action executor and focused tests.
- Logic: allow read-only list, block unconfirmed mutation, allow confirmed
  mutation through matching gate, report provider blockers.
- Edge cases: provider not ready, update candidate missing, confirmed update
  still executes.

### 4. Execute Implementation
- Implementation notes: reused connector gates and action observations; no new
  confirmation subsystem was introduced.

### 5. Verify and Test
- Validation performed: action, connector policy, runtime focused tests.
- Result: pass.

### 6. Self-Review
- Simpler option considered: block all mutation without triage.
- Technical debt introduced: no
- Scalability assessment: the matching-gate check can be reused by future
  connector mutation paths.
- Refinements made: runtime scenarios now assert confirmation-required blocker
  instead of direct mutation.

### 7. Update Documentation and Knowledge
- Docs updated: planning/context/state docs.
- Context updated: yes.
- Learning journal updated: not applicable.
