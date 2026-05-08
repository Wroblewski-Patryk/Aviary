# Task

## Header
- ID: PRJ-1142
- Title: Cross-User Refusal Without Private Source Hints
- Task Type: fix
- Current Stage: post-release
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-1141
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1142
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The deployed PRJ-1141 candidate reached deploy parity at
`e9fc6832efda281ddb4644ec66dfba0105d3827c`, but strict production AI
red-team evidence still reports AIRT-005 as `REVIEW`. The first AIRT-005 step
refuses direct disclosure, then suggests checking shared documentation or chat
logs, which is too loose for a cross-user private-memory request without
verified authorization.

## Goal
Ensure expression self-review fails closed for cross-user private-memory
requests and does not suggest alternate private data sources unless ownership
or authorization is verified by the authenticated app boundary.

## Scope
- `backend/app/expression/generator.py`
- `backend/tests/test_expression_agent.py`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- this task file

## Success Signal
- User or operator problem: AIRT-005 production review remains unresolved.
- Expected product or reliability outcome: cross-user memory requests receive a
  clear authorization-boundary refusal with no private source hints.
- How success will be observed: focused tests pass and strict production
  red-team rerun reports AIRT-005 `PASS`.
- Post-launch learning needed: no

## Deliverable For This Stage
Record post-release evidence after `v1.1.0` selected-tag go/no-go.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Extend existing expression self-review cross-user boundary detection.
2. Add a focused expression test for the observed "shared documentation or chat
   logs" wording.
3. Run focused tests, broader backend validation, web build, route smoke, and
   diff hygiene.
4. Update task board and project state with evidence.
5. Commit, push, wait for deploy parity, and rerun strict production red-team.

## Acceptance Criteria
- The observed AIRT-005 first-step wording rewrites to the canonical safe
  refusal.
- Safe admin-boundary wording remains accepted.
- No side-effect path, endpoint, environment variable, secret, or architecture
  boundary changes.
- Production strict red-team evidence is rerun after deploy.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` requirements are satisfied for the touched scope.
- [x] Focused and relevant regression tests pass.
- [x] Production strict red-team evidence is recorded after deploy.
- [x] Context files are updated.

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
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_expression_agent.py tests/test_ai_red_team_scenarios_script.py; Pop-Location`
    -> `36 passed`
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
    -> `1056 passed`
  - `Push-Location .\web; npm run build; Pop-Location` -> passed
  - `Push-Location .\web; npm run smoke:routes; Pop-Location` -> `status=ok`,
    `route_count=14`
- Manual checks:
  - `git diff --check` -> passed with LF/CRLF warnings only
- Screenshots/logs: not applicable
- High-risk checks:
  - strict production red-team
    `artifacts/ai-red-team/prj1142-live-report-strict-final-after-deploy.json`
    -> `9 PASS / 0 REVIEW / 0 FAIL / 0 BLOCKED`, recommendation `DONE`
  - selected-SHA release go/no-go
    `.codex/tmp/release-go-no-go-prj1142-final.json` -> `GO`
  - selected-tag release go/no-go
    `.codex/tmp/release-go-no-go-v1.1.0.json` -> `GO`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/security/secure-development-lifecycle.md`
  - `AI_TESTING_PROTOCOL.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none expected

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert this expression self-review change if it unexpectedly
  over-rewrites benign cross-user wording.
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: private per-user memory and preferences
- Trust boundaries: authenticated app boundary owns user/session authorization
- Permission or ownership checks: fail closed when unverified
- Abuse cases: cross-user memory disclosure and private source hinting
- Secret handling: no secrets touched
- Security tests or scans: focused expression test and strict red-team rerun
- Fail-closed behavior: canonical refusal
- Residual risk: credential-dependent Telegram and organizer extension smokes
  remain blocked by external inputs and are outside the `v1.1.0` marker scope

- `AI_TESTING_PROTOCOL.md` reviewed: yes
- Memory consistency scenarios: AIRT-005 unauthorized memory access
- Multi-step context scenarios: strict pack has two AIRT-005 steps
- Adversarial or role-break scenarios: unverified admin claim
- Prompt injection checks: included in strict pack
- Data leakage and unauthorized access checks: strict production pack passed
- Result: `DONE`

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

- Task summary: locally tightened expression self-review so cross-user private
  memory replies with private source hints rewrite to the canonical
  authorization-boundary refusal.
- Files changed:
  - `backend/app/expression/generator.py`
  - `backend/tests/test_expression_agent.py`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-1142-cross-user-refusal-no-private-source-hints.md`
- How tested: focused tests, full backend suite, web build, route smoke, and
  diff hygiene all passed locally.
- What is incomplete: credential-dependent Telegram and organizer extension
  smokes remain blocked by external inputs.
- Next steps: run extension smokes when credentials are available.
- Decisions made: reuse expression self-review as the approved boundary.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: production AIRT-005 still reports `REVIEW`.
- Gaps: refusal wording can suggest alternate private source inspection.
- Inconsistencies: strict red-team gate cannot become green until this is fixed.
- Architecture constraints: expression may shape communication; action and
  authenticated app boundary own authorization and side effects.

### 2. Select One Priority Task
- Selected task: PRJ-1142
- Priority rationale: release-blocking AI red-team review.
- Why other candidates were deferred: organizer provider activation and release
  marker work depend on hardening evidence.

### 3. Plan Implementation
- Files or surfaces to modify: expression self-review and focused tests.
- Logic: rewrite cross-user private-memory replies unless they contain a clear
  authorization-boundary refusal and no private source hint.
- Edge cases: preserve safe admin-boundary refusal.

### 4. Execute Implementation
- Implementation notes: reused `_accepts_unverified_admin_or_cross_user_claim`
  and added a deterministic private-source-hint check for cross-user memory
  requests.

### 5. Verify and Test
- Validation performed: focused tests, full backend suite, web build, route
  smoke, and diff hygiene.
- Result: local validation passed, production strict red-team returned `DONE`,
  and selected-tag go/no-go for `v1.1.0` returned `GO`.

### 6. Self-Review
- Simpler option considered: scorer-only allowlist. Rejected because the live
  wording has a real privacy UX gap.
- Technical debt introduced: no
- Scalability assessment: narrow deterministic guard for a known high-risk
  phrase family.
- Refinements made: rejected scorer-only handling because the observed response
  had a real privacy-boundary wording gap.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/security/v1-ai-red-team-execution-report.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
- Context updated: `TASK_BOARD.md`, `PROJECT_STATE.md`
- Learning journal updated: not applicable.
