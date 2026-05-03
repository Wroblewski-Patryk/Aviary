# Task

## Header
- ID: PRJ-1083
- Title: Extract dashboard cognitive flow track
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1082
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1083
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1082` selected the dashboard cognitive flow track as a small, track-only
dashboard extraction.

## Goal
Add and reuse `DashboardCognitiveFlowTrack` while preserving flow track classes,
active-step class behavior, and route-owned phase computation.

## Scope
- `web/src/components/dashboard.tsx`
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1083-dashboard-cognitive-flow-track-extraction.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `DashboardCognitiveFlowTrack` to `web/src/components/dashboard.tsx`.
2. Replace the inline dashboard cognitive step map in `App.tsx`.
3. Keep current phase computation and flow shell layout in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- Dashboard cognitive flow steps use `DashboardCognitiveFlowTrack`.
- Existing `aion-dashboard-flow-*` classes and active-step class behavior are
  preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Shared dashboard cognitive flow track component exists and is used by the
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
- New shared pattern introduced: `DashboardCognitiveFlowTrack`
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
- Task summary: added `DashboardCognitiveFlowTrack` and reused it for dashboard
  cognitive flow steps.
- Files changed: dashboard component, `App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: full flow panel extraction remains deferred.
- Next steps: audit the next frontend architecture cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: dashboard cognitive flow steps were inline in `App.tsx`.
- Gaps: dashboard component owner did not cover flow-track presentation.
- Inconsistencies: other dashboard maps now have shared wrappers.
- Architecture constraints: keep current phase and flow shell in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1083.
- Priority rationale: selected by PRJ-1082 and limited to the track map.
- Why other candidates were deferred: full flow panel, figure notes, settings
  controls, tools groups, and route data helpers are broader.

### 3. Plan Implementation
- Files or surfaces to modify: dashboard component owner, route JSX,
  docs/context.
- Logic: render `token/title/detail/active` steps with active modifier class.
- Edge cases: preserve inactive blank class behavior from prior string.

### 4. Execute Implementation
- Implementation notes: added `DashboardCognitiveFlowTrack` and replaced the
  inline cognitive flow map.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: move the entire flow panel.
- Technical debt introduced: no
- Scalability assessment: track-only extraction preserves flagship layout.
- Refinements made: current phase aside remains inline.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
