# Task

## Header
- ID: PRJ-1253
- Title: Chat desktop cognitive belt quieting
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1252
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1253
- Quality Scenario Rows: QA-UX-1253
- Risk Rows: RISK-UI-1253
- Iteration: 1253
- Operation Mode: BUILDER
- Mission ID: PRJ-1253-chat-desktop-cognitive-belt-quieting
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] Affected module confidence, requirement, quality, and risk rows were identified.
- [x] The task improves release confidence, not only local appearance.

## Mission Block
- Mission objective: make desktop Chat's cognitive belt flatter and visually secondary to the transcript/persona stage.
- Release objective advanced: v1.2 web Chat canonical desktop first-read quality.
- Included slices: CSS-only desktop/large-screen belt card size, material, typography, meta, and progress tuning.
- Explicit exclusions: no Chat copy, source markers, transcript fixtures, persona image, shared shell, mobile rail, backend data, or route behavior changes.
- Checkpoint cadence: CSS patch, Chat screenshot gate, build, chat transcript test, navigation/account proof if needed, cleanup, source-of-truth update.
- Stop conditions: source markers regress, mobile Chat rail regresses, transcript readability regresses, document overflow appears, or any supported belt item disappears.
- Handoff expectation: next checkpoint should pick one exact route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Halley subagent | canonical Chat asset, latest screenshots | Read-only priority report | Checkpoint recommendation | Report integrated | DONE |
| QA/Test | Fermat subagent | route-smoke scripts, cleanup notes | Read-only validation plan | Commands and pitfalls | Report integrated | DONE |
| Frontend/UX | Active chat | canonical screenshot, `docs/ux/design-memory.md` | `web/src/index.css` | CSS-only Chat belt pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
`PRJ-1250` quieted the Chat transcript source marker, while Dashboard and Personality received verified mobile passes in `PRJ-1251` and `PRJ-1252`. The latest desktop Chat screenshot still shows the top cognitive belt as six chunky text cards. The canonical Chat v5 reference treats the belt as flatter, icon-led support metadata above the transcript/persona stage.

## Goal
Reduce desktop Chat cognitive-belt visual weight while preserving every supported item, all labels/values, source markers, transcript behavior, and mobile rail behavior.

## Scope
- `web/src/index.css`
- Route/surface: `/chat`
- Selectors: `.aion-chat-cognitive-belt`, `.aion-chat-belt-card`, `.aion-chat-belt-card-head`, `.aion-chat-belt-eyebrow`, `.aion-chat-belt-meta`, `.aion-chat-belt-title`, `.aion-chat-belt-body`, `.aion-chat-belt-progress`

## Implementation Plan
1. Keep `ChatCognitiveBelt` component and item data unchanged.
2. Tune large-screen belt cards to lower height, lighter material, tighter type, and quieter meta chips.
3. Preserve mobile/tablet-specific rail behavior unless screenshot proof shows a regression.
4. Run focused Chat screenshots, build, chat transcript test, navigation/account proof as needed, and cleanup checks.
5. Update source-of-truth state and design memory before closure.

## Acceptance Criteria
- Desktop Chat cognitive belt reads as support metadata, not six competing cards.
- All supported belt items, labels, values, and progress remain visible.
- Transcript, composer, source marker, persona panel, and mobile rail behavior are unchanged in function.
- Chat desktop/tablet/mobile screenshot gate passes.
- Build, `test:chat-transcript`, navigation/account proof if applicable, `git diff --check`, and cleanup checks pass.

## Definition of Done
- [x] CSS-only Chat cognitive-belt patch is implemented.
- [x] Chat desktop/tablet/mobile screenshot gate passes.
- [x] Build and `npm run test:chat-transcript` pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing Chat copy, transcript fixture content, source mapping, source labels, backend-backed data, route behavior, shared shell, Dashboard, Personality, persona image, or canonical assets
- hiding supported belt items

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS.
  - `node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1253-chat-desktop-cognitive-belt\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1253-chat-desktop-cognitive-belt\report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`.
  - `npm run test:chat-transcript` -> first run hit a CDP `Page.navigate` timeout; immediate rerun passed with `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`.
  - `node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1253-chat-desktop-cognitive-belt\navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1253-chat-desktop-cognitive-belt\account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Desktop Chat screenshot reviewed against `aion-chat-canonical-reference-v5.png`: the belt is flatter, lower, and visually secondary to the transcript/persona stage.
  - Tablet and mobile screenshots reviewed for no route-level overflow; mobile rail remains horizontally scrollable and functional.
- Screenshots/logs:
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/desktop-chat.png`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/tablet-chat.png`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/mobile-chat.png`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/report.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/navigation-proof.json`
  - `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/account-proof.json`
- Cleanup:
  - No active Personality/Aviary `node.exe` route-smoke, chat-transcript, or Vite validation process found after checks.
  - No active `chrome-headless-shell` process remained on final check.
  - No listener on ports `5173` or `4173`.
  - Six fresh route-smoke temp profiles from this checkpoint were removed; older historical temp profiles were left untouched.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`; `.codex/artifacts/prj1250-chat-source-marker-polish/screenshots/desktop-chat.png`
- Canonical visual target: desktop cognitive belt as a flat, secondary support strip above the transcript/persona stage.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-chat-cognitive-belt`
- New shared pattern introduced: no
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical icon metaphors and content parity remain separate content/data decisions; this slice is a verified hierarchy/density pass.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof

## Result Report
- Task summary: quieted desktop Chat cognitive belt so it supports the transcript/persona stage instead of competing as six heavy text cards.
- Files changed: `web/src/index.css`; project state, task, requirement, quality, risk, design-memory, and coordination ledgers.
- How tested: build, focused Chat desktop/tablet/mobile screenshot gate, `test:chat-transcript`, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- What is incomplete: not a full 95% pixel parity claim; exact icon metaphors, fixture copy, and richer content/data alignment remain separate product/data decisions.
- Next steps: choose one exact remaining screenshot mismatch on one route, or make a content/data decision before changing canonical labels, icons, source labels, or route fixture content.
- Decisions made: keep all Chat belt items and transcript/source behavior unchanged; use CSS-only card density/material/type tuning.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: desktop Chat cognitive belt is still more card-heavy than canonical v5.
- Gaps: no backend/API work needed; the existing component already contains the supported metadata.
- Inconsistencies: canonical belt is flatter and secondary, while current belt competes with the transcript/persona stage.
- Architecture constraints: preserve existing data and route/component contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1253 Chat desktop cognitive belt quieting.
- Priority rationale: the UX parity lane identified this as the next concrete route-local mismatch after Dashboard/Personality mobile passes.
- Why other candidates were deferred: exact canonical icon/content parity requires separate content decisions; Personality timeline rail is still valid but lower priority than balancing the three flagship surfaces.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only large-screen belt density and hierarchy tuning.
- Edge cases: mobile rail regression, hidden labels, low contrast, source-marker/transcript regression, overflow.

### 4. Execute Implementation
- Implementation notes: reduced desktop belt card height, radius, material weight, shadow, typography scale, meta-chip weight, and progress spacing; added a tiny noninteractive accent marker to reduce the all-text-card feel without changing component data.

### 5. Verify and Test
- Validation performed: build, focused Chat screenshot gate across desktop/tablet/mobile, chat transcript characterization, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- Result: PASS; `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`; transcript rerun `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`; navigation/account proof passed.

### 6. Self-Review
- Simpler option considered: hiding belt body copy would reduce density faster, but it would remove supported context and make the belt less truthful.
- Technical debt introduced: no
- Scalability assessment: CSS-only route-local change stays inside the existing Chat cognitive-belt pattern and does not add a new component family.
- Refinements made: reduced the pseudo-marker after screenshot review showed the first version crowded the eyebrow labels.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`
- Context updated: `.codex/context/PROJECT_STATE.md`, `.codex/context/TASK_BOARD.md`, `.agents/state/active-mission.md`, `.agents/state/current-focus.md`, `.agents/state/next-steps.md`, `.agents/state/module-confidence-ledger.md`, `.agents/state/requirements-verification-matrix.md`, `.agents/state/quality-attribute-scenarios.md`, `.agents/state/risk-register.md`, `.agents/state/system-health.md`, `.agents/state/agent-evals.md`
- Learning journal updated: not applicable
