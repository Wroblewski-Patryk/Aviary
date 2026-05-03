# Task

## Header
- ID: PRJ-1108
- Title: Align public hero card data shape with motif highlights
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1107
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1108
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1107` selected the public hero card projection as the next smallest safe
frontend cleanup. `publicHeroCards` used `{ title, body }` while
`MotifFigurePanel` consumes `{ label, value }`, forcing a JSX-local map.

## Goal
Align public hero card data with `MotifFigurePanel`'s highlight shape so the
public hero can pass data directly without an inline projection.

## Success Signal
- User or operator problem: `App.tsx` has one fewer unnecessary JSX-local data
  projection.
- Expected product or reliability outcome: public hero text remains unchanged
  while the data shape matches the component contract.
- How success will be observed: build and route smoke pass.
- Post-launch learning needed: no

## Scope
- Update `publicHeroCards` in `web/src/App.tsx`.
- Replace the inline `publicHomeSurface.heroCards.map(...)` projection with a
  direct `highlights` prop.
- Update docs/context.

## Deliverable For This Stage
A verified data-shape alignment for public hero motif highlights.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Change `publicHeroCards` entries from `{ title, body }` to
   `{ label, value }`.
2. Update the `satisfies` type.
3. Pass `publicHomeSurface.heroCards` directly to `MotifFigurePanel`.
4. Run build, route smoke, remaining-map inspection, and diff check.

## Acceptance Criteria
- Public hero card copy remains the same.
- `MotifFigurePanel` receives `highlights={publicHomeSurface.heroCards}`.
- The public hero projection map is gone from JSX.
- Build and route smoke pass.

## Definition of Done
- [x] Data shape aligned.
- [x] Public hero projection removed.
- [x] Build and route smoke pass.
- [x] Docs/context updated.

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
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: passed with `status=ok`, `route_count=14`
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "\.map\(" -Context 1,4`
  - result: remaining maps inspected; public hero projection is gone
- Screenshots/logs: command output recorded in session.
- High-risk checks:
  - `git diff --check`
  - result: passed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference: current public hero implementation
- Canonical visual target: current public landing hero
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable for data-shape cleanup
- Visual-direction brief reviewed: not applicable for data-shape cleanup
- Existing shared pattern reused: `MotifFigurePanel` highlight contract
- New shared pattern introduced: no
- Design-memory entry reused: frontend route/component map
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: not assessed
- State checks: public route mount smoke
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: route smoke only
- Input-mode checks: not changed
- Accessibility checks: no markup change
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert public hero card shape if needed
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
This task intentionally does not touch public feature pillars, because they use
`title/body` as their natural card shape and are consumed by a different
component contract.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future frontend maintainers
- Existing workaround or pain: JSX-local projection adapted public hero data to
  the motif component shape.
- Smallest useful slice: align source data shape with the component contract.
- Success metric or signal: route smoke passes and public hero projection is
  removed.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: public landing route
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert the data-shape change

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: built-dist public route smoke
- Regression check performed:
  - `npm run build`
  - `npm run smoke:routes`

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no user data touched
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: not applicable
- Residual risk: none for data-shape cleanup

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary:
  - aligned public hero cards with the `MotifFigurePanel` highlight contract.
- Files changed:
  - `.codex/tasks/PRJ-1108-public-hero-card-data-shape-alignment.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/TASK_BOARD.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
- How tested:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - remaining maps are data projections, transcript state updates, chat
    transcript rendering, and mobile tabbar refs.
- Next steps:
  - `PRJ-1109` audit chat transcript render-map extraction readiness.
- Decisions made:
  - do not change public feature pillar data shape.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - public hero card data needed a projection to satisfy `MotifFigurePanel`.
- Gaps:
  - none.
- Inconsistencies:
  - source data used `title/body` while the component contract used
    `label/value`.
- Architecture constraints:
  - public shell component contract remains the owner of motif highlight
    rendering.

### 2. Select One Priority Task
- Selected task:
  - `PRJ-1108` align public hero card data shape with motif highlights.
- Priority rationale:
  - it is the smallest safe implementation target selected by `PRJ-1107`.
- Why other candidates were deferred:
  - chat transcript and mobile tabbar maps remain behavior/ref-sensitive.

### 3. Plan Implementation
- Files or surfaces to modify:
  - `web/src/App.tsx`
  - docs/context/task files
- Logic:
  - rename public hero card fields and remove the JSX projection.
- Edge cases:
  - preserve localized text exactly.

### 4. Execute Implementation
- Implementation notes:
  - `publicHeroCards` now uses `{ label, value }`.
  - `MotifFigurePanel` now receives `publicHomeSurface.heroCards` directly.

### 5. Verify and Test
- Validation performed:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - keep projection but compute it outside JSX.
- Technical debt introduced: no
- Scalability assessment:
  - data shape now matches the only consumer.
- Refinements made:
  - remaining maps were re-inspected after the change.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
