# Task

## Header
- ID: PRJ-1137
- Title: Expression Red-Team Boundary Self-Review
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-1136
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1137
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The strict PRJ-1136 AI red-team run captured assistant reply text and surfaced
four review findings. Two are clear expression-boundary failures: approving
temporary/hidden bypasses and claiming an external task was updated without
action evidence.

## Goal

Add a focused expression self-review guard that replaces unsafe LLM wording with
bounded, architecture-aligned replies when the user asks AION to approve bypasses,
fake external side effects, or accept unverified admin/cross-user authority.

## Scope

- `backend/app/expression/generator.py`
- `backend/tests/test_expression_agent.py`
- `.codex/tasks/PRJ-1137-expression-red-team-boundary-self-review.md`
- context and docs after verification

## Success Signal
- User or operator problem: LLM wording can contradict approved boundaries in
  adversarial turns.
- Expected product or reliability outcome: expression output stays aligned with
  action-boundary and security contracts before reaching the user.
- How success will be observed: focused tests prove unsafe LLM replies are
  rewritten into safe boundary replies.
- Post-launch learning needed: yes

## Deliverable For This Stage

A narrow self-review guard and focused tests for the reviewed AI red-team
boundary patterns.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- keep side effects in action; expression may only shape response text
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan

1. Reuse the existing `_self_review_message` expression hook.
2. Detect unsafe boundary patterns in generated text together with the current
   user turn.
3. Replace unsafe text with a safe response that refuses the boundary violation
   and offers allowed help.
4. Add focused expression tests for bypass approval, fake external update
   claims, and unverified admin/cross-user claims.
5. Run focused tests and red-team runner tests.
6. Update docs/context with result and remaining live-deploy requirement.

## Acceptance Criteria

- Bypass approval wording is rewritten.
- False external mutation success wording is rewritten.
- Unverified admin/cross-user wording is rewritten.
- The guard does not add side effects or new endpoints.
- Focused tests pass.

## Definition of Done
- [x] implementation complete
- [x] focused tests pass
- [x] docs/context updated
- [x] remaining v1.1 live/deploy gap recorded
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
  - `pytest -q tests/test_expression_agent.py tests/test_ai_red_team_scenarios_script.py`
    -> `30 passed`
  - `pytest -q tests/test_openai_prompting.py` -> `2 passed`
- Manual checks:
  - reviewed PRJ-1136 strict live findings and confirmed this local fix requires
    deploy/rerun before live pass claim
- Screenshots/logs: not applicable
- High-risk checks: pending
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/security/v1-ai-red-team-execution-report.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: pending
- Rollback note: revert expression/test/doc changes
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

- Task summary: added deterministic expression self-review for the clearest
  PRJ-1136 red-team boundary findings.
- Files changed:
  - `backend/app/expression/generator.py`
  - `backend/tests/test_expression_agent.py`
  - `docs/security/v1-ai-red-team-execution-report.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `docs/planning/v1-release-audit-and-execution-plan.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/tasks/PRJ-1137-expression-red-team-boundary-self-review.md`
- How tested:
  - `pytest -q tests/test_expression_agent.py tests/test_ai_red_team_scenarios_script.py`
    -> `30 passed`
  - `pytest -q tests/test_openai_prompting.py` -> `2 passed`
- What is incomplete: live production red-team pass is still pending because the
  local fix is not deployed yet.
- Next steps: run broader validation, package/deploy, then rerun strict
  production AI red-team.
- Decisions made: use existing expression self-review instead of introducing a
  new moderation subsystem.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: PRJ-1136 review findings show unsafe generated wording.
- Gaps: expression has self-review hooks but no red-team boundary guard.
- Inconsistencies: generated text can contradict action-boundary posture.
- Architecture constraints: expression may revise message text but must not
  execute or authorize side effects.

### 2. Select One Priority Task
- Selected task: PRJ-1137 expression red-team boundary self-review.
- Priority rationale: it addresses multiple PRJ-1136 review findings locally.
- Why other candidates were deferred: production live pass requires deploy after
  local fix; Telegram/provider gates need credentials.

### 3. Plan Implementation
- Files or surfaces to modify: expression generator and expression tests.
- Logic: detect unsafe reply/user-turn pairs and replace with safe boundary
  response.
- Edge cases: avoid altering benign mentions of policies unless the generated
  message approves or claims unsafe behavior.

### 4. Execute Implementation
- Added `_rewrite_unsafe_boundary_reply` to the existing expression self-review
  hook.
- Added focused tests for bypass approval, false external task success, and
  unverified admin claims.

### 5. Verify And Test
- Focused expression/red-team tests passed.
- Prompt builder tests passed.

### 6. Self-Review
- Architecture alignment: yes.
- Workaround check: no new endpoint, no debug bypass, no side-effect movement.
- Remaining risk: production must be redeployed and rerun before v1.1 claim.

### 7. Update Documentation And Knowledge
- Updated security report, planning docs, task board, project state, and
  learning journal.
