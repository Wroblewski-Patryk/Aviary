# Task

## Header
- ID: PRJ-1057
- Title: Extract shared route stat-card list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1056
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1057
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1056` selected shared stat-card list extraction. Multiple module routes
repeat the same `RouteStatCard` map inside an existing `ModuleStatRow`.

## Goal
Add and reuse a shared route stat-card list while preserving stat row wrappers,
stat-card selectors, and route stat data ownership.

## Scope
- `web/src/components/shared.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1057-route-stat-card-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `RouteStatCardList` to `web/src/components/shared.tsx`.
2. Replace repeated `RouteStatCard` maps inside existing `ModuleStatRow`
   wrappers.
3. Keep route stat arrays in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Repeated module stat-card maps use `RouteStatCardList`.
- Existing `aion-*-stat-card` selectors are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared list component exists and is used by target module routes.
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
  - `docs/frontend/route-component-map.md`
  - `docs/frontend/app-route-cluster-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: `RouteStatCard`
- New shared pattern introduced: `RouteStatCardList`
- Screenshot comparison pass completed: no; no intentional visual change

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
- Task summary: added `RouteStatCardList` and reused it in module stat rows.
- Files changed: shared component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: route data helper extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: seven routes repeated the same stat-card map.
- Gaps: `RouteStatCard` had no list-level counterpart.
- Inconsistencies: other repeated list shapes already use shared wrappers.
- Architecture constraints: preserve `ModuleStatRow` wrappers and data arrays.

### 2. Select One Priority Task
- Selected task: PRJ-1057.
- Priority rationale: selected by PRJ-1056 and remains presentation-only.
- Why other candidates were deferred: settings overview, dashboard flagship
  panels, route data helpers, and decorative panels are broader.

### 3. Plan Implementation
- Files or surfaces to modify: shared component, route JSX, docs/context.
- Logic: map items through existing `RouteStatCard`.
- Edge cases: keep wrapper selectors on `ModuleStatRow`.

### 4. Execute Implementation
- Implementation notes: added and reused `RouteStatCardList`.

### 5. Verify and Test
- Validation performed: build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: replace only non-health module routes.
- Technical debt introduced: no
- Scalability assessment: list wrapper follows established shared component
  style.
- Refinements made: retained `ModuleStatRow` ownership.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
