# Task

## Header
- ID: PRJ-1064
- Title: Audit next frontend cleanup after personality signal-row list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1063
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1064
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1063` extracted the repeated personality signal-row list. The next
frontend cleanup should remain similarly small and visual-neutral.

## Goal
Select the next smallest frontend architecture cleanup without broad dashboard
layout changes.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1064-next-cleanup-after-personality-signal-row-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining repeated frontend route maps.
2. Select exactly one small dashboard-safe extraction candidate.
3. Confirm the candidate reuses existing dashboard component ownership.
4. Record deferred broader dashboard and route-data candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task avoids dashboard layout or data changes.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Get-Content web/src/components/dashboard.tsx`
  - `Select-String -Path web/src/App.tsx -Pattern "dashboardSignalCards" -Context 2,8`
  - `git diff --check`
- Result: repeated dashboard signal-card column maps found; diff check passed.

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
- Task summary: selected dashboard signal-column extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard component and route JSX inspection, `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1065.
- Next steps: add and reuse `DashboardSignalColumn`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard left and right signal columns duplicate the same
  filter-and-map around `DashboardSignalCard`.
- Gaps: `web/src/components/dashboard.tsx` owns `DashboardSignalCard` but not
  the repeated signal-column wrapper.
- Inconsistencies: other repeated card/list shells have been moved behind
  owner-specific list components.
- Architecture constraints: avoid dashboard layout changes, visual redesign,
  data movement, or screenshot-driven polish in this slice.

### 2. Select One Priority Task
- Selected task: PRJ-1065 extract `DashboardSignalColumn`.
- Priority rationale: small, reversible dashboard presentation cleanup that
  reuses an existing component owner.
- Why other candidates were deferred: figure notes, cognitive flow, public
  shell, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: filter cards by placement and render existing `DashboardSignalCard`.
- Edge cases: preserve `aion-dashboard-signal-column` wrapper class and card
  props.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard JSX inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave duplicate left/right maps until a larger
  dashboard refactor.
- Technical debt introduced: no
- Scalability assessment: selected wrapper keeps the flagship route layout
  untouched while reducing repeated render logic.
- Refinements made: deferred all dashboard figure and flow markup.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
