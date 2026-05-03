# Task

## Header
- ID: PRJ-977
- Title: Extract chat flow stage component from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-976
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 977
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The chat route still had the pure `ChatFlowStage` presentational component in
`web/src/App.tsx`, even though route smoke coverage now protects chat route
mounting.

## Goal

Move `ChatFlowStage` into a chat component module without changing transcript,
composer, or chat send behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: chat flow presentation was still hidden inside the
  app monolith.
- Expected product or reliability outcome: first chat presentational component
  has a clear owner while chat state remains in `App()`.
- How success will be observed: build and route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ChatFlowStage` to `web/src/components/chat.tsx`.

## Constraints
- use existing systems and approved mechanisms
- do not move transcript, composer, send, or API state out of `App()`
- do not alter markup, copy, chat behavior, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `web/src/components/chat.tsx`.
2. Move `ChatFlowStage` unchanged into that module.
3. Import `ChatFlowStage` from `App.tsx`.
4. Run web build and route smoke.
5. Update docs and context.

## Acceptance Criteria
- `ChatFlowStage` no longer lives in `App.tsx`.
- `web/src/components/chat.tsx` owns `ChatFlowStage`.
- Chat route usage still renders through the imported component.
- `npm run build` passes.
- `npm run smoke:routes` passes.

## Definition of Done
- [x] Chat flow stage extracted.
- [x] Chat state and API behavior remain in `App()`.
- [x] Behavior-preserving validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - confirmed `App.tsx` imports `ChatFlowStage` and no longer defines it
- Screenshots/logs:
  - no screenshots; no visible behavior intentionally changed
- High-risk checks:
  - chat send/transcript logic was untouched
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
  - route map now records `ChatFlowStage` under chat component ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing chat flow stage markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: exact existing flow-stage markup/classes
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: chat transcript/composer and route-local views still
  live in `App.tsx`
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
- Rollback note: move `ChatFlowStage` back into `App.tsx`
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

This is the first chat component extraction. Chat state remains intentionally
centralized in `App()` until a larger route-module slice is selected.

## Production-Grade Required Contract

- Goal: clarify chat presentational component ownership.
- Scope: `ChatFlowStage` only.
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
- Existing workaround or pain: chat presentation embedded in monolith
- Smallest useful slice: one pure chat component
- Success metric or signal: build and route smoke pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: chat route entry
- SLI: route smoke pass rate
- SLO: route smoke remains green after extraction
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: route smoke JSON output
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert chat flow stage extraction

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
- Residual risk: transcript rendering and composer logic still remain in
  `App.tsx`

## Result Report

- Task summary: moved `ChatFlowStage` into `web/src/components/chat.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/chat.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - chat transcript/composer, auth modal, and route-local views still live in
    `App.tsx`
- Next steps:
  - extract a small personality timeline component or chat transcript helper
    cluster
- Decisions made:
  - keep chat state in `App()` and move only the pure stage component

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: `ChatFlowStage` remained in `App.tsx`.
- Gaps: chat route module ownership is still partial.
- Inconsistencies: chat presentation had no component module owner.
- Architecture constraints: keep runtime chat state and API calls unchanged.

### 2. Select One Priority Task
- Selected task: PRJ-977 chat flow stage extraction.
- Priority rationale: low-risk chat component split behind route smoke.
- Why other candidates were deferred: transcript/composer extraction needs more
  state coupling review.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/chat.tsx`, docs/context.
- Logic: move `ChatFlowStage` unchanged and import it.
- Edge cases: active-stage class remains prop driven.

### 4. Execute Implementation
- Implementation notes: extracted only stateless markup.

### 5. Verify and Test
- Validation performed: web build and route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: leave component in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: chat component ownership can now grow gradually.
- Refinements made: avoided moving transcript or send logic.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
