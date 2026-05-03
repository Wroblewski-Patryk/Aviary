# Task

## Header
- ID: PRJ-1042
- Title: Audit next frontend cleanup after dashboard progress extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1041
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1042
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1041` moved dashboard progress row presentation into
`web/src/components/dashboard.tsx`. The task board points to this audit as the
next smallest frontend architecture slice before more v1 work continues.

## Goal
Select one narrow, architecture-aligned frontend cleanup target that advances
v1 without changing route behavior, introducing new systems, or touching broad
flagship visual layout work.

## Scope
- `.codex/tasks/PRJ-1042-next-cleanup-after-dashboard-progress-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: v1 frontend cleanup needs a clear next safe slice.
- Expected product or reliability outcome: route extraction continues in small
  reversible steps with documented ownership.
- How success will be observed: source-of-truth docs name one next task and
  explain why other candidates were deferred.
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
1. Review the latest task-board and frontend route-component context.
2. Inspect current route-local rendering in `web/src/App.tsx`.
3. Compare remaining local JSX clusters against existing shared components.
4. Select exactly one next implementation target.
5. Update task, board, project state, and planning docs with evidence.

## Acceptance Criteria
- One next frontend cleanup target is selected.
- Deferred candidates are documented.
- Architecture alignment and validation evidence are recorded.

## Definition of Done
- [x] PRJ-1042 task contract is complete with seven-step loop evidence.
- [x] Frontend source-of-truth docs record the selected next task.
- [x] Context files are synchronized.

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
- High-risk checks: architecture/source-of-truth cross-check completed.
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
- Design source reference: existing implemented shell and route component map
- Canonical visual target: preserve current `/insights` UI while extracting
  matching presentation shells.
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable; no visual change in this audit.
- Visual-direction brief reviewed: not applicable; no visual change in this audit.
- Existing shared pattern reused: planned `ModuleOverviewBar`, `ModuleStatRow`,
  `ModuleValueRowList`
- New shared pattern introduced: no
- Design-memory entry reused: route-keyed shared module components
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: decorative orbit panel deferred
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no; implementation deferred
- Remaining mismatches: `/insights` still owns local overview/stat/signal JSX
  until PRJ-1043.
- State checks: loading not applicable | empty not applicable | error not applicable | success not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop not changed | tablet not changed | mobile not changed
- Input-mode checks: touch not changed | pointer not changed | keyboard not changed
- Accessibility checks: selected target preserves current aria labels.
- Parity evidence: docs-only selection.

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
Selected next task: `PRJ-1043` align the `/insights` route with existing shared
module shell/list components.

Deferred candidates:
- dashboard route data-helper extraction, because the dashboard is a flagship
  surface and broad data movement is riskier than one presentational module
  cleanup.
- automations flow rows, because they are health/proactive-derived and closer
  to runtime posture.
- integrations side panels, because they are provider-boundary presentation and
  should follow the already selected `/insights` shell/list cleanup.
- decorative orbit/map panels, because they are visual-specific and should not
  be mixed with simple shared-shell extraction.

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
- Existing workaround or pain: route-local JSX ownership remains large in
  `web/src/App.tsx`.
- Smallest useful slice: `/insights` shared overview/stat/signal presentation.
- Success metric or signal: next implementation can preserve selectors while
  reducing local JSX.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/insights` route mount
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: planned for PRJ-1043
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

- Task summary: selected `/insights` shared-shell/list alignment as the next
  frontend v1 cleanup.
- Files changed: task, task board, project state, frontend audit, v1 roadmap.
- How tested: `git diff --check`.
- What is incomplete: implementation is intentionally deferred to PRJ-1043.
- Next steps: implement PRJ-1043.
- Decisions made: use existing shared components before route data-helper or
  decorative-panel work.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `/insights` still carries local overview bar, stat-row wrapper, and
  signal value-row JSX in `App.tsx`.
- Gaps: route-local JSX remains after broader module route cleanup.
- Inconsistencies: `/memory`, `/reflections`, `/plans`, `/goals`,
  `/automations`, and `/integrations` already reuse shared shell components
  more than `/insights`.
- Architecture constraints: keep data derivation in `App()` for now; reuse
  existing route-keyed presentational components; preserve current selectors.

### 2. Select One Priority Task
- Selected task: `PRJ-1042` audit next frontend cleanup after dashboard progress
  extraction.
- Priority rationale: it is the task-board-indicated next slice and prevents
  accidental broad work.
- Why other candidates were deferred: dashboard/data/helper and decorative
  panels are broader; provider/health rows have stronger runtime coupling.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: record the selected next implementation target and deferrals.
- Edge cases: avoid selecting a task that changes route semantics or adds a new
  abstraction.

### 4. Execute Implementation
- Implementation notes: created this task contract and synchronized frontend
  planning sources.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: selecting broad dashboard route-helper extraction.
- Technical debt introduced: no
- Scalability assessment: selected target reuses existing route-keyed shared
  components and keeps extraction incremental.
- Refinements made: decorative orbit/map panels were explicitly deferred.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
