# Task

## Header
- ID: LUC-1690
- Title: Tools and integrations proof-link closure
- Task Type: research
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: LUC-1675
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: AVIARY-ARCH-GRAPH-MEDIUM-PROOF-001, AVIARY-WEB-TOOLS-CAPABILITY-001, AVIARY-WEB-TOOLS-CONTRACT-001, AVIARY-WEB-INTEGRATIONS-EXTERNAL-001, AVIARY-WEB-CONNECTOR-CONSENT-001, AVIARY-WEB-PROVIDER-SETUP-GUIDANCE-001
- Requirement Rows: not applicable
- Quality Scenario Rows: not applicable
- Risk Rows: provider credential activation remains deferred
- Iteration: LUC-1690
- Operation Mode: TESTER
- Mission ID: LUC-1675-evidence-collection-and-architecture-baseline
- Mission Status: CHECKPOINTED

## Process Self-Audit
- [x] All seven autonomous loop steps are represented in this evidence task.
- [x] Exactly one priority task was selected.
- [x] The task is aligned with the LUC-1675 preparation-only source-of-truth.
- [x] Affected module confidence rows were identified.
- [x] This task improves release confidence by turning architecture report signals into exact node/test/proof mapping and residual-gap notes.

## Mission Block
- Mission objective: close or justify Tools, Integrations, connector confirmation, and provider setup guidance proof-link signals without behavior changes.
- Release objective advanced: Aviary known-state preparation evidence.
- Included slices: `/app/connectors/confirm`, `/app/tools/overview`, `/app/tools/preferences`, `/app/tools/telegram/link/start`, `/telegram/set-webhook`, Tools/Integrations frontend characterization evidence.
- Explicit exclusions: no implementation, schema changes, live provider credential activation, deployment, protected smoke, or frontend UI edits.
- Checkpoint cadence: one focused backend proof run, focused frontend characterization attempts, and docs/state closure.
- Stop conditions: endpoint ownership missing, focused backend proof failing, or evidence gap requiring live credentials.
- Handoff expectation: close as done if proof links are mapped and residual gaps are explicitly justified.

## Context
`docs/status/task-synchronization-report.md` still lists the Tools/Integrations-related route and component entities under `Implementation Without Task Links`. Existing backend route tests and frontend characterization scripts already cover most of the behavior. This task records the exact mapping and reruns the smallest proof set allowed by the preparation-only boundary.

## Goal
Map Tools/Integrations endpoint and UI node IDs to existing evidence, rerun focused proof where practical, and record residual gaps that are exporter/tooling or live-provider scope rather than hidden product claims.

## Scope
- `backend/app/api/routes.py`
- `backend/app/core/app_tools_policy.py`
- `backend/tests/test_api_routes.py`
- `web/src/App.tsx`
- `web/src/components/tools.tsx`
- `web/src/lib/api.ts`
- `web/src/lib/tool-formatting.ts`
- `web/scripts/tools-directory-characterization.mjs`
- `web/scripts/connector-confirmation-render-characterization.mjs`
- `docs/graphs/architecture-awareness.csv`
- `docs/graphs/architecture-proof-register.csv`
- `docs/status/task-synchronization-report.md`
- `.agents/state/module-confidence-ledger.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/active-mission.md`
- `.agents/state/next-steps.md`

## Implementation Plan
1. Read the generated architecture and synchronization reports.
2. Extract Tools/Integrations endpoint and component node IDs currently counted in missing task-link output.
3. Map each node to existing focused backend tests and frontend characterization evidence.
4. Run the narrow backend route proof pack and focused frontend characterization commands.
5. Record pass/fail/deferred evidence and update source-of-truth state.

## Acceptance Criteria
- Tools/Integrations API endpoint nodes are listed with IDs and paths.
- Existing tests/scripts are mapped to endpoint and UI behavior.
- Fresh focused backend proof is recorded.
- Frontend proof status is recorded honestly, including any blocked local browser runner.
- Live provider credential activation remains external/deferred unless explicitly approved.

## Definition of Done
- [x] Tools/Integrations endpoint nodes identified from generated architecture reports.
- [x] Existing backend test evidence mapped.
- [x] Focused backend proof passed.
- [x] Frontend characterization status recorded with residual gaps.
- [x] No behavior, credential, deployment, or provider mutation performed.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_tools or app_connector_confirmation or telegram_link or set_webhook"; Pop-Location` -> `19 passed, 115 deselected in 48.89s`.
  - `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location` -> PASS, `status=ok`, cases `pending`, `submitting`, `success`, `error`.
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location` -> FAILED locally in browser runner with `Runtime.evaluate failed` / `Error: Uncaught`; cleanup warning reported locked temp Chrome profile.
  - `Push-Location .\web; CHROME_PATH=...\msedge.exe npm run test:tools-directory; Pop-Location` -> BLOCKED by command timeout after `126s`.
- Manual checks: read `docs/status/task-synchronization-report.md`, `docs/graphs/architecture-awareness.csv`, `docs/graphs/architecture-proof-register.csv`, `backend/app/api/routes.py`, `backend/tests/test_api_routes.py`, `web/scripts/tools-directory-characterization.mjs`, and existing module confidence rows.
- Screenshots/logs: not applicable in this preparation-only heartbeat.
- High-risk checks: backend tests cover authenticated-session rejection, server-side connector replay validation, stale/drift rejection, user isolation, action-executor unavailable path, confirmed replay execution, Tools overview grouping, provider readiness, preferences persistence, Telegram link start/configuration guard, link confirmation through Telegram event ingress, expired link rejection, and webhook secret selection.
- Cleanup evidence: validation-owned `node scripts/tools-directory-characterization.mjs` and temp-profile Chrome process for `aion-tools-directory-bb8pag` were stopped; no remaining process matched `tools-directory-characterization.mjs`, `aion-tools-directory-bb8pag`, or `aion-tools-directory-cHmGpz`.
- Module confidence ledger updated: yes, via LUC-1690 evidence overlay.
- Module confidence rows closed or changed: listed in the header.
- Reality status: partially verified for current heartbeat; backend/API proof is verified, connector render proof is verified, current Tools browser characterization is blocked by local runner, and live provider activation is deferred.

## Architecture Evidence
- Architecture source reviewed: `docs/graphs/architecture-awareness.csv`, `docs/graphs/architecture-proof-register.csv`, `docs/status/task-synchronization-report.md`.
- Fits approved architecture: yes.
- Mismatch discovered: yes, generated synchronization still reports implementation entities without task links even though direct test and characterization evidence exists for this cluster.
- Decision required from user: no.
- Follow-up architecture doc updates: exporter/task-link inference remains owned by `LUC-1687`; this task records a manual evidence overlay only.

## Tools/Integrations Endpoint Evidence Map

| Node ID | Endpoint | Existing proof |
| --- | --- | --- |
| `api_endpoint:post-app-connectors-confirm:329c7f6271` | `POST /app/connectors/confirm` | `test_app_connector_confirmation_requires_authenticated_session`; `test_app_connector_confirmation_validates_server_side_evidence_and_fails_closed_without_replay`; `test_app_connector_confirmation_rejects_replay_when_action_executor_is_unavailable`; `test_app_connector_confirmation_executes_confirmed_replay_through_action`; `test_app_connector_confirmation_returns_blocked_when_confirmed_replay_execution_fails`; `test_app_connector_confirmation_rejects_replay_snapshot_drift`; `test_app_connector_confirmation_rejects_candidate_drift`; `test_app_connector_confirmation_rejects_stale_evidence`; `test_app_connector_confirmation_isolates_authenticated_users` |
| `api_endpoint:get-app-tools-overview:add8084a44` | `GET /app/tools/overview` | `test_app_tools_overview_excludes_raw_provider_payloads`; `test_app_tools_overview_requires_authenticated_session`; `test_app_tools_overview_exposes_grouped_backend_truth`; `test_app_tools_overview_marks_provider_backed_integrations_ready_when_configured`; Telegram link start/confirm tests re-check overview state |
| `api_endpoint:patch-app-tools-preferences:ffaead5701` | `PATCH /app/tools/preferences` | `test_app_patch_tools_preferences_updates_requested_enablement_state`; `test_app_patch_tools_preferences_requires_authenticated_session`; Telegram link confirmation test verifies enabled Telegram state after preference update |
| `api_endpoint:post-app-tools-telegram-link-start:ec9b2bbb0c` | `POST /app/tools/telegram/link/start` | `test_app_start_telegram_link_requires_authenticated_session`; `test_app_start_telegram_link_creates_pending_link_code`; `test_app_start_telegram_link_requires_configured_provider`; `test_event_endpoint_confirms_telegram_link_code_and_updates_tools_overview`; `test_event_endpoint_rejects_expired_telegram_link_code` |
| `api_endpoint:post-telegram-set-webhook:9242a5d9b5` | `POST /telegram/set-webhook` | `test_set_webhook_uses_request_secret_or_settings_default`; `test_set_webhook_prefers_explicit_request_secret_over_settings_default` |

## UI/Characterization Evidence Map

| Node / surface | Evidence status |
| --- | --- |
| `component:tools-tsx:8693e1aad9` / `web/src/components/tools.tsx` | Existing module-confidence evidence from `PRJ-1334..PRJ-1338`; current browser characterization attempt failed/then timed out locally, so this heartbeat does not refresh the Tools browser proof. |
| `web/scripts/tools-directory-characterization.mjs` | Existing prior PASS evidence in `AVIARY-WEB-TOOLS-*` rows; current run blocked by local Chrome/CDP runner behavior. |
| `web/scripts/connector-confirmation-render-characterization.mjs` | Fresh PASS in this heartbeat for pending/submitting/success/error render cases. |
| `/tools` and `/integrations` route smoke/screenshots | Prior PASS evidence recorded in module-confidence rows; not rerun in this backend/API preparation heartbeat because the issue did not authorize broad frontend/browser smoke and the focused Tools browser runner was blocked. |

## Residual Proof Gaps
- Generated task-link report still lists this cluster under `Implementation Without Task Links`; this is an architecture exporter/task-link inference gap, not a newly found backend behavior gap. Owner: `LUC-1687`.
- Current `npm run test:tools-directory` did not complete locally. The runner produced a Chrome `Runtime.evaluate` failure, then Edge rerun timed out. This is recorded as blocked local browser-runner proof, not as a product behavior pass.
- Live provider credential activation for Telegram, ClickUp, Google Calendar, and Google Drive remains explicitly deferred/external to this preparation lane.
- No deployment, protected smoke, provider mutation, or credential access was performed.

## Result Report
- Task summary: closed LUC-1690 as an evidence/proof-link overlay for Tools, Integrations, connector confirmation, and provider setup guidance.
- Files changed: this task packet plus state/context evidence notes.
- How tested: focused backend route proof passed with 19 tests; connector confirmation render characterization passed; Tools directory browser characterization failed/timed out locally and was cleaned up.
- What is incomplete: exporter still reports missing task links; current Tools browser characterization was blocked; live provider activation remains deferred.
- Next steps: `LUC-1687` should repair exporter/task-link inference; a frontend/QA owner can rerun Tools browser characterization or route smoke once the local browser runner is stable.
- Decisions made: no implementation change was required.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: generated task synchronization reports Tools/Integrations endpoints and components in missing task-link output.
- Gaps: task-link inference gap and current local browser-runner proof gap.
- Inconsistencies: prior PRJ evidence exists for Tools/Integrations rows, while current synchronization still counts route/component entities as missing task links.
- Architecture constraints: preparation-only boundary; no behavior/deploy/provider mutation.

### 2. Select One Priority Mission Objective
- Selected task: LUC-1690 Tools and integrations proof-link closure.
- Priority rationale: assigned scoped wake and backend/API ownership.
- Why other candidates were deferred: exporter reproducibility is `LUC-1687`; auth/identity is already `LUC-1688`; chat/personality is `LUC-1689`.

### 3. Plan Implementation
- Files or surfaces to modify: evidence/task/state docs only.
- Logic: map generated node IDs to existing tests and fresh proof.
- Edge cases: do not claim live provider activation or browser characterization pass when the current runner failed.

### 4. Execute Implementation
- Implementation notes: no runtime code changed.

### 5. Verify and Test
- Validation performed: focused backend route pytest selection and focused frontend characterization commands.
- Result: backend `19 passed`; connector render PASS; Tools directory browser proof blocked by local runner.

### 6. Self-Review
- Simpler option considered: issue comment only.
- Technical debt introduced: no.
- Scalability assessment: evidence overlay is bounded; exporter inference repair remains separate.
- Refinements made: residual gaps separated from behavior proof.

### 7. Update Documentation and Knowledge
- Docs updated: task packet, state/context ledgers.
- Context updated: yes.
- Learning journal updated: not applicable; browser-runner flake is already represented as a known module-confidence caveat and was cleaned up in this heartbeat.
