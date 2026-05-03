# Task

## Header
- ID: PRJ-1060
- Title: Audit next frontend cleanup after personality timeline-row list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1059
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1060
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1059` extracted `PersonalityTimelineRowList`, reducing repeated
timeline-row maps while keeping route data in `App()`.

## Goal
Select the next smallest frontend cleanup that moves v1 closer to the approved
component architecture without introducing a new system or broader route-data
movement.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1060-next-cleanup-after-personality-timeline-row-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining frontend component import and usage drift after PRJ-1059.
2. Select exactly one small follow-up.
3. Record deferred candidates and validation evidence.
4. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- Broader frontend cleanup candidates remain deferred.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern "RouteStatCard" -Context 0,2`
  - `git diff --check`
- Result: `RouteStatCard` is only a stale direct import in `App.tsx`; diff
  check passed.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

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
- Task summary: selected stale `RouteStatCard` import removal as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: usage inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1061.
- Next steps: remove the stale `RouteStatCard` import from `App.tsx`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `App.tsx` still imports `RouteStatCard` directly after all route stat
  maps moved behind `RouteStatCardList`.
- Gaps: no active direct `RouteStatCard` call site remains in `App.tsx`.
- Inconsistencies: the import list advertises a direct component dependency
  that no route JSX uses anymore.
- Architecture constraints: keep `RouteStatCard` exported for
  `RouteStatCardList`; only remove the stale route-shell import.

### 2. Select One Priority Task
- Selected task: PRJ-1061 remove stale `RouteStatCard` import.
- Priority rationale: smallest reversible cleanup from the current extraction
  chain.
- Why other candidates were deferred: settings overview, dashboard flagship
  panels, decorative panels, and route data-helper movement are broader.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/App.tsx` and source-of-truth docs.
- Logic: remove the unused named import only.
- Edge cases: keep `RouteStatCardList` import and shared component export.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: usage inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave the import until a larger cleanup pass.
- Technical debt introduced: no
- Scalability assessment: selected task keeps the component boundary explicit.
- Refinements made: deferred all broader frontend movement.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
