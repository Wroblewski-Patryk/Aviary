# Task

## Header
- ID: PRJ-982
- Title: Extract route note/side-card component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-981
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 982
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Insights, automations, and integrations use the same `aion-*-note-card`
presentational structure inside `web/src/App.tsx`. Full route smoke now covers
all affected routes.

## Goal

Move the matching route note-card markup into a shared component while
preserving route-specific CSS class names and route data ownership.

## Scope

- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated note-card markup was scattered across
  route render branches.
- Expected product or reliability outcome: matching route note cards have a
  shared renderer while route-specific classes remain intact.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `RouteNoteCard` into `web/src/components/shared.tsx` and use it for
insights, automations, and integrations note-card clusters.

## Constraints
- use existing systems and approved mechanisms
- do not move route data derivation out of `App()`
- preserve route-specific CSS class names
- do not alter route behavior, labels, values, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `RouteNoteCard` to `web/src/components/shared.tsx`.
2. Replace matching `aion-*-note-card` markup in `App.tsx`.
3. Leave non-matching prompt/step/signal card patterns untouched.
4. Run web build and full route smoke.
5. Update docs and context.

## Acceptance Criteria
- Matching note-card markup is replaced by `RouteNoteCard`.
- Route-specific `aion-*-note-*` class names remain unchanged.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Shared note-card component extracted.
- [x] Route data derivation remains in `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed only matching `aion-*-note-card` clusters were extracted
- High-risk checks:
  - prompt/step/signal card variants were left untouched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates:
  - route map now records `RouteNoteCard` under shared presentational panels

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing route note-card markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Existing shared pattern reused: exact existing route note-card class names
- New shared pattern introduced: no
- Remaining mismatches: route-local view bodies still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: inline note-card markup back into `App.tsx`
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

- Task summary: moved matching route note-card markup into `RouteNoteCard`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/shared.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - non-matching prompt, step, and signal card variants remain route-local
- Next steps:
  - extract a route activity-row cluster or remove confirmed dead components
- Decisions made:
  - extract only exact `aion-*-note-card` matches

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: matching note-card markup existed in three route branches.
- Gaps: route-local view bodies remain large.
- Inconsistencies: matching note-card structures had no shared owner.
- Architecture constraints: keep route data derivation unchanged.

### 2. Select One Priority Task
- Selected task: PRJ-982 route note-card extraction.
- Priority rationale: small repeated component protected by full route smoke.
- Why other candidates were deferred: non-matching side cards need separate
  component contracts.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/shared.tsx`, docs/context.
- Logic: use `RouteNoteCard` with route-specific class prefix.
- Edge cases: routeKey preserves existing CSS selectors.

### 4. Execute Implementation
- Implementation notes: extracted only exact matching markup.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave repeated markup.
- Technical debt introduced: no
- Scalability assessment: note-card ownership is now clearer.
- Refinements made: kept prompt/step/signal variants out of scope.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
