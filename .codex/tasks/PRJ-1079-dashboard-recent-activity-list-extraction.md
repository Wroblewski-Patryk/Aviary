# Task

## Header
- ID: PRJ-1079
- Title: Extract dashboard recent activity list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1078
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1079
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1078` selected the dashboard recent activity list as a dashboard-specific
presentational extraction.

## Goal
Add and reuse `DashboardRecentActivityList` while preserving dashboard recent
row classes and keeping recent activity data selection in `App()`.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1079-dashboard-recent-activity-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardRecentActivityList` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard recent activity map in `App.tsx`.
3. Keep `personalityRecentActivity.slice(0, 4)` in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard recent activity rows use `DashboardRecentActivityList`.
- Existing `aion-dashboard-recent-row` class, text classes, and wrapper spacing
  are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard recent activity list component exists and is used by the
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
- New shared pattern introduced: `DashboardRecentActivityList`
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
- Task summary: added `DashboardRecentActivityList` and reused it for dashboard
  recent activity rows.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: personality activity rows remain deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard recent activity rows were inline in `App.tsx`.
- Gaps: dashboard component owner did not cover recent activity presentation.
- Inconsistencies: other dashboard lists now have shared wrappers.
- Architecture constraints: keep data selection in `App()` and avoid merging
  with different personality activity row markup.

### 2. Select One Priority Task
- Selected task: PRJ-1079.
- Priority rationale: selected by PRJ-1078 and limited to dashboard
  presentation.
- Why other candidates were deferred: personality activity rows, dashboard
  figure/flow pieces, settings controls, tools groups, and route data helpers
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render `key/title/when` rows in the existing grid wrapper.
- Edge cases: preserve `slice(0, 4)` outside the component.

### 4. Execute Implementation
- Implementation notes: added `DashboardRecentActivityList` and replaced the
  inline dashboard recent activity map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract cross-route recent activity.
- Technical debt introduced: no
- Scalability assessment: dashboard-specific wrapper avoids false sharing with
  personality route activity rows.
- Refinements made: kept slice limit in `App()`.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
