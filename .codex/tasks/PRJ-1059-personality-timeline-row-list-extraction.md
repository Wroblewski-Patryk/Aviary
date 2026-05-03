# Task

## Header
- ID: PRJ-1059
- Title: Extract shared personality timeline-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1058
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1059
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1058` selected a shared list wrapper for repeated
`PersonalityTimelineRow` maps in memory, reflections, plans, and personality.

## Goal
Add and reuse `PersonalityTimelineRowList` while preserving existing wrapper
classes and route data ownership.

## Scope
- `web/src/components/personality.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1059-personality-timeline-row-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PersonalityTimelineRowList` with a `className` prop.
2. Replace repeated `PersonalityTimelineRow` maps in memory, reflections,
   plans, and personality.
3. Keep all route data arrays in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Repeated timeline-row maps use `PersonalityTimelineRowList`.
- Existing wrapper classes are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared list component exists and is used by target route sections.
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
  - `docs/frontend/route-component-map.md`
  - `docs/frontend/app-route-cluster-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: `PersonalityTimelineRow`
- New shared pattern introduced: `PersonalityTimelineRowList`
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
- Task summary: added `PersonalityTimelineRowList` and reused it in memory,
  reflections, plans, and personality route sections.
- Files changed: personality component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: route data helper extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: four sections repeated the same timeline-row map.
- Gaps: `PersonalityTimelineRow` had no list-level counterpart.
- Inconsistencies: other repeated list shapes now have shared wrappers.
- Architecture constraints: preserve wrapper classes and data ownership.

### 2. Select One Priority Task
- Selected task: PRJ-1059.
- Priority rationale: selected by PRJ-1058 and remains presentation-only.
- Why other candidates were deferred: settings overview, dashboard flagship
  panels, route data helpers, and decorative panels are broader.

### 3. Plan Implementation
- Files or surfaces to modify: personality component, route JSX, docs/context.
- Logic: map items through existing `PersonalityTimelineRow`.
- Edge cases: preserve all current wrapper classes through `className`.

### 4. Execute Implementation
- Implementation notes: added and reused `PersonalityTimelineRowList`.

### 5. Verify and Test
- Validation performed: build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: extract only module route timelines.
- Technical debt introduced: no
- Scalability assessment: wrapper prop keeps visual ownership explicit.
- Refinements made: default wrapper class kept for simple personality usage.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
