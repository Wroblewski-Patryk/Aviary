# Task

## Header
- ID: PRJ-937
- Title: Sync Aviary Repository Truth For V1 Deploy
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-930, PRJ-936
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 937
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents after the
  user confirmed `Aviary` is the current repository name.

## Context
The local branch is ahead of `origin/main`, and PRJ-936 blocks a v1 release
marker until the selected release SHA is deployed and production release smoke
passes. A repository-truth mismatch was found before deployment: some current
docs still treated `Wroblewski-Patryk/Personality` as canonical, while local
`origin` and the user's clarification confirm the repository was renamed again
and the current deploy source is `Wroblewski-Patryk/Aviary`.

## Goal
Repair repository/deploy source truth before pushing the selected local
candidate to the canonical production source repository.

## Scope
- `.codex/tasks/PRJ-937-sync-aviary-repository-truth-and-deploy-v1-candidate.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `docs/operations/runtime-ops-runbook.md`
- `docs/planning/next-iteration-plan.md`
- `docs/planning/open-decisions.md`
- `docs/planning/v1-deployment-trigger-slo-evidence.md`

## Implementation Plan
1. Confirm local `origin` and current `HEAD`.
2. Update repo/deploy source docs to name `Wroblewski-Patryk/Aviary` as current
   canonical truth and `Personality` as the former name.
3. Run documentation validation.
4. Commit the documentation repair before deployment.
5. Push `main` to `origin` as the next release action.
6. Run production release smoke with deploy parity against
   `https://aviary.luckysparrow.ch` as the next release action.

## Acceptance Criteria
- Current source-of-truth docs no longer identify `Personality` as the active
  production deploy repository.
- Current source-of-truth docs identify `Wroblewski-Patryk/Aviary` as the
  active production deploy repository.
- The next release action is unambiguous: push `main` to the current `origin`
  and run release smoke with deploy parity.

## Definition of Done
- [x] Repository-truth drift is repaired in current docs and context.
- [x] Documentation validation passes.
- [x] Changes are ready to commit before push.
- [x] Deployment command path remains the existing source-automation path.

## Stage Exit Criteria
- [x] The verification-stage output contains repo-truth validation evidence.
- [x] Any remaining deployment action is explicit and not hidden behind docs.
- [x] Rollback path remains the existing Coolify/source-history rollback path.

## Forbidden
- new deployment systems
- manual webhook/UI redeploy as primary proof unless source automation fails
- release tag creation before green production evidence
- changing runtime behavior while repairing docs/deploy truth

## Validation Evidence
- Tests:
  - not applicable; documentation-only deploy-source truth repair
- Manual checks:
  - `git remote -v`
  - `git rev-parse HEAD`
  - repository-truth search across `.codex` and `docs`
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no runtime behavior changed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/planning/v1-release-marker-blocker.md`
- Fits approved architecture: yes
- Mismatch discovered: yes
- Decision required from user: yes, resolved by user selecting current `origin`
  and clarifying that `Aviary` is the renamed repository
- Approval reference if architecture changed: user confirmation on 2026-05-03
- Follow-up architecture doc updates:
  - current deploy-source docs updated in this task

## Deployment / Ops Evidence
- Deploy impact: low
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: repo-truth notes only
- Rollback note:
  - use existing Coolify deployment history rollback/redeploy to the last green
    SHA if release smoke fails after push
- Observability or alerting impact:
  - `/health.deployment` and release smoke remain the proof surfaces
- Staged rollout or feature flag: not applicable

## Result Report

- Task summary: pending
- Task summary:
  - repaired current docs and context so `Wroblewski-Patryk/Aviary` is the
    active production deploy repository and `Personality` is the former name
- Files changed:
  - listed in Scope
- How tested:
  - `git remote -v`
  - `git rev-parse HEAD`
  - repository-truth search across `.codex` and `docs`
- What is incomplete:
  - push and production release smoke are the next release actions after this
    documentation repair is committed
- Next steps:
  - commit this repair, push `main`, and run production release smoke with
    deploy parity
- Decisions made:
  - `Wroblewski-Patryk/Aviary` is the current canonical repository;
    `Personality` is a former name

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - local `main` was ahead of `origin/main`
  - production still served an older SHA
  - docs had stale `Personality` deploy-source references
- Gaps:
  - selected local release candidate not deployed yet
- Inconsistencies:
  - runbook/current planning docs disagreed with local `origin`
- Architecture constraints:
  - source automation is the primary deployment path

### 2. Select One Priority Task
- Selected task:
  - PRJ-937 Sync Aviary Repository Truth And Deploy V1 Candidate
- Priority rationale:
  - deployment cannot safely proceed while the canonical source repository is
    ambiguous
- Why other candidates were deferred:
  - tag/marker work depends on green deploy parity

### 3. Plan Implementation
- Files or surfaces to modify:
  - current ops/planning/context docs
- Logic:
  - no runtime logic changes
- Edge cases:
  - do not tag if production smoke fails

### 4. Execute Implementation
- Implementation notes:
  - updated current deploy-source docs and context; no runtime files changed

### 5. Verify And Test
- Validation performed:
  - confirmed local `origin` points at `https://github.com/Wroblewski-Patryk/Aviary.git`
  - searched current docs and context for stale active `Personality` repo truth
- Result:
  - current deploy-source truth now points at `Wroblewski-Patryk/Aviary`

### 6. Self-Review
- Simpler option considered:
  - pushing without doc repair was rejected because it would preserve deploy
    source drift
- Technical debt introduced: no
- Scalability assessment:
  - documentation-only source truth repair
- Refinements made:
  - scoped the task to repository-truth repair so deployment smoke can validate
    the exact pushed commit without a follow-up evidence commit changing HEAD

### 7. Update Documentation And Knowledge
- Docs updated:
  - runbook and deployment-trigger SLO evidence
- Context updated:
  - task board, project state, learning journal
- Learning journal updated: yes
