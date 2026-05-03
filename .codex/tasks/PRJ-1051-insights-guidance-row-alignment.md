# Task

## Header
- ID: PRJ-1051
- Title: Align insights guidance rows with shared module dot-row list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1050
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1051
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1050` selected `/insights` guidance-row shared alignment. The current
guidance rows manually render the same wrapper and row shape already provided
by `ModuleDotRowList`.

## Goal
Replace local `/insights` guidance-row presentation with `ModuleDotRowList`
while preserving route data ownership, selectors, and route behavior.

## Scope
- `web/src/App.tsx`
- `.codex/tasks/PRJ-1051-insights-guidance-row-alignment.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Replace local insights guidance row wrapper/map with `ModuleDotRowList`.
2. Remove the now-unused `ModuleRouteSideRow` import from `App.tsx`.
3. Keep `insightGuidanceCards` and decorative panels in `App()`.
4. Run frontend build, route smoke, and diff validation.
5. Sync docs/context.

## Acceptance Criteria
- `/insights` guidance rows use `ModuleDotRowList`.
- Existing `aion-insights-guidance-*` selectors are preserved.
- Build, route smoke, and diff check pass.

## Definition of Done
- [x] Implementation is complete and scoped to insights guidance rows.
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
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/frontend/app-route-cluster-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Existing shared pattern reused: `ModuleDotRowList`
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; no intentional visual change
- Remaining mismatches: decorative panels remain route-local by design.

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none

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

## Production-Grade Required Contract
- Goal: align insights guidance rows with shared dot-row list.
- Scope: `web/src/App.tsx` plus task/context/docs.
- Implementation Plan: replace local map, remove stale import, validate, sync.
- Acceptance Criteria: shared component reuse with preserved selectors.
- Definition of Done: build, smoke, diff check, context sync.
- Result Report: insights guidance rows now use `ModuleDotRowList`.

## Result Report
- Task summary: insights guidance rows now reuse `ModuleDotRowList`.
- Files changed: `web/src/App.tsx`, task/context/docs.
- How tested: frontend build, full route smoke, `git diff --check`.
- What is incomplete: decorative panels remain route-local by design.
- Next steps: audit next cleanup target.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: local insights guidance row map duplicated shared dot-row structure.
- Gaps: `ModuleRouteSideRow` usage remained after several shared list
  extractions.
- Inconsistencies: similar title/body rows already use `ModuleDotRowList`.
- Architecture constraints: keep route data in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-1051.
- Priority rationale: selected by PRJ-1050.
- Why other candidates were deferred: route data helpers and decorative panels
  are broader.

### 3. Plan Implementation
- Files or surfaces to modify: insights branch in `web/src/App.tsx` plus
  docs/context.
- Logic: pass `insightGuidanceCards` to `ModuleDotRowList`.
- Edge cases: preserve classes via route/row keys and remove stale import only
  if no call sites remain.

### 4. Execute Implementation
- Implementation notes: replaced only local guidance row map.

### 5. Verify and Test
- Validation performed: build, route smoke, diff check.
- Result: passed.

### 6. Self-Review
- Simpler option considered: leave one-off row map.
- Technical debt introduced: no
- Scalability assessment: reduces local JSX while preserving shared pattern.
- Refinements made: removed stale import from `App.tsx`.

### 7. Update Documentation and Knowledge
- Docs updated: frontend audit, frontend component map, v1 roadmap.
- Context updated: task board and project state.
- Learning journal updated: not applicable.
