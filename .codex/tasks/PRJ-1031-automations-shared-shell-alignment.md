# Task

## Header
- ID: PRJ-1031
- Title: Align automations route with shared module shell components
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1030
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1031
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1030 selected `/automations` shared-shell alignment because the route still
had inline overview/stat wrappers that match existing shared module components.
Health-derived scheduler and attention data remain route-owned in `App()`.

## Goal
Reuse existing shared module shell components in `/automations` without
changing scheduler, attention, health, API, or state behavior.

## Scope
- `web/src/App.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: `/automations` shell presentation was disconnected
  from the shared module route pattern.
- Expected product or reliability outcome: route shell ownership is more
  consistent across module routes.
- How success will be observed: build and 14-route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified automations shared-shell alignment with docs and context synced.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep health/scheduler/attention data derivation in `App()`

## Implementation Plan
1. Replace inline automations overview bar with `ModuleOverviewBar`.
2. Replace inline automations stat-row wrapper with `ModuleStatRow`.
3. Keep automation stat cards, flow rows, side panels, health-derived values,
   and scheduler summary in `App()`.
4. Update frontend docs, roadmap, task board, and project state.
5. Run build, route smoke, and diff validation.

## Acceptance Criteria
- Existing `aion-automations-overview-*` and `aion-automations-stat-*`
  selectors remain available through shared route-keyed components.
- Health-derived scheduler and attention data remain in `App()`.
- `npm run build`, `npm run smoke:routes`, and `git diff --check` pass.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a frontend refactor slice.
- [x] Shared automations shell components are used.
- [x] Route behavior and health-derived data ownership are unchanged.
- [x] Relevant docs and context updated.
- [x] Validation evidence recorded.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - `git diff --check`
- Manual checks:
  - confirmed shared route keys preserve automations CSS selectors
- High-risk checks:
  - no API, health, scheduler, auth, persistence, or deployment code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - audit next route/helper cleanup target after automations shell alignment

## Notes
This is presentation-only. It intentionally defers `conversationChannelStatus`
and any health/scheduler helper movement.

## Result Report

- Task summary: aligned `/automations` overview and stat row with shared module
  shell components.
- Files changed:
  - `web/src/App.tsx`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `npm run build`
  - `npm run smoke:routes`
  - `git diff --check`
- What is incomplete:
  - health/helper ownership remains a later audited slice
- Next steps:
  - audit next cleanup target after automations shared-shell alignment
- Decisions made:
  - reuse existing shared components instead of adding automations-specific
    components

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - automations route repeated shell wrappers already solved elsewhere
- Gaps:
  - route shell alignment was incomplete for `/automations`
- Inconsistencies:
  - similar routes used shared overview/stat wrappers while automations did not
- Architecture constraints:
  - health-derived scheduler posture remains route-owned in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1031 automations shared-shell alignment
- Priority rationale:
  - low-risk follow-up from PRJ-1030
- Why other candidates were deferred:
  - health helper movement and decorative panels need separate audit

### 3. Plan Implementation
- Files or surfaces to modify:
  - `App.tsx`, frontend docs, context
- Logic:
  - route-keyed shared component usage only
- Edge cases:
  - preserve route-specific CSS selectors

### 4. Execute Implementation
- Implementation notes:
  - replaced overview and stat wrappers

### 5. Verify and Test
- Validation performed:
  - frontend build
  - route smoke
  - diff check
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - leave automations untouched, but it had a direct shared component fit
- Technical debt introduced: no
- Scalability assessment:
  - keeps health-adjacent route shell aligned without touching health logic
- Refinements made:
  - kept all automation card data arrays in `App()`

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, route component map, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
