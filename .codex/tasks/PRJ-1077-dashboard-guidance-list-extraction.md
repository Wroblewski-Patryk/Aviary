# Task

## Header
- ID: PRJ-1077
- Title: Extract dashboard guidance list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1076
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1077
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1076` selected the dashboard guidance row list as a small presentational
extraction with no CTA behavior change.

## Goal
Add and reuse `DashboardGuidanceList` while preserving guidance row classes,
lead-row styling, passive button behavior, and route-owned guidance data.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1077-dashboard-guidance-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardGuidanceList` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard guidance-row map in `App.tsx`.
3. Keep `dashboardGuidanceCards` and CTA behavior in `App()`/current markup
   semantics.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard guidance rows use `DashboardGuidanceList`.
- Existing `aion-dashboard-guidance-*` classes, lead-row class, and passive
  button type/classes are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard guidance list component exists and is used by the target
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
- New shared pattern introduced: `DashboardGuidanceList`
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
- Task summary: added `DashboardGuidanceList` and reused it for dashboard
  guidance rows.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: dashboard figure/flow extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard guidance rows were inline in `App.tsx`.
- Gaps: dashboard component owner did not cover guidance row-list presentation.
- Inconsistencies: other dashboard lists now have shared wrappers.
- Architecture constraints: preserve passive button behavior and keep data in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1077.
- Priority rationale: selected by PRJ-1076 and limited to presentational markup.
- Why other candidates were deferred: figure/flow pieces, settings controls,
  tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render first four guidance rows through a wrapper and preserve lead
  row class.
- Edge cases: do not add or change button handlers.

### 4. Execute Implementation
- Implementation notes: added `DashboardGuidanceList` and replaced the inline
  guidance-row map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: defer because row contains a button.
- Technical debt introduced: no
- Scalability assessment: component preserves existing passive CTA semantics.
- Refinements made: kept the panel-level CTA outside the wrapper.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
