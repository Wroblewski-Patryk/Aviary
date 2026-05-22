# Task

## Header
- ID: PRJ-1235
- Title: Mobile shell first-viewport polish
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1234
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: `AVIARY-WEB-RESP-001`
- Requirement Rows: `REQ-UX-1235`
- Quality Scenario Rows: `QA-UX-1235`
- Risk Rows: `RISK-UI-1235`
- Iteration: 1235
- Operation Mode: TESTER
- Mission ID: PRJ-1235-mobile-shell-first-viewport-polish
- Mission Status: COMPLETED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed in active mission context.
- [x] `.agents/core/mission-control.md` was reviewed in active mission context.
- [x] Missing or template-like state tables were confirmed not needed for this CSS-only slice.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: reduce authenticated mobile shell chrome so every web route gives more first-viewport authority to the actual view while keeping one header and one navigation.
- Release objective advanced: local v1.2 web mobile-transfer confidence.
- Included slices: shared mobile header/tabbar density polish, module numeric typography, quieter desktop sidebar support cards, inert desktop utility chips, account disclosure semantics, full screenshot-audit script, screenshot proof, docs/state update.
- Explicit exclusions: backend/API/runtime, native app implementation, production release, new product behavior for utility actions.
- Checkpoint cadence: one focused mobile shell patch followed by full local UX gate.
- Stop conditions: mobile navigation becomes unclear, route identity is lost, screenshot gate reports overflow/clipping, or product behavior changes are needed.
- Handoff expectation: green gate, refreshed mobile screenshots, and clear residual risk.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | `AGENTS.md`, active mission, task board | Integration, state, final decision | Mission closure | Parent validation gate | DONE |
| UX Residual Audit | Subagent Meitner | PRJ-1234 screenshots, design memory | Remaining visual gaps | Ranked read-only report | Lane report | DONE |
| Code/A11y Audit | Subagent Euclid | web shell/CSS/reports | Safe quality improvements | Ranked read-only report | Lane report | DONE |
| Frontend/UX | Active chat | shared shell CSS and shell semantics | `web/src/index.css`, `web/src/App.tsx`, `web/src/components/shell.tsx`, `web/package.json` | Mobile shell density/accessibility patch | Build/screenshots | DONE |
| QA/Test | Active chat | route-smoke | local UX gate | Proof reports | 42 screenshots + nav/account | DONE |
| Docs/State | Active chat | state docs | task/state docs | durable evidence | Updated ledgers | DONE |

## Context
PRJ-1234 verified the local v1.2 flagship UX checkpoint. Residual screenshot review shows the authenticated mobile shell still consumes too much first-viewport space across routes.

## Goal
Make every authenticated mobile route feel more app-like and less web-chrome-heavy by compacting the shared mobile header and route navigation without adding new chrome or route-local special cases.

## Scope
- `web/src/index.css`
- `web/src/App.tsx`
- `web/src/components/shell.tsx`
- `web/package.json`
- `.codex/tasks/PRJ-1235-mobile-shell-first-viewport-polish.md`
- required state/context docs

## Implementation Plan
1. Inspect PRJ-1234 mobile screenshots and shared shell CSS.
2. Apply CSS-only compact mobile shell rules under the existing mobile breakpoint.
3. Run build, route smoke, full screenshot gate, navigation proof, account proof, and cleanup checks.
4. Review refreshed mobile screenshots for Dashboard, Chat, Personality, Tools, and Settings.
5. Update source-of-truth docs and commit if green.

## Success Signal
- User or operator problem: mobile routes should show the product surface sooner, with less repeated shell weight.
- Expected product or reliability outcome: one header and one navigation remain, but they are quieter and more native-ready.
- How success will be observed: full screenshot gate green and manual mobile first-viewport review.
- Post-launch learning needed: yes

## Deliverable For This Stage
CSS patch plus validation artifacts for the mobile shell first-viewport slice.

## Constraints
- use existing shell patterns
- do not introduce a second nav, sidebar, modal, or route-local header
- do not hide route identity
- do not change backend/API/runtime behavior
- do not claim production release

## Acceptance Criteria
- Authenticated mobile header is visibly shorter across all routes.
- Route identity remains visible.
- Route navigation remains reachable and scrollable.
- Account trigger remains visible and proof still passes.
- Full local UX proof remains green.

## Definition of Done
- [x] Shared shell patch is scoped to shared mobile shell, shell semantics, numeric typography, and quieter shared sidebar support chrome.
- [x] `node --check scripts/route-smoke.mjs` passes.
- [x] `npm run build` passes.
- [x] route smoke reports `route_count=14`, `status=ok`.
- [x] responsive screenshot gate reports `screenshot_count=42`, `failed_count=0`.
- [x] navigation proof and account proof pass.
- [x] Manual mobile screenshot review confirms improved first viewport.
- [x] Cleanup check shows no validation-owned leftovers.
- [x] State docs are updated.

## Forbidden
- new navigation systems
- route-local header forks
- temporary bypasses or screenshot-only hacks
- hidden route identity
- production release claim

## Validation Evidence
- Tests:
  - `Push-Location .\web; node --check scripts/route-smoke.mjs; npm run build; Pop-Location` -> PASS.
  - route smoke -> `route_count=14`, `status=ok`.
  - full responsive screenshot gate -> `viewport_count=3`, `screenshot_count=42`, `failed_count=0`.
  - navigation proof -> `step_count=4`, `failed_count=0`.
  - account proof -> `step_count=1`, `failed_count=0`, `panel_visible=true`.
- Manual checks:
  - Reviewed `mobile-dashboard.png`, `mobile-tools.png`, `mobile-settings.png`, and `desktop-dashboard.png`.
  - Mobile header now hides the repeated workspace label, compacts the Aviary lockup/account row, and keeps one route rail.
  - Module count values use unambiguous UI numeric typography.
  - Desktop sidebar support stack is quieter without removing its content.
- Screenshots/logs:
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/screenshots/`
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/screenshot-gate-report.json`
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/navigation-proof-report.json`
  - `.codex/artifacts/prj1235-mobile-shell-first-viewport-polish/account-proof-report.json`
- High-risk checks:
  - In-app Browser preview was attempted at `http://127.0.0.1:4173/dashboard`; because the plain preview does not include the route-smoke authenticated API mock, it reached the login modal instead of the authenticated shell. Authenticated visual proof therefore remains the route-smoke harness.
  - Route-smoke reports zero document overflow, zero framework overlay, zero visible unnamed interactive controls, and no overflowing elements across the checked routes.
  - Cleanup check stopped the validation-owned Vite preview process tree and found no remaining PRJ-1235 `chrome-headless-shell`, route-smoke/dev-server processes, or `5173`/`4173` listeners.
- Reality status: verified local web UX checkpoint

## Result Report
PRJ-1235 is complete as a local v1.2 web polish checkpoint. The shared mobile authenticated shell is more compact across routes, desktop utility chips no longer expose inert fake buttons, account triggers now match disclosure-panel semantics, module numeric values are clearer, and the full current screenshot audit script is available as `npm run audit:ui-responsive:full`.
