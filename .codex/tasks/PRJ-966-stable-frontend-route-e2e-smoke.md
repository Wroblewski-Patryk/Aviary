# Task

## Header
- ID: PRJ-966
- Title: Add stable frontend route e2e smoke
- Task Type: test
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-965
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 966
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`docs/planning/v1-reality-audit-and-roadmap.md` marked web-led v1 confidence
as partial because the browser shell had route maps and build evidence, but no
repeatable headless route smoke that mounts the app against app-facing API
contracts.

## Goal

Add a stable no-visible-window frontend smoke command that builds on the
existing Vite output and proves the core public/authenticated route surfaces
mount without requiring a live backend or provider credentials.

## Scope

- `web/scripts/route-smoke.mjs`
- `web/package.json`
- `docs/engineering/testing.md`
- `docs/frontend/route-component-map.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: frontend route regressions can be missed when only
  backend route tests and `npm run build` run.
- Expected product or reliability outcome: public, dashboard, chat,
  personality, and tools route surfaces have repeatable headless smoke proof.
- How success will be observed: `npm run smoke:routes` prints
  `frontend_route_smoke_report` with `status=ok`.
- Post-launch learning needed: no

## Deliverable For This Stage

A committed route-smoke command plus documentation/context updates recording
how to run it and what it proves.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not open a visible browser window

## Implementation Plan
1. Add a Node-based route smoke server for `web/dist`.
2. Mock only the app-facing read endpoints required for route mounting.
3. Use installed Chrome/Edge in headless `--dump-dom` mode with
   `windowsHide=true`.
4. Assert stable route container markers instead of fragile copy strings.
5. Document the command and update v1 planning/context.
6. Run build, route smoke, and whitespace validation before commit.

## Acceptance Criteria
- `npm run build` passes.
- `npm run smoke:routes` passes without opening a visible browser window.
- The smoke covers `/`, `/login`, `/dashboard`, `/chat`, `/personality`, and
  `/tools`.
- The v1 roadmap no longer claims stable frontend route smoke is missing.

## Definition of Done
- [x] Route smoke command exists in `web/package.json`.
- [x] Route smoke implementation is grounded in current route containers from
  `web/src/App.tsx`.
- [x] Testing docs explain when to run the command.
- [x] Task board and project state are synchronized.
- [x] Validation evidence is recorded.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=6`
- Manual checks:
  - verified route markers against `web/src/App.tsx`
- Screenshots/logs:
  - no screenshots; smoke is headless by design
- High-risk checks:
  - visible browser window avoided through Chrome/Edge headless mode and
    `windowsHide=true`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/frontend/route-component-map.md`
  - `docs/engineering/testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - route map and testing docs now name the smoke command

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing app route containers in `web/src/App.tsx`
- Canonical visual target: not applicable for this no-screenshot smoke
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: route containers and backend-owned API client
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: route/component extraction remains a follow-up
- State checks: success
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: frontend route smoke command documented
- Rollback note: remove `web/scripts/route-smoke.mjs` and the package script
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

This is not a full visual parity suite. It is a deterministic route-mount smoke
that closes the v1 route-coverage gap without opening a browser window.

## Production-Grade Required Contract

- Goal: add stable frontend route-mount evidence for the v1 shell.
- Scope: web smoke script, package script, docs, planning, context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: see below.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: no, local mock API path is used for frontend route
  mounting only
- Endpoint and client contract match: yes, mocked endpoints follow current
  `web/src/lib/api.ts` consumers
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: static server starts fresh per run
- Regression check performed: yes

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: route confidence depended on route docs and web
  build evidence only
- Smallest useful slice: five-route headless mount smoke
- Success metric or signal: `frontend_route_smoke_report.status=ok`
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: initial public entry and authenticated core route entry
- SLI: route smoke pass rate
- SLO: route smoke should pass before frontend route refactors
- Error budget posture: not applicable
- Health/readiness check: not applicable
- Logs, dashboard, or alert route: JSON command output
- Smoke command or manual smoke: `npm run smoke:routes`
- Rollback or disable path: remove package script

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: synthetic local smoke data only
- Trust boundaries: smoke mocks same-origin app read endpoints locally
- Permission or ownership checks: no live user data or credentials touched
- Abuse cases: not applicable
- Secret handling: no secrets used
- Security tests or scans: not applicable
- Fail-closed behavior: command exits non-zero when a route marker is missing
- Residual risk: smoke proves route mounting, not full user interaction

## Result Report

- Task summary: added headless frontend route smoke for root, the login shell,
  and four core authenticated routes.
- Files changed:
  - `web/scripts/route-smoke.mjs`
  - `web/package.json`
  - `docs/engineering/testing.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - `Push-Location .\web; npm run build; Pop-Location`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
- What is incomplete:
  - full visual/screenshot parity and interaction e2e remain separate future
    work
- Next steps:
  - `PRJ-967` split `web/src/App.tsx` after this route safety net
- Decisions made:
  - use headless Chrome/Edge DOM dump instead of adding a new e2e dependency

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: v1 roadmap listed frontend route e2e smoke as the missing web
  confidence proof.
- Gaps: no stable no-window route-mount command existed.
- Inconsistencies: roadmap had PRJ-966 queued while route-map still said no
  dedicated frontend e2e suite existed.
- Architecture constraints: keep web as a thin client over backend-owned
  contracts.

### 2. Select One Priority Task
- Selected task: PRJ-966 stable frontend route e2e smoke.
- Priority rationale: it unblocks safer `App.tsx` route/component extraction.
- Why other candidates were deferred: PRJ-962 and PRJ-963 need external
  operator credentials; PRJ-967 should follow after route smoke coverage.

### 3. Plan Implementation
- Files or surfaces to modify: web smoke script, package script, docs/context.
- Logic: serve built assets, mock required API reads, run headless browser DOM
  checks, fail on missing route container markers.
- Edge cases: no visible browser window, missing build output, missing
  Chrome/Edge executable, route auth bootstrap.

### 4. Execute Implementation
- Implementation notes: route markers use stable top-level route container
  classes from `web/src/App.tsx`.

### 5. Verify and Test
- Validation performed: web build, route smoke.
- Result: both passed.

### 6. Self-Review
- Simpler option considered: text-only static file checks.
- Technical debt introduced: no
- Scalability assessment: the route list can be extended when new shell routes
  need mount proof.
- Refinements made: replaced fragile copy markers with stable route container
  classes.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/engineering/testing.md`
  - `docs/frontend/route-component-map.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
