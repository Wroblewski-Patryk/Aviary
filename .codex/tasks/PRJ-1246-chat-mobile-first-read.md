# Task

## Header
- ID: PRJ-1246
- Title: Chat mobile first-read compression
- Task Type: design
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1245
- Priority: P1
- Module Confidence Rows: AVIARY-WEB-RESP-001
- Requirement Rows: REQ-UX-1246
- Quality Scenario Rows: QA-UX-1246
- Risk Rows: RISK-UI-1246
- Iteration: 1246
- Operation Mode: BUILDER
- Mission ID: PRJ-1246-chat-mobile-first-read
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
- Mission objective: make mobile Chat reach the conversation faster by compressing the cognitive belt into a horizontal context rail.
- Release objective advanced: v1.2 web mobile Chat canonical usability.
- Included slices: mobile-only Chat cognitive belt layout and card density.
- Explicit exclusions: no desktop/tablet changes, no backend/API changes, no new data, no route behavior changes, no composer changes, no hiding supported actions.
- Checkpoint cadence: one CSS patch, Chat screenshot gate, full route smoke, navigation/account proof, state update.
- Stop conditions: horizontal document overflow, unreadable belt labels, transcript pushed lower, route failure, or account/navigation regression.
- Handoff expectation: next checkpoint should be another single route/screenshot mismatch or a content/data decision.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, canonical UX docs | Integration, docs/state, final decision | Parent acceptance integrated | Validation gate passed | DONE |
| UX Parity | Gibbs subagent | Chat mobile screenshot/reference | Read-only mobile Chat audit | Confirmed mobile belt rail is the smallest useful checkpoint | Report integrated | DONE |
| QA/Test | Chandrasekhar subagent | route-smoke scripts | Validation plan | Sequential validation pack and cleanup risks | Commands executed | DONE |
| Frontend/UX | Active chat | screenshots, design memory | `web/src/index.css` | CSS-only mobile Chat pass | Fresh screenshots passed | DONE |
| Documentation/Memory | Active chat | state/context ledgers | Task, mission, ledgers | Durable handoff | Source-of-truth diff | DONE |

## Context
PRJ-1245 flattened Chat's secondary chrome, but mobile Chat still stacks two cognitive-belt cards before the transcript, making the first read feel more like route status than conversation.

## Goal
Preserve context while moving mobile Chat closer to conversation-first behavior by showing the cognitive belt as a compact horizontal rail on narrow screens.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep the implementation CSS-only and mobile Chat-specific

## Definition of Done
- [x] Mobile Chat cognitive belt is compressed without hiding supported data.
- [x] Build passes.
- [x] Chat desktop/tablet/mobile screenshot gate passes.
- [x] Full route smoke, navigation proof, and account proof pass.
- [x] Project state and confidence ledgers are updated.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- adding or hiding controls, fake data, unsupported cards, or product rename

## Validation Evidence
- Tests:
  - `node --check scripts/route-smoke.mjs` -> PASS
  - `npm run build` in `web/` -> PASS
  - `node scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1246-chat-mobile-first-read/screenshots --report .codex/artifacts/prj1246-chat-mobile-first-read/chat-responsive-report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `screenshot_count=3`, `failed_count=0`
  - `node scripts/route-smoke.mjs --report .codex/artifacts/prj1246-chat-mobile-first-read/route-smoke-report.json` -> PASS, `route_count=14`, `status=ok`
  - `node scripts/route-smoke.mjs --navigation-proof --report .codex/artifacts/prj1246-chat-mobile-first-read/navigation-proof.json` -> PASS, `step_count=4`, `failed_count=0`
  - `node scripts/route-smoke.mjs --account-proof --report .codex/artifacts/prj1246-chat-mobile-first-read/account-proof.json` -> PASS, `step_count=1`, `failed_count=0`, `panel_visible=true`
  - `git diff --check` -> PASS with LF/CRLF warning only
- Manual checks:
  - Reviewed mobile Chat screenshot and confirmed the cognitive belt now reads as a compact horizontal rail with transcript and composer appearing sooner.
  - Cleanup checks found no validation-owned `route-smoke.mjs`, `chrome-headless-shell`, or 5173/4173 listener leftovers.
- Screenshots/logs:
  - `.codex/artifacts/prj1246-chat-mobile-first-read/screenshots/mobile-chat.png`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/screenshots/tablet-chat.png`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/screenshots/desktop-chat.png`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/chat-responsive-report.json`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/route-smoke-report.json`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/navigation-proof.json`
  - `.codex/artifacts/prj1246-chat-mobile-first-read/account-proof.json`
- Module confidence ledger updated: yes
- Requirements matrix updated: yes
- Quality scenarios updated: yes
- Risk register updated: yes
- Reality status: verified

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: `docs/ux/assets/aion-chat-canonical-reference-v5.png`
- Canonical visual target: mobile Chat conversation-first first read
- Fidelity target: structurally_faithful
- Existing shared pattern reused: Chat cognitive belt, transcript, composer, portrait stage
- New shared pattern introduced: no
- Visual gap audit completed: yes
- Screenshot comparison pass completed: yes
- Remaining mismatches: exact canonical icon/content/copy parity remains a separate content/data decision
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: route-smoke unnamed interactive audit, navigation proof, account proof
