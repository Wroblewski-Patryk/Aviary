# Task

## Header
- ID: PRJ-1136
- Title: AI Red-Team Event Reply Message Capture
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1135
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1136
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`PRJ-958` executed the AI red-team scenario pack against production but returned
`REVIEW_REQUIRED` because the runner only read `reply.text`. The approved
`EventReplyResponse` schema uses `reply.message`, and `/event` builds the
response from `result.expression.message`.

## Goal

Update the existing AI red-team runner to capture the approved
`reply.message` field without adding a new debug path or workaround.

## Scope

- `backend/scripts/run_ai_red_team_scenarios.py`
- `backend/tests/test_ai_red_team_scenarios_script.py`
- `.codex/tasks/PRJ-1136-ai-red-team-event-reply-message-capture.md`
- context and evidence docs after verification

## Success Signal
- User or operator problem: live AI red-team execution cannot score responses
  even when `/event` returns the approved reply message field.
- Expected product or reliability outcome: red-team runner can score actual
  assistant reply text from the existing `/event` contract.
- How success will be observed: unit tests prove `reply.message` capture and
  the scenario pack can be rerun with pass/fail/review evidence.
- Post-launch learning needed: no

## Deliverable For This Stage

A focused script/test fix that reads `reply.message` and keeps `reply.text`
compatibility for any older local stubs.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan

1. Confirm the existing API schema and `/event` route use `reply.message`.
2. Update `_reply_text` to read `reply.text` or `reply.message`.
3. Add a regression test proving `reply.message` is captured and scored.
4. Run focused tests.
5. Rerun the red-team pack if the script fix passes.
6. Update PRJ-958/PRJ-1135 docs and context with the new evidence.

## Acceptance Criteria

- `_reply_text` reads approved `reply.message`.
- Existing `reply.text` stub compatibility remains.
- Tests cover both message capture and no-reply review behavior.
- No new endpoint, debug bypass, or auth workaround is introduced.

## Definition of Done
- [x] script fix implemented
- [x] focused regression tests pass
- [x] red-team scenario pack rerun evidence captured or blocker recorded
- [x] docs/context updated with result
- [x] `git diff --check` passes

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `pytest -q tests/test_ai_red_team_scenarios_script.py` -> `6 passed`
- Manual checks:
  - strict live rerun against `https://aviary.luckysparrow.ch`
  - artifact:
    `artifacts/ai-red-team/prj1136-live-report-strict-v3.json`
  - result:
    `5 PASS / 4 REVIEW / 0 FAIL / 0 BLOCKED`, recommendation
    `REVIEW_REQUIRED`
- Screenshots/logs: not applicable
- High-risk checks: no new debug path or credential path added
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/security/v1-ai-red-team-execution-report.md`
  - `backend/app/api/schemas.py`
  - `backend/app/api/routes.py`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none unless later packaged and released
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: pending
- Rollback note: revert script/test/doc changes
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist (mandatory)
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was completed in this iteration.
- [x] Operation mode was selected according to iteration rotation.
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Result Report

- Task summary: fixed the red-team runner to read the approved `/event`
  `reply.message` field and reran strict live evidence.
- Files changed:
  - `backend/scripts/run_ai_red_team_scenarios.py`
  - `backend/tests/test_ai_red_team_scenarios_script.py`
  - `docs/security/v1-ai-red-team-execution-report.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-1136-ai-red-team-event-reply-message-capture.md`
- How tested:
  - `pytest -q tests/test_ai_red_team_scenarios_script.py` -> `6 passed`
  - live strict red-team rerun -> `5 PASS / 4 REVIEW / 0 FAIL / 0 BLOCKED`
- What is incomplete: AI red-team is still `REVIEW_REQUIRED`; v1.1 cannot claim
  this gate passed yet.
- Next steps: fix or explicitly risk-accept `AIRT-001`, `AIRT-002`,
  `AIRT-003`, and `AIRT-005`, then rerun the strict pack.
- Decisions made: use the existing `/event` reply contract instead of adding a
  new red-team endpoint.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: runner reads `reply.text`; API schema exposes `reply.message`.
- Gaps: live scoring is incomplete because reply text extraction is wrong.
- Inconsistencies: PRJ-958 described missing `reply.text`, but the approved
  contract uses `message`.
- Architecture constraints: side effects stay on existing event path; no debug
  bypass.

### 2. Select One Priority Task
- Selected task: PRJ-1136 AI red-team event reply message capture.
- Priority rationale: first unblocked v1.1 hardening gate from PRJ-1135.
- Why other candidates were deferred: Telegram/provider gates need external
  credentials.

### 3. Plan Implementation
- Files or surfaces to modify: existing red-team runner and tests.
- Logic: prefer `reply.text` when present for compatibility, otherwise use
  `reply.message`.
- Edge cases: no reply remains `REVIEW_REQUIRED`.

### 4. Execute Implementation
- Updated `_reply_text` to read `reply.text` or `reply.message`.
- Added regression coverage for the approved `reply.message` contract.
- Added review sentinels for unsafe success and release-claim language.

### 5. Verify And Test
- Focused tests passed: `6 passed`.
- Strict live runner evidence captured all 21 steps with real reply excerpts.

### 6. Self-Review
- Architecture alignment: yes.
- Workaround check: no new endpoint, debug path, or auth bypass introduced.
- Remaining risk: four scenarios require review before AI red-team pass.

### 7. Update Documentation And Knowledge
- Updated security report, planning docs, task board, and project state.
