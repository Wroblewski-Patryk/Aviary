# PRJ-1334 - Tools Capability Strip

## Header
- ID: PRJ-1334
- Title: Tools capability strip
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1334
- Module Confidence Rows: AVIARY-WEB-TOOLS-CAPABILITY-001, AVIARY-WEB-RESP-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
The active mission maps backend capabilities into a magical, truthful Aviary UI. The Tools route already consumed `/app/tools/overview`, but the safest backend mapping signals for each item, capabilities, skill bindings, and source-of-truth entries, were mostly hidden inside technical details.

## Goal
Make each Tools card immediately show a compact backend capability map while keeping raw provider payloads and operations/debug fields out of the primary UI.

## Scope
- `web/src/components/tools.tsx`
- `web/src/App.tsx`
- `web/src/index.css`
- `web/scripts/tools-directory-characterization.mjs`
- Tools route capability visibility only

## Implementation Plan
1. Run read-only backend/API and frontend coverage lanes for Tools/Integrations.
2. Keep `/app/tools/overview` as the primary UI adapter.
3. Add a compact per-tool strip for capability count, skill-binding count, and source count.
4. Localize count suffixes for EN/PL/DE.
5. Style the strip within the existing Tools card system across desktop and mobile.
6. Extend Tools characterization to assert three capability chips per tool card.
7. Validate build, characterization, responsive screenshots, and account proof.

## Acceptance Criteria
- Each rendered Tools card shows three visible backend-mapping chips.
- The chips use existing safe `/app/tools/overview` fields only.
- Technical detail disclosures remain available for deeper capability/source inspection.
- Tools toggle and Telegram link characterization still pass.
- `/tools` and `/integrations` remain stable across desktop, tablet, and mobile screenshots.
- No backend contract changes.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1334-tools-capability-strip\screenshots --report ..\.codex\artifacts\prj1334-tools-capability-strip\report.json --screenshot-routes /tools,/integrations --viewports desktop,tablet,mobile --account-proof; Pop-Location` -> PASS
- Characterization:
  - full case: `groupCount=2`, `itemCount=3`, `toggleCount=2`, `hasTelegramLinkPanel=true`, `capabilityChipCount=9`, `technicalDetailsCount=3`
  - toggle case: `clickup_enabled=true`
  - Telegram link start: `linkStarts=1`, code visible
  - loading, empty, and error states passed
- Screenshots/logs:
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1334-tools-capability-strip\report.json`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1334-tools-capability-strip\screenshots\desktop-tools.png`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1334-tools-capability-strip\screenshots\mobile-tools.png`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1334-tools-capability-strip\screenshots\mobile-integrations.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: Tools route as a clear backend capability directory with explicit user control and provider posture.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Tools item cards, decision pills, technical details disclosure.
- New pattern introduced: compact `aion-tools-capability-strip` inside Tools item cards.
- State checks: full, toggle, Telegram link start, loading, empty, error.
- Responsive checks: desktop, tablet, mobile for `/tools` and `/integrations`.
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`.
- Parity evidence: screenshot gate passed for 6 Tools/Integrations screenshots.

## Architecture Evidence
- Architecture source reviewed: `/app/tools/overview` backend policy, Tools API route/schema, frontend API types, subagent backend/frontend reports.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is UI exposure of existing safe adapter fields.

## Result Report
- Task summary: Tools cards now surface capability, skill-binding, and source-count signals before the technical details disclosure.
- Files changed:
  - `web/src/components/tools.tsx`
  - `web/src/App.tsx`
  - `web/src/index.css`
  - `web/scripts/tools-directory-characterization.mjs`
- How tested: web build, Tools directory characterization, route-smoke screenshot/account proof for `/tools` and `/integrations`.
- What is incomplete: frontend fixtures still model only a 2-group/3-item subset while backend currently supports a broader Tools catalog; deeper skill-binding operation details remain a future slice.
- Next steps: align Tools route-smoke/characterization fixtures to the broader backend contract, then enrich technical details with allowed operations, execution owner, authority, and all next actions.

## Autonomous Loop Evidence
### 1. Analyze Current State
- `/app/tools/overview` already supplied safe capability metadata, but primary Tools cards hid most of it in details.

### 2. Select One Priority Mission Objective
- Selected task: make per-tool backend capability mapping visible in the primary card without broad redesign.

### 3. Plan Implementation
- Reuse existing Tools item card data and add a narrow count strip before current status details.

### 4. Execute Implementation
- Added localized labels, new card strip rendering, CSS, and characterization assertions.

### 5. Verify and Test
- Build PASS.
- Tools characterization PASS.
- `/tools,/integrations` screenshot/account route-smoke PASS.

### 6. Self-Review
- No backend contract changes.
- No raw provider payloads or env names exposed.
- The primary UI gained truthful backend coverage without turning into an admin/debug panel.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Active mission, task board, project state, delivery map, requirement matrix, module confidence, quality/risk/system health, agent eval, and next steps updated in the same cycle.
