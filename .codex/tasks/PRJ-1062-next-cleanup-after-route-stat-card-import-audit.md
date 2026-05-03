# Task

## Header
- ID: PRJ-1062
- Title: Audit next frontend cleanup after stale RouteStatCard import removal
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1061
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1062
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1061` removed a stale route-shell import after route stat-card rendering
moved behind `RouteStatCardList`.

## Goal
Select the next smallest frontend architecture cleanup that reduces repeated
route JSX while preserving route data ownership in `App()`.

## Scope
- `web/src/App.tsx`
- `web/src/components/personality.tsx`
- `.codex/tasks/PRJ-1062-next-cleanup-after-route-stat-card-import-audit.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Inspect remaining repeated map clusters in `App.tsx`.
2. Select exactly one small extraction candidate.
3. Confirm that the candidate fits an existing component owner.
4. Record deferred candidates and validation evidence.
5. Sync source-of-truth context and planning docs.

## Acceptance Criteria
- The next task is explicitly selected.
- The selected task has a narrow component owner and no data movement.
- No production code changes are made during this audit task.

## Definition of Done
- [x] Next frontend cleanup task is selected.
- [x] Validation evidence is recorded.
- [x] Source-of-truth docs and context are synchronized.

## Validation Evidence
- Tests: not applicable; audit-only task.
- Manual checks:
  - `Select-String -Path web/src/App.tsx -Pattern ".map((" -Context 1,4`
  - `Select-String -Path web/src/App.tsx -Pattern "personalityConsciousSignals|personalitySubconsciousSignals" -Context 2,8`
  - `git diff --check`
- Result: repeated personality signal-row maps found; diff check passed.

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
- Task summary: selected `PersonalitySignalRowList` extraction as the next tiny
  frontend cleanup.
- Files changed: task/context/planning docs only.
- How tested: repeated-map inspection and `git diff --check`.
- What is incomplete: implementation is deferred to PRJ-1063.
- Next steps: add and reuse `PersonalitySignalRowList`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: conscious and subconscious personality side panels duplicate the same
  `aion-personality-signal-row` map markup.
- Gaps: `web/src/components/personality.tsx` owns timeline rows but not the
  adjacent personality signal rows.
- Inconsistencies: similar repeated route maps have shared list wrappers.
- Architecture constraints: keep signal data arrays in `App()` and avoid route
  data-helper movement in this slice.

### 2. Select One Priority Task
- Selected task: PRJ-1063 extract `PersonalitySignalRowList`.
- Priority rationale: smallest presentational extraction still left in the
  personality route cluster.
- Why other candidates were deferred: dashboard flagship panels, public shell
  pieces, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: personality component owner, route JSX,
  component map, docs/context.
- Logic: render `label/value` items through a shared list wrapper.
- Edge cases: preserve existing `grid gap-3` wrapper and
  `aion-personality-signal-*` selectors.

### 4. Execute Implementation
- Implementation notes: audit only; no production code changed.

### 5. Verify and Test
- Validation performed: repeated-map inspection and diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave two duplicated maps until broader
  personality route extraction.
- Technical debt introduced: no
- Scalability assessment: selected wrapper matches the current personality
  component ownership boundary.
- Refinements made: deferred activity rows because they have a different shape.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit and v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
