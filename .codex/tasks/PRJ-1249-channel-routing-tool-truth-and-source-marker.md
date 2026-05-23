# Task

## Header
- ID: PRJ-1249
- Title: Channel routing truth and chat source marker
- Task Type: fix
- Current Stage: release
- Status: DONE
- Owner: Backend Builder + Frontend Builder + QA/Test
- Priority: P1
- Module Confidence Rows: AVIARY-COGNITIVE-RUNTIME-001, AVIARY-WEB-RESP-001
- Requirement Rows: Shared Communication Governance Contract, Shared App Chat Transcript Contract, Durable Capability-Record Contract
- Mission ID: PRJ-1249-channel-routing-tool-truth-and-source-marker
- Mission Status: VERIFIED

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the current builder iteration.
- [x] The task is aligned with repository source-of-truth documents.
- [x] `.agents/core/project-memory-index.md` was reviewed.
- [x] `.agents/core/mission-control.md` was reviewed for long-running work.
- [x] Affected module confidence rows were identified.
- [x] Affected requirement, quality scenario, and risk rows were identified.
- [x] The task improves release confidence, not only local code appearance.

## Mission Block
- Mission objective: make Aviary truthful about action-owned web knowledge tools and visibly distinguish app versus Telegram transcript messages in the first-party chat.
- Release objective advanced: v1.2 web/runtime communication continuity confidence.
- Included slices: backend expression truthfulness, transcript channel projection, web Chat source marker, focused validation, state sync.
- Explicit exclusions: no new connector provider, no Telegram credential activation, no live Telegram smoke, no notification fan-out redesign, no second chat store.
- Checkpoint cadence: implementation, validation, state sync.
- Stop conditions: architecture mismatch in action ownership, failing channel transcript contract, or validation blocker needing credentials.
- Handoff expectation: task result report, validation evidence, updated mission/state files.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Expected output | Required proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, active mission, contracts | Integration, task closure, memory updates | Parent decision and final acceptance | Backend + web focused gates | DONE |
| Architecture | Coordinator + backend explorer | `docs/architecture/15_runtime_flow.md`, `docs/architecture/16_agent_contracts.md` | Contract alignment | No mismatch, minimal patch scope | Source review | DONE |
| Backend/API | Coordinator | `backend/app/expression/generator.py`, `backend/app/memory/repository.py`, tests | Truthfulness and channel projection guardrails | No false capability-denial when tool hints are loaded; Telegram-delivered assistant rows project as Telegram | Focused pytest | DONE |
| Frontend/UX | Coordinator | `web/src/components/chat.tsx`, `web/src/App.tsx`, `web/src/index.css` | Source marker in transcript metadata | App/Telegram marker visible without new transcript store | Build + chat characterization + screenshots | DONE |
| QA/Test | Coordinator | backend/web tests | Regression proof | Commands and cleanup evidence | PASS | DONE |
| Documentation/Memory | Coordinator | `.agents/state/*`, `.codex/context/*` | Durable mission state | Future-session handoff | Source-of-truth diff review | DONE |

## Context
The user showed an Aviary conversation where the assistant incorrectly denied web search/browser capability and did not understand channel routing expectations. Architecture already defines the first-party app as the canonical transcript owner, Telegram as a linked transport mirror, expression as wording owner, and action/delivery as side-effect owner.

## Goal
Ensure Aviary does not deny bounded action-owned search/page-read capability when runtime foreground awareness marks those tools as available, and ensure the first-party chat transcript visibly marks whether each message came through the app or Telegram.

## Scope
- Backend: `backend/app/expression/generator.py`, `backend/app/memory/repository.py`, focused tests in `backend/tests/`
- Web: `web/src/components/chat.tsx`, `web/src/App.tsx`, `web/src/index.css`, `web/scripts/chat-transcript-characterization.mjs`
- Docs/state: this task file and mission/context state

## Implementation Plan
1. Add expression self-review for false web-search/page-read capability denial when `ContextOutput.available_tool_hints` is populated.
2. Preserve the action boundary by returning a correction message rather than executing tools from expression.
3. Project assistant transcript channel from delivered transport, so scheduler-originated Telegram delivery displays as `telegram`.
4. Render a compact source marker in the existing chat message metadata row.
5. Extend focused backend and web characterization tests.
6. Run build, route screenshot, focused pytest, and cleanup checks.

## Acceptance Criteria
- App-originated `/app/chat/message` stays `reply.channel == "api"` and does not call Telegram delivery.
- Telegram-originated or Telegram-delivered transcript rows are marked `telegram`.
- Web chat renders `App` and `Telegram` markers in message metadata.
- Focused backend and web validation passes.

## Definition of Done
- [x] Backend truthfulness guardrail covers bounded search/page-read denial.
- [x] Chat transcript displays a compact source marker for app/API versus Telegram.
- [x] Focused backend and web validation pass.
- [x] Relevant source-of-truth state files are updated.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_expression_agent.py::test_expression_rewrites_false_web_tool_capability_denial tests/test_expression_agent.py::test_expression_rewrites_english_false_web_tool_capability_denial tests/test_api_routes.py::test_app_chat_message_runs_runtime_under_authenticated_user tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order tests/test_memory_repository.py::test_memory_repository_hides_scheduler_internal_prompt_but_keeps_delivered_scheduler_reply tests/test_runtime_pipeline.py::test_runtime_pipeline_projects_shared_transcript_for_api_and_telegram_turns_under_same_user tests/test_runtime_pipeline.py::test_runtime_pipeline_keeps_scheduler_prompt_out_of_shared_transcript_while_preserving_delivered_reply; Pop-Location` -> PASS, `7 passed`
  - `Push-Location .\web; npm run build; Pop-Location` -> PASS
  - `Push-Location .\web; npm run test:chat-transcript; Pop-Location` -> PASS, `status=ok`, `appSourceCount=2`, `telegramSourceCount=2`
  - `node web/scripts/route-smoke.mjs --screenshots .codex/artifacts/prj1249-channel-source-marker/screenshots --report .codex/artifacts/prj1249-channel-source-marker/chat-route-report.json --screenshot-routes /chat --viewports desktop,tablet,mobile --fail-on-ui-findings` -> PASS, `status=ok`, `screenshot_count=3`, `failed_count=0`
  - `git diff --check` -> PASS with LF/CRLF warnings only
- Manual checks: source review against communication/channel contracts
- Screenshots/logs: `.codex/artifacts/prj1249-channel-source-marker/`
- High-risk checks: live Telegram credential smoke not run because no credential activation or live Telegram delivery was in scope.
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/15_runtime_flow.md`, `docs/architecture/16_agent_contracts.md`, `docs/implementation/runtime-reality.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Follow-up architecture doc updates: none required; implementation now better matches existing contracts.

## UX/UI Evidence
- Design source type: approved_snapshot
- Design source reference: existing Chat transcript meta row
- Fidelity target: structurally_faithful
- Existing shared pattern reused: `aion-chat-message-meta`
- New shared pattern introduced: no
- Screenshot comparison pass completed: yes
- Remaining mismatches: no source-marker regression found in focused proof
- Responsive checks: desktop | tablet | mobile
- Accessibility checks: source marker is text in the existing metadata row; delivery state remains aria-labeled icon.
- Parity evidence: route-smoke `/chat` screenshots across desktop/tablet/mobile passed.

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert the touched backend expression/transcript projection and web chat marker files.
- Observability or alerting impact: none

## Result Report
- Task summary: backend expression now corrects false denial of action-owned web knowledge tools when foreground awareness says they are available; app chat now renders source markers; transcript projection marks delivered Telegram assistant outreach as Telegram.
- Files changed: backend expression/transcript projection and focused tests;
  web Chat transcript source marker, styles, and characterization test;
  source-of-truth state files.
- How tested: focused backend pytest, web build, chat transcript characterization, focused Chat route screenshot gate.
- What is incomplete: live Telegram credential smoke was out of scope.
- Next steps: keep live Telegram credential smoke as a separate operator-gated task; continue UI polish as single-route screenshot checkpoints.
