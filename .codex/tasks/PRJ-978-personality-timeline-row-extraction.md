# Task

## Header
- ID: PRJ-978
- Title: Extract personality timeline row component from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-977
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 978
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PersonalityTimelineRow` is a pure row component used across memory,
reflections, plans, and personality routes. It remained embedded in
`web/src/App.tsx` after earlier shell and chat extractions.

## Goal

Move `PersonalityTimelineRow` into a personality component module without
changing learned-state derivation or route behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/personality.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: a shared personality timeline row was hidden in
  the app monolith.
- Expected product or reliability outcome: shared personality presentation has
  a clear owner while learned-state logic remains unchanged.
- How success will be observed: build and route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `PersonalityTimelineRow` to `web/src/components/personality.tsx`.

## Constraints
- use existing systems and approved mechanisms
- do not move learned-state derivation out of `App()`
- do not alter markup, copy, route behavior, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `web/src/components/personality.tsx`.
2. Move `PersonalityTimelineRow` unchanged into that module.
3. Import `PersonalityTimelineRow` from `App.tsx`.
4. Run web build and route smoke.
5. Update docs and context.

## Acceptance Criteria
- `PersonalityTimelineRow` no longer lives in `App.tsx`.
- `web/src/components/personality.tsx` owns the row component.
- Existing route usages still render through the imported component.
- `npm run build` passes.
- `npm run smoke:routes` passes.

## Definition of Done
- [x] Timeline row extracted.
- [x] Learned-state logic remains in `App()`.
- [x] Behavior-preserving validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - confirmed `App.tsx` imports `PersonalityTimelineRow` and no longer defines
    it
- Screenshots/logs:
  - no screenshots; no visible behavior intentionally changed
- High-risk checks:
  - learned-state row derivation was untouched
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - route map now records `PersonalityTimelineRow` under personality component
    ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing personality timeline row markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: exact existing row markup/classes
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: route-local views still live in `App.tsx`
- State checks: success
- Feedback locality checked: unchanged
- Raw technical errors hidden from end users: unchanged
- Responsive checks: route smoke only
- Input-mode checks: unchanged
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: move `PersonalityTimelineRow` back into `App.tsx`
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

## Notes

This task intentionally keeps derived timeline row data in `App()` and moves
only the row renderer.

## Production-Grade Required Contract

- Goal: clarify personality presentation ownership.
- Scope: `PersonalityTimelineRow` only.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: see below.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: unchanged
- DB schema and migrations verified: not applicable
- Loading state verified: unchanged
- Error state verified: unchanged
- Refresh/restart behavior verified: route smoke starts fresh per run
- Regression check performed: yes

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: future frontend maintainers and agents
- Existing workaround or pain: shared timeline row embedded in monolith
- Smallest useful slice: one pure row component
- Success metric or signal: build and route smoke pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: personality and learned-state routes
- SLI: route smoke pass rate
- SLO: route smoke remains green after extraction
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: route smoke JSON output
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert personality row extraction

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: no data changed
- Trust boundaries: unchanged
- Permission or ownership checks: unchanged
- Abuse cases: not applicable
- Secret handling: no secrets touched
- Security tests or scans: not applicable
- Fail-closed behavior: unchanged
- Residual risk: route-local view bodies still remain in `App.tsx`

## Result Report

- Task summary: moved `PersonalityTimelineRow` into
  `web/src/components/personality.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/personality.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - route-local view bodies still live in `App.tsx`
- Next steps:
  - extract a small route summary/card cluster or begin route-module
    extraction with stronger route coverage
- Decisions made:
  - keep learned-state row construction in `App()` and move only the row
    renderer

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `PersonalityTimelineRow` remained in `App.tsx`.
- Gaps: personality route module ownership is still partial.
- Inconsistencies: shared learned-state row presentation had no module owner.
- Architecture constraints: keep learned-state derivation unchanged.

### 2. Select One Priority Task
- Selected task: PRJ-978 personality timeline row extraction.
- Priority rationale: small pure presentational extraction used by several
  learned-state routes.
- Why other candidates were deferred: full route-module extraction has broader
  state and route coverage risk.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/personality.tsx`,
  docs/context.
- Logic: move `PersonalityTimelineRow` unchanged and import it.
- Edge cases: duplicate timeline token labels remain unchanged.

### 4. Execute Implementation
- Implementation notes: extracted only stateless row markup.

### 5. Verify and Test
- Validation performed: web build and route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave row in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: personality component ownership can now grow
  gradually.
- Refinements made: avoided moving learned-state data construction.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
