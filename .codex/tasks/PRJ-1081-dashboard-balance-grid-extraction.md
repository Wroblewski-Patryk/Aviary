# Task

## Header
- ID: PRJ-1081
- Title: Extract dashboard balance grid
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1080
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1081
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1080` selected the dashboard balance grid as a small dashboard component
extraction.

## Goal
Add and reuse `DashboardBalanceGrid` while preserving balance-row classes,
index-based token classes, and route-owned balance data.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1081-dashboard-balance-grid-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardBalanceGrid` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard balance-row map in `App.tsx`.
3. Keep `dashboardBalanceRows` in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard summary balance rows use `DashboardBalanceGrid`.
- Existing `aion-dashboard-summary-balance-*` classes and index-based token
  classes are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard balance grid component exists and is used by the target
  section.
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
- Existing shared pattern reused: dashboard component owner
- New shared pattern introduced: `DashboardBalanceGrid`
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
- Task summary: added `DashboardBalanceGrid` and reused it for dashboard
  summary balance rows.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: full summary band extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard balance rows were inline in `App.tsx`.
- Gaps: dashboard component owner did not cover the balance grid.
- Inconsistencies: other dashboard list/grid shapes now have shared wrappers.
- Architecture constraints: keep full summary band and data ownership in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1081.
- Priority rationale: selected by PRJ-1080 and limited to static grid markup.
- Why other candidates were deferred: full summary band, figure/flow pieces,
  settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render `label/value` rows with index-based token class.
- Edge cases: preserve token class numbering.

### 4. Execute Implementation
- Implementation notes: added `DashboardBalanceGrid` and replaced the inline
  balance map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move full summary band.
- Technical debt introduced: no
- Scalability assessment: grid-only extraction keeps the slice reversible.
- Refinements made: no route data moved.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
