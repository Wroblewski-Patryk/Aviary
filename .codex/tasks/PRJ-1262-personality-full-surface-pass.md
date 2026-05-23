# Task

## Header
- ID: PRJ-1262
- Title: Personality full-surface pass
- Task Type: design
- Current Stage: implementation
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1261
- Priority: P1
- Requirement Rows: REQ-UX-1262
- Quality Scenario Rows: QA-UX-1262
- Risk Rows: RISK-UI-1262
- Iteration: 1262
- Operation Mode: BUILDER
- Mission ID: PRJ-1262-personality-full-surface-pass
- Mission Status: DONE

## Context
User requested one complete, end-to-end pass for a single web view instead of many cosmetic iterations. This task closes `/personality` as one broad CSS-only surface pass across desktop and mobile.

## Goal
Deliver one cohesive Personality view polish pass that feels final in desktop and mobile composition, with calmer hierarchy and reduced control/card noise, while preserving all supported route data and behaviors.

## Scope
- `web/src/index.css`
- route: `/personality`
- surfaces: overview bar, hero/callout material, timeline panel/rows, side panels, responsive rhythm

## Definition of Done
- [x] `node --check scripts/route-smoke.mjs` passes.
- [x] `npm run build` passes.
- [x] Focused `/personality` screenshot/nav/account gate passes.
- [x] `git diff --check` passes with no whitespace errors.
- [x] Screenshot review confirms desktop and mobile improvements in one cohesive pass.
- [x] Validation cleanup confirms no owned browser/server leftovers.
- [x] State/docs ledgers are updated.

## Result
One cohesive Personality full-surface pass landed in `web/src/index.css` with a calmer, more structured hierarchy on desktop and mobile while preserving route data and controls. The pass tightened hero/overview composition, reduced card heaviness, and clarified timeline readability without introducing new components.

## Validation Evidence
- `node --check web/scripts/route-smoke.mjs` -> PASS
- `npm run build` in `web/` -> PASS
- `node web/scripts/route-smoke.mjs --screenshots artifacts/route-smoke/prj-1262 --screenshot-routes /personality --viewports desktop,mobile --navigation-proof --account-proof --report artifacts/route-smoke/prj-1262/report.json` -> PASS (`status=ok`, `route_count=14`, `ui_audit.failed_count=0`, `navigation_proof.failed_count=0`, `account_proof.failed_count=0`)
- artifacts:
  - `artifacts/route-smoke/prj-1262/desktop-personality.png`
  - `artifacts/route-smoke/prj-1262/mobile-personality.png`
  - `artifacts/route-smoke/prj-1262/report.json`
