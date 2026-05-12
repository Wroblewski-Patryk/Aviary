# Task

## Header
- ID: PRJ-810
- Title: Freeze app-facing connector confirmation handoff contract
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-808, PRJ-809
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 810
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-808 made ClickUp create/update fail closed behind connector permission
gates, and PRJ-809 synchronized the docs. The remaining risk is product/API
ambiguity: the web app can send chat messages, but there is no app-facing
confirmation handoff contract that ties a user approval to one specific
connector operation and observed candidate.

## Goal
Record the smallest safe app-facing confirmation contract before any UI or API
implementation attempts to authorize external mutations.

## Success Signal
- User or operator problem: confirmation-required action stops have an explicit
  next contract instead of becoming ad hoc chat-text approval.
- Expected product or reliability outcome: future UI/API work can implement
  confirmation without bypassing connector permission gates or action
  ownership.
- How success will be observed: docs and context name the required handoff
  invariants and the forbidden shortcuts.
- Post-launch learning needed: no

## Deliverable For This Stage
Contract-only documentation and task/context updates.

## Scope
- `docs/planning/skill-guided-bounded-action-loop-plan.md`
- `docs/architecture/16_agent_contracts.md`
- `docs/architecture/15_runtime_flow.md`
- `docs/planning/next-iteration-plan.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`
- `.codex/tasks/PRJ-810-freeze-app-facing-connector-confirmation-handoff-contract.md`

## Implementation Plan
1. Audit current app chat/API and connector permission contracts.
2. Record that plain follow-up chat text is not a safe mutation confirmation
   vehicle by itself.
3. Freeze the minimum future confirmation handoff invariants.
4. Update task/context/state and run text/diff validation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- contract-only; no runtime, API, or UI behavior changes

## Acceptance Criteria
- [x] Docs state that confirmation must be tied to one source event/trace,
  connector kind, provider, operation, and bounded candidate summary.
- [x] Docs state that confirmed execution must re-enter action with only the
  same typed domain intent and a matching allowed connector permission gate.
- [x] Docs forbid treating a generic later chat message as sufficient mutation
  authorization.
- [x] Docs state that confirmation must fail closed on user/session mismatch,
  stale evidence, provider mismatch, or candidate drift.

## Definition of Done
- [x] Confirmation handoff contract is recorded in canonical planning and
  architecture docs.
- [x] Context and agent state are synchronized.
- [x] Validation evidence is recorded.

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
- provider mutation, endpoint implementation, or UI implementation in this task

## Validation Evidence
- Tests: not run for contract-only documentation.
- Manual checks:
  - targeted scans for app chat response, connector permission gates,
    `confirmation_required`, and ClickUp mutation wording
  - `git diff --check` passed with LF/CRLF warnings only
- Screenshots/logs: not applicable.
- High-risk checks: no docs authorize generic chat-text approval as mutation
  confirmation.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `backend/app/api/routes.py`
  - `backend/app/api/schemas.py`
  - `backend/app/core/contracts.py`
  - `backend/app/core/connector_policy.py`
  - `backend/app/core/action.py`
- Fits approved architecture: yes
- Mismatch discovered: no; this is a missing handoff contract after the
  confirmation gate implementation.
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: completed in this task.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert PRJ-810 docs/context edits only.
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

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: first-party web users confirming connector
  mutations.
- Existing workaround or pain: unconfirmed ClickUp mutations now stop safely,
  but the product shell has no safe confirmation handoff contract.
- Smallest useful slice: contract-only handoff freeze before API/UI work.
- Success metric or signal: future API/UI work has explicit invariants and
  forbidden shortcuts.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: user task metadata and external connector mutation
  candidates.
- Trust boundaries: authenticated app session, connector permission gate,
  action-owned provider execution.
- Permission or ownership checks: future confirmation must bind to the same
  authenticated user/session scope and source event evidence.
- Abuse cases: generic chat text or stale candidate replay must not authorize a
  provider mutation.
- Secret handling: no changes.
- Security tests or scans: not run; no code change.
- Fail-closed behavior: required by contract.
- Residual risk: endpoint/UI implementation remains future work.

## Result Report
- Task summary: Froze the app-facing connector confirmation handoff contract.
- Files changed: planning docs, architecture docs, context/state, and this task
  file.
- How tested: targeted review; final `git diff --check`.
- What is incomplete: no app endpoint or UI confirmation workflow implemented.
- Next steps: implement a narrow app-facing pending-confirmation response/API
  only after selecting that implementation slice.
- Decisions made: generic later chat text is not sufficient confirmation for
  provider mutation.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: ClickUp mutations stop safely, but app chat does not expose a
  structured pending-confirmation object.
- Gaps: no contract ties a future confirmation to one event, operation,
  provider, and candidate.
- Inconsistencies: none in current behavior; this is a known next-contract gap.
- Architecture constraints: action owns side effects and connector permission
  gates remain the authorization boundary.

### 2. Select One Priority Task
- Selected task: PRJ-810.
- Priority rationale: prevent future confirmation UX/API work from becoming an
  accidental bypass.
- Why other candidates were deferred: broader loop extensions should wait
  until the mutation confirmation handoff is explicit.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context/state only.
- Logic: record invariants and forbidden shortcuts.
- Edge cases: stale evidence, user/session mismatch, provider mismatch, and
  candidate drift.

### 4. Execute Implementation
- Implementation notes: documented the future handoff boundary without adding
  endpoint, UI, or provider behavior.

### 5. Verify and Test
- Validation performed: targeted scans and `git diff --check`.
- Result: pass.

### 6. Self-Review
- Simpler option considered: leave this as a loose next step.
- Technical debt introduced: no
- Scalability assessment: contract can apply to ClickUp first and later to
  other mutate-with-confirmation connectors.
- Refinements made: separated pending-confirmation presentation from actual
  mutation authorization.

### 7. Update Documentation and Knowledge
- Docs updated: yes.
- Context updated: yes.
- Learning journal updated: not applicable.
