# PRJ-1333 - Chat Empty Transcript Truth

## Header
- ID: PRJ-1333
- Title: Chat empty transcript truth
- Task Type: design
- Current Stage: verification
- Status: DONE
- Owner: Coordinator + Frontend Builder
- Priority: P1
- Requirement Rows: REQ-UX-1333
- Module Confidence Rows: AVIARY-WEB-CHAT-EMPTY-001, AVIARY-WEB-RESP-001
- Mission ID: PRJ-1331-backend-capability-to-final-personality-ui
- Mission Status: CHECKPOINTED

## Context
The active mission maps backend capabilities into a magical, truthful Aviary UI. Backend/API and frontend chat lanes confirmed that `/app/chat/history` returns `items: []` for a truly empty transcript, but the web UI rendered three fake `preview-*` messages as if they were conversation history.

## Goal
Remove fake chat transcript rows for empty backend history and replace them with a beautiful, localized, truthful first-message state.

## Scope
- `web/src/App.tsx`
- `web/src/components/chat.tsx`
- `web/src/index.css`
- `web/scripts/chat-transcript-characterization.mjs`
- `web/scripts/route-smoke.mjs`
- Chat transcript empty state only

## Implementation Plan
1. Keep backend/API and frontend lane reports read-only.
2. Remove the `visibleTranscriptItems` demo fallback and preview mode from real chat rendering.
3. Add localized empty transcript copy for EN/PL/DE.
4. Add a reusable `ChatTranscriptEmptyState` component.
5. Render empty state only when backend history loading has completed and `transcriptItems.length === 0`.
6. Update chat transcript characterization to assert empty history has no fake rows.
7. Add a route-smoke `--empty-chat-history` proof mode for screenshot validation.

## Acceptance Criteria
- Empty `/app/chat/history` renders zero `.aion-chat-message-row` items.
- Empty transcript renders one designed empty state and one starter action.
- Existing full transcript and optimistic send states still pass characterization.
- Chat route remains stable across desktop, tablet, and mobile with normal and empty history fixtures.
- No backend contract changes.

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; ...; npm run test:chat-transcript; ...` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --screenshots ..\.codex\artifacts\prj1333-chat-empty-truth\screenshots --report ..\.codex\artifacts\prj1333-chat-empty-truth\report.json --screenshot-routes /chat,/dashboard --viewports desktop,tablet,mobile --account-proof; ...` -> PASS
  - `Push-Location .\web; node scripts/route-smoke.mjs --empty-chat-history --screenshots ..\.codex\artifacts\prj1333-chat-empty-truth\empty-screenshots --report ..\.codex\artifacts\prj1333-chat-empty-truth\empty-report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --account-proof; ...` -> PASS
- Characterization:
  - empty case: `rowCount=0`, `emptyStateCount=1`, `emptyActionCount=1`, `previewMetaCount=0`, `previewCopyCount=0`
  - full case: `rowCount=4`, `appSourceCount=2`, `telegramSourceCount=2`
  - send case: optimistic `sendingCount=1`, delivered `rowCount=2`
- Screenshots/logs:
  - `.codex/artifacts/prj1333-chat-empty-truth/report.json`
  - `.codex/artifacts/prj1333-chat-empty-truth/empty-report.json`
  - `.codex/artifacts/prj1333-chat-empty-truth/empty-screenshots/desktop-chat.png`
  - `.codex/artifacts/prj1333-chat-empty-truth/empty-screenshots/tablet-chat.png`
  - `.codex/artifacts/prj1333-chat-empty-truth/empty-screenshots/mobile-chat.png`
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/canonical-ui-layout-index.md`, `docs/ux/visual-direction-brief.md`, `docs/ux/design-memory.md`
- Canonical visual target: conversation-first Chat surface with truthful backend transcript state.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Chat transcript shell and composer
- New shared pattern introduced: `ChatTranscriptEmptyState`
- State checks: loading, empty, full transcript, optimistic send, delivered send
- Responsive checks: desktop, tablet, mobile
- Accessibility checks: route-smoke found `unnamedInteractiveCount=0`
- Parity evidence: empty Chat screenshot gate passed for 3 viewports.

## Architecture Evidence
- Architecture source reviewed: `/app/chat/history` and `/app/chat/message` contracts, backend tests, frontend chat transcript model, subagent reports.
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none; this is UI truth mapping over an existing endpoint.

## Result Report
- Task summary: Chat no longer fabricates preview transcript rows when backend history is empty.
- Files changed:
  - `web/src/App.tsx`
  - `web/src/components/chat.tsx`
  - `web/src/index.css`
  - `web/scripts/chat-transcript-characterization.mjs`
  - `web/scripts/route-smoke.mjs`
- How tested: web build, chat characterization, normal route-smoke screenshot/account proof, empty-history screenshot/account proof.
- What is incomplete: full backend capability coverage remains a multi-slice mission; Tools/Integrations, connector confirmation history, and module metric derivation remain future slices.
- Next steps: deepen Tools/Integrations capability mapping or connector confirmation history.

## Autonomous Loop Evidence
### 1. Analyze Current State
- The frontend rendered fake preview messages when backend history returned `items: []`.

### 2. Select One Priority Mission Objective
- Selected task: make Chat empty transcript truthful while preserving full transcript and send states.

### 3. Plan Implementation
- Use the existing `transcriptItems` model and replace only the empty rendering branch.

### 4. Execute Implementation
- Removed demo fallback messages, added localized empty copy, reusable component, styling, and test harness updates.

### 5. Verify and Test
- Build PASS.
- Chat transcript characterization PASS.
- Normal and empty-history route-smoke screenshot gates PASS.

### 6. Self-Review
- No backend changes.
- No fake messages remain in empty transcript state.
- Pending connector and send states remain backend/client-boundary honest.

### 7. Update Documentation and Knowledge
- Task artifact created.
- Active mission, task board, project state, delivery map, requirement matrix, module confidence, quality/risk/system health, and next steps updated in the same cycle.
