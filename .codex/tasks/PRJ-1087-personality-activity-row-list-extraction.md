# Task

## Header
- ID: PRJ-1087
- Title: Extract personality activity row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1086
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1087
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1086` selected the personality activity row list as a personality-owned
presentational extraction.

## Goal
Add and reuse `PersonalityActivityRowList` while preserving personality activity
row classes, action chip label, and route-owned recent activity data.

## Scope
- `web/src/components/personality.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1087-personality-activity-row-list-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PersonalityActivityRowList` to `web/src/components/personality.tsx`.
2. Replace the inline personality activity-row map in `App.tsx`.
3. Keep `personalityRecentActivity` data in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Personality activity rows use `PersonalityActivityRowList`.
- Existing `aion-personality-activity-row`, text classes, and chip class are
  preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared personality activity row list component exists and is used by the
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
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: personality component owner
- New shared pattern introduced: `PersonalityActivityRowList`
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
- Task summary: added `PersonalityActivityRowList` and reused it for
  personality recent activity rows.
- Files changed: personality component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: settings/tools route extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: personality activity row list was inline in `App.tsx`.
- Gaps: personality component owner did not cover activity row-list
  presentation.
- Inconsistencies: personality timeline and signal rows already had wrappers.
- Architecture constraints: keep route data and panel composition in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1087.
- Priority rationale: selected by PRJ-1086 and limited to personality
  presentation.
- Why other candidates were deferred: settings controls, tools groups, route
  data helpers, and full route extraction are broader.

### 3. Plan Implementation
- Files or surfaces to modify: personality component owner, route JSX,
  docs/context.
- Logic: render `key/title/when` rows and caller-provided chip label.
- Edge cases: preserve chip styling and avoid sharing with dashboard rows.

### 4. Execute Implementation
- Implementation notes: added `PersonalityActivityRowList` and replaced the
  inline personality activity map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: reuse dashboard recent activity list.
- Technical debt introduced: no
- Scalability assessment: owner-specific list preserves route semantics.
- Refinements made: chip label is caller-provided.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
