# Task

## Header
- ID: PRJ-976
- Title: Extract app icon/control component cluster from `web/src/App.tsx`
- Task Type: refactor
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-975
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 976
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

After shell and public glyph extraction, `web/src/App.tsx` still owned several
pure SVG icon primitives used by auth, sidebar, and chat controls.

## Goal

Move the pure app icon primitives into a dedicated component module without
changing auth, sidebar, or chat behavior.

## Scope

- `web/src/App.tsx`
- `web/src/components/app-icons.tsx`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: repeated icon primitives were hidden inside the app
  monolith.
- Expected product or reliability outcome: shared control icons have one
  obvious owner while route behavior remains unchanged.
- How success will be observed: build and route smoke pass.
- Post-launch learning needed: no

## Deliverable For This Stage

Extract `ChevronDownIcon`, `CloseIcon`, `PlusIcon`, `MicrophoneIcon`, and
`SendArrowIcon` to `web/src/components/app-icons.tsx`.

## Constraints
- use existing systems and approved mechanisms
- do not move auth, sidebar, or chat state out of `App()`
- do not alter SVG markup, button behavior, copy, or visual classes
- do not open a visible browser window

## Implementation Plan
1. Add `web/src/components/app-icons.tsx`.
2. Move the pure icon primitives unchanged into that module.
3. Import the icons from `App.tsx`.
4. Run web build and route smoke.
5. Update docs and context.

## Acceptance Criteria
- Icon primitives no longer live in `App.tsx`.
- `web/src/components/app-icons.tsx` owns the icon primitives.
- Existing auth/sidebar/chat icon usages still render through imports.
- `npm run build` passes.
- `npm run smoke:routes` passes.

## Definition of Done
- [x] Icon primitives extracted.
- [x] App state and behavior remain in `App()`.
- [x] Behavior-preserving validation completed.
- [x] Docs and context updated.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - confirmed `App.tsx` imports the icon primitives and no longer defines them
- Screenshots/logs:
  - no screenshots; no visible behavior intentionally changed
- High-risk checks:
  - SVG markup was preserved
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
  - route map now records app icon primitives under shared component ownership

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing icon SVG markup
- Canonical visual target: unchanged
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: exact existing icon SVG markup
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: unchanged
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: auth modal, chat flow stages, and route-local views
  still live in `App.tsx`
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
- Rollback note: move icon primitives back into `App.tsx`
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

This task intentionally avoids extracting auth modal or chat composer state.

## Production-Grade Required Contract

- Goal: clarify app control icon ownership.
- Scope: pure SVG icon primitives only.
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
- Existing workaround or pain: pure icon primitives embedded in monolith
- Smallest useful slice: one pure icon module
- Success metric or signal: build and route smoke pass
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: public auth entry and chat route entry
- SLI: route smoke pass rate
- SLO: route smoke remains green after extraction
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: route smoke JSON output
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: revert app icon extraction

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
- Residual risk: route-local views still remain in `App.tsx`

## Result Report

- Task summary: moved pure app icon primitives into
  `web/src/components/app-icons.tsx`.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/app-icons.tsx`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - auth modal, chat flow stages, and route-local views still live in
    `App.tsx`
- Next steps:
  - extract `ChatFlowStage` or a small auth modal presentational cluster
- Decisions made:
  - use a neutral app-icons module because the icons are shared across public,
    shell, and chat controls

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: pure icon primitives remained in `App.tsx`.
- Gaps: route-local render extraction remains queued.
- Inconsistencies: shared control icons did not have a module owner.
- Architecture constraints: keep stateful control behavior in `App()`.

### 2. Select One Priority Task
- Selected task: PRJ-976 app icon/control component cluster extraction.
- Priority rationale: low-risk pure extraction before stateful component work.
- Why other candidates were deferred: chat/auth component extraction has more
  state and copy coupling.

### 3. Plan Implementation
- Files or surfaces to modify: `App.tsx`, `components/app-icons.tsx`,
  docs/context.
- Logic: move icon SVG functions unchanged and import them.
- Edge cases: send button loading still uses string fallback owned by `App()`.

### 4. Execute Implementation
- Implementation notes: extracted only stateless SVG primitives.

### 5. Verify and Test
- Validation performed: web build and route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: keep icons in `App.tsx`.
- Technical debt introduced: no
- Scalability assessment: icon ownership is now explicit.
- Refinements made: avoided moving any button behavior.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
