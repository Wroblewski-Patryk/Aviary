# Task

## Header
- ID: PRJ-1045
- Title: Align integrations side panels with shared module side-panel components
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1044
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1045
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1044` selected `/integrations` side-panel shared alignment. The route has
two local side-panel wrappers that duplicate `ModuleRouteSidePanel` exactly,
including the boundary variant class.

## Goal
Replace local `/integrations` side-panel wrappers with `ModuleRouteSidePanel`
without changing route data, selectors, visual structure, or backend behavior.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1045-integrations-side-panel-alignment.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: frontend route presentation still has avoidable
  local duplication.
- Expected product or reliability outcome: integrations uses the same shared
  side-panel pattern as insights and automations.
- How success will be observed: frontend build, route smoke, and diff check
  pass.
- Post-launch learning needed: no

## Deliverable For This Stage
Verified implementation and synchronized docs/context.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Replace integrations boundary side-panel `<section>` with
   `ModuleRouteSidePanel` using `variant="boundary"`.
2. Replace integrations readiness side-panel `<section>` with
   `ModuleRouteSidePanel`.
3. Keep child `RouteNoteCard`, `ModuleDotRowList`, provider rows, readiness
   rows, and decorative map/web panel unchanged.
4. Run frontend build, route smoke, and diff whitespace validation.
5. Update task, docs, task board, and project state.

## Acceptance Criteria
- Integrations side panels use `ModuleRouteSidePanel`.
- Existing `aion-integrations-side-panel` and
  `aion-integrations-side-panel-boundary` classes are preserved.
- Build and route smoke pass.
- No runtime, API, or data ownership changes are introduced.

## Definition of Done
- [x] Implementation is complete and scoped to integrations side panels.
- [x] Frontend build passes.
- [x] Full route smoke passes.
- [x] Source-of-truth docs and context are synchronized.

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
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Screenshots/logs: route smoke reported `status=ok`, `route_count=14`.
- High-risk checks: class parity reviewed in JSX.
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
- Canonical visual target: no intentional visual change
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable; behavior-neutral
  presentation extraction.
- Visual-direction brief reviewed: not applicable; behavior-neutral
  presentation extraction.
- Existing shared pattern reused: `ModuleRouteSidePanel`
- New shared pattern introduced: no
- Design-memory entry reused: route-keyed shared side-panel pattern
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy: decorative web/map panel preserved
  in place
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no; no intentional visual change
- Remaining mismatches: integrations decorative web/map panel remains
  route-local by design.
- State checks: loading not applicable | empty not applicable | error not applicable | success route smoke
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: desktop route smoke | tablet not changed | mobile not changed
- Input-mode checks: touch not changed | pointer not changed | keyboard not changed
- Accessibility checks: no aria behavior changed.
- Parity evidence: route smoke passed.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert this refactor if visual regression appears.
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
Next likely audit: choose a low-risk follow-up after integrations side-panel
alignment, likely automations flow rows if selector parity is clean.

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
- Regression check performed: frontend build and route smoke

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: maintainers preparing v1
- Existing workaround or pain: side-panel wrapper duplication.
- Smallest useful slice: integrations side-panel wrappers.
- Success metric or signal: build and full route smoke pass.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: authenticated `/integrations` route mount
- SLI: route smoke availability
- SLO: route smoke passes locally
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert this refactor

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

- Task summary: integrations side panels now reuse `ModuleRouteSidePanel`.
- Files changed: `web/src/App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: decorative web/map panel remains route-local by design.
- Next steps: audit the next low-risk frontend cleanup target.
- Decisions made: reuse existing shared component and keep data ownership in
  `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: integrations side panels duplicated `ModuleRouteSidePanel` markup.
- Gaps: route side-panel shared pattern was not consistently reused.
- Inconsistencies: insights and automations used shared side panels; integrations
  still used local section wrappers.
- Architecture constraints: keep provider and readiness data in `App()`; avoid
  visual-specific map extraction.

### 2. Select One Priority Task
- Selected task: `PRJ-1045` align integrations side panels with shared module
  side-panel components.
- Priority rationale: selected by PRJ-1044 and smallest behavior-neutral slice.
- Why other candidates were deferred: automations rows and route data helpers
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: integrations branch in `web/src/App.tsx` plus
  docs/context.
- Logic: replace section wrappers with `ModuleRouteSidePanel`.
- Edge cases: preserve boundary variant class and child spacing classes.

### 4. Execute Implementation
- Implementation notes: reused `ModuleRouteSidePanel`; children stayed
  unchanged.

### 5. Verify and Test
- Validation performed:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Result: passed.

### 6. Self-Review
- Simpler option considered: only boundary panel extraction.
- Technical debt introduced: no
- Scalability assessment: matches existing shared side-panel usage and reduces
  route-local duplication.
- Refinements made: both side panels were aligned because they share the same
  component contract.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
