# Task

## Header
- ID: PRJ-981
- Title: Extract shared stat-card component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-980
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 981
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Several secondary routes rendered the same stat-card structure with route-local
CSS prefixes directly inside `web/src/App.tsx`. `PRJ-980` expanded route smoke
coverage to all current routes first.

## Goal

Move repeated route stat-card markup into a shared presentational component
without changing route data derivation, labels, values, or CSS class names.

## Scope

- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated route stat-card markup was scattered in
  the app monolith.
- Expected product or reliability outcome: stat-card ownership is centralized
  while route-specific styling remains intact.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `RouteStatCard` into `web/src/components/shared.tsx` and use it for
memory, reflections, plans, goals, insights, automations, and integrations
summary cards.

## Constraints
- use existing systems and approved mechanisms
- do not move route data derivation out of `App()`
- preserve route-specific CSS class names
- do not alter route behavior, labels, values, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `RouteStatCard` to `web/src/components/shared.tsx`.
2. Replace repeated route stat-card article markup in `App.tsx`.
3. Keep route data arrays and route-specific row wrappers in `App()`.
4. Run web build and full route smoke.
5. Update docs and context.

## Acceptance Criteria
- Repeated stat-card markup is replaced by `RouteStatCard`.
- Route-specific `aion-*-stat-*` class names remain unchanged.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Shared stat-card component extracted.
- [x] Route data derivation remains in `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed stat-card CSS class names are generated from the same route keys
- Screenshots/logs:
  - route smoke JSON output only
- High-risk checks:
  - no route data arrays were moved
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - route map now records `RouteStatCard` under shared presentational panels

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing route stat-card markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Stitch used: no
- Existing shared pattern reused: exact existing route stat-card class names
- New shared pattern introduced: no
- Design-memory update required: no
- Remaining mismatches: route-local view bodies still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: inline stat-card markup back into `App.tsx`
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

Dynamic `aion-${routeKey}-stat-*` classes intentionally preserve existing
route-specific CSS selectors.

## Production-Grade Required Contract

- Goal: centralize repeated route stat-card markup.
- Scope: stat-card renderer only.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: see below.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: unchanged
- Regression check performed: yes

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future frontend maintainers and agents
- Existing workaround or pain: repeated stat-card markup in monolith
- Smallest useful slice: one shared stat-card renderer
- Success metric or signal: full route smoke passes
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- Critical user journey: route entry for all current app routes
- SLI: route smoke pass rate
- SLO: all current routes mount after extraction
- Error budget posture: not applicable
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert shared stat-card extraction

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- Data classification: no data changed
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Secret handling: no secrets touched
- Fail-closed behavior: route smoke exits non-zero when any marker is missing
- Residual risk: route-local view bodies still remain in `App.tsx`

## Result Report

- Task summary: moved repeated route stat-card markup into `RouteStatCard`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/shared.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - route-local view bodies and side-card clusters still live in `App.tsx`
- Next steps:
  - extract a route note/side-card component cluster or remove confirmed dead
    components
- Decisions made:
  - preserve route CSS through explicit `routeKey`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: repeated stat-card markup existed across secondary routes.
- Gaps: route-local views remain large.
- Inconsistencies: stat-card structures had no shared owner.
- Architecture constraints: keep route data derivation unchanged.

### 2. Select One Priority Task
- Selected task: PRJ-981 shared route stat-card extraction.
- Priority rationale: full route smoke now protects these routes.
- Why other candidates were deferred: side-card clusters vary more by route.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/shared.tsx`, docs/context.
- Logic: use `RouteStatCard` with route-specific class prefix.
- Edge cases: values may be strings or numbers, so props use `ReactNode`.

### 4. Execute Implementation
- Implementation notes: extracted only stateless markup.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: keep repeated markup.
- Technical debt introduced: no
- Scalability assessment: future stat-card changes now have one renderer.
- Refinements made: avoided moving route data arrays.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
