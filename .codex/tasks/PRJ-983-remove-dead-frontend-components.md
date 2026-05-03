# Task

## Header
- ID: PRJ-983
- Title: Remove or relocate dead frontend component definitions
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-982
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 983
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

After several component extractions, `web/src/App.tsx` still contained
component-shaped definitions that needed a live-use audit before being moved or
removed.

## Goal

Confirm component definitions that still live in `App.tsx`, relocate live
public-shell ownership, and remove only genuinely unused code.

## Scope

- `web/src/App.tsx`
- `web/src/components/public-shell.tsx`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: dead component definitions made frontend ownership
  harder to read.
- Expected product or reliability outcome: `App.tsx` no longer carries unused
  component definitions.
- How success will be observed: search confirms no live references and build
  plus full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Move live `MotifFigurePanel` into `web/src/components/public-shell.tsx` and
remove unused `PersonalityLayerCard` from `web/src/App.tsx`.

## Constraints
- use existing systems and approved mechanisms
- confirm current `web/src` references before removal or relocation
- do not remove CSS or historical docs in this task
- do not alter live route behavior
- do not open a visible browser window

## Implementation Plan
1. Search `web/src` for `MotifFigurePanel` and `PersonalityLayerCard`.
2. Relocate live `MotifFigurePanel` to the public-shell module.
3. Remove `PersonalityLayerCard` only if it has no live uses.
4. Run web build and full route smoke.
5. Update planning and context docs.

## Acceptance Criteria
- `MotifFigurePanel` is imported from `web/src/components/public-shell.tsx`.
- Search confirms `PersonalityLayerCard` has no live `web/src` references.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Live public component relocated.
- [x] Dead component definition removed.
- [x] Live-use search completed.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - public route smoke caught that `MotifFigurePanel` was live
  - `PersonalityLayerCard` has no live `web/src` references
- High-risk checks:
  - no CSS or route render branches were removed
  - public route smoke passes after relocation
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - roadmap now records this cleanup as done

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing live routes
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Remaining mismatches: route-local view bodies still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged live markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: restore removed unused definitions if needed
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

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

- Task summary: moved live `MotifFigurePanel` into
  `web/src/components/public-shell.tsx` and removed unused
  `PersonalityLayerCard` from `web/src/App.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/public-shell.tsx`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - route-local view bodies still live in `App.tsx`
- Next steps:
  - extract tool helper logic or route activity-row clusters behind full route
    smoke
- Decisions made:
  - relocate live public-shell code and remove only confirmed dead code

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: component ownership needed live-use confirmation after extraction.
- Gaps: route-local view bodies remain large.
- Inconsistencies: initial search missed root `web/src/App.tsx`; public route
  smoke caught the live `MotifFigurePanel` reference.
- Architecture constraints: do not invent component modules for dead code.

### 2. Select One Priority Task
- Selected task: PRJ-983 dead frontend component cleanup.
- Priority rationale: prevents carrying stale component ownership forward.
- Why other candidates were deferred: further extraction is clearer after dead
  code is removed.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, roadmap, context.
- Logic: relocate live public-shell code and remove only definitions with no
  live references.
- Edge cases: public route smoke must remain green.

### 4. Execute Implementation
- Implementation notes: moved `MotifFigurePanel` to `public-shell.tsx` and
  removed `PersonalityLayerCard`.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: move dead components to modules.
- Technical debt introduced: no
- Scalability assessment: frontend ownership map is cleaner.
- Refinements made: corrected the initial live-use assumption after smoke
  evidence and left CSS untouched because removing unused styling is a separate
  visual-risk task.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
