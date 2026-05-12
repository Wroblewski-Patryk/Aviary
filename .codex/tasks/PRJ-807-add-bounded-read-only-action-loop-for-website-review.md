# Task

## Header
- ID: PRJ-807
- Title: Add bounded read-only action loop for website review
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-806
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 807
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
PRJ-806 made provider-step observations explicit on `ActionResult`, but
website review still behaved as either a direct page read or a failure when the
turn contained only an ambiguous website/topic target. The approved
skill-guided bounded action loop plan allows `website_review` to use
`knowledge_search.search_web` followed by `web_browser.read_page` when the
plan already selected the website-review skill and the connector policies allow
the read-only operations.

## Goal
Implement the smallest action-owned, read-only website-review loop:
search for a bounded target page when no URL is present, read the first bounded
result, emit bounded observations, and preserve the existing action boundary.

## Success Signal
- User or operator problem: ambiguous website-review requests can complete in
  one foreground turn without pretending a page was read.
- Expected product or reliability outcome: action can run search -> page read
  within the approved `website_review` skill and expose bounded evidence.
- How success will be observed: unit and runtime tests show two approved tool
  steps, no raw payload inclusion, and runtime debug observations.
- Post-launch learning needed: no

## Deliverable For This Stage
A verified backend slice with action executor logic, unit coverage, runtime
pipeline coverage, and source-of-truth updates.

## Scope
- `backend/app/core/action.py`
- `backend/tests/test_action_executor.py`
- `backend/tests/test_runtime_pipeline.py`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`
- `.agents/state/regression-log.md`
- `docs/planning/skill-guided-bounded-action-loop-plan.md`

## Implementation Plan
1. Reuse existing `KnowledgeSearchDomainIntent`, `WebBrowserAccessDomainIntent`,
   DuckDuckGo search client, generic HTTP page client, connector policy gates,
   delivery merge, and observation contract.
2. In action, when `website_review` is selected and a page-read intent lacks a
   bounded URL, execute at most search -> read.
3. Emit bounded search and page-read observations with no raw payloads.
4. Preserve direct URL page-read behavior and existing failure behavior when the
   skill is not selected.
5. Add focused executor and runtime-pipeline tests.
6. Update task/context/planning truth and run focused validation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- no new provider family, auth surface, DB schema, deployment path, or side
  effect owner
- skills remain metadata-only and do not authorize execution

## Acceptance Criteria
- [x] Ambiguous `website_review` page-read intent searches with limit `3`.
- [x] The first bounded result URL is read with the existing generic HTTP page
  reader.
- [x] The action result records `duckduckgo_search_web` and
  `generic_http_read_page`.
- [x] Observations show `web_search` then `web_browser`, with
  `raw_payload_included=false`.
- [x] Runtime pipeline selects `website_review`, emits a browser access intent,
  and exposes the observations in `system_debug.action_result`.
- [x] Direct provider, permission, and delivery boundaries remain unchanged.

## Definition of Done
- [x] Implementation is narrowly scoped to the approved website-review loop.
- [x] Relevant unit and runtime tests pass.
- [x] Source-of-truth docs and agent state are updated.
- [x] `DEFINITION_OF_DONE.md` requirements were considered for this runtime
  slice.

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
- JavaScript execution, form submission, login flow, crawling, or mutation

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py -k website_review; Pop-Location`
    -> `1 passed, 47 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k website_review; Pop-Location`
    -> `1 passed, 109 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py; Pop-Location`
    -> `48 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py -k "website_review or web_search or page_read or role_skill"; Pop-Location`
    -> `4 passed, 106 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_action_executor.py tests/test_runtime_pipeline.py -k "website_review or web_search or page_read or role_skill"; Pop-Location`
    -> `7 passed, 151 deselected`
  - `git diff --check`
    -> passed with LF/CRLF warnings only
- Manual checks: code review against skill-guided bounded action loop plan.
- Screenshots/logs: not applicable.
- High-risk checks: action boundary, skill metadata-only posture, read-only
  connector operations, no raw provider payloads.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/planning/skill-guided-bounded-action-loop-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - planning/context/state truth updated for implemented PRJ-807

## UX/UI Evidence
- Design source type: not applicable
- Design source reference: not applicable
- Canonical visual target: not applicable
- Fidelity target: not applicable
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: not applicable
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches: none
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: not required
- Rollback note: revert the PRJ-807 action executor and test changes to return
  ambiguous website-review requests to the prior missing-URL failure behavior.
- Observability or alerting impact: runtime debug action observations now show
  the two-step website-review path when it runs.
- Staged rollout or feature flag: existing provider readiness and connector
  policy gates.

## Review Checklist
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

## Notes
- This is not a general web crawler and not a second planner.
- The loop is intentionally capped to the approved two-step read-only path.
- Learning journal update is not required because no recurring environment or
  execution pitfall was confirmed.

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: users asking for website review without a URL.
- Existing workaround or pain: the runtime could search and read separately
  but could not bridge an ambiguous website-review request inside action.
- Smallest useful slice: one search and one read when `website_review` is
  selected.
- Success metric or signal: passing executor and runtime tests with bounded
  observations.
- Feature flag, staged rollout, or disable path: existing provider readiness
  and connector gates
- Post-launch feedback or metric check: not required

## User Feedback Evidence
- `docs/governance/user-feedback-loop.md` reviewed: not applicable
- Feedback item IDs: none
- Feedback accepted: none
- Feedback needs clarification: none
- Feedback conflicts: none
- Feedback deferred or rejected: none
- Active task changed by feedback: no
- New task created from feedback: no
- Design memory updated: not applicable
- Learning journal updated: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: website-review request without explicit URL.
- SLI: focused tests for action and runtime pipeline pass.
- SLO: not applicable for local implementation slice.
- Error budget posture: not applicable
- Health/readiness check: existing search/browser client readiness gates.
- Logs, dashboard, or alert route: runtime debug observations.
- Smoke command or manual smoke: focused pytest commands above.
- Rollback or disable path: remove PRJ-807 loop or disable provider readiness.

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: no, fake provider clients in tests
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: covered by existing missing-URL and provider-not-ready
  paths
- Refresh/restart behavior verified: not applicable
- Regression check performed: focused executor/runtime tests

## AI Testing Evidence
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: runtime pipeline test covers the two-step
  foreground action path.
- Adversarial or role-break scenarios: not applicable for this read-only slice.
- Prompt injection checks: no raw page payload is persisted or promoted to
  executable authority.
- Data leakage and unauthorized access checks: public read-only providers only;
  raw payload inclusion is false.
- Result: pass

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public web/search summaries only
- Trust boundaries: action owns provider calls; skills remain metadata-only
- Permission or ownership checks: existing connector policies and provider
  readiness gates
- Abuse cases: no JS, forms, login, crawling, mutation, or credential access
- Secret handling: no secret changes
- Security tests or scans: focused tests verify no raw payload inclusion
- Fail-closed behavior: provider missing or missing bounded target returns a
  blocker/failure instead of pretending success
- Residual risk: selected first search result may not be the ideal page; this
  is recorded as bounded evidence, not hidden certainty

## Result Report
- Task summary: Added a bounded `website_review` loop that searches for one
  target page when no URL is present, reads the selected page, and emits
  observations for both steps.
- Files changed:
  - `backend/app/core/action.py`
  - `backend/tests/test_action_executor.py`
  - `backend/tests/test_runtime_pipeline.py`
  - this task file and source-of-truth docs/state
- How tested: focused action executor and runtime pipeline pytest commands.
- What is incomplete: ClickUp multi-step read/confirmation loop remains future
  PRJ-808 scope.
- Next steps: PRJ-808.
- Decisions made: cap the first website-review loop to search -> first result
  read, using existing provider clients and observations.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: website-review skill metadata existed, and observations existed, but
  ambiguous website-review requests had no action-owned search -> read bridge.
- Gaps: no runtime proof for skill-selected website review without a URL.
- Inconsistencies: none.
- Architecture constraints: action owns provider calls; skills are
  metadata-only; read-only public web operations only.

### 2. Select One Priority Task
- Selected task: PRJ-807.
- Priority rationale: it is the first bounded multi-step read loop after the
  observation contract.
- Why other candidates were deferred: ClickUp loop is higher-risk because it
  includes confirmation-gated mutation and should follow the read-only web
  proof.

### 3. Plan Implementation
- Files or surfaces to modify: action executor and focused tests.
- Logic: if `website_review` is selected and no bounded URL is present, search
  with limit `3`, select the first bounded URL, read it, and emit observations.
- Edge cases: provider not ready, empty search result, selected result without
  URL, page-read provider failure.

### 4. Execute Implementation
- Implementation notes: reused existing clients, result merge, observation
  helper, and tool-grounded learning candidates.

### 5. Verify and Test
- Validation performed: focused executor and runtime pipeline pytest commands.
- Result: pass.

### 6. Self-Review
- Simpler option considered: fail on ambiguous URL and ask for clarification.
- Technical debt introduced: no
- Scalability assessment: intentionally narrow; future loops should reuse the
  observation and stop-condition pattern.
- Refinements made: runtime test pins selected skill, intent type, used tools,
  observations, and provider calls.

### 7. Update Documentation and Knowledge
- Docs updated: planning/context/state docs.
- Context updated: yes.
- Learning journal updated: not applicable.
