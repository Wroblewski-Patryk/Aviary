# Task

## Header
- ID: PRJ-858
- Title: Add Behavior Scenarios For Observer-Gated Proactivity
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-857
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 858
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-856` changed proactive cadence behavior and `PRJ-857` preserved internal evidence for skipped/failed observer-admitted work. This task records the scenario anchors that prove the behavior across time-sensitive proactive paths.

## Goal
Make observer-gated proactivity scenario coverage explicit in canonical behavior-testing docs and engineering testing guidance.

## Success Signal
- User or operator problem: anti-spam behavior must be proven as behavior, not only module output.
- Expected product or reliability outcome: future changes know which scenarios must stay true.
- How success will be observed: `T22.1..T22.4` are documented and backed by scheduler/repository tests.
- Post-launch learning needed: no

## Deliverable For This Stage
Scenario anchors and testing guidance updates for silent no-op, due outreach, relation-care handoff, and internal failure learning evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- keep tests deterministic and free of live wall-clock dependency

## Scope
- `docs/architecture/29_runtime_behavior_testing.md`
- `docs/engineering/testing.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-858-observer-gated-proactivity-behavior-scenarios.md`

## Implementation Plan
1. Add `T22.1..T22.4` scenario anchors to runtime behavior testing docs.
2. Add proactive-runtime testing guidance for the observer-gated scenario family.
3. Tie the anchors to the focused scheduler and persistence tests added in `PRJ-856..PRJ-857`.
4. Update task board and project state.
5. Run scenario-focused validation.

## Acceptance Criteria
- [x] Silent no-op scenario is documented.
- [x] Due planned-work admission scenario is documented.
- [x] Relation-care planned-work/proposal handoff scenario is documented.
- [x] Failure-learning evidence scenario is documented.
- [x] Deterministic focused validation passes.

## Definition of Done
- [x] DEFINITION_OF_DONE.md posture is satisfied for this docs/testing slice.
- [x] Canonical behavior-testing docs and engineering testing guidance are updated.
- [x] Validation evidence is attached.
- [x] No unrelated dirty worktree changes are staged.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- live wall-clock scenario dependency
- user-visible pseudo-turn from empty scheduler cadence
- new behavior harness without approval
- unrelated UI/context staging

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_scheduler_worker.py tests/test_memory_repository.py -k "proactive or passive_active or scheduler_cadence_evidence"; Pop-Location`
  - result: `9 passed, 76 deselected`
  - `git diff --check`
  - result: passed
- Manual checks: docs cross-review.
- Screenshots/logs: not applicable.
- High-risk checks: scenario anchors map to deterministic scheduler/repository coverage.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/29_runtime_behavior_testing.md`
  - `docs/planning/passive-active-trigger-implementation-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: `PRJ-853`
- Follow-up architecture doc updates: scenario anchors added.

## UX/UI Evidence
- Design source type: not applicable
- Design source reference: not applicable
- Canonical visual target: not applicable
- Fidelity target: not applicable
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not applicable
- Remaining mismatches: none
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not in this slice
- Rollback note: revert docs/task/context only.
- Observability or alerting impact: scenario expectations documented.
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
- [x] Learning journal update remains lane-level work for `PRJ-859`.

## Notes
This task records scenario anchors over the focused deterministic tests added in `PRJ-856..PRJ-857`; it does not introduce a new behavior harness.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY` or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB -> validation -> error handling -> test. Partial implementations, mock-only paths, placeholders, fake data, and temporary fixes are forbidden.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: user receiving unwanted proactive messages.
- Existing workaround or pain: disabling all proactivity.
- Smallest useful slice: scenario anchors over existing deterministic tests.
- Success metric or signal: `T22.1..T22.4` are canonical.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: proactive outreach and planned-work follow-up.
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: focused pytest.
- Rollback or disable path: docs revert.

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: scheduler/repository tests.
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused tests.

## AI Testing Evidence

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: docs/testing metadata.
- Trust boundaries: no new runtime trust boundary.
- Permission or ownership checks: not applicable
- Abuse cases: unwanted proactive outreach.
- Secret handling: no secrets touched.
- Security tests or scans: not applicable
- Fail-closed behavior: empty cadence no-op scenario documented.
- Residual risk: release-smoke visibility remains `PRJ-859`.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: `T22.4` failure evidence anchor.
- Multi-step context scenarios: future behavior-validation expansion.
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: no new data exposure.
- Result: pass

## Result Report

- Task summary: added `T22.1..T22.4` observer-gated proactive behavior anchors.
- Files changed:
  - `docs/architecture/29_runtime_behavior_testing.md`
  - `docs/engineering/testing.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-858-observer-gated-proactivity-behavior-scenarios.md`
- How tested: focused scheduler/repository scenario-related tests and `git diff --check`.
- What is incomplete: release-smoke visibility remains `PRJ-859`.
- Next steps: `PRJ-859`.
- Decisions made: document anchors over existing deterministic tests instead of introducing a new harness.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: behavior existed in tests but scenario anchors did not name the observer-gated family.
- Gaps: testing guidance still pointed at older proactive posture only.
- Inconsistencies: passive/active plan required behavior scenarios.
- Architecture constraints: no new harness without approval.

### 2. Select One Priority Task
- Selected task: `PRJ-858`
- Priority rationale: scenario truth should be explicit before smoke/ops sync.
- Why other candidates were deferred: release-smoke visibility belongs to `PRJ-859`.

### 3. Plan Implementation
- Files or surfaces to modify: behavior-testing docs, engineering testing docs, context.
- Logic: add T22 anchors mapped to existing deterministic scheduler/repository tests.
- Edge cases: no live wall-clock dependency.

### 4. Execute Implementation
- Implementation notes: added scenario anchors and proactive-runtime testing guidance.

### 5. Verify and Test
- Validation performed: focused pytest, `git diff --check`, and docs review.
- Result: pass.

### 6. Self-Review
- Simpler option considered: relying only on task notes.
- Technical debt introduced: no
- Scalability assessment: anchors can later be added to behavior-validation scripts without changing semantics.
- Refinements made: split no-op, due, relation-care, and failure-learning anchors.

### 7. Update Documentation and Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: deferred to `PRJ-859`.
