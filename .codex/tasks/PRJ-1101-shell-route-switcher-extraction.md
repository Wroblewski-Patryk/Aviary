# Task

## Header
- ID: PRJ-1101
- Title: Extract shell route switcher
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1100
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1101
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1100` selected the non-ref route-header switcher as the next smallest shell
cleanup. The bottom mobile tabbar remains in `App()` because it owns scroll
refs.

## Goal
Move route-header switcher presentation into the existing shell component owner
without changing route state, labels, or navigation callback ownership.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `ShellRouteSwitcher` to `web/src/components/shell.tsx`.
2. Replace the route-header `ROUTES.map(...)` in `App.tsx`.
3. Keep `ROUTES`, `route`, `routeLabel`, `resolvedUiLanguage`, and
   `changeRoute` in `App()`.
4. Sync docs/context.
5. Run frontend build, route smoke, and diff validation sequentially.

## Acceptance Criteria
- [x] `App.tsx` no longer maps the route-header switcher inline.
- [x] Existing wrapper, scroll row, and button classes are preserved.
- [x] Route state, labels, and navigation callback remain in `App()`.
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
- Design source reference: existing route-header switcher
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
- Rollback note: revert `ShellRouteSwitcher` usage and docs/context updates

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
- Task summary: added `ShellRouteSwitcher` and reused it for the route-header
  switcher.
- Files changed:
  - `.codex/tasks/PRJ-1101-shell-route-switcher-extraction.md`
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
- Decisions made: keep bottom mobile tabbar in `App()` because it owns refs.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: route-header switcher map was inline in `App.tsx`.
- Gaps: shell component owner lacked a non-ref route switcher wrapper.
- Inconsistencies: no behavior inconsistency; only shell presentation ownership.
- Architecture constraints: keep route state, route labels, and route changes in
  `App()`.

### 2. Select One Priority Task
- Selected task: extract `ShellRouteSwitcher`.
- Priority rationale: small route-control wrapper without refs selected by
  `PRJ-1100`.
- Why other candidates were deferred: bottom mobile tabbar owns refs, settings
  options are form-control details, tools directory is side-effectful, and data
  projections are not presentation work.

### 3. Plan Implementation
- Files or surfaces to modify: `shell.tsx`, `App.tsx`, docs/context.
- Logic: render existing wrapper, scroll row, and route buttons from callback
  props.
- Edge cases: preserve active button classes and route callback.

### 4. Execute Implementation
- Implementation notes: `ShellRouteSwitcher` receives labels through
  `labelForRoute` so shell does not own route copy or language.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave the switcher inline.
- Technical debt introduced: no
- Scalability assessment: route generic keeps shell independent of route
  constants.
- Refinements made: bottom mobile tabbar remained in `App()` due to refs.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
