# PRJ-1336 - Integrations External Only

## Header
- ID: PRJ-1336
- Title: Integrations external-only provider map
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1336
- Module Confidence Rows: AVIARY-WEB-INTEGRATIONS-EXTERNAL-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
`PRJ-1335` aligned Tools fixtures to the backend-shaped `/app/tools/overview` catalog, but the Integrations route still rendered every tool item. That made first-party and integral capabilities such as Internal chat, Web search, and Web browser appear as external integrations.

## Goal
Make Integrations a truthful external provider/channel surface while preserving the full Tools catalog.

## Scope
- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `web/src/lib/tool-formatting.ts`
- `web/scripts/route-smoke.mjs`
- `web/scripts/tools-directory-characterization.mjs`

## Implementation Plan
1. Use backend/API and frontend/UX read-only lanes to confirm the Integrations filter boundary.
2. Keep `/app/tools/overview` as the shared data source.
3. Derive Integrations rows from only non-integral items where `kind` is `integration` or `channel`.
4. Recompute Integrations counts from the filtered rows instead of global Tools summary counts.
5. Translate known backend `next_actions` into calmer user-facing product copy.
6. Add route-smoke assertions that `/integrations` includes only Telegram, ClickUp, Google Calendar, and Google Drive.
7. Verify Tools still renders the full 7-item catalog.

## Acceptance Criteria
- Integrations provider map includes Telegram, ClickUp, Google Calendar, and Google Drive.
- Integrations provider map excludes Internal chat, Web search, and Web browser.
- Integrations summary counts are derived from external provider/channel rows only.
- Tools keeps the full 4-group / 7-tool catalog.
- No backend changes.
- Desktop, tablet, and mobile `/integrations` and `/tools` remain free of horizontal overflow and unnamed visible controls.

## Validation Evidence
- Tests:
  - `Push-Location .\web; node --check scripts/route-smoke.mjs; node --check scripts/tools-directory-characterization.mjs; Pop-Location` -> PASS
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1336-integrations-external-only\screenshots --report ..\.codex\artifacts\prj1336-integrations-external-only\report.json --screenshot-routes /integrations,/tools --viewports desktop,tablet,mobile --account-proof --fail-on-ui-findings; Pop-Location` -> PASS
- Route-smoke contract proof:
  - `/integrations` `integrationProviderCount=4`
  - `/integrations` `integrationProviderTitles=["Telegram","ClickUp","Google Calendar","Google Drive"]`
  - `/integrations` excludes Internal chat, Web search, and Web browser through route-smoke pass criteria.
  - `/tools` still passes with the full Tools route marker and no horizontal overflow.
- Screenshots/logs:
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1336-integrations-external-only\report.json`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1336-integrations-external-only\screenshots\desktop-integrations.png`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1336-integrations-external-only\screenshots\mobile-integrations.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: existing_design_system
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: Integrations route as a calm external edge map, not a duplicate Tools catalog.
- Fidelity target: structurally_faithful
- State checks: default provider map, Tools full catalog preservation, account proof.
- Responsive checks: desktop, tablet, mobile for `/integrations` and `/tools`.
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`.

## Architecture Evidence
- Architecture source reviewed: `/app/tools/overview` backend policy and backend API tests.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is frontend filtering against an existing backend contract.

## Result Report
- Task summary: Integrations now maps only external provider/channel surfaces, while Tools remains the full capability directory.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/tools.tsx`
  - `web/src/lib/tool-formatting.ts`
  - `web/scripts/route-smoke.mjs`
  - `web/scripts/tools-directory-characterization.mjs`
- How tested: script syntax checks, web build, Tools characterization, strict `/integrations,/tools` route-smoke screenshot/account proof.
- What is incomplete: Provider-specific setup flows are still owned by Tools and backend confirmation/link contracts; this slice does not activate credentials or call external providers.
- Next steps: continue backend-to-UI mapping through connector confirmation history, module metric derivation, or richer provider setup copy.

## Autonomous Loop Evidence
### 1. Analyze Current State
- Integrations used all Tools items and mixed integral capabilities with external providers.

### 2. Select One Priority Mission Objective
- Selected task: make Integrations external-only before deeper provider polish.

### 3. Plan Implementation
- Filter only the Integrations view and preserve shared Tools data.

### 4. Execute Implementation
- Added external filter, recomputed counts, calmer next-action copy, and route-smoke contract assertions.

### 5. Verify and Test
- Syntax checks, build, characterization, and strict screenshot/account route-smoke passed.

### 6. Self-Review
- No backend changes.
- No provider calls or credential activation.
- Integral first-party/product capabilities remain in Tools, not Integrations.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Mission and state files updated in the same cycle.
