# Task

## Header
- ID: PRJ-1028
- Title: Audit next frontend v1 architecture slice after dot-row extraction
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1027
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 1028
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The module-route cleanup has extracted shared overview, stat, activity,
text-card, and dot-row presentation for the core learned-state routes.
`/integrations` still has inline overview/stat/health-row presentation even
though equivalent shared route-keyed components now exist.

## Goal
Choose the next frontend v1 architecture slice after `ModuleDotRowList` without
touching provider readiness semantics or health/tool data ownership.

## Scope
- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: `/integrations` presentation is still less aligned
  with the shared module route shell than similar routes.
- Expected product or reliability outcome: the next slice can reduce repeated
  presentation without changing provider behavior.
- How success will be observed: docs select one implementation task and defer
  higher-risk helper ownership.
- Post-launch learning needed: no

## Deliverable For This Stage
A completed audit selecting one next implementation task.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep provider/health/tool data derivation in `App()` for the next slice

## Implementation Plan
1. Inspect remaining `/integrations`, module UI, provider/health, and
   decorative route clusters.
2. Compare candidates by behavior risk and existing shared component coverage.
3. Select one next implementation slice.
4. Update frontend docs, roadmap, and context files.
5. Run `git diff --check`.

## Acceptance Criteria
- Exactly one next task is selected.
- Provider/health helper extraction is either selected with clear evidence or
  deferred with a reason.
- The next task has validation expectations.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for a docs-only planning slice.
- [x] Audit result recorded in frontend docs.
- [x] Task board and project state updated.
- [x] `git diff --check` passes.

## Validation Evidence
- Tests:
  - `git diff --check`
- Manual checks:
  - reviewed `/integrations` inline overview/stat/health rows and current
    shared components
- High-risk checks:
  - no runtime code changed

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - add PRJ-1029 as the next integrations shared-shell alignment task

## Notes
Selected next task:
- PRJ-1029: align `/integrations` with existing shared module shell components.

The selected slice should replace inline integrations overview/stat wrappers
and readiness dot rows with `ModuleOverviewBar`, `ModuleStatRow`, and
`ModuleDotRowList`, while preserving existing route-specific selectors and
keeping `integrationItems`, `integrationStatCards`, provider rows, and readiness
summary data in `App()`.

Deferred:
- `conversationChannelStatus` and provider/health helper movement because they
  encode route semantics and should be audited with integration/provider
  ownership.
- decorative provider-map web visual because it is route-specific and more
  visual-sensitive.
- memory signal card extraction because it is currently a single-route shape.

## Result Report

- Task summary: selected `/integrations` shared-shell alignment as the next
  frontend v1 architecture slice.
- Files changed:
  - `.codex/tasks/PRJ-1028-next-frontend-v1-slice-after-dot-row-audit.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - implementation is intentionally deferred to PRJ-1029
- Next steps:
  - implement shared-shell alignment for `/integrations`
- Decisions made:
  - defer provider/health helper movement

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - integrations route still repeats module-shell wrappers already extracted
- Gaps:
  - integration route docs do not yet record the next shared-shell alignment
- Inconsistencies:
  - similar module routes use shared components, while integrations still has
    local overview/stat wrappers
- Architecture constraints:
  - provider/tool truth remains backend-owned and route-derived in `App()`

### 2. Select One Priority Task
- Selected task:
  - PRJ-1028 audit next frontend v1 architecture slice
- Priority rationale:
  - it picks a low-risk slice before touching provider semantics
- Why other candidates were deferred:
  - helper movement and decorative panels are higher risk

### 3. Plan Implementation
- Files or surfaces to modify:
  - docs and context only
- Logic:
  - select the next task
- Edge cases:
  - avoid treating provider-ready semantics as presentation-only

### 4. Execute Implementation
- Implementation notes:
  - selected PRJ-1029

### 5. Verify and Test
- Validation performed:
  - `git diff --check`
- Result:
  - passed

### 6. Self-Review
- Simpler option considered:
  - continue extracting single-route memory cards, but integrations has more
    existing shared-component overlap
- Technical debt introduced: no
- Scalability assessment:
  - aligns another route to the shared module shell before broader route splits
- Refinements made:
  - provider helper extraction remains explicitly deferred

### 7. Update Documentation and Knowledge
- Docs updated:
  - route cluster audit, v1 roadmap
- Context updated:
  - task board, project state
- Learning journal updated: not applicable
