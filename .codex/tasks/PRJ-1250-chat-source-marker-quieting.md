# Task

## Header
- ID: PRJ-1250
- Title: Chat source marker visual quieting
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1249
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1250
- Quality Scenario Rows: QA-UX-1250
- Risk Rows: RISK-UI-1250
- Iteration: 1250
- Operation Mode: TESTER
- Mission ID: PRJ-1250-chat-source-marker-quieting
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` and active mission state were reviewed through the current mission packet.
- [x] Affected module confidence, requirement, quality, and risk rows were identified.
- [x] The task improves release confidence, not only local appearance.

## Mission Block
- Mission objective: keep Chat's `App` / `Telegram` transcript source marker visible while making it subordinate to speaker, time, and message content.
- Release objective advanced: v1.2 web Chat communication clarity and visual coherence.
- Included slices: CSS-only source marker material, spacing, and mobile quieting.
- Explicit exclusions: no source mapping changes, no backend/runtime changes, no component structure changes, no copy/data changes, no Dashboard/Personality/shared shell changes.
- Checkpoint cadence: one CSS patch, Chat screenshot gate, chat transcript characterization, full route smoke, navigation/account proof, state update.
- Stop conditions: source marker becomes hard to see, metadata wraps awkwardly, delivery status loses distinction, route failure, or account/navigation regression.
- Handoff expectation: next checkpoint should be another single route/screenshot mismatch or a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance | Validation gate | DONE |
| UX Parity | Sagan subagent | Chat screenshots and PRJ-1249 output | Read-only source-marker audit | Scope and risks | Report integrated | DONE |
| QA/Test | Copernicus subagent | route-smoke scripts | Validation plan | Commands and risks | Report integrated | DONE |
| Frontend/UX | Active chat | screenshots, design memory | `web/src/index.css` | CSS-only Chat marker pass | Fresh screenshots | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1249 added useful `App` / `Telegram` source truth to Chat metadata. Fresh screenshots show the teal source marker is clear but visually competes with speaker and message content in the dense transcript.

## Goal
Keep the source marker visible and truthful while reducing its visual weight so it reads as metadata, not a second primary accent.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation CSS-only and Chat-specific

## Definition of Done
- [x] Chat source marker is quieter but still visible.
- [x] Build and chat transcript characterization pass.
- [x] Chat desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- changing source labels, channel mapping, backend behavior, route fixture content, composer behavior, or product rename

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS.
  - `Push-Location .\web; npm run test:chat-transcript; Pop-Location` -> PASS, `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`, `deliveredCount=1`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --screenshots .codex/artifacts/prj1250-chat-source-marker-polish/screenshots --report .codex/artifacts/prj1250-chat-source-marker-polish/report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings; Pop-Location` -> PASS, `screenshot_count=3`, `failed_count=0`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --report .codex/artifacts/prj1250-chat-source-marker-polish/route-smoke-report.json; Pop-Location` -> PASS, `route_count=14`, `status=ok`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --navigation-proof --report .codex/artifacts/prj1250-chat-source-marker-polish/navigation-proof.json; Pop-Location` -> PASS, `step_count=4`, `failed_count=0`.
  - `Push-Location .\web; node scripts\route-smoke.mjs --account-proof --report .codex/artifacts/prj1250-chat-source-marker-polish/account-proof.json; Pop-Location` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`.
  - `git diff --check` -> PASS with LF/CRLF warning only.
- Manual checks:
  - Reviewed mobile Chat screenshot. The `App` source marker reads as a quiet metadata chip, remains visible, and does not wrap awkwardly.
  - Full route proof still reports the Dashboard mobile cognitive-flow rail as contained overflowing elements in the intentional rail, with no document-level horizontal overflow and no failed status.
- Screenshots/logs:
  - `.codex/artifacts/prj1250-chat-source-marker-polish/screenshots/mobile-chat.png`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/route-smoke-report.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/navigation-proof.json`
  - `.codex/artifacts/prj1250-chat-source-marker-polish/account-proof.json`
- Cleanup:
  - `npm run test:chat-transcript` emitted a transient Chrome profile `EBUSY` cleanup warning after successful proof.
  - Follow-up checks found no route-smoke, Vite, or 5173/4173 listener leftovers.
  - A later final cleanup check reported two stale `chrome-headless-shell`
    handles with empty command lines; `taskkill` reported `no running instance
    of the task`, so they were recorded as stale Windows handles rather than
    active validation work.
  - The locked temp profile directory was removed with targeted cleanup after confirming no owning process remained.
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: implementation_continuity
- Design source reference: PRJ-1249 Chat transcript source marker
- Canonical visual target: Chat metadata source truth as quiet support text
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-chat-message-meta`
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical copy/icon/content parity remains outside this CSS-only source-marker quieting slice
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof; marker remains text
