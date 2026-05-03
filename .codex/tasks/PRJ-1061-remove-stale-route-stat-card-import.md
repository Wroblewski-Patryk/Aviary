# Task

## Header
- ID: PRJ-1061
- Title: Remove stale RouteStatCard route-shell import
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1060
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1061
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1060` confirmed that `App.tsx` no longer calls `RouteStatCard`
directly after route stat-card maps moved behind `RouteStatCardList`.

## Goal
Remove the stale `RouteStatCard` named import from the route shell while
keeping the shared card export available for `RouteStatCardList`.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1061-remove-stale-route-stat-card-import.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Remove the unused `RouteStatCard` named import from `App.tsx`.
2. Keep `RouteStatCardList` and the shared `RouteStatCard` export intact.
3. Run frontend build, route smoke, and diff validation.
4. Sync source-of-truth docs and context.

## Acceptance Criteria
- `App.tsx` no longer imports `RouteStatCard` directly.
- `RouteStatCardList` usage remains unchanged.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Stale route-shell import is removed.
- [x] Frontend build passes.
- [x] Full route smoke passes.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- Manual checks:
  - `git diff --check`
- Result: passed; route smoke reported `status=ok`, `route_count=14`.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: `RouteStatCardList`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; no visual change

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report
- Task summary: removed the stale `RouteStatCard` import from `App.tsx`.
- Files changed: `App.tsx` and task/context/planning docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: route data-helper extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `RouteStatCard` remained in the route-shell import list without a
  direct route-shell call site.
- Gaps: stale import could obscure the newer `RouteStatCardList` boundary.
- Inconsistencies: other extracted route list wrappers no longer require direct
  card imports in `App.tsx`.
- Architecture constraints: do not remove the shared component export because
  `RouteStatCardList` owns that rendering path.

### 2. Select One Priority Task
- Selected task: PRJ-1061.
- Priority rationale: selected by PRJ-1060 and safely reversible.
- Why other candidates were deferred: settings overview, dashboard flagship
  panels, decorative panels, and route data-helper movement are broader.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, task/context/docs.
- Logic: remove only the unused named import.
- Edge cases: preserve `RouteStatCardList` import and usage.

### 4. Execute Implementation
- Implementation notes: removed `RouteStatCard` from the shared component
  import list in `App.tsx`.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: keep stale import until larger route-shell cleanup.
- Technical debt introduced: no
- Scalability assessment: import list now matches live route-shell ownership.
- Refinements made: kept shared component export intact.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
