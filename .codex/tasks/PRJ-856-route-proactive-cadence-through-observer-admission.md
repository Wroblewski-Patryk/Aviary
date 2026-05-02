# Task

## Header
- ID: PRJ-856
- Title: Route Proactive Cadence Through Observer Admission
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-855
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 856
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-855` made planned-action observer posture visible. This task changes the proactive cadence behavior so generic time/opt-in candidates no longer start foreground runtime by themselves.

## Goal
Route proactive cadence through observer-admitted due planned work or actionable proposal posture, with empty proactive scans ending as cheap no-ops.

## Success Signal
- User or operator problem: scheduler cadence could still produce unwanted outreach because time passed.
- Expected product or reliability outcome: empty proactive cadence does not call foreground runtime.
- How success will be observed: scheduler proactive summaries report `observer_state=empty_noop` with zero foreground events when no due/actionable work exists.
- Post-launch learning needed: yes

## Deliverable For This Stage
Implemented scheduler behavior change, focused tests, and runtime/operator documentation updates.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- keep user-authored turns unaffected

## Scope
- `backend/app/workers/scheduler.py`
- `backend/tests/test_scheduler_worker.py`
- `docs/implementation/runtime-reality.md`
- `docs/operations/runtime-ops-runbook.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/tasks/PRJ-856-route-proactive-cadence-through-observer-admission.md`

## Implementation Plan
1. Replace generic proactive candidate runtime dispatch with observer-admitted due planned-work dispatch.
2. Preserve disabled/external-owner dispatch posture.
3. Record observer state/reason and counts in proactive cadence summaries.
4. Keep due planned work foreground handoff on the existing `planned_work_due` path.
5. Update scheduler tests for empty no-op and due planned-work admission.
6. Update runtime reality, runbook, task board, and project state.
7. Run scheduler and runtime-pipeline validation.

## Acceptance Criteria
- [x] Proactive tick with no due/actionable work records no-op and emits zero foreground events.
- [x] Generic proactive candidates no longer start foreground runtime by themselves.
- [x] Due planned work still reaches conscious planning through the existing foreground handoff.
- [x] User-authored turns remain unaffected.
- [x] Focused scheduler/runtime tests pass.

## Definition of Done
- [x] DEFINITION_OF_DONE.md posture is satisfied for this narrow runtime slice.
- [x] Code, tests, docs, task board, and project state are updated.
- [x] Validation evidence is attached.
- [x] No unrelated dirty worktree changes are staged.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- direct background delivery
- new scheduler engine
- generic time-passing foreground events
- schema changes
- unrelated UI/context staging

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_scheduler_worker.py -k "proactive"; Pop-Location`
  - result: `4 passed, 15 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_scheduler_worker.py; Pop-Location`
  - result: `19 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py; Pop-Location`
  - result: `109 passed`
  - `git diff --check`
  - result: passed
- Manual checks: diff review confirms proactive no longer calls `get_proactive_scheduler_candidates(...)` for foreground dispatch.
- Screenshots/logs: not applicable.
- High-risk checks: empty proactive scans do not call `runtime.run(...)`.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/passive-active-trigger-implementation-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: `PRJ-853`
- Follow-up architecture doc updates: none

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
- Deploy impact: medium
- Env or secret changes: none
- Health-check impact: proactive tick summaries now include observer admission fields.
- Smoke steps updated: runbook interpretation updated; release-smoke parser update remains `PRJ-859`.
- Rollback note: revert scheduler proactive observer-admission change or disable outreach with `PROACTIVE_ENABLED=false`.
- Observability or alerting impact: proactive cadence summaries distinguish `empty_noop` from due planned-work admission.
- Staged rollout or feature flag: existing `PROACTIVE_ENABLED=false` remains the emergency outreach rollback.

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
- [x] Learning journal update was not required because `PRJ-859` owns the lane-level guardrail entry.

## Notes
This slice intentionally keeps skipped/failed learning evidence for `PRJ-857`.

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
- Existing workaround or pain: disable all proactivity.
- Smallest useful slice: observer admission for proactive cadence.
- Success metric or signal: empty proactive scans emit zero foreground events.
- Feature flag, staged rollout, or disable path: `PROACTIVE_ENABLED=false`
- Post-launch feedback or metric check: observer no-op versus due-admission counts.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: proactive outreach and planned-work follow-up.
- SLI: proactive foreground events emitted only after observer admission.
- SLO: not defined in this slice.
- Error budget posture: not applicable
- Health/readiness check: `/health.proactive` and `/health.scheduler.last_proactive_summary`.
- Logs, dashboard, or alert route: scheduler logs include observer state and counts.
- Smoke command or manual smoke: scheduler/runtime tests.
- Rollback or disable path: `PROACTIVE_ENABLED=false`

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: scheduler worker path.
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: scheduler and runtime-pipeline suites.

## AI Testing Evidence

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: scheduler summary metadata.
- Trust boundaries: background cadence observes; action remains side-effect owner.
- Permission or ownership checks: no raw planned-work text added to health beyond existing summary handoff.
- Abuse cases: unwanted scheduler-driven outreach.
- Secret handling: no secrets touched.
- Security tests or scans: not applicable
- Fail-closed behavior: empty/no due work produces no foreground run.
- Residual risk: skipped/failed learning evidence is still pending in `PRJ-857`.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: future `PRJ-858`
- Multi-step context scenarios: future `PRJ-858`
- Adversarial or role-break scenarios: future hardening
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: no provider payloads added.
- Result: pass

## Result Report

- Task summary: proactive cadence now no-ops when observer finds no due/actionable work and admits due planned work through the existing foreground handoff.
- Files changed:
  - `backend/app/workers/scheduler.py`
  - `backend/tests/test_scheduler_worker.py`
  - `docs/implementation/runtime-reality.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-856-route-proactive-cadence-through-observer-admission.md`
- How tested: focused scheduler proactive tests, full scheduler worker tests,
  runtime pipeline tests, and `git diff --check`.
- What is incomplete: skipped/failed passive-active evidence persistence remains `PRJ-857`.
- Next steps: `PRJ-857`.
- Decisions made: generic proactive candidates are no longer foreground triggers.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: proactive tick still emitted foreground events from generic opt-in candidates.
- Gaps: observer posture existed but did not gate proactive cadence behavior.
- Inconsistencies: architecture required passive no-op before conscious foreground.
- Architecture constraints: side effects remain in conscious action path.

### 2. Select One Priority Task
- Selected task: `PRJ-856`
- Priority rationale: this is the behavior-changing anti-spam step after PRJ-855 visibility.
- Why other candidates were deferred: skipped/failed learning evidence belongs to `PRJ-857`.

### 3. Plan Implementation
- Files or surfaces to modify: scheduler, scheduler tests, runtime/ops docs, context.
- Logic: scan due planned work, classify observer state, emit no foreground event when empty.
- Edge cases: external scheduler owner, proactive disabled, due planned-work handoff.

### 4. Execute Implementation
- Implementation notes: reused `_handoff_due_planned_work(...)` and `_dispatch_due_planned_work_foreground(...)`.

### 5. Verify and Test
- Validation performed: focused and full scheduler tests, runtime pipeline,
  and `git diff --check`.
- Result: pass.

### 6. Self-Review
- Simpler option considered: only suppress candidate selection when zero candidates.
- Technical debt introduced: no
- Scalability assessment: observer-admission helper can be extended with proposal-only admission later.
- Refinements made: scheduler snapshot now passes latest summaries into proactive observer posture.

### 7. Update Documentation and Knowledge
- Docs updated: yes
- Context updated: yes
- Learning journal updated: deferred to `PRJ-859`.
