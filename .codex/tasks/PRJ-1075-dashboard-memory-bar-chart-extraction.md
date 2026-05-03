# Task

## Header
- ID: PRJ-1075
- Title: Extract dashboard memory bar chart
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1074
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1075
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1074` selected the dashboard memory bar chart as a narrow dashboard
component extraction.

## Goal
Add and reuse `DashboardMemoryBarChart` while preserving dynamic bar heights,
dashboard bar classes, and route-owned metric calculations.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1075-dashboard-memory-bar-chart-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardMemoryBarChart` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard memory bar map in `App.tsx`.
3. Keep `dashboardMemoryBars` and scaled metric calculations in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard memory card uses `DashboardMemoryBarChart`.
- Existing `aion-dashboard-bar-*` classes and `style={{ height }}` behavior are
  preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard memory bar chart component exists and is used by the
  target section.
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
- New shared pattern introduced: `DashboardMemoryBarChart`
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
- Task summary: added `DashboardMemoryBarChart` and reused it for the dashboard
  memory bar chart.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: dashboard guidance CTA rows remain deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard memory bar chart was inline in `App.tsx`.
- Gaps: dashboard component owner did not cover the memory bar chart shell.
- Inconsistencies: neighboring dashboard lists now have shared wrappers.
- Architecture constraints: keep metric calculation and route data ownership in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1075.
- Priority rationale: selected by PRJ-1074 and preserves dynamic height as a
  prop.
- Why other candidates were deferred: guidance CTA rows, figure/flow pieces,
  settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render `label/height` bars through the existing class contract.
- Edge cases: preserve inline `height` style.

### 4. Execute Implementation
- Implementation notes: added `DashboardMemoryBarChart` and replaced the inline
  chart map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: keep the bar chart inline because of dynamic
  height.
- Technical debt introduced: no
- Scalability assessment: component keeps dynamic values external while
  centralizing dashboard presentation markup.
- Refinements made: no route data moved.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
