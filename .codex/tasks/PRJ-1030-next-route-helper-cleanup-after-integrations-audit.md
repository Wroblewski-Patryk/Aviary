# Task

## Header
- ID: PRJ-1030
- Title: Audit next frontend route/helper cleanup after integrations shell alignment
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1029
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1030
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-1029 aligned `/integrations` overview, stat row, and readiness rows with
existing shared module shell components while leaving provider semantics in
`App()`. The next cleanup choice should avoid broad provider/health helper
movement unless the evidence shows it is the lowest-risk slice.

## Goal
Select the next frontend route/helper cleanup target after integrations shell
alignment.

## Scope
- `web/src/App.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: route-local shell wrappers remain uneven across
  module routes.
- Expected product or reliability outcome: the next task reduces frontend
  architectural drift without changing runtime/provider semantics.
- How success will be observed: docs select one next implementation task.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting the next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep health/provider semantics in `App()` unless a later audit proves a safe
  helper boundary

## Implementation Plan
1. Inspect remaining `/automations`, `/integrations`, memory, and health helper
   candidates.
2. Compare candidates by behavior risk and existing shared component fit.
3. Select one next implementation slice.
4. Update frontend docs, roadmap, and context files.
5. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- Deferred candidates and reasons are documented.
- The selected task can be validated with build and route smoke.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed `/automations` inline overview/stat wrappers and remaining
    provider/helper candidates
- High-risk checks:
  - no runtime code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - add PRJ-1031 as automations shared-shell alignment

## Notes
Selected next task:
- PRJ-1031: align `/automations` with existing `ModuleOverviewBar` and
  `ModuleStatRow`.

Deferred:
- `conversationChannelStatus` because it encodes health/channel semantics.
- integrations provider rows because they include route-specific provider-map
  list shape and fallback behavior.
- memory signal cards because they are currently a single-route `meta` shape.
- decorative route panels because they need separate visual audits.

## Result Report

- Task summary: selected `/automations` shared-shell alignment as the next
  frontend v1 architecture slice.
- Files changed:
  - `.codex/tasks/PRJ-1030-next-route-helper-cleanup-after-integrations-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is deferred to PRJ-1031
- Next steps:
  - implement `/automations` shared-shell alignment
- Decisions made:
  - defer health/provider helper extraction

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - `/automations` still has inline module-shell wrappers
- Gaps:
  - no current task points to the next low-risk post-integrations cleanup
- Inconsistencies:
  - similar routes now use shared overview/stat wrappers while automations does
    not
- Architecture constraints:
  - health-derived scheduler posture remains route-owned in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1030 audit next cleanup target
- Priority rationale:
  - selects a low-risk implementation step before provider/health helper work
- Why other candidates were deferred:
  - they are either semantically richer or single-route shapes

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select next implementation task
- Edge cases:
  - avoid mixing shell extraction with health helper movement

### 4. Execute Implementation
- Implementation notes:
  - selected PRJ-1031

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - skip another shell alignment, but automations has the clearest remaining
    shared component fit
- Technical debt introduced: no
- Scalability assessment:
  - aligns another health-adjacent route without touching health semantics
- Refinements made:
  - explicitly deferred `conversationChannelStatus`

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
