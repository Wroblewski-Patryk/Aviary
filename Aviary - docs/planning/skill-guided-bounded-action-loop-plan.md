# Skill-Guided Bounded Action Loop Plan

## Purpose

This plan records the approved direction for making AION's tool use feel more
like a coherent digital cognition loop instead of a set of one-off handlers.

The goal is to let the personality:

- choose a relevant skill for a task
- use only tools approved for that skill
- execute several bounded tool steps in one foreground turn
- observe results between steps
- adjust execution order without escaping the user's goal or permission gates
- return one truthful answer with source-backed evidence

This plan does not add new provider families. The first implementation uses
the already-approved `web_search`, `web_browser`, and ClickUp paths.

## Current Baseline

Already implemented or visible in the repo:

- `knowledge_search.search_web` through DuckDuckGo HTML
- `web_browser.read_page` through generic HTTP page reading
- ClickUp `create_task`, `list_tasks`, and `update_task` through action-owned
  provider adapters when credentials are configured
- `/app/tools/overview` as the backend-owned tools truth for the product shell
- connector permission gates and action guardrails for read-only,
  suggestion-only, and mutate-with-confirmation operations
- architecture rule that only action executes side effects

Current limitation:

- planning can emit several intents, and action now exposes bounded
  provider-step observations plus a first-class `ActionResult.action_loop`
  summary, but it does not yet run a deeper reusable
  execute-observe-adjust loop beyond the currently approved bounded flows
- skill metadata now binds `website_review`, `web_research`,
  `clickup_task_management`, and `work_partner_task_management` to their
  approved tools as metadata-only capability truth
- website review is still too close to a narrow web-read use case instead of a
  reusable skill-guided workflow

## Target Model

The intended model is:

`event -> plan -> selected skills -> allowed tools -> action loop -> observations -> final answer -> memory`

Planning owns:

- turn goal
- constraints
- detailed model plan
- selected skills
- allowed tool families
- connector permission gates
- typed domain intents

Action owns:

- tool/provider execution
- execution loop state
- bounded observations
- confirmation enforcement
- failure handling
- final action evidence

Skills own:

- reusable strategy metadata
- preferred workflow shape
- allowed tool bindings
- limits and forbidden moves

Tools own:

- one bounded operation
- provider-specific execution
- bounded result evidence

## Implementation Queue

### PRJ-803 Freeze Skill-Tool Binding And Bounded Action Loop Contract

Status: DONE in planning/docs.

Result:

- architecture records the approved skill/tool/action-loop boundary
- implementation plan records the staged rollout
- no runtime behavior changes are made in this slice

Validation:

- doc and context diff validation

### PRJ-804 Expose Skill-Tool Bindings In Tools Overview

Status: DONE.

Result:

- `/app/tools/overview` now exposes metadata-only `skill_tool_bindings` for
  `web_search`, `web_browser`, and `clickup`.
- `web_search` links to `web_research` and `website_review`.
- `web_browser` links to `website_review` and `web_research`.
- `clickup` links to `clickup_task_management` and
  `work_partner_task_management`.
- each binding records allowed operations, read/confirmation posture, action
  as execution owner, and explicit metadata-only authority.
- the web Tools route renders these bindings in the existing technical-details
  panel.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k tools_overview; Pop-Location`
  -> `4 passed, 119 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py; Pop-Location`
  -> `123 passed`
- `Push-Location .\web; npm run build; Pop-Location` -> passed.

Goal:

- make `/app/tools/overview` show which skills can use each active tool
- make the web tools screen truthful for browser, search, and ClickUp

Scope:

- `backend/app/core/app_tools_policy.py`
- app-facing tools overview schema tests
- web tools rendering if it currently omits the new fields
- docs/context sync

Expected output:

- `web_search` links to `web_research` and `website_review`
- `web_browser` links to `website_review` and optionally `web_research`
- `clickup` links to `clickup_task_management` or `work_partner_task_management`
- each binding states whether it is read-only or confirmation-gated

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py; Pop-Location`
- `Push-Location .\web; npm run build; Pop-Location` if UI changes

### PRJ-805 Add Skill Registry Metadata For Tool-Aware Skills

Status: DONE.

Result:

- runtime skill registry now contains metadata-only records for:
  - `website_review`
  - `web_research`
  - `clickup_task_management`
  - `work_partner_task_management`
- capability catalog skill count is now `9`.
- each tool-aware skill records allowed tools, limitations, `action` as
  execution owner, connector permission gates as authorization boundary, and
  `tool_execution_allowed=false`.
- role selection may emit these skills as metadata hints for clear web,
  website-review, and ClickUp requests, but skills still cannot execute tools
  or authorize provider access.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_role_agent.py tests/test_api_routes.py; Pop-Location`
  -> `142 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k role_skill; Pop-Location`
  -> `1 passed, 108 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py -k "capability_catalog or incident_bundle"; Pop-Location`
  -> `2 passed, 62 deselected`

Goal:

- ensure runtime capability truth has explicit skill records for:
  - `website_review`
  - `web_research`
  - `clickup_task_management`

Scope:

- existing skill registry or capability catalog owners
- role/skill policy snapshots
- health/debug visibility
- tests for metadata-only skill posture

Expected output:

- skills remain metadata-only
- each skill exposes allowed tools, limitations, and side-effect posture
- no skill can execute tools directly

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_role_agent.py tests/test_api_routes.py; Pop-Location`

### PRJ-806 Introduce Action Execution Observation Contract

Status: DONE.

Result:

- `ActionResult` now carries `observations` beside existing notes and
  tool-grounded-learning candidates.
- each observation records tool id, operation, provider path, source reference,
  bounded summary, confidence, blocker, next-step relevance, and
  `raw_payload_included=false`.
- existing provider-backed paths now emit observations for ClickUp
  create/list/update, Google Calendar availability, Google Drive file listing,
  web search, and browser page read.
- runtime debug exposes the same observations through
  `system_debug.action_result`.
- no execute-observe-adjust loop was introduced in this slice.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py; Pop-Location`
  -> `47 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_runtime_pipeline.py -k "web_search or page_read or clickup or role_skill"; Pop-Location`
  -> `11 passed, 145 deselected`

Goal:

- add one structured observation format for tool-step results inside action

Scope:

- action result contract
- runtime debug payload
- tests for bounded result summaries

Expected output:

- observations include tool id, operation, provider path, source reference,
  bounded summary, blocker/confidence, and next-step relevance
- raw provider payloads remain out of memory and debug responses

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_runtime_pipeline.py; Pop-Location`

### PRJ-807 Add Bounded Read-Only Action Loop For Website Review

Status: DONE.

Result:

- action now runs the first bounded `website_review` loop when:
  - the selected skill is `website_review`
  - the plan carries a `web_browser_access_intent`
  - the page-read intent has no bounded URL
- the loop uses the existing approved read-only tool path:
  `knowledge_search.search_web` -> `web_browser.read_page`.
- search uses limit `3`, selects the first bounded result URL, reads that page
  with the generic HTTP page client, and stops within the approved two-step
  posture.
- `ActionResult.observations` records `web_search` followed by `web_browser`
  with next-step relevance and `raw_payload_included=false`.
- direct URL page reads, connector permission gates, provider readiness checks,
  delivery merge, auth, database, env, secret, and deployment behavior remain
  unchanged.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k website_review; Pop-Location`
  -> `1 passed, 47 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k website_review; Pop-Location`
  -> `1 passed, 109 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py; Pop-Location`
  -> `48 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "website_review or web_search or page_read or role_skill"; Pop-Location`
  -> `4 passed, 106 deselected`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_runtime_pipeline.py -k "website_review or web_search or page_read or role_skill"; Pop-Location`
  -> `7 passed, 151 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

Goal:

- let one foreground turn execute a bounded website-review workflow:
  direct URL read or search-first page review, then fact extraction or
  source-backed summary

Scope:

- action-owned loop only
- web search and browser clients
- planning/action contract tests
- behavior validation scenario

Expected output:

- if URL is present, action reads the page directly
- if target is ambiguous, action may search first and then read one selected
  result
- action may perform a small bounded retry only inside the approved goal
- the answer includes source and uncertainty/blocker notes

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_planning_agent.py tests/test_action_executor.py tests/test_runtime_pipeline.py; Pop-Location`
- behavior validation scenario for website phone-number extraction

### PRJ-808 Extend The Loop To ClickUp Read And Confirmation-Gated Mutation

Status: DONE.

Result:

- ClickUp `list_tasks` remains provider-backed and read-only.
- ClickUp `create_task` and `update_task` now require a matching
  `task_system/clickup/<operation>` connector permission gate with
  `requires_confirmation=true` and `allowed=true` before provider mutation
  executes.
- unconfirmed `update_task` performs read-only `list_tasks` candidate triage,
  emits a `confirmation_required` observation, and stops before mutation.
- provider-not-ready ClickUp requests emit a bounded
  `clickup_client_not_ready` observation instead of disappearing silently.
- runtime behavior tests now expect confirmation gating rather than direct
  mutation for normal planner-emitted ClickUp update requests.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k clickup; Pop-Location`
  -> `6 passed, 44 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py; Pop-Location`
  -> `51 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "clickup or role_governed_tool_usage or work_partner_scenarios"; Pop-Location`
  -> `4 passed, 106 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_connector_policy.py; Pop-Location`
  -> `6 passed`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_connector_policy.py; Pop-Location`
  -> `57 passed`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_connector_policy.py tests/test_runtime_pipeline.py -k "clickup or role_governed_tool_usage or work_partner_scenarios or connector_operation"; Pop-Location`
  -> `13 passed, 154 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

Goal:

- let the executor use ClickUp skill guidance for multi-step task review and
  safe updates without bypassing confirmation gates

Scope:

- ClickUp action path
- confirmation-gated mutation handling
- tests and debug evidence

Expected output:

- read-only task triage can happen in one turn when enabled and configured
- create/update still requires explicit confirmation
- action loop reports blocker when credentials or opt-in are missing

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_connector_policy.py tests/test_runtime_pipeline.py; Pop-Location`

### PRJ-809 Sync Runtime Docs, Ops Notes, And Behavior Evidence

Status: DONE.

Result:

- architecture/runtime docs now describe action-owned bounded observations and
  confirmation-required mutation stops.
- ClickUp provider readiness is documented as adapter availability, not
  mutation authorization.
- debugging docs name `system_debug.action_result.observations` as the
  canonical bounded action-loop evidence surface.
- behavior-testing docs now describe T14/T15 ClickUp scenarios as task triage
  with confirmation-gated mutation, not direct mutation.
- ops notes now explain `confirmation_required` and
  `clickup_client_not_ready` blockers for ClickUp action-loop triage.

Validation:

- targeted source scans for `ClickUp`, `confirmation_required`,
  `observations`, `T14.3`, and bounded action-loop wording
- stale direct-mutation wording scan returned no matches
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-810 Freeze App-Facing Connector Confirmation Handoff Contract

Status: DONE in contract/docs.

Result:

- the first-party app confirmation path is explicitly contract-bound before
  any endpoint or UI implementation
- a pending confirmation must be tied to one source event or trace, connector
  kind, provider, operation, mode, bounded candidate summary, and source
  reference
- confirmed execution must re-enter action with only the same typed domain
  intent and a matching connector permission gate where
  `requires_confirmation=true` and `allowed=true`
- generic later chat text, tool preference toggles, or provider readiness must
  not authorize external mutation
- confirmation must fail closed on user/session mismatch, stale evidence,
  provider mismatch, or candidate drift

Validation:

- targeted scans across app chat/API response shape, connector permission
  gates, action confirmation stops, and ClickUp mutation wording
- `git diff --check` -> passed with LF/CRLF warnings only

Goal:

- prevent confirmation UX/API work from becoming an accidental provider
  mutation bypass

Scope:

- contract documentation only
- no endpoint, UI, storage, or provider behavior changes

Expected output for a future implementation slice:

- app chat or a dedicated app endpoint may expose a bounded
  `pending_confirmation` object
- a separate authenticated confirmation submission must carry the original
  source event or trace plus the exact connector operation and candidate
  reference
- action receives the matching allowed connector permission gate only after
  that confirmation contract is satisfied

### PRJ-811 Expose App Chat Pending Connector Confirmation

Status: DONE.

Result:

- `/app/chat/message` can now return a bounded `pending_confirmation` object
  when action produced a `confirmation_required` observation and a matching
  not-yet-allowed connector permission gate exists
- the response includes source event, trace, connector kind, provider,
  operation, mode, bounded candidate summary, source reference, and reason
- app chat still does not expose debug/system-debug payloads
- the web chat composer renders the pending confirmation as read-only blocked
  state; it does not add a mutation confirmation button or endpoint

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_message"; Pop-Location`
  -> `3 passed, 121 deselected`
- `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
- At the time of `PRJ-811`, a Browser rendered check against local Vite was
  attempted, but the in-app browser blocked `localhost:5173` with
  `net::ERR_BLOCKED_BY_CLIENT`. Later `PRJ-820` and `PRJ-821` added
  repeatable Chrome/CDP browser proof for the confirmation and route-smoke
  paths.
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-812 Persist Pending Connector Confirmation Evidence

Status: DONE.

Result:

- pending confirmation projection now lives in one shared core helper
- `/app/chat/message` and episode persistence reuse the same bounded payload
- action persistence stores `pending_connector_confirmation` in the episode
  payload when a confirmation-required connector mutation stops safely
- runtime ClickUp update triage now proves the persisted evidence is present
- no confirmation submission endpoint or provider mutation execution was added

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "app_chat_message"; Pop-Location`
  -> `3 passed, 121 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "pending_connector_confirmation or clickup"; Pop-Location`
  -> `8 passed, 44 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "clickup_task_update_until_confirmation"; Pop-Location`
  -> `1 passed, 109 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py -k "pending_connector_confirmation or app_chat_message"; Pop-Location`
  -> `4 passed, 172 deselected`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_runtime_pipeline.py -k "pending_connector_confirmation or app_chat_message or clickup_task_update_until_confirmation"; Pop-Location`
  -> `6 passed, 280 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-813 Add Fail-Closed Connector Confirmation Submit Path

Status: DONE.

Result:

- `/app/connectors/confirm` now provides the dedicated app-authenticated
  confirmation submission path.
- the route loads pending confirmation evidence only from the authenticated
  user's persisted episode and checks source event, trace, connector kind,
  provider, operation, mode, bounded candidate summary, source reference, and
  freshness.
- at the time of `PRJ-813`, valid pending evidence still failed closed with
  `confirmation_replay_unavailable` because PRJ-812 had not yet persisted a
  replayable typed plan snapshot.
- stale, drifted, missing, or cross-user evidence is rejected before action can
  receive any allowed confirmation gate.
- no provider mutation, replay execution, new connector family, env, secret, or
  deployment behavior changed.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
  -> `8 passed, 121 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py -k "episode_by_user_and_event_id or structured_episode_payload" --basetemp ..\.codex\tmp\pytest-prj813; Pop-Location`
  -> `2 passed, 64 deselected`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py tests/test_memory_repository.py -k "connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj813-combined; Pop-Location`
  -> `9 passed, 186 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-814 Persist Connector Confirmation Replay Snapshot

Status: DONE.

Result:

- action persistence now stores `connector_confirmation_replay` beside
  `pending_connector_confirmation` when the original turn has matching pending
  evidence.
- the snapshot contains the typed domain intent, the matching
  not-yet-allowed connector permission gate, and the bounded confirmation
  observation.
- replay evidence is generated server-side and records
  `execution_allowed=false`.
- `/app/connectors/confirm` recognizes that replay evidence exists but still
  fails closed with `confirmation_replay_not_implemented`.
- no allowed gate, confirmed action replay, provider mutation, new provider
  family, env, secret, or deployment behavior changed.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "pending_connector_confirmation"; Pop-Location`
  -> `1 passed, 51 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
  -> `9 passed, 121 deselected`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_memory_repository.py -k "pending_connector_confirmation or connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj814-combined; Pop-Location`
  -> `11 passed, 237 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-815 Execute Confirmed Connector Replay From Snapshot

Status: DONE.

Result:

- `/app/connectors/confirm` now rebuilds a replay `PlanOutput` from the stored
  `connector_confirmation_replay` snapshot.
- the route rechecks authenticated user scope, source event, trace, provider,
  operation, mode, candidate summary, source reference, and freshness before
  replay.
- only the matching stored connector permission gate is converted to
  `allowed=true` with `explicit_user_confirmation_received`.
- confirmed replay calls `ActionExecutor.execute` with the standard action
  delivery envelope, preserving action as the only provider mutation owner.
- successful replay returns bounded action status, actions, notes, and pending
  confirmation evidence.
- replay drift, missing executor, missing replay evidence, stale evidence, and
  cross-user evidence remain fail-closed.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "connector_confirmation or app_chat_message"; Pop-Location`
  -> `11 passed, 121 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "clickup_update or pending_connector_confirmation"; Pop-Location`
  -> `1 passed, 51 deselected`
- final focused regression:
  `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_api_routes.py tests/test_memory_repository.py -k "pending_connector_confirmation or connector_confirmation or app_chat_message or episode_by_user_and_event_id" --basetemp ..\.codex\tmp\pytest-prj815-combined; Pop-Location`
  -> `13 passed, 237 deselected`
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-816 Add App Chat Connector Confirmation Controls

Status: DONE.

Result:

- web chat now renders first-party confirmation controls around the existing
  `/app/connectors/confirm` endpoint.
- the frontend submits only the server-projected pending confirmation payload.
- submitting, success, and fail-closed error feedback remain local to the
  confirmation surface.
- provider mutation ownership stays in backend action replay.

Validation:

- `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  -> passed
- `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-817 Add Connector Confirmation UI Characterization

Status: DONE.

Result:

- `npm run test:connector-confirmation` now pins the app-facing confirmation
  source contract:
  - API client wiring
  - bounded pending payload submission
  - pending/submitting/success/error state transitions
  - localized copy
  - composer controls
  - aria-live feedback and style hooks

Validation:

- `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  -> passed
- `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  -> passed
- `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed

### PRJ-818 Harden Frontend Chrome Characterization Launch

Status: DONE.

Result:

- Chrome-based frontend harnesses now use conservative launch flags and bounded
  DevTools command timeouts.
- route smoke failures became bounded/actionable instead of hanging.
- this slice did not claim browser proof by itself.

Validation:

- `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  -> passed
- `git diff --check` -> passed with LF/CRLF warnings only

### PRJ-819 Add Connector Confirmation Component Render Characterization

Status: DONE.

Result:

- `npm run test:connector-confirmation-render` renders `ChatComposerShell`
  through `react-dom/server`.
- pending, submitting, success, and fail-closed error markup are covered
  without depending on local browser availability.
- the render proof verifies candidate details, disabled submitting control,
  success cleanup without a stale confirm button, and retry posture.

Validation:

- `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
  -> passed
- `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  -> passed
- `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  -> passed

### PRJ-820 Add Connector Confirmation Browser Characterization

Status: DONE.

Result:

- `npm run test:connector-confirmation-browser` now serves the built app with
  synthetic app-facing API data and drives real Chrome through CDP.
- the browser proof covers chat send, bounded pending confirmation rendering,
  exact server-projected payload submission, fail-closed stale confirmation
  retry, and successful confirmation cleanup.

Validation:

- `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
  -> passed with report status `ok`
- `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  -> passed
- `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
  -> passed

### PRJ-821 Repair Route Smoke Browser Rendering

Status: DONE.

Result:

- `npm run smoke:routes` now serves `web/dist` and drives Chrome through CDP
  `Runtime.evaluate`.
- the smoke waits for route markers and passes for all `14` current public and
  authenticated web routes.
- the `/tools` synthetic app-facing payload now includes
  `skill_tool_bindings`, matching the current `AppToolItem` contract.

Validation:

- `Push-Location .\web; npm run smoke:routes; Pop-Location`
  -> passed with `14` routes and status `ok`
- `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
  -> passed with report status `ok`
- `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  -> passed

### PRJ-822 Run Post-Confirmation Architecture Confidence Gate

Status: DONE.

Result:

- the accumulated action-loop and connector-confirmation lane is green across
  full backend and web gates.
- release-smoke tests now expect the current `9` item skill catalog.
- work-partner orchestration tests now assert expanded selected skill metadata
  and confirmation-gated ClickUp mutation behavior.
- no runtime, provider, DB, auth, env, secret, deployment, or health behavior
  changed.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q --basetemp ..\.codex\tmp\pytest-prj822-full-final; Pop-Location`
  -> `1074 passed`
- `Push-Location .\web; npm run test:connector-confirmation; Pop-Location`
  -> passed
- `Push-Location .\web; npm run test:connector-confirmation-render; Pop-Location`
  -> passed
- `Push-Location .\web; npm run test:connector-confirmation-browser; Pop-Location`
  -> passed with report status `ok`
- `Push-Location .\web; npm run smoke:routes; Pop-Location`
  -> passed with `14` routes and status `ok`
- `Push-Location .\web; npm exec -- tsc -b --pretty false; Pop-Location`
  -> passed
- `Push-Location .\web; npm exec -- vite build; Pop-Location` -> passed

### PRJ-924 Expose Action-Loop Summary On Action Result

Status: DONE.

Result:

- `ActionResult` now carries an action-owned `action_loop` summary with the
  loop summary policy owner, execution owner, step count, selected skill ids,
  used tools, completion state, blockers, and `raw_payload_included=false`.
- website-review search-first execution reports `completion_state=satisfied`
  with `web_search` and `web_browser` tool usage.
- confirmation-gated ClickUp update triage reports
  `completion_state=needs_confirmation` with a `confirmation_required`
  blocker.
- no provider behavior, auth, DB, env, secret, deployment, UI, or new
  execution authority changed.

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k "search_first_website_review_loop or triages_clickup_task_update_until_confirmation" --basetemp ..\.codex\tmp\pytest-prj924-action-focused-3; Pop-Location`
  -> `2 passed, 50 deselected`
- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "website_review_loop or work_partner_orchestration_baseline" --basetemp ..\.codex\tmp\pytest-prj924-runtime-focused-3; Pop-Location`
  -> `2 passed, 108 deselected`

### PRJ-926 Sync Action-Loop Debug And Ops Docs

Status: DONE.

Result:

- logging/debugging docs now name `system_debug.action_result.action_loop` as
  the canonical action-loop summary surface for operator triage.
- per-step observations remain the canonical detailed evidence after the
  summary is inspected.
- the runtime ops runbook now explains how to triage `completion_state`,
  blockers, selected skills, used tools, and bounded observations.
- no runtime, API, provider, auth, DB, env, secret, deployment, UI, or health
  behavior changed.

Validation:

- targeted scans for `system_debug.action_result.action_loop`,
  `completion_state`, `raw_payload_included=false`, and stale
  observations-only wording
- `git diff --check` on touched docs/context/state files

Remaining Goal For Future Loop Extension:

- make the new loop visible and operable without ambiguity

Scope:

- runtime docs
- testing docs
- ops runbook if health/debug surfaces change
- behavior-validation artifacts
- context sync

Expected output:

- docs describe the loop as action-owned
- health/debug evidence can prove which skills/tools were selected and used
- operators can distinguish a blocked provider from a failed plan

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`

## Acceptance Criteria

- tools overview truth shows skill-tool bindings for search, browser, and
  ClickUp
- skill metadata remains non-executable
- action owns all tool execution and all provider calls
- multi-step read-only flows can complete in one foreground turn
- mutation paths remain confirmation-gated
- bounded observations are available for final answers, memory, and debug
- no raw provider payloads are persisted as learned knowledge

## Risks And Guardrails

- Risk: action loop becomes a hidden second planner.
  - Guardrail: loop may adjust execution order only inside the approved goal,
    selected skill, allowed tool set, and max-step policy.
- Risk: skills become accidental execution authority.
  - Guardrail: skills remain metadata-only and action checks connector policy.
- Risk: tool results leak too much data.
  - Guardrail: observations are bounded summaries and raw payloads are
    forbidden from memory/debug output.
- Risk: complex tasks silently half-complete.
  - Guardrail: completion state must be explicit:
    `satisfied|blocked|needs_confirmation|needs_clarification|step_limit`.

## Future Extension

Gmail or other mailbox tools should be added only after this loop is in place.
The likely future skill is `mailbox_review`, bound to read-only mailbox
operations plus a checkpoint model for "new since yesterday" or "new since
last check" comparisons.
