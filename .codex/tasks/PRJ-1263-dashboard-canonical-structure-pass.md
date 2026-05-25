# Task

## Header
- ID: PRJ-1263
- Title: Dashboard canonical structure pass
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1262
- Priority: P1
- Iteration: 1263
- Operation Mode: BUILDER
- Mission ID: PRJ-1263-dashboard-canonical-structure-pass
- Mission Status: DONE

## Context
User requested another full 1:1-focused view pass and indicated that flagship views still drift from canonical references and notes. This checkpoint targets `/dashboard` only.

## Goal
Move Dashboard closer to canonical composition by reducing desktop over-compression and restoring clearer flagship hierarchy.

## Scope
- `web/src/index.css`
- route: `/dashboard`
- desktop/mobile layout and surface rhythm only

## Definition of Done
- [x] `npm run build` passes.
- [x] Focused `/dashboard` screenshot/nav/account gate passes.
- [x] Desktop and mobile screenshots reviewed.
- [x] Route behavior and backend data mapping remain unchanged.

## Result
Adjusted Dashboard structure with a wider and clearer right guidance rail, larger hero proportion, less compressed typography, stronger flow-section readability, restored desktop recent-activity panel visibility, and calmer card rhythm while preserving existing data, interactions, and route contracts.

## Validation Evidence
- `npm run build` in `web/` -> PASS
- `node web/scripts/route-smoke.mjs --screenshots artifacts/route-smoke/prj-1263-dashboard-pass --screenshot-routes /dashboard --viewports desktop,mobile --navigation-proof --account-proof --report artifacts/route-smoke/prj-1263-dashboard-pass/report.json` -> PASS
- artifacts:
  - `artifacts/route-smoke/prj-1263-dashboard-pass/desktop-dashboard.png`
  - `artifacts/route-smoke/prj-1263-dashboard-pass/mobile-dashboard.png`
  - `artifacts/route-smoke/prj-1263-dashboard-pass/report.json`
