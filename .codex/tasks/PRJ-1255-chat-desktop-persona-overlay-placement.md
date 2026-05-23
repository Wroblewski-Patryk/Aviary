# Task

## Header
- ID: PRJ-1255
- Title: Chat desktop persona-stage overlay placement
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1254
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1255
- Quality Scenario Rows: QA-UX-1255
- Risk Rows: RISK-UI-1255
- Iteration: 1255
- Operation Mode: TESTER
- Mission ID: PRJ-1255-chat-desktop-persona-overlay-placement
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
- Mission objective: place desktop Chat's Planning overlay as a persona-stage annotation instead of anchoring it to the transcript-facing lower-left edge.
- Release objective advanced: v1.2 web Chat canonical desktop persona-stage composition.
- Included slices: CSS-only desktop overlay placement, width, and material tuning inside the portrait panel.
- Explicit exclusions: no transcript layout, composer behavior, source markers, cognitive belt density, mobile Chat rail, backend data, route behavior, Dashboard, or Personality changes.
- Checkpoint cadence: CSS patch, Chat screenshot gate, optional chat transcript proof, navigation/account proof, cleanup, source-of-truth update.
- Stop conditions: overlay covers face/core figure awkwardly, transcript/composer changes, source markers regress, mobile Chat rail regresses, or document overflow appears.
- Handoff expectation: next checkpoint should pick one exact route mismatch or request a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, task board | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Pascal subagent | canonical Chat v5, latest screenshots | Read-only refinement | Selector guidance | Report integrated | DONE |
| QA/Test | Parfit subagent | route-smoke scripts, cleanup notes | Read-only validation plan | Commands and pitfalls | DONE |
| Frontend/UX | Active chat | canonical screenshot, `docs/ux/design-memory.md` | `web/src/index.css` | CSS-only overlay placement pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
`PRJ-1253` quieted the desktop Chat cognitive belt. Faraday's UX lane then identified the next concrete mismatch: the Planning overlay on the persona stage sits on the transcript-facing lower-left edge, while the canonical Chat v5 reference composes persona-stage annotations around the figure's right/bottom side.

## Goal
Move and quiet the desktop Chat Planning overlay so the persona stage feels intentionally annotated and less pulled toward the transcript gutter.

## Scope
- `web/src/index.css`
- Route/surface: `/chat`
- Selectors: `.aion-chat-portrait-overlay`, `.aion-chat-portrait-overlay-facts`, `.aion-chat-portrait-panel`, `.aion-chat-portrait-note-*`

## Implementation Plan
1. Keep `ChatPortraitPanel` component and data unchanged.
2. On desktop, move `.aion-chat-portrait-overlay` away from the lower-left transcript-facing edge toward the lower-right/bottom persona annotation zone.
3. Preserve mobile/tablet placement rules unless screenshot proof requires adjustment.
4. Run focused Chat screenshots, build, chat transcript proof, navigation/account proof, `git diff --check`, and cleanup checks.
5. Update source-of-truth state and design memory before closure.

## Acceptance Criteria
- Desktop Planning overlay reads as part of the persona-stage annotation system.
- Overlay no longer pulls attention toward the transcript gutter.
- Persona face/core figure remains unobstructed.
- Transcript, composer, source markers, cognitive belt, and mobile rail remain functionally stable.
- Chat desktop/tablet/mobile screenshot gate passes.

## Definition of Done
- [x] CSS-only Chat persona overlay patch is implemented.
- [x] Chat desktop/tablet/mobile screenshot gate passes.
- [x] Build and relevant Chat proof pass.
- [x] Cleanup checks are recorded.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing transcript content, source markers, source mapping, composer behavior, cognitive belt density, mobile Chat rail, backend data, Dashboard, Personality, or canonical assets
- hiding supported persona-stage annotations

## Validation Evidence
- Tests:
  - `npm run build` in `web/` -> PASS.
  - `node scripts\route-smoke.mjs --screenshots C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1255-chat-desktop-persona-overlay\screenshots --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1255-chat-desktop-persona-overlay\report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `route_count=14`, `status=ok`, `screenshot_count=3`, `failed_count=0`.
  - `npm run test:chat-transcript` -> PASS, `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`.
  - `node scripts\route-smoke.mjs --navigation-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1255-chat-desktop-persona-overlay\navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`.
  - `node scripts\route-smoke.mjs --account-proof --report C:\Personal\Projekty\Aplikacje\Personality\.codex\artifacts\prj1255-chat-desktop-persona-overlay\account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Desktop Chat screenshot reviewed against `aion-chat-canonical-reference-v5.png`: Planning overlay now reads as a lower-right persona-stage annotation instead of a transcript-facing lower-left label stack.
  - Tablet screenshot keeps the same right/bottom annotation relationship without overlap.
  - Mobile screenshot remains stable with no document-level horizontal overflow.
- Screenshots/logs:
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/screenshots/desktop-chat.png`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/screenshots/tablet-chat.png`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/screenshots/mobile-chat.png`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/report.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/navigation-proof.json`
  - `.codex/artifacts/prj1255-chat-desktop-persona-overlay/account-proof.json`
- Cleanup:
  - No validation-owned node/Vite, route-smoke, or chat-transcript process remained.
  - No active `chrome-headless-shell` or `chromium` process remained.
  - No listener on ports `5173` or `4173`.
  - Three fresh route-smoke temp profiles from this checkpoint were removed.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`; `.codex/artifacts/prj1253-chat-desktop-cognitive-belt/screenshots/desktop-chat.png`
- Canonical visual target: desktop persona-stage annotations around the figure's right/bottom composition rather than transcript-facing lower-left.
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-chat-portrait-overlay`
- New shared pattern introduced: no
- Design-memory update required: yes
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: full Chat 95% pixel parity, exact icon metaphors, fixture copy/content, and richer data alignment remain separate decisions.
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation/account proof

## Result Report
- Task summary: moved the desktop/tablet Chat Planning overlay from the transcript-facing lower-left edge to a lower-right persona-stage annotation position.
- Files changed: `web/src/index.css`; project task, state, requirement, quality, risk, design-memory, and coordination ledgers.
- How tested: build, focused Chat desktop/tablet/mobile screenshot gate, chat transcript characterization, navigation proof, account proof, screenshot review, `git diff --check`, and cleanup checks.
- What is incomplete: not a full 95% Chat pixel parity claim; exact canonical icon/content/data parity remains separate.
- Next steps: pick one exact remaining screenshot mismatch on one route, or make a content/data decision before changing fixture copy, icon metaphors, or backend-backed labels.
- Decisions made: keep `ChatPortraitPanel` markup/data unchanged; keep mobile placement stable by explicitly resetting `right: auto` in the mobile override.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: desktop Chat overlay is compositionally attached to the transcript gutter.
- Gaps: no backend/API or component work needed.
- Inconsistencies: canonical Chat v5 places persona annotations around the right/bottom figure composition.
- Architecture constraints: preserve existing route/component/data contracts.

### 2. Select One Priority Mission Objective
- Selected task: PRJ-1255 Chat desktop persona overlay placement.
- Priority rationale: it is the first explicit next-step item in `.agents/state/next-steps.md` from Faraday's UX lane.
- Why other candidates were deferred: exact content/icon parity requires product decisions; recent Chat/Personality hierarchy slices are verified.

### 3. Plan Implementation
- Files or surfaces to modify: `web/src/index.css`.
- Logic: CSS-only overlay placement and material tuning.
- Edge cases: face occlusion, source-marker/transcript regression, mobile rail regression, z-index conflicts, overflow.

### 4. Execute Implementation
- Implementation notes: adjusted `.aion-chat-portrait-overlay` base placement to `right`/lower `bottom`, slightly widened the annotation, and added a mobile override reset so narrow Chat keeps its existing placement.

### 5. Verify and Test
- Validation performed: build, focused Chat screenshot gate, chat transcript characterization, navigation proof, account proof, `git diff --check`, screenshot review, and cleanup checks.
- Result: verified.

### 6. Self-Review
- Simpler option considered: only moving the existing overlay placement, without component or copy changes.
- Technical debt introduced: no
- Scalability assessment: route-local CSS remains bounded to the existing Chat portrait pattern.
- Refinements made: mobile override now resets `right` so the desktop placement does not leak into the narrow layout.

### 7. Update Documentation and Knowledge
- Docs updated: `docs/ux/design-memory.md`
- Context updated: task board, project state, active mission, current focus, next steps, module confidence ledger, requirements matrix, quality scenarios, risk register, system health, and agent evals.
- Learning journal updated: not applicable
