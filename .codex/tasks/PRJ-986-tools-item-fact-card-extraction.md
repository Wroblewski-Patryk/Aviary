# Task

## Header
- ID: PRJ-986
- Title: Extract tools item fact-card component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-985
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 986
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The tools route still rendered repeated item fact-card chrome inline in
`web/src/App.tsx`. The cards include availability, provider readiness, user
control, and link-state facts.

## Goal

Move the repeated tools fact-card shell into the tools component module without
changing tool toggle, link-state, provider, or availability behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: tools item facts were hidden in the app monolith.
- Expected product or reliability outcome: tools route presentation ownership
  is clearer while route behavior stays unchanged.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ToolsFactCard` to `web/src/components/tools.tsx` and use it for the
tools item fact cards.

## Constraints
- use existing systems and approved mechanisms
- do not move tools overview API calls or state out of `App()`
- do not alter labels, values, route behavior, link behavior, or visual classes
- keep toggle event handling in the existing route context
- do not open a visible browser window

## Implementation Plan
1. Add a small `ToolsFactCard` component that owns only fact-card chrome.
2. Replace the repeated fact-card wrappers in `App.tsx`.
3. Keep all tool facts, toggle handling, and link-state formatting at the
   current call site.
4. Run web build and full route smoke.
5. Update docs and context.

## Acceptance Criteria
- Tools item fact-card wrapper markup no longer repeats inline in `App.tsx`.
- `web/src/components/tools.tsx` owns `ToolsFactCard`.
- Toggle handling still lives in `App.tsx`.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Tools fact-card shell extracted.
- [x] Tools overview state, API, link, and toggle behavior remain in `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed `/tools` uses `ToolsFactCard`
- High-risk checks:
  - toggle `onChange`, saving state, and link-state formatting were not moved
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
  - route map now records tools fact-card ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing tools fact-card markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Remaining mismatches: tools detail cards still live in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged toggle/input markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: inline `ToolsFactCard` markup back into `App.tsx`
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

- Task summary: moved tools item fact-card chrome into
  `web/src/components/tools.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/tools.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - tools detail cards still live in `App.tsx`
- Next steps:
  - extract the tools detail-card component cluster
- Decisions made:
  - keep toggle and link-state behavior at the existing call site

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: tools item fact-card wrappers repeated inline.
- Gaps: tools detail cards remain inline.
- Inconsistencies: tools component ownership was partial after PRJ-985.
- Architecture constraints: keep tools state/API in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-986 tools item fact-card extraction.
- Priority rationale: small pure-presentational cleanup protected by full smoke.
- Why other candidates were deferred: detail cards are adjacent but separate
  from the toggle/link fact cluster.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/tools.tsx`, docs/context.
- Logic: move only the card wrapper and label.
- Edge cases: the control card contains the live toggle and must preserve its
  existing event handler.

### 4. Execute Implementation
- Implementation notes: extracted a `children`-based card shell and left all
  facts/actions at the call site.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave fact cards inline.
- Technical debt introduced: no
- Scalability assessment: tools route can continue shedding route-local
  presentation without moving behavior prematurely.
- Refinements made: avoided moving toggle handler.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
