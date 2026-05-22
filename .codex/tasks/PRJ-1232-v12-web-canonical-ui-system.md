# Task

## Header
- ID: PRJ-1232
- Title: V1.2 Web Canonical UI System
- Task Type: frontend
- Current Stage: release
- Status: DONE
- Owner: Coordinator
- Depends on: PRJ-1231
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-WEB-RESP-001, AVIARY-STATUS-001
- Requirement Rows: REQ-UX-001, REQ-MOB-001
- Quality Scenario Rows: canonical visual parity, responsive shell, web route rendering, accessibility/overflow
- Risk Rows: UX_CANONICAL_DRIFT, MOBILE_TRANSFER_DRIFT, VALIDATION_EVIDENCE_GAP
- Iteration: 1232
- Operation Mode: BUILDER
- Mission ID: PRJ-1232-v12-web-canonical-ui-system
- Mission Status: COMPLETED

## Context
V1.1.1 is production-released. The user requested v1.2 frontend work using the
canonical images in documentation as the source for a future mobile app. The
work must cover web mobile and desktop views, remain functional, and avoid
unnecessary decorative or explanatory clutter.

## Goal
Create and execute a coordinated v1.2 web UI mission that moves every relevant
web view toward the canonical mobile/desktop product baseline with evidence.

## Constraints
- Treat canonical documentation images as accepted specs, not loose
  inspiration.
- Work in bounded batches and verify mobile/desktop screenshots before moving
  to dependent surfaces.
- Do not disturb the production `v1.1.1` tag or release marker.
- Do not invent new visible copy, routes, systems, or decorative filler without
  a route need or canonical support.
- Reuse current web route contracts and backend data shapes.

## Definition of Done
- [x] UX spec lane maps canonical references to surfaces.
- [x] Frontend architecture lane maps route files, style ownership, and safe
      first write scope.
- [x] QA lane defines screenshot, smoke, overflow, accessibility, and cleanup
      gates.
- [x] First implementation batch is selected from source-of-truth surface order.
- [x] Batch implementation has desktop/mobile proof and green web gates.
- [x] Source-of-truth state records v1.2 scope, evidence, and next batch.

## Forbidden
- replacing canonical imagery with generic gradients or placeholder assets
- changing backend/API behavior for visual polish
- broad route rewrites without a batch-level proof plan
- calling a surface done without screenshot comparison
- shipping inert or fake controls when existing controls have real behavior

## Responsibility Lanes

| Lane | Owner | Expected output | Proof | Status |
| --- | --- | --- | --- | --- |
| Coordinator | Active chat | Mission, batch choice, integration, implementation gate | Parent validation | COMPLETED |
| UX Spec Auditor | Explorer | Canonical reference map by surface | Read-only report | COMPLETED |
| Frontend Architecture Auditor | Explorer | Route/component/CSS ownership and first write scope | Read-only report | COMPLETED |
| QA/Visual Gate Planner | Explorer | Commands, screenshot proof, cleanup gates | Read-only report | COMPLETED |
| Implementation | Coordinator after lane integration | Bounded v1.2 UI checkpoints | Web build/audits/screenshots | COMPLETED |

## Implementation Plan
1. Inventory canonical assets and route targets.
2. Map current implementation ownership and risks.
3. Define v1.2 acceptance gates for desktop and mobile.
4. Select one first batch from the canonical order.
5. Implement only that batch.
6. Run web gates and screenshot comparison.
7. Update project state and next batch.

## Acceptance Criteria
- Mission produces a concrete, evidence-backed v1.2 queue, not a vague polish
  promise.
- First batch improves a canonical surface without regressing route smoke or
  mobile/desktop layout.
- Remaining surfaces are tracked with owners and proof needs.

## Validation Evidence
- UX Spec Auditor mapped canonical references:
  - public home: `docs/ux/assets/aion-landing-canonical-reference-v1.png`
  - shell/sidebar: `docs/ux/assets/aviary-sidebar-layout-canonical-reference-v1.png`
  - dashboard: `docs/ux/assets/aion-dashboard-canonical-reference-v2.png`
  - chat: `docs/ux/assets/aion-chat-canonical-reference-v5.png`
  - personality: `docs/ux/assets/aion-personality-canonical-reference-v1.png`
  - module routes use shared shell/material rules unless a route-specific
    canonical screenshot exists.
- Frontend Architecture Auditor found safest first write scope in route
  metadata and route-smoke ownership before broad `App.tsx`/CSS surgery.
- QA/Visual Gate Planner defined per-batch gates: `node --check`,
  `npm run build`, route smoke, responsive screenshots, navigation proof,
  account proof, visual review, and process cleanup.
- Foundation batch:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - responsive screenshot gate -> `screenshot_count=18`, `failed_count=0`
    for `/`, `/dashboard`, `/chat`, `/personality`, `/settings`, `/tools`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`,
    `panel_visible=true`
- Mobile foundation batch:
  - mobile screenshots for `/chat`, `/settings`, `/dashboard` stored in
    `.codex/artifacts/prj1232-mobile-foundation-gate/`
  - mobile Chat context cards now stack vertically instead of starting with a
    clipped horizontal belt.
  - route-smoke overflow audit now ignores only contained, intentional
    horizontal scrollers and still reports document-level horizontal overflow.
  - mobile screenshot audit -> `screenshot_count=3`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`,
    `overflowingElementCount=0`
  - account proof -> `step_count=1`, `failed_count=0`,
    `overflowingElementCount=0`
- Public Home batch:
  - `npm run build` in `web/` -> PASS
  - public Home/Login screenshot gate in
    `.codex/artifacts/prj1232-public-home-gate/` -> `screenshot_count=4`,
    `failed_count=0`
  - `/` and `/login` pass desktop/mobile with `horizontalOverflow=false`,
    `unnamedInteractiveCount=0`, and `overflowingElementCount=0`
  - scenic landing background no longer uses transform scaling that produced a
    decorative out-of-viewport element in smoke diagnostics.
- Shell/Dashboard batch:
  - mobile/tablet Dashboard route label changed from ambiguous `Home/Start` to
    `Dash`/`Panel`, keeping public Home distinct from authenticated Dashboard.
  - desktop Dashboard received route-local density tuning for hero signals,
    cognitive flow, lower cards, and right rail.
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - `.codex/artifacts/prj1232-dashboard-shell-gate/report.json` ->
    `screenshot_count=3`, `failed_count=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
- Chat batch:
  - desktop cognitive belt is lighter and lower while preserving six visible
    status cards in one row.
  - `.codex/artifacts/prj1232-chat-belt-gate/report.json` ->
    `screenshot_count=3`, `failed_count=0`
- Personality batch:
  - desktop hero figure is more flagship-forward.
  - mobile overview removes redundant explanatory subtitle and keeps status
    aligned in the compact header before the hero.
  - `.codex/artifacts/prj1232-personality-hero-gate/report.json` ->
    `screenshot_count=3`, `failed_count=0`
- Final cross-route gate:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - `.codex/artifacts/prj1232-final-route-smoke/report.json` ->
    `route_count=14`, `status=ok`
  - `.codex/artifacts/prj1232-final-responsive-gate/report.json` ->
    `screenshot_count=39`, `failed_count=0`
  - `.codex/artifacts/prj1232-navigation-proof/report.json` ->
    `navigation_proof.status=ok`, `step_count=4`, `failed_count=0`
  - `.codex/artifacts/prj1232-account-proof/report.json` ->
    `account_proof.status=ok`, `step_count=1`, `failed_count=0`,
    `panel_visible=true`

## Result Report
- Task summary: v1.2 web canonical UI checkpoint set is complete. The mission
  created a shared route manifest, hardened route-smoke, improved mobile Chat,
  cleared public Home/Login overflow diagnostics, disambiguated Dashboard
  mobile/tablet nav labels, tightened Dashboard desktop density, lightened the
  Chat cognitive belt, improved Personality hero rhythm, and proved module
  route consistency across desktop/tablet/mobile.
- Files changed:
  - `.agents/state/active-mission.md`
  - `.codex/tasks/PRJ-1232-v12-web-canonical-ui-system.md`
  - `web/src/route-manifest.json`
  - `web/src/routes.ts`
  - `web/src/index.css`
  - `web/scripts/route-smoke.mjs`
- How tested: see Validation Evidence.
- Remaining surfaces: no blocking v1.2 web checkpoint remains. Exact
  pixel-perfect parity is not claimed; future work can continue from visual
  taste refinements rather than functional/responsive blockers.
- Final verdict: DONE for v1.2 web/mobile foundation checkpoints.
