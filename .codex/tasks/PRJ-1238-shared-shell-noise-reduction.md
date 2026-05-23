# Task

## Header
- ID: PRJ-1238
- Title: Shared shell noise reduction and first UI simplification pass
- Task Type: implementation
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1237
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: `AVIARY-WEB-RESP-001`
- Requirement Rows: `REQ-UX-1238`
- Quality Scenario Rows: `QA-UX-1238`
- Risk Rows: `RISK-UI-1238`
- Iteration: 1238
- Operation Mode: BUILDER
- Mission ID: PRJ-1238-shared-shell-noise-reduction
- Mission Status: COMPLETED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with `docs/ux/canonical-ui-layout-index.md`.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: execute the first implementation slice from the canonical UI simplification index by removing shared-shell noise and documenting route-noise decisions.
- Release objective advanced: v1.2 web UI simplification on `main`.
- Included slices: `PASS-NOISE-AUDIT` table, `PASS-SHELL` shared chrome reduction, state updates, validation.
- Explicit exclusions: broad route rewrite, backend/API changes, native generation, production deploy claim.
- Checkpoint cadence: shell first, then route-local simplification passes.
- Stop conditions: a visible element cannot map to the canonical index, validation introduces route/navigation/account regressions, or deploy/source branch drift makes release claims unsafe.
- Handoff expectation: shared shell is calmer and future route passes have an audit queue.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `AGENTS.md`, mission-control, PRJ-1237 | Integration, state, final decision | Mission closure | Parent validation gate | COMPLETED |
| UX/Noise Audit | Subagent Faraday | canonical UI index, screenshots, web code | Read-only route/shell audit | Noise table | Lane report | COMPLETED |
| Shell Review | Subagent Dirac | shell components/styles | Read-only shell patch recommendation | Patch plan | Lane report | COMPLETED |
| Frontend Builder | Active chat | web shell implementation | shared shell code/CSS | Small PASS-SHELL patch | build and UI audits | COMPLETED |
| QA/Test | Active chat | web scripts | validation | route, navigation, screenshot evidence | command evidence | COMPLETED |
| Docs/State | Active chat | state docs | durable project memory | ledger/task updates | source-of-truth diff | COMPLETED |

## Context
`PRJ-1237` created the canonical UI layout index after the user identified too many controls, cards, badges, chips, and equal-weight groups across the app. The next step is implementation, beginning with the shared shell because every route inherits it.

## Goal
Make the global authenticated shell simpler by demoting or removing inert utility chrome, duplicate status material, and decorative support cards while preserving one desktop sidebar, one mobile header, one mobile route rail, account access, and route navigation.

## Scope
- `web/src/components/shell.tsx`
- shell-related JSX in `web/src/App.tsx`
- shell-related CSS in `web/src/index.css`
- `docs/ux/canonical-ui-layout-index.md` if the route-noise audit needs durable rows
- project state/task ledgers

## Implementation Plan
1. Read the canonical UI layout index and current shell code.
2. Delegate read-only noise audit and shell-review lanes.
3. Patch the shared shell first: remove fake search/capture/notification/status clutter and reduce support-card density.
4. Validate build, route smoke, navigation/account proof, and responsive screenshots for representative routes.
5. Integrate lane reports into route-noise queue and state docs.

## Acceptance Criteria
- Desktop has one sidebar, one utility/account area, and one route canvas.
- Mobile has one compact header, one route rail, one account disclosure, and no duplicate route-local nav.
- Inert search/capture/notification-looking chrome is removed or rendered as low-emphasis status only.
- Sidebar support no longer reads like multiple competing cards.
- No route/navigation/account regression is introduced.

## Definition of Done
- [x] Shared shell noise is reduced in code.
- [x] Noise audit decisions are recorded.
- [x] Subagent lane reports are integrated or explicitly bounded.
- [x] `npm run build` passes.
- [x] Route/navigation/account or responsive proof passes for the touched shell scope.
- [x] State docs are updated.

## Forbidden
- adding new fake controls
- route-local redesign before shell is stable
- new backend contracts
- changing route order without a product decision
- production deploy claim without deploy parity

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run audit:ui-navigation` in `web/` -> PASS, `step_count=4`, `failed_count=0`
  - route smoke -> `route_count=14`, `status=ok`
  - account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`
  - screenshot gate -> `viewport_count=3`, `screenshot_count=42`, `failed_count=0`
- Manual checks:
  - reviewed desktop Dashboard and Chat screenshots after fake utility chrome removal
  - reviewed mobile Dashboard and Settings screenshots after mobile `Workspace` label removal
  - Browser/IAB proof attempted but runtime bootstrap exited unexpectedly; Playwright route-smoke screenshots remain the rendered proof for this checkpoint
- Screenshots/logs:
  - `.codex/artifacts/prj1238-shared-shell-noise-reduction/route-smoke-report.json`
  - `.codex/artifacts/prj1238-shared-shell-noise-reduction/account-proof-report.json`
  - `.codex/artifacts/prj1238-shared-shell-noise-reduction/screenshot-gate-report.json`
  - `.codex/artifacts/prj1238-shared-shell-noise-reduction/screenshots/`
- High-risk checks:
  - removed inert/fake utility controls instead of adding new controls
  - preserved one sidebar, one desktop utility/account area, one mobile header, and one mobile route rail
  - validation cleanup removed route-smoke-owned `chrome-headless-shell` processes; unrelated `Obiekty` Vite listener on `5173/5180` was left untouched
- Reality status: verified local web shell checkpoint

## Result Report
`PRJ-1238` completed the first implementation slice from the canonical UI
simplification index. The desktop utility bar now contains only current route
context and the account disclosure; fake search, Focus mode, Quick capture, and
notification chrome were removed. The desktop sidebar health card lost its
duplicate diagnostics pill. Mobile route headers no longer repeat the visible
`Workspace` label above the route title. The `PASS-NOISE-AUDIT` queue is
recorded in `docs/ux/canonical-ui-layout-index.md` for the next Settings,
Tools, and module simplification slices.
