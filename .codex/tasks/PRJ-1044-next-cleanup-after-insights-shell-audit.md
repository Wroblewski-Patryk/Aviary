# Task

## Header
- ID: PRJ-1044
- Title: Audit next frontend cleanup after insights shell alignment
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1043
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1044
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1043` aligned `/insights` with shared module shell/list components. The
next cleanup should keep reducing route-local presentation while avoiding
provider, health, route-data, or decorative visual complexity.

## Goal
Select one narrow, architecture-aligned frontend cleanup target after insights
shell alignment.

## Scope
- `.codex/tasks/PRJ-1044-next-cleanup-after-insights-shell-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: v1 frontend cleanup needs a clear next safe slice.
- Expected product or reliability outcome: shared route presentation patterns
  continue without changing runtime behavior.
- How success will be observed: source-of-truth docs name one next task and
  explain deferrals.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation slice.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Review current task board and frontend route audit.
2. Inspect `/integrations` and `/automations` remaining route-local JSX.
3. Compare candidates against existing shared component contracts.
4. Select exactly one next implementation task.
5. Update task, board, project state, and planning docs.

## Acceptance Criteria
- One next frontend cleanup target is selected.
- Deferred candidates are documented.
- Validation evidence is recorded.

## Definition of Done
- [x] PRJ-1044 task contract is complete.
- [x] Frontend docs and context record the selected next task.
- [x] Validation evidence is attached.

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
- Tests: not run; docs-only audit.
- Manual checks:
  - `git diff --check`
- Screenshots/logs: not applicable
- High-risk checks: selector/class parity checked against `ModuleRouteSidePanel`.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/frontend/route-component-map.md`
  - `docs/frontend/app-route-cluster-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing implemented `/integrations` route
- Canonical visual target: preserve current integrations side panels.
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable; no visual implementation in
  this audit.
- Visual-direction brief reviewed: not applicable; no visual implementation in
  this audit.
- Existing shared pattern reused: planned `ModuleRouteSidePanel`
- New shared pattern introduced: no
- Design-memory entry reused: route-keyed shared side panel pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: integrations web/map panel deferred
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no; implementation deferred
- Remaining mismatches: integrations side panels remain route-local until
  PRJ-1045.
- State checks: loading not applicable | empty not applicable | error not applicable | success not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop not changed | tablet not changed | mobile not changed
- Input-mode checks: touch not changed | pointer not changed | keyboard not changed
- Accessibility checks: no behavior changed
- Parity evidence: docs-only selection

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert docs/context edits.
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

## Notes
Selected next task: `PRJ-1045` align integrations side panels with shared
module side-panel components.

Deferred candidates:
- automations flow-row presentation, because those rows are health/proactive
  posture-facing and should be audited after the simpler side-panel cleanup.
- route data-helper extraction, because route data ownership is broader than a
  presentational slice.
- decorative web/map panels, because they are visual-specific.

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
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Existing workaround or pain: route-local JSX ownership remains large.
- Smallest useful slice: `/integrations` side-panel presentation.
- Success metric or signal: PRJ-1045 can preserve classes through existing
  shared component props.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/integrations` route mount
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: planned for PRJ-1045
- Rollback or disable path: revert docs/context edits

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data changed
- Trust boundaries: no runtime boundary changed
- Permission or ownership checks: no permission surface changed
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: none introduced

## Result Report

- Task summary: selected integrations side-panel shared alignment as the next
  frontend cleanup.
- Files changed: task, task board, project state, frontend audit, v1 roadmap.
- How tested: `git diff --check`.
- What is incomplete: implementation is intentionally deferred to PRJ-1045.
- Next steps: implement PRJ-1045.
- Decisions made: prefer existing `ModuleRouteSidePanel` before broader route
  data or decorative panel work.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/integrations` still has local side-panel section wrappers.
- Gaps: route side-panel shared pattern is already used by insights and
  automations but not by integrations.
- Inconsistencies: integrations side panels duplicate the same section,
  eyebrow, optional title, and variant classes that `ModuleRouteSidePanel`
  already owns.
- Architecture constraints: keep provider/readiness data and decorative map
  panel in `App()`.

### 2. Select One Priority Task
- Selected task: `PRJ-1044` audit next frontend cleanup after insights shell
  alignment.
- Priority rationale: task-board-indicated next slice and ARCHITECT-mode
  structure cleanup.
- Why other candidates were deferred: automations rows are more runtime-coupled;
  route-data helpers and decorative panels are broader.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: select a class-preserving shared side-panel cleanup.
- Edge cases: verify `variant="boundary"` creates the existing
  `aion-integrations-side-panel-boundary` class.

### 4. Execute Implementation
- Implementation notes: created this task contract and synchronized planning
  sources.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: automations flow rows.
- Technical debt introduced: no
- Scalability assessment: selected target removes duplication using an existing
  shared component.
- Refinements made: explicitly deferred visual map panels.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
