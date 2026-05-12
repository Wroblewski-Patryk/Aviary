# Task

## Header
- ID: PRJ-804
- Title: Expose skill-tool bindings in tools overview
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-803
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 804
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
`PRJ-803` froze the skill-guided bounded action loop architecture. The next
smallest implementation slice is to make current tool-to-skill bindings visible
through the existing `/app/tools/overview` product/API truth without granting
skills any execution authority.

## Goal
Expose approved metadata-only skill-tool bindings for web search, web browser,
and ClickUp in `/app/tools/overview`, and render them in the existing Tools
surface.

## Scope
- `backend/app/core/app_tools_policy.py`
- `backend/tests/test_api_routes.py`
- `web/src/lib/api.ts`
- `web/src/components/tools.tsx`
- `web/src/App.tsx`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.agents/state/current-focus.md`
- `.agents/state/next-steps.md`
- `.agents/state/system-health.md`
- `.agents/state/regression-log.md`
- `docs/planning/skill-guided-bounded-action-loop-plan.md`

## Success Signal
- User or operator problem: the product shell should truthfully show which
  reusable skills may consider each approved tool.
- Expected product or reliability outcome: future bounded action-loop work can
  reuse visible skill/tool truth instead of inventing a second capability map.
- How success will be observed: `/app/tools/overview` returns
  `skill_tool_bindings`, web build succeeds, and API tests pin the contract.
- Post-launch learning needed: no

## Deliverable For This Stage
Verification-backed implementation of the existing tools overview contract
extension.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- skills remain metadata-only and never execute tools directly
- action remains the only execution owner for provider calls or side effects

## Implementation Plan
1. Add a bounded `skill_tool_bindings` field to existing tool items.
2. Populate bindings for `web_research`, `website_review`,
   `clickup_task_management`, and `work_partner_task_management`.
3. Pin the API contract in tools-overview tests.
4. Extend web API types and render bindings in the existing technical-details
   panel.
5. Run focused API validation and web build.
6. Sync planning, context, and state files.

## Acceptance Criteria
- `web_search` links to `web_research` and `website_review`.
- `web_browser` links to `website_review` and `web_research`.
- `clickup` links to `clickup_task_management` and
  `work_partner_task_management`.
- Each binding states posture, allowed operations, execution owner, and
  metadata-only authority.
- Existing tool enablement and provider-readiness semantics do not change.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` reviewed for applicable API/UI criteria.
- [x] `INTEGRATION_CHECKLIST.md` reviewed for response/client parity.
- [x] `NO_TEMPORARY_SOLUTIONS.md` reviewed.
- [x] Focused API tests pass.
- [x] Web build passes.
- [x] Source-of-truth and state files are updated.

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
- skill-owned execution or authorization

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k tools_overview; Pop-Location`
    -> `4 passed, 119 deselected`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py; Pop-Location`
    -> `123 passed`
  - `Push-Location .\web; npm run build; Pop-Location` -> passed.
- Manual checks:
  - reviewed `backend/app/core/app_tools_policy.py` output shape against
    `docs/architecture/16_agent_contracts.md` skill-tool binding contract.
- Screenshots/logs: not applicable; this slice renders inside the existing
  technical details panel and does not alter layout primitives.
- High-risk checks: no secrets, provider calls, mutation gates, auth policy, DB
  schema, or deployment behavior changed.
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/planning/skill-guided-bounded-action-loop-plan.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
- Design source type: not applicable
- Design source reference: existing Tools surface
- Canonical visual target: existing Tools technical details pattern
- Fidelity target: structurally_faithful
- Stitch used: no
- Experience-quality bar reviewed: not applicable
- Visual-direction brief reviewed: not applicable
- Existing shared pattern reused: `ToolsTechnicalDetailPanel`
- New shared pattern introduced: no
- Design-memory entry reused: not applicable
- Design-memory update required: no
- Visual gap audit completed: not applicable
- Background or decorative asset strategy: not applicable
- Canonical asset extraction required: no
- Screenshot comparison pass completed: not applicable
- Remaining mismatches: none known
- State checks: loading | empty | error | success remain owned by existing
  Tools surface and unchanged
- Feedback locality checked: yes
- Raw technical errors hidden from end users: not applicable
- Responsive checks: covered by existing grid and web build; no new layout
  primitive introduced
- Input-mode checks: not applicable
- Accessibility checks: details/summary pattern unchanged
- Parity evidence: existing Tools detail panel reused

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert this task's frontend/backend contract changes; no data
  migration or provider rollback required.
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes
This task intentionally does not implement the bounded execute-observe-adjust
loop. It only makes approved skill-tool metadata visible through the existing
tools overview contract.

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: product-shell users and future implementation
  agents
- Existing workaround or pain: skill/tool bindings were only described in docs,
  not visible in the app-facing tool truth.
- Smallest useful slice: add metadata-only bindings to current overview.
- Success metric or signal: API test pins binding shape and web build compiles.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: not applicable

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: Tools overview inspection
- SLI: not applicable
- SLO: not applicable
- Error budget posture: not applicable
- Health/readiness check: no health contract changed
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: focused API test and web build
- Rollback or disable path: revert scoped files

## Integration Evidence
- `INTEGRATION_CHECKLIST.md` reviewed: yes
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: unchanged
- Error state verified: unchanged
- Refresh/restart behavior verified: stateless response metadata
- Regression check performed: focused API contract test plus web build

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public capability metadata
- Trust boundaries: skills are metadata only; action remains execution owner
- Permission or ownership checks: unchanged authenticated `/app/tools/overview`
- Abuse cases: skill metadata must not imply authorization or execution
- Secret handling: no secrets touched
- Security tests or scans: provider payload sentinel test remains in
  `test_api_routes.py`
- Fail-closed behavior: no execution path added
- Residual risk: future PRJ-805 must align registry metadata with this visible
  binding shape.

## AI Testing Evidence (required for AI features)
- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report
- Task summary: `/app/tools/overview` now returns metadata-only skill-tool
  bindings for web search, web browser, and ClickUp; the Tools route renders
  them in technical details.
- Files changed:
  - `backend/app/core/app_tools_policy.py`
  - `backend/tests/test_api_routes.py`
  - `web/src/lib/api.ts`
  - `web/src/components/tools.tsx`
  - `web/src/App.tsx`
  - task/context/state/planning docs
- How tested:
  - focused tools overview API tests
  - full API route regression file
  - web production build
- What is incomplete:
  - `PRJ-805` still needs runtime skill registry metadata for the same
    tool-aware skills.
- Next steps:
  - `PRJ-805` Add skill registry metadata for tool-aware skills.
- Decisions made:
  - binding authority is explicit as `metadata_only_not_execution_authority`.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: skill/tool bindings existed in architecture docs but not in product
  API truth.
- Gaps: Tools overview could show capabilities but not the skill metadata that
  may consider them.
- Inconsistencies: none requiring architecture decision.
- Architecture constraints: action-only execution, no skill-owned side effects.

### 2. Select One Priority Task
- Selected task: `PRJ-804`.
- Priority rationale: first implementation slice after `PRJ-803`; reduces
  architecture/API visibility drift without changing behavior.
- Why other candidates were deferred: `PRJ-805+` depend on visible binding
  truth or deeper runtime contract changes.

### 3. Plan Implementation
- Files or surfaces to modify: backend overview policy, tests, web types, Tools
  detail rendering, context/state docs.
- Logic: add metadata-only binding list per relevant tool.
- Edge cases: tools without bindings return an empty list.

### 4. Execute Implementation
- Implementation notes: reused `_tool_item` and existing
  `ToolsTechnicalDetailPanel`; no new endpoint, provider, or style primitive.

### 5. Verify and Test
- Validation performed: focused API tests and web build.
- Result: passed. Full `tests/test_api_routes.py` also passed with
  `123 passed`.

### 6. Self-Review
- Simpler option considered: placing bindings only in `capabilities`; rejected
  because it would blur tool operation capability with skill metadata.
- Technical debt introduced: no
- Scalability assessment: field can be reused by `PRJ-805` registry metadata
  and later action-loop diagnostics.
- Refinements made: binding records include execution owner and metadata-only
  authority to avoid UI/auth ambiguity.

### 7. Update Documentation and Knowledge
- Docs updated: task, planning queue, project state, task board, agent state.
- Context updated: yes
- Learning journal updated: not applicable.
