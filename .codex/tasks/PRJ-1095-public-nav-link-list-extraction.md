# Task

## Header
- ID: PRJ-1095
- Title: Extract public nav link list
- Task Type: refactor
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1094
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1095
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-1094` selected the public-home nav link map as the next smallest
presentation cleanup. Public copy/data remains owned by `App()`.

## Goal
Move public nav link presentation into the existing public-shell component owner
without changing link labels or target behavior.

## Scope
- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `docs/frontend/app-route-cluster-audit.md`
- `docs/frontend/route-component-map.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Implementation Plan
1. Add `PublicNavLinkList` to `web/src/components/public-shell.tsx`.
2. Replace the inline `publicHomeSurface.nav.map(...)` in `App.tsx`.
3. Keep public copy/data in `App()`.
4. Sync docs/context.
5. Run frontend build, route smoke, and diff validation.

## Acceptance Criteria
- [x] `App.tsx` no longer maps public nav links inline.
- [x] Existing `aion-public-nav-links` and `aion-public-nav-link` selectors are preserved.
- [x] Existing `#aviary-home` link target is preserved.
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
- Design source reference: existing public-home nav implementation
- Fidelity target: structurally_faithful
- Existing shared pattern reused: public-shell component owner
- New shared pattern introduced: no
- Screenshot comparison pass completed: no; markup-only extraction covered by build and route smoke
- Remaining mismatches: none introduced

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert `PublicNavLinkList` usage and docs/context updates

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
- Task summary: added `PublicNavLinkList` and reused it for public home nav links.
- Files changed:
  - `.codex/tasks/PRJ-1095-public-nav-link-list-extraction.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `web/src/App.tsx`
  - `web/src/components/public-shell.tsx`
- How tested: frontend build, route smoke, and diff check passed.
- What is incomplete: nothing known.
- Next steps: audit the next smallest frontend cleanup.
- Decisions made: keep public-home copy/data in `App()`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: public nav link map was inline in `App.tsx`.
- Gaps: public-shell owner lacked a nav-link list wrapper.
- Inconsistencies: no runtime inconsistency; only presentation ownership.
- Architecture constraints: keep public copy/data in `App()`.

### 2. Select One Priority Task
- Selected task: extract `PublicNavLinkList`.
- Priority rationale: smallest display-only extraction selected by `PRJ-1094`.
- Why other candidates were deferred: tools directory, shell account facts, form options, route navigation, and data projections have broader ownership.

### 3. Plan Implementation
- Files or surfaces to modify: `public-shell.tsx`, `App.tsx`, docs/context.
- Logic: render existing nav wrapper and anchors from public nav labels.
- Edge cases: preserve `#aviary-home` target as default prop.

### 4. Execute Implementation
- Implementation notes: `PublicNavLinkList` renders existing wrapper and anchor classes; `App.tsx` passes `publicHomeSurface.nav`.

### 5. Verify and Test
- Validation performed: frontend build, route smoke, diff check.
- Result: passed; build completed, route smoke reported `status=ok` with
  `route_count=14`, and diff check returned exit code 0.

### 6. Self-Review
- Simpler option considered: leave the nav map inline.
- Technical debt introduced: no
- Scalability assessment: public-specific wrapper avoids shell-wide nav abstraction.
- Refinements made: target href is explicit and defaults to the existing value.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/app-route-cluster-audit.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
