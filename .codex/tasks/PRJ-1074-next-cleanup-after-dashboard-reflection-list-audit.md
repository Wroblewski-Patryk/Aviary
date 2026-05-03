# Task

## Header
- ID: PRJ-1074
- Title: Audit next frontend cleanup after dashboard reflection-list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1073
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1074
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1073` extracted `DashboardReflectionList`. The adjacent dashboard memory
bar chart remains an inline map but has a narrow presentation shape.

## Goal
Select the next smallest frontend cleanup after dashboard reflection-list
extraction.

## Scope
- `web/src/App.tsx`
- `web/src/components/dashboard.tsx`
- `.codex/tasks/PRJ-1074-next-cleanup-after-dashboard-reflection-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect the remaining dashboard memory bar chart map.
2. Select exactly one small extraction candidate.
3. Confirm dynamic height stays data-owned and visual-neutral.
4. Record deferred broader dashboard candidates.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task preserves dynamic bar height behavior.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "dashboardMemoryBars|aion-dashboard-bar" -Context 1,5`
  - `Get-Content web/src/components/dashboard.tsx`
  - `git diff --check`
- Result: dashboard memory bar chart map found; diff check passed.

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
- Task summary: selected `DashboardMemoryBarChart` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: dashboard route/component inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1075.
- Next steps: add and reuse `DashboardMemoryBarChart`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard memory bar chart map remains inline in `App.tsx`.
- Gaps: dashboard component owner does not yet cover this bar chart shell.
- Inconsistencies: adjacent dashboard reflection list now has a shared wrapper.
- Architecture constraints: keep bar data and scaled height calculation in
  `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1075 extract `DashboardMemoryBarChart`.
- Priority rationale: small dashboard presentation cleanup where dynamic height
  stays an item prop.
- Why other candidates were deferred: guidance CTA rows, figure/flow pieces,
  settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  component map, docs/context.
- Logic: render `label/height` bars through a shared chart wrapper.
- Edge cases: preserve `style={{ height }}` behavior and all
  `aion-dashboard-bar-*` classes.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: dashboard route/component inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave chart inline because of dynamic style.
- Technical debt introduced: no
- Scalability assessment: extracting the wrapper keeps dynamic data outside the
  component while reducing route JSX.
- Refinements made: deferred guidance CTA rows because they include buttons.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
