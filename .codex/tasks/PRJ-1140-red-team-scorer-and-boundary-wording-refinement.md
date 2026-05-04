# Task

## Header
- ID: PRJ-1140
- Title: Red-Team Scorer And Boundary Wording Refinement
- Task Type: fix
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1139
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1140
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The deployed strict red-team run after PRJ-1139 improved AIRT-003, but AIRT-001
failed because the safe fallback repeated the exact `must_not` phrase. AIRT-005
and AIRT-007 remained review due to broad sentinels that flagged safe refusal
phrases mentioning `user B` or `secrets`.

## Goal

Refine the local boundary wording and scorer so the strict pack flags unsafe
behavior, not safe refusal text.

## Scope

- `backend/app/expression/generator.py`
- `backend/scripts/run_ai_red_team_scenarios.py`
- focused tests for expression/scorer behavior
- task/context/docs after validation

## Success Signal
- User or operator problem: strict red-team output is still noisy and one safe
  fallback repeats a forbidden phrase.
- Expected product or reliability outcome: safe refusal text avoids exact
  `must_not` phrases and scorer review sentinels skip clearly safe refusals.
- How success will be observed: focused tests pass locally before packaging.
- Post-launch learning needed: no

## Deliverable For This Stage

Focused local fix and validation.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- do not mark v1.1 pass before deploy and live rerun

## Implementation Plan

1. Change the expression safe fallback wording to avoid exact `must_not` text.
2. Refine scorer sentinel handling for safe `user B` and `secret` refusal
   language.
3. Add focused regression coverage.
4. Run focused tests, then broader candidate validation if focused tests pass.
5. Package/deploy/rerun in a later release slice.

## Acceptance Criteria

- AIRT-001 safe fallback no longer repeats the exact `must_not` phrase.
- Safe refusal mentioning user B does not trigger broad review.
- Safe refusal mentioning secrets does not trigger broad review.
- Unsafe success/bypass patterns still trigger review or fail.

## Definition of Done
- [x] implementation complete
- [x] focused tests pass
- [x] docs/context updated
- [x] remaining deploy/rerun gap recorded

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
  - focused expression/scorer tests: `32 passed`
  - backend full suite: `1052 passed`
  - web build: passed
  - web route smoke: `status=ok`, `route_count=14`
  - `git diff --check`: passed with LF/CRLF warnings only
- Manual checks:
  - inspected PRJ-1140 strict production report findings for AIRT-001,
    AIRT-005, and AIRT-007 before refining local code
- Screenshots/logs: not applicable
- High-risk checks: v1.1 pass remains blocked until deploy/rerun
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
- Deploy impact: low after packaging
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: revert local fix commit
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

- Task summary: refined safe boundary wording and scorer safe-refusal handling
  for the remaining strict red-team noise.
- Files changed:
  - `backend/app/expression/generator.py`
  - `backend/scripts/run_ai_red_team_scenarios.py`
  - `backend/tests/test_expression_agent.py`
  - `backend/tests/test_ai_red_team_scenarios_script.py`
  - `.codex/tasks/PRJ-1140-red-team-scorer-and-boundary-wording-refinement.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - focused `32 passed`
  - backend `1052 passed`
  - web build passed
  - route smoke `status=ok`, `route_count=14`
  - diff hygiene passed
- What is incomplete: local fix must be committed, pushed, deployed, and strict
  production red-team rerun.
- Next steps: package/push/deploy PRJ-1140, then rerun strict AI red-team.
- Decisions made: scorer is refined, not weakened; exact `must_not` checks
  remain fail-fast.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: deployed strict run has one wording-induced fail and two false-positive
  review sentinels.
- Gaps: local scorer lacks safe-refusal exceptions.
- Inconsistencies: safe fallback repeated exact forbidden phrase.
- Architecture constraints: no new endpoint or runtime path.

### 2. Select One Priority Task
- Selected task: PRJ-1140 scorer and boundary wording refinement.
- Priority rationale: strict red-team gate cannot pass until this is clean.
- Why other candidates were deferred: release marker waits for clean live rerun.

### 3. Plan Implementation
- Files or surfaces to modify: expression guard, scorer, focused tests.
- Logic: keep exact must-not failures; skip broad sentinels only for clear safe
  refusal language.
- Edge cases: unsafe mentions still review/fail.

### 4. Execute Implementation
- Updated safe boundary wording to avoid exact `must_not` phrase repetition.
- Added scorer safe-refusal exceptions for benign `user B` and `secret`
  refusal text.
- Added focused regressions.

### 5. Verify And Test
- Focused tests passed.
- Backend full suite passed.
- Web build and route smoke passed.
- Diff hygiene passed.

### 6. Self-Review
- Architecture alignment: yes.
- Workaround check: no workaround introduced.
- Remaining risk: production requires deploy and strict rerun.

### 7. Update Documentation And Knowledge
- Updated task and context.
