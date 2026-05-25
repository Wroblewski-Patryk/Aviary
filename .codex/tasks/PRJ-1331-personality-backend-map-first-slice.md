# PRJ-1331 - Personality Backend Map First Slice

## Header
- ID: PRJ-1331
- Title: Personality backend map first slice
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1331
- Module Confidence Rows: AVIARY-WEB-PERSONALITY-MAP-001, AVIARY-WEB-RESP-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
The user requested a broad coordinated push to map every backend capability into a magical, beautiful UI and bring the experience toward a final version for their personality. Read-only Backend/API, Frontend Coverage, and UX/Product lanes agreed that `/app/personality/overview` is the strongest first product surface because it is the user-facing map of identity, memory, planning, skills, and recent activity.

## Goal
Make the Personality route more truthful to the backend snapshot and less like a hardcoded decorative status surface, without changing backend contracts, route structure, auth, data persistence, or the canonical embodied map.

## Scope
- `web/src/App.tsx`
- `web/src/index.css`
- `/personality` route only
- Existing `/app/personality/overview` client data and existing shared UI components only

## Implementation Plan
1. Keep subagent lane output read-only and integrate findings locally.
2. Add localized Personality copy for backend-backed map/status/timeline concepts.
3. Track Personality overview loading and error state explicitly.
4. Replace hardcoded English Personality map labels with UI copy and backend-derived values.
5. Add loading, error, and empty/learning state panels for the Personality snapshot.
6. Keep CSS scoped to the new status detail line.
7. Run web build and focused `/personality` screenshot route proof.

## Acceptance Criteria
- Personality overview status is not hardcoded `Stable`; it reflects loading, error, learning, or backend-signal presence.
- Identity, learned knowledge, planning, skills, role, timeline, conscious/subconscious panels, and recent activity use localized product copy.
- The route still maps to existing backend-derived values from `/app/personality/overview`.
- Desktop, tablet, and mobile `/personality` screenshots pass route-smoke UI audit with no overflow or unnamed controls.
- No backend/API/schema behavior changes.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1331-personality-backend-map\screenshots --report ..\.codex\artifacts\prj1331-personality-backend-map\report.json --screenshot-routes /personality --viewports desktop,tablet,mobile --account-proof; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
- Screenshots/logs:
  - `.codex/artifacts/prj1331-personality-backend-map/report.json`
  - `.codex/artifacts/prj1331-personality-backend-map/screenshots/desktop-personality.png`
  - `.codex/artifacts/prj1331-personality-backend-map/screenshots/tablet-personality.png`
  - `.codex/artifacts/prj1331-personality-backend-map/screenshots/mobile-personality.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: Personality embodied cognition map remains the primary stage.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `StatePanel`, Personality callouts, timeline rows, side panels
- New shared pattern introduced: no
- State checks: loading, empty/learning, error, success
- Responsive checks: desktop, tablet, mobile
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`
- Parity evidence: focused `/personality` screenshot gate passed for 3 viewports.

## Architecture Evidence
- Architecture source reviewed: `docs/ux/canonical-ui-layout-index.md`, `/app/personality/overview` client contract, subagent Backend/API inventory.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is UI copy/state mapping only.

## Result Report
- Task summary: First Personality UI slice now makes the embodied map more backend-aware, localized, and stateful.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/index.css`
- How tested: web build and focused route-smoke screenshot/account proof.
- What is incomplete: full backend capability coverage across all routes remains a multi-slice mission; sidebar health, demo transcript, static module metrics, Tools detail, and connector confirmation history remain future slices.
- Next steps: continue `Personality` first-viewport/map fidelity or take the next truth-mapping slice by replacing static shell health with `/health`.

## Autonomous Loop Evidence
### 1. Analyze Current State
- Subagents found that UI uses core app endpoints but still has static or weak capability exposure.
- UX lane recommended Personality as the heart of final personality UI.

### 2. Select One Priority Mission Objective
- Selected task: improve `/personality` backend map truth and state handling.
- Other candidates deferred: health sidebar, chat empty state, goals/insights static metrics, tools/integrations deep capability views.

### 3. Plan Implementation
- Use existing `/app/personality/overview` data and existing components.
- Avoid backend/schema changes.

### 4. Execute Implementation
- Added localized Personality copy and route state derivation.
- Added Personality loading/error/empty state panels.
- Added scoped status-detail CSS.

### 5. Verify and Test
- Build PASS.
- Focused `/personality` desktop/tablet/mobile screenshot gate PASS.

### 6. Self-Review
- No workaround path introduced.
- No fake backend data added.
- Existing embodied-map design system preserved.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Active mission, task board, project state, delivery map, requirement matrix, module confidence, and next steps updated in the same cycle.
