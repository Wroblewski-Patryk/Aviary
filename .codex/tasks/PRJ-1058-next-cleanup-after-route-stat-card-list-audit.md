# Task

## Header
- ID: PRJ-1058
- Title: Audit next frontend cleanup after route stat-card list extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1057
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1058
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1057` added `RouteStatCardList`. Remaining low-risk presentation
duplication appears in repeated `PersonalityTimelineRow` maps.

## Goal
Select one next small frontend cleanup after route stat-card list extraction.

## Scope
- `.codex/tasks/PRJ-1058-next-cleanup-after-route-stat-card-list-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect repeated `PersonalityTimelineRow` mappings.
2. Confirm wrapper classes can be preserved through a `className` prop.
3. Select exactly one next implementation target.
4. Sync docs/context and validate whitespace.

## Acceptance Criteria
- One target is selected.
- Deferred candidates are documented.
- `git diff --check` passes.

## Definition of Done
- [x] Task contract is complete.
- [x] Docs and context are synchronized.
- [x] Validation evidence is recorded.

## Validation Evidence
- Tests: not run; docs-only audit.
- Manual checks:
  - `git diff --check`
- Result: passed.

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
- Task summary: selected shared `PersonalityTimelineRowList` extraction.
- Files changed: task, task board, project state, frontend audit, v1 roadmap.
- How tested: `git diff --check`.
- What is incomplete: implementation deferred to PRJ-1059.
- Next steps: implement PRJ-1059.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: memory, reflections, plans, and personality route sections repeat the
  same `PersonalityTimelineRow` map.
- Gaps: `PersonalityTimelineRow` has no list-level counterpart.
- Inconsistencies: other repeated card/list patterns now have shared wrappers.
- Architecture constraints: preserve wrapper classes and keep route data arrays
  in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1058.
- Priority rationale: small presentation-only duplication with existing
  component ownership.
- Why other candidates were deferred: route data helpers, settings overview,
  dashboard flagship panels, and decorative panels are broader.

### 3. Plan Implementation
- Files or surfaces to modify: docs/context only.
- Logic: select `PersonalityTimelineRowList` with configurable wrapper class.
- Edge cases: preserve `aion-memory-continuity-list`,
  `aion-reflections-flow-list`, `aion-plans-flow-list`, and personality route
  grid spacing.

### 4. Execute Implementation
- Implementation notes: recorded target and deferrals.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only extract memory/reflections/plans.
- Technical debt introduced: no
- Scalability assessment: list wrapper matches established extraction pattern.
- Refinements made: selected a `className` prop instead of hard-coding route
  wrappers.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
