# Task

## Header
- ID: PRJ-1097
- Title: Extract shell account fact list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1096
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1097
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1096` selected the repeated shell account facts as the next smallest
frontend cleanup. Desktop and mobile account panels use the same `label/value`
data but different wrappers.

## Goal
Move account fact presentation into the existing shell component owner while
keeping account data, account panel state, route navigation, and sign-out
actions in `App()`.

## Scope
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `ShellAccountFactList` to `web/src/components/shell.tsx`.
2. Replace desktop account popover fact map in `App.tsx`.
3. Replace mobile account panel fact map in `App.tsx`.
4. Keep account data and actions in `App()`.
5. Sync docs/context.
6. Run frontend build, route smoke, and diff validation.

## Acceptance Criteria
- [x] `App.tsx` no longer maps `accountSummaryItems` for account facts inline.
- [x] Desktop account fact classes are preserved.
- [x] Mobile account fact classes are preserved.
- [x] Account actions and panel state remain in `App()`.
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
- Result: passed after sequential validation; build completed, route smoke
  reported `status=ok` with `route_count=14`, and diff check returned exit
  code 0. The first parallel route-smoke attempt hit a build/smoke race on
  `web/dist/index.html`, so the learning journal now records the sequential
  validation guardrail.

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
- Design source reference: existing shell account fact renderings
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
- Rollback note: revert `ShellAccountFactList` usage and docs/context updates

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
- Task summary: added `ShellAccountFactList` and reused it for desktop and
  mobile account fact displays.
- Files changed:
  - `.codex/tasks/PRJ-1097-shell-account-fact-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/shell.tsx`
- How tested: frontend build, route smoke, and diff check passed after rerunning
  route smoke sequentially after build.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep account data, panel state, route navigation, and actions
  in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: account facts were repeated inline in desktop and mobile account
  panels.
- Gaps: shell component owner lacked a fact-list wrapper.
- Inconsistencies: no behavior inconsistency; only repeated presentation.
- Architecture constraints: keep state and actions in `App()`.

### 2. Select One Priority Task
- Selected task: extract `ShellAccountFactList`.
- Priority rationale: small repeated display-only shell presentation selected
  by `PRJ-1096`.
- Why other candidates were deferred: route navigation controls, form option
  maps, tools directory, and data projections have broader ownership.

### 3. Plan Implementation
- Files or surfaces to modify: `shell.tsx`, `App.tsx`, docs/context.
- Logic: render the same account facts using `popover` and `mobile` variants.
- Edge cases: preserve both wrapper classes and leave actions outside the list.

### 4. Execute Implementation
- Implementation notes: `ShellAccountFactList` defaults to the desktop popover
  rendering and accepts `variant="mobile"` for the mobile panel.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed after sequential validation; build completed, route smoke
  reported `status=ok` with `route_count=14`, and diff check returned exit
  code 0.

### 6. Self-Review
- Simpler option considered: keep both maps inline.
- Technical debt introduced: no
- Scalability assessment: shell-specific variant keeps the abstraction bounded.
- Refinements made: no action buttons moved into the component.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: yes.
