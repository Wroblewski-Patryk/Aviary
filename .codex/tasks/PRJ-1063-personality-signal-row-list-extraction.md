# Task

## Header
- ID: PRJ-1063
- Title: Extract shared personality signal-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1062
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1063
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1062` selected the repeated personality signal-row maps in the conscious
and subconscious side panels as the next small cleanup.

## Goal
Add and reuse `PersonalitySignalRowList` while preserving existing selectors,
wrapper spacing, and route data ownership.

## Scope
- `web/src/components/personality.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1063-personality-signal-row-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PersonalitySignalRowList` to `web/src/components/personality.tsx`.
2. Replace conscious and subconscious signal-row maps in `App.tsx`.
3. Keep signal data arrays in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Conscious and subconscious signal panels use `PersonalitySignalRowList`.
- Existing `aion-personality-signal-*` selectors and `grid gap-3` spacing are
  preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared signal-row list component exists and is used by target sections.
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
- Existing shared pattern reused: personality component owner and
  `aion-personality-signal-*` selectors
- New shared pattern introduced: `PersonalitySignalRowList`
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
- Task summary: added `PersonalitySignalRowList` and reused it for conscious
  and subconscious personality signal rows.
- Files changed: personality component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: broader personality activity extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: two personality side panels duplicated identical signal-row markup.
- Gaps: personality component ownership covered timeline rows but not signal
  rows.
- Inconsistencies: repeated list presentation was still inline in the route
  shell.
- Architecture constraints: keep route data construction in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1063.
- Priority rationale: selected by PRJ-1062 and limited to presentation.
- Why other candidates were deferred: dashboard flagship panels, public shell
  pieces, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: personality component owner, route JSX,
  docs/context.
- Logic: map `label/value` items through a reusable signal-row list.
- Edge cases: preserve wrapper spacing and CSS selectors.

### 4. Execute Implementation
- Implementation notes: added `PersonalitySignalRowList` and replaced two
  inline maps.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract only a single row component.
- Technical debt introduced: no
- Scalability assessment: list wrapper matches the existing timeline wrapper
  pattern and avoids new route-shell rendering duplication.
- Refinements made: kept default wrapper class identical to prior markup.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
