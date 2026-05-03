# Task

## Header
- ID: PRJ-1078
- Title: Audit next frontend cleanup after dashboard guidance-list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1077
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1078
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1077` extracted `DashboardGuidanceList`. The dashboard recent activity
panel still has a small inline list with a dashboard-specific row shape.

## Goal
Select the next smallest frontend cleanup after dashboard guidance-list
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1078-next-cleanup-after-dashboard-guidance-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the dashboard recent activity list.
2. Select exactly one small extraction candidate.
3. Confirm the candidate does not overlap with the personality activity row.
4. Record deferred broader candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task preserves dashboard-specific recent activity markup.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "aion-dashboard-recent|personalityRecentActivity.slice(0, 4)" -Context 1,5`
  - `Select-String -Path web/src/App.tsx -Pattern "personalityRecentActivity.map|aion-personality-activity-row" -Context 1,6`
  - `git diff --check`
- Result: dashboard recent activity row list found; diff check passed.

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
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; audit-only task

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
- Task summary: selected `DashboardRecentActivityList` extraction as the next
  tiny frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard/personality activity row inspection and
  `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1079.
- Next steps: add and reuse `DashboardRecentActivityList`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard recent activity rows remain inline in `App.tsx`.
- Gaps: dashboard component owner does not cover recent activity list
  presentation.
- Inconsistencies: other dashboard list shapes now have shared wrappers.
- Architecture constraints: do not merge with personality activity rows because
  they have a different action-bearing shape.

### 2. Select One Priority Task
- Selected task: PRJ-1079 extract `DashboardRecentActivityList`.
- Priority rationale: small dashboard-only presentation extraction with no
  behavior changes.
- Why other candidates were deferred: personality activity rows, figure/flow
  pieces, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: render `key/title/when` rows with existing dashboard recent classes.
- Edge cases: preserve `slice(0, 4)` data selection in `App()`.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard/personality activity row inspection and diff
  check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract a cross-route activity list.
- Technical debt introduced: no
- Scalability assessment: dashboard-specific wrapper avoids false abstraction.
- Refinements made: personality activity rows remain deferred.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
