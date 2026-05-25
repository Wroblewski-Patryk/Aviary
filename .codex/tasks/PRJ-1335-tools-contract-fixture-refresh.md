# PRJ-1335 - Tools Contract Fixture Refresh

## Header
- ID: PRJ-1335
- Title: Tools contract fixture refresh
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1335
- Module Confidence Rows: AVIARY-WEB-TOOLS-CONTRACT-001, AVIARY-WEB-RESP-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
`PRJ-1334` surfaced safe Tools capability counts, but the frontend characterization and route-smoke fixtures still represented a smaller 2-group/3-item or 2-group/2-item catalog. Backend tests pin the real default `/app/tools/overview` catalog at 4 groups and 7 tools.

## Goal
Refresh Tools frontend proof fixtures toward the backend catalog and expose richer safe binding details behind the existing technical-details disclosure.

## Scope
- `web/scripts/tools-directory-characterization.mjs`
- `web/scripts/route-smoke.mjs`
- `web/src/components/tools.tsx`
- `web/src/index.css`

## Implementation Plan
1. Use read-only backend and frontend sidecar reports to confirm the current backend contract.
2. Expand Tools characterization fixture to 4 groups and 7 tools.
3. Expand route-smoke Tools overview mock to the same backend-shaped catalog.
4. Add disclosure-only rendering for binding allowed operations, execution owner, authority, and all next actions.
5. Update characterization assertions for group/item/toggle/chip/detail counts and binding metadata.
6. Fix any responsive overflow caused by longer backend action strings.
7. Validate build, characterization, and screenshot/account proof.

## Acceptance Criteria
- Tools characterization full state verifies 4 groups, 7 tools, 4 toggles, 21 capability chips, and 7 technical disclosures.
- Binding authority, allowed operations, and full next actions are present in disclosure content.
- Route-smoke `/app/tools/overview` fixture reports 4 groups and 7 tools with backend-like ready/blocked/link counts.
- `/tools` and `/integrations` remain stable across desktop, tablet, and mobile with no horizontal overflow.
- No backend changes.

## Validation Evidence
- Tests:
  - `Push-Location .\web; node --check scripts/tools-directory-characterization.mjs; node --check scripts/route-smoke.mjs; Pop-Location` -> PASS
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1335-tools-contract-fixture-refresh\screenshots --report ..\.codex\artifacts\prj1335-tools-contract-fixture-refresh\report.json --screenshot-routes /tools,/integrations --viewports desktop,tablet,mobile --account-proof --fail-on-ui-findings; Pop-Location` -> PASS
- Characterization:
  - full case: `groupCount=4`, `itemCount=7`, `toggleCount=4`, `capabilityChipCount=21`, `technicalDetailsCount=7`
  - binding metadata proof: `hasBindingAuthority=true`, `hasBindingOperations=true`, `hasFullNextAction=true`
  - toggle, Telegram link start, loading, empty, and error states passed
- Screenshots/logs:
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1335-tools-contract-fixture-refresh\report.json`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1335-tools-contract-fixture-refresh\screenshots\desktop-tools.png`
  - `C:\Personal\Projekty\Aplikacje\.codex\artifacts\prj1335-tools-contract-fixture-refresh\screenshots\mobile-tools.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: Tools route as a truthful backend capability directory.
- Fidelity target: structurally_faithful
- State checks: full, toggle, Telegram link start, loading, empty, error.
- Responsive checks: desktop, tablet, mobile for `/tools` and `/integrations`.
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`.
- Responsive repair: long backend next-action strings initially caused mobile `/tools` overflow; CSS now wraps route-local Tools action text and constrains Tools route children on mobile.

## Architecture Evidence
- Architecture source reviewed: `/app/tools/overview` backend policy and backend API tests.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is frontend proof alignment to an existing backend contract.

## Result Report
- Task summary: Tools proof fixtures now exercise the broader backend catalog and technical details expose safe binding metadata and full next actions.
- Files changed:
  - `web/scripts/tools-directory-characterization.mjs`
  - `web/scripts/route-smoke.mjs`
  - `web/src/components/tools.tsx`
  - `web/src/index.css`
- How tested: script syntax checks, web build, Tools characterization, strict route-smoke screenshot/account proof.
- What is incomplete: Integrations route still maps all tool items instead of filtering to external integrations/channels; richer user-facing copy for raw backend action IDs remains future polish.
- Next steps: filter Integrations provider map to true external surfaces and translate backend next-action IDs into calmer product copy where appropriate.

## Autonomous Loop Evidence
### 1. Analyze Current State
- Frontend proof used stale smaller Tools fixtures despite backend pinning a 4-group/7-item catalog.

### 2. Select One Priority Mission Objective
- Selected task: align Tools fixtures and proof with backend catalog before deeper product polish.

### 3. Plan Implementation
- Update proof data first, then enrich only existing disclosure surfaces.

### 4. Execute Implementation
- Expanded fixtures, added binding metadata and next-action disclosure rendering, and repaired mobile overflow.

### 5. Verify and Test
- Syntax checks, build, characterization, and strict screenshot/account route-smoke passed.

### 6. Self-Review
- No backend changes.
- No raw provider payloads or environment names exposed.
- Longer backend identifiers are still contained within disclosure/route-local wrapping.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Mission and state files updated in the same cycle.
