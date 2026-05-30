# Task

## Header
- ID: LUC-942
- Title: [Aviary][QA] Verify core chat API workflow (P0)
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: none
- Priority: P0
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-API-CHAT-WORKFLOW-001
- Requirement Rows: not applicable
- Quality Scenario Rows: not applicable
- Risk Rows: not applicable
- Iteration: 1
- Operation Mode: BUILDER
- Mission ID: LUC-691-preparation-baseline-reconciliation
- Mission Status: VERIFIED

## Context
Paperclip wake payload assigned `LUC-942` with explicit scope to verify core chat API workflow. This heartbeat is verification-only and must avoid broad implementation.

## Goal
Provide reproducible P0 evidence that the authenticated chat API workflow is green for:
- `GET /app/chat/history`
- `POST /app/chat/message`

## Scope
- In scope:
  - execute focused backend tests for app chat history/message workflow
  - record pass/fail evidence and sync source-of-truth state files
- Out of scope:
  - feature implementation
  - deployment/runtime mutation
  - unrelated full-suite validation

## Implementation Plan
1. Locate tests that exercise core app chat API workflow.
2. Run a focused pytest subset only for `app_chat_history` and `app_chat_message`.
3. Record evidence and update task/state artifacts.

## Acceptance Criteria
- Focused test subset passes with no failures.
- Evidence is stored in a dedicated `LUC-942` task packet.
- `TASK_BOARD` and `PROJECT_STATE` include this checkpoint.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Core chat API focused tests executed and passing
- [x] Evidence captured in task artifact
- [x] Source-of-truth state synchronized

## Validation Evidence
- Tests:
  - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_history or app_chat_message"; Pop-Location`
  - result: `9 passed, 123 deselected in 16.03s`
  - deterministic fixture/history assertion pack:
    - `Push-Location backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "test_app_chat_history_returns_recent_transcript_messages_for_authenticated_user or test_app_chat_history_returns_latest_ten_messages_in_chronological_order or test_app_chat_history_merges_linked_telegram_and_app_turns_for_authenticated_user or test_app_chat_message_runs_runtime_under_authenticated_user"; Pop-Location`
    - result: `4 passed, 128 deselected in 6.39s`
- Manual checks:
  - pre-check command variant from repo root failed due to import/working-directory mismatch; rerun from `backend/` succeeded
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - focused P0 API workflow only
- Reality status: verified

## Architecture Evidence
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/15_runtime_flow.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: not applicable

## Result Report
- Task summary:
  - Verified core authenticated chat API workflow for app chat history and message endpoints using focused backend route tests.
- Files changed:
  - `.codex/tasks/LUC-942-qa-verify-core-chat-api-workflow-p0.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.agents/state/active-mission.md`
  - `.agents/state/module-confidence-ledger.md`
- How tested:
  - focused pytest subset (command above)
- What is incomplete:
  - full backend regression and production smoke were intentionally out of scope for this heartbeat
- Next steps:
  - if required by board, run release-smoke pack after any chat API changes
- Decisions made:
  - treated this issue as verification-only, no implementation changes
