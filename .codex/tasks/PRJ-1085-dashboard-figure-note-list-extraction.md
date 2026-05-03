# Task

## Header
- ID: PRJ-1085
- Title: Extract dashboard figure note list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1084
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1085
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1084` selected the dashboard figure note list as a note-only extraction
that leaves the hero figure stage layout in `App()`.

## Goal
Add and reuse `DashboardFigureNoteList` while preserving figure note classes
and keeping the hero image, halo, badge, and layout in `App()`.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1085-dashboard-figure-note-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardFigureNoteList` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard figure note map in `App.tsx`.
3. Keep the hero image, halo, badge, and stage layout in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard figure notes use `DashboardFigureNoteList`.
- Existing note class names and note text classes are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard figure note list component exists and is used by the
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
- New shared pattern introduced: `DashboardFigureNoteList`
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
- Task summary: added `DashboardFigureNoteList` and reused it for dashboard
  hero figure notes.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: full hero figure stage extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard figure note map was inline in `App.tsx`.
- Gaps: dashboard component owner did not cover figure note presentation.
- Inconsistencies: other dashboard repeated maps now have shared wrappers.
- Architecture constraints: do not move hero image, halo, badge, or figure
  stage layout.

### 2. Select One Priority Task
- Selected task: PRJ-1085.
- Priority rationale: selected by PRJ-1084 and limited to note markup.
- Why other candidates were deferred: full hero figure stage, current phase
  panel, settings controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render caller-owned note classes and note text fields.
- Edge cases: return a fragment so surrounding figure stage layout is unchanged.

### 4. Execute Implementation
- Implementation notes: added `DashboardFigureNoteList` and replaced the inline
  figure note map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move the full figure stage.
- Technical debt introduced: no
- Scalability assessment: note-only component preserves flagship hero layout.
- Refinements made: image, halo, badge, and stage wrapper remain inline.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
