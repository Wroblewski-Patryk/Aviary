# Task

## Header
- ID: PRJ-1099
- Title: Extract shell nav button list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1098
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1099
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1098` selected the desktop sidebar nav map as the next smallest shell
cleanup. Route state and navigation callbacks remain owned by `App()`.

## Goal
Move desktop sidebar nav button-list presentation into the existing shell
component owner without changing route state, route labels, disabled behavior,
or navigation semantics.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `ShellNavButtonItem` and `ShellNavButtonList` to
   `web/src/components/shell.tsx`.
2. Type `shellNavItems` with `ShellNavButtonItem<RoutePath>` in `App.tsx`.
3. Replace the inline desktop sidebar nav map with `ShellNavButtonList`.
4. Keep `route`, `changeRoute`, and nav item data in `App()`.
5. Sync docs/context.
6. Run frontend build, route smoke, and diff validation sequentially.

## Acceptance Criteria
- [x] `App.tsx` no longer maps `shellNavItems` inline for the desktop sidebar.
- [x] Existing `aion-sidebar-nav` wrapper and `ShellNavButton` behavior are
  preserved.
- [x] Route state and `changeRoute` remain in `App()`.
- [x] Frontend validation passes.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` was considered for the task size.
- [x] Implementation is tiny, testable, and reversible.
- [x] No temporary solutions, mocks, bypasses, or duplicated logic were added.
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
  - `docs/architecture/02_architecture.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing desktop sidebar nav
- Fidelity target: structurally_faithful
- Existing shared pattern reused: authenticated shell component owner
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; markup-only extraction covered by
  build and route smoke
- Remaining mismatches: none introduced

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `ShellNavButtonList` usage and docs/context updates

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report
- Task summary: added `ShellNavButtonList` and reused it for desktop sidebar
  nav buttons.
- Files changed:
  - `.codex/tasks/PRJ-1099-shell-nav-button-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/shell.tsx`
- How tested: frontend build, route smoke, and diff check passed.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep route state, route data, and route navigation callback
  in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: desktop sidebar nav map was inline in `App.tsx`.
- Gaps: shell component owner had individual nav buttons but no list wrapper.
- Inconsistencies: no behavior inconsistency; only presentation ownership.
- Architecture constraints: keep route state and navigation in `App()`.

### 2. Select One Priority Task
- Selected task: extract `ShellNavButtonList`.
- Priority rationale: small shell-owned wrapper around existing button
  component selected by `PRJ-1098`.
- Why other candidates were deferred: mobile tabbar owns refs, settings options
  are form-control details, tools directory is side-effectful, and projections
  are data shaping.

### 3. Plan Implementation
- Files or surfaces to modify: `shell.tsx`, `App.tsx`, docs/context.
- Logic: render sidebar nav wrapper and buttons from typed items with active
  route and route-change callback.
- Edge cases: avoid route callback when an item lacks `route`; preserve disabled
  prop.

### 4. Execute Implementation
- Implementation notes: `ShellNavButtonList` delegates individual buttons to
  existing `ShellNavButton`.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave the desktop nav map inline.
- Technical debt introduced: no
- Scalability assessment: route generic keeps the component reusable without
  importing route constants into shell components.
- Refinements made: removed stale `SidebarIconKind` import from `App.tsx`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
