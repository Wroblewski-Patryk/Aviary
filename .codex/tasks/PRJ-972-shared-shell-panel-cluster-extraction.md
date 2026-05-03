# Task

## Header
- ID: PRJ-972
- Title: Extract next shared shell panel cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-971
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 972
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-971` established `web/src/components/shared.tsx` as the first shared
presentation owner. `App.tsx` still contained several pure shared panel
components that could move without touching state, data flow, or route copy.

## Goal

Move the next pure shared shell panel cluster into the shared component module
while preserving behavior and markup.

## Scope

- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: more shared shell components were hidden in
  `App.tsx`.
- Expected product or reliability outcome: shared route panels have clearer
  ownership before route-local extraction.
- How success will be observed: build and route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ModuleEntryCard`, `FlowRail`, `RouteHeroPanel`, and `InsightPanel` to
`web/src/components/shared.tsx`.

## Constraints
- use existing systems and approved mechanisms
- do not alter visual markup or CSS classes
- do not move route state or route-local data derivation
- do not open a visible browser window
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Move the four pure shared panel components into `components/shared.tsx`.
2. Import the components from `App.tsx`.
3. Run web build and headless route smoke.
4. Update docs and context with the new ownership split.

## Acceptance Criteria
- The four shared panel components no longer live in `App.tsx`.
- The shared component module exports them.
- `npm run build` passes.
- `npm run smoke:routes` passes.
- Documentation records remaining route-local monolith risk.

## Definition of Done
- [x] Shared shell panel cluster extracted.
- [x] Behavior-preserving validation completed.
- [x] Docs and context updated.
- [x] Remaining extraction target is explicit.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - confirmed `App.tsx` no longer defines `ModuleEntryCard`, `FlowRail`,
    `RouteHeroPanel`, or `InsightPanel`
- Screenshots/logs:
  - no screenshots; no visual behavior was intentionally changed
- High-risk checks:
  - route smoke proved root, login, dashboard, chat, personality, and tools
    still mount
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
  - route map now records the expanded shared panel owner

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing shared panel markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: exact existing panel markup/classes
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: route-local render sections still live in `App.tsx`
- State checks: success
- Feedback locality checked: unchanged
- Raw technical errors hidden from end users: unchanged
- Responsive checks: route smoke only
- Input-mode checks: not applicable
- Accessibility checks: unchanged markup
- Parity evidence: route smoke only

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: move the components back into `App.tsx`
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

This is still not route-local decomposition. It clears shared panel ownership
first so later route extraction can stay smaller.

## Production-Grade Required Contract

- Goal: continue component ownership extraction behind route smoke.
- Scope: pure shared panel cluster only.
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
- Existing workaround or pain: shared panels were embedded in the monolith
- Smallest useful slice: four presentation-only components
- Success metric or signal: build and route smoke pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: route entry and shell panels
- SLI: route smoke pass rate
- SLO: route smoke remains green after extraction
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: route smoke JSON output
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert component extraction

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
- Residual risk: route-local monolith still remains

## Result Report

- Task summary: moved four additional shared panel components into
  `web/src/components/shared.tsx`.
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
  - route-local components and route state remain mostly inside `App.tsx`
- Next steps:
  - extract shell chrome or a low-risk route-local component cluster
- Decisions made:
  - keep all props and markup unchanged to avoid visual drift

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: shared shell panels still lived in `App.tsx`.
- Gaps: route-local render extraction remains queued.
- Inconsistencies: route map needed a more accurate shared component owner.
- Architecture constraints: preserve route smoke and thin client behavior.

### 2. Select One Priority Task
- Selected task: PRJ-972 shared shell panel cluster extraction.
- Priority rationale: next smallest behavior-free split.
- Why other candidates were deferred: shell chrome extraction touches more
  props and icon types.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, shared component module, docs/context.
- Logic: move pure panel functions and import them.
- Edge cases: preserve `ReactNode` typing in the shared module.

### 4. Execute Implementation
- Implementation notes: moved `ModuleEntryCard`, `FlowRail`, `RouteHeroPanel`,
  and `InsightPanel`.

### 5. Verify and Test
- Validation performed: web build and route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: stop after PRJ-971.
- Technical debt introduced: no
- Scalability assessment: shared component ownership is now ready for shell
  chrome extraction.
- Refinements made: corrected `ModuleEntryCard` markup to match the exact
  source component before validation.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
