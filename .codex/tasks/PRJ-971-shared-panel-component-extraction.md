# Task

## Header
- ID: PRJ-971
- Title: Extract first shared panel components from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-967
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 971
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-967` moved route ownership into `web/src/routes.ts`, but
`web/src/App.tsx` still owns most render helpers and route-local UI. The next
safe slice is a tiny presentation-only extraction behind the route smoke added
in `PRJ-966`.

## Goal

Move the first shared presentation components out of `App.tsx` without
changing route behavior, API usage, state ownership, or visual styling.

## Scope

- `web/src/App.tsx`
- `web/src/components/shared.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: shared shell UI was hidden inside the large app
  file.
- Expected product or reliability outcome: low-risk shared panels have a small
  owner module and future route extraction has a tested precedent.
- How success will be observed: web build and route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `StatePanel` and `FeedbackBanner` into a shared component module.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new styling patterns
- do not change route rendering, data loading, or auth behavior
- do not open a visible browser window
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add `web/src/components/shared.tsx`.
2. Move `StatePanel` and `FeedbackBanner` unchanged into the shared module.
3. Import the components from `App.tsx`.
4. Run web build and headless route smoke.
5. Update route/component map, roadmap, task board, and project state.

## Acceptance Criteria
- `StatePanel` and `FeedbackBanner` no longer live in `App.tsx`.
- Shared component module owns those panels.
- `npm run build` passes.
- `npm run smoke:routes` passes.
- Docs record the new shared component owner and remaining monolith gap.

## Definition of Done
- [x] Shared components extracted.
- [x] Behavior-preserving validation completed.
- [x] Docs and context updated.
- [x] Remaining route-rendering extraction gap stays explicit.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - reviewed diff to confirm the components were moved without behavior logic
    changes
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
  - route map now names `web/src/components/shared.tsx` as the shared panel
    owner

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing shared panel components
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

This intentionally avoids extracting route-local components or state. The next
slice should move one additional pure shared shell cluster or one low-risk
route view behind the same smoke gate.

## Production-Grade Required Contract

- Goal: start component ownership extraction behind route smoke.
- Scope: two shared presentation components only.
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
- Smallest useful slice: two presentation-only components
- Success metric or signal: build and route smoke pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: route entry and shell feedback surfaces
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

- Task summary: moved `StatePanel` and `FeedbackBanner` into
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
  - extract another pure shared shell cluster or one low-risk route view
- Decisions made:
  - keep markup/classes unchanged to avoid visual behavior drift

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `App.tsx` still owned shared presentation helpers.
- Gaps: no component extraction precedent beyond routes.
- Inconsistencies: route map did not yet name a shared component owner.
- Architecture constraints: preserve route behavior and shell visuals.

### 2. Select One Priority Task
- Selected task: PRJ-971 shared panel component extraction.
- Priority rationale: smallest safe component split after route ownership.
- Why other candidates were deferred: route-local extraction has higher state
  and visual risk.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, new shared component module,
  docs/context.
- Logic: move pure components unchanged and import them.
- Edge cases: keep loading, success, and error panel rendering unchanged.

### 4. Execute Implementation
- Implementation notes: moved only `StatePanel` and `FeedbackBanner`.

### 5. Verify and Test
- Validation performed: web build and route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave all panels in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: the shared module can host further pure shell
  components if they remain behavior-free.
- Refinements made: kept route-local views out of scope.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
