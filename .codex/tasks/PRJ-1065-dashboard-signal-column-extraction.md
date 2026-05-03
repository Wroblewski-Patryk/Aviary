# Task

## Header
- ID: PRJ-1065
- Title: Extract dashboard signal-card column
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1064
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1065
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1064` selected the repeated left/right dashboard signal-card maps as a
small dashboard-safe extraction.

## Goal
Add and reuse `DashboardSignalColumn` while preserving the existing dashboard
hero layout, signal card props, and route-owned data.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1065-dashboard-signal-column-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardSignalColumn` to `web/src/components/dashboard.tsx`.
2. Replace left and right dashboard signal-column maps in `App.tsx`.
3. Keep `dashboardSignalCards` data in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard left and right signal columns use `DashboardSignalColumn`.
- Existing `aion-dashboard-signal-column` and signal card selectors are
  preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard signal-column component exists and is used by target
  sections.
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
- Existing shared pattern reused: `DashboardSignalCard`
- New shared pattern introduced: `DashboardSignalColumn`
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
- Task summary: added `DashboardSignalColumn` and reused it for left/right
  dashboard signal-card columns.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: dashboard figure/flow extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard left and right signal columns duplicated the same filtered
  `DashboardSignalCard` map.
- Gaps: dashboard component ownership did not include the signal-column shell.
- Inconsistencies: repeated owner-specific list wrappers exist elsewhere.
- Architecture constraints: preserve hero layout and keep data construction in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1065.
- Priority rationale: selected by PRJ-1064 and limited to existing dashboard
  presentation.
- Why other candidates were deferred: figure notes, cognitive flow, public
  shell, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: filter cards by placement and render existing signal cards.
- Edge cases: preserve column class, card keys, and card props.

### 4. Execute Implementation
- Implementation notes: added `DashboardSignalColumn` and replaced two inline
  maps.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract only a helper function in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: component owner now matches the dashboard signal
  presentation boundary.
- Refinements made: kept placement filtering inside the wrapper to preserve
  current route data shape.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
