# Task

## Header
- ID: PRJ-984
- Title: Extract tool route helper logic from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-983
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 984
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Tool status, link-state, and next-action formatting helpers were still defined
inside `web/src/App.tsx`, even though they are pure tools/integrations route
logic.

## Goal

Move tool formatting helpers into a dedicated frontend library module without
changing tools or integrations route behavior.

## Scope

- `web/src/App.tsx`
- `web/src/lib/tool-formatting.ts`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: tools route formatting logic was hidden in the app
  monolith.
- Expected product or reliability outcome: tool formatting has a small explicit
  owner and `App.tsx` is less coupled.
- How success will be observed: build and full route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `toolStatusClass`, `formatToolState`, `formatToolLinkState`, and
`summarizeToolAction` to `web/src/lib/tool-formatting.ts`.

## Constraints
- use existing systems and approved mechanisms
- do not move tools route state or API calls out of `App()`
- do not import `UI_COPY` into the helper module
- do not alter labels, status mapping, or route behavior
- do not open a visible browser window

## Implementation Plan
1. Add `web/src/lib/tool-formatting.ts`.
2. Move pure formatting helpers into that module.
3. Use a small structural `ToolFormattingCopy` type instead of importing
   `UI_COPY`.
4. Import helpers from `App.tsx`.
5. Run web build and full route smoke.
6. Update docs and context.

## Acceptance Criteria
- Tool formatting helpers no longer live in `App.tsx`.
- `web/src/lib/tool-formatting.ts` owns the helpers.
- Tools and integrations routes still render through the imported helpers.
- `npm run build` passes.
- `npm run smoke:routes` passes with `route_count=14`.

## Definition of Done
- [x] Tool formatting helpers extracted.
- [x] Tools route state and API behavior remain in `App()`.
- [x] Full route smoke validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
- Manual checks:
  - confirmed `App.tsx` imports helpers from `tool-formatting.ts`
- High-risk checks:
  - status/link mappings are unchanged
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
  - route map now records tools formatting helper ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing tools route behavior
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Remaining mismatches: tools item rendering still lives in `App.tsx`
- State checks: success
- Responsive checks: route smoke only
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Rollback note: move helpers back into `App.tsx`
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

- Task summary: moved tools route formatting helpers into
  `web/src/lib/tool-formatting.ts`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/lib/tool-formatting.ts`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - tools item rendering still lives in `App.tsx`
- Next steps:
  - extract tools summary card or tools item fact-card cluster
- Decisions made:
  - use a structural copy type instead of importing `UI_COPY`

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: pure tools formatting helpers remained in `App.tsx`.
- Gaps: tools route rendering remains large.
- Inconsistencies: tool formatter ownership was not separated from route state.
- Architecture constraints: keep API/state in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-984 tool route helper extraction.
- Priority rationale: pure logic extraction before larger tools component work.
- Why other candidates were deferred: tools item component extraction has more
  interaction state coupling.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `lib/tool-formatting.ts`,
  docs/context.
- Logic: move pure formatting helpers unchanged.
- Edge cases: unknown statuses keep existing fallback labels/classes.

### 4. Execute Implementation
- Implementation notes: helpers now use `ToolFormattingCopy`.

### 5. Verify and Test
- Validation performed: web build and full route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave helpers in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: tools formatting logic can now be tested or reused
  independently.
- Refinements made: avoided coupling helper module to `UI_COPY`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
