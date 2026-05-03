# Task

## Header
- ID: PRJ-938
- Title: V1 Deploy Parity Blocked By Source Automation
- Task Type: release
- Current Stage: release
- Status: BLOCKED
- Owner: Ops/Release
- Depends on: PRJ-937
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 938
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The Aviary repository-truth repair was committed and pushed to the canonical
`origin/main` repository. Production release smoke with deploy parity then
waited for Coolify source automation, but production continued serving the
previous deployed SHA.

## Goal
Record the deploy-parity blocker without creating a misleading v1 deployment or
release marker claim.

## Scope
- `.codex/tasks/PRJ-938-v1-deploy-parity-blocked-by-source-automation.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-release-marker-blocker.md`

## Implementation Plan
1. Record the pushed candidate SHA.
2. Record the production SHA that remained active after the deploy-parity wait.
3. Record the release smoke command and failure result.
4. Preserve the PRJ-936 release-marker blocker.
5. Name the required operator action: Coolify source-history check or approved
   webhook/UI fallback.

## Acceptance Criteria
- The release queue states that `origin/main` is updated but production parity
  is not green.
- The exact candidate and production SHAs are recorded.
- The next action is clear and uses existing approved deployment mechanisms.
- No release marker or tag is created.

## Definition of Done
- [x] Deploy parity failure is recorded.
- [x] No v1 release marker was created.
- [x] No fallback path was invented.
- [x] Existing fallback requirements remain explicit.

## Stage Exit Criteria
- [x] The release-stage output records the blocking evidence.
- [x] Work from later stages was not mixed in.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- inventing a new deployment path
- claiming v1 deployed while production serves an older SHA
- creating a release tag without green production smoke
- storing or exposing deployment secrets in repository docs

## Validation Evidence
- Tests:
  - documentation-only blocker record
- Manual checks:
  - `git push origin main`
  - production release smoke with deploy parity
  - `GET https://aviary.luckysparrow.ch/health`
  - `GET https://aviary.luckysparrow.ch/settings`
- Screenshots/logs: not applicable
- High-risk checks:
  - no release marker or tag created
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/planning/v1-release-marker-blocker.md`
- Fits approved architecture: yes
- Mismatch discovered: yes
- Decision required from user: no; deploy remains blocked until the existing
  Coolify source automation or approved fallback is available
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - release marker blocker updated with current evidence

## Deployment / Ops Evidence
- Deploy impact: medium
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note:
  - production is still serving the prior SHA, so no runtime rollback was
    needed from this push
- Observability or alerting impact:
  - `/health.deployment.runtime_build_revision` remains the blocker signal
- Staged rollout or feature flag: not applicable

## Result Report

- Task summary:
  - `origin/main` was updated, but production did not deploy the selected
    candidate within the release-smoke parity window
- Files changed:
  - listed in Scope
- How tested:
  - release smoke with deploy parity failed after 900 seconds
  - direct health/settings checks still reported the old production SHA
- What is incomplete:
  - Coolify source automation did not deploy the selected candidate
  - approved webhook fallback could not be run locally because Coolify webhook
    URL/secret were not present in the environment
- Next steps:
  - verify Coolify deployment history/source connection for app
    `jr1oehwlzl8tcn3h8gh2vvih`
  - if source automation is missing, run the approved webhook fallback with
    operator-provided webhook URL/secret or use Coolify UI redeploy as the
    documented exception-only fallback
  - rerun release smoke with deploy parity
- Decisions made:
  - v1 is not marked deployed until production serves the selected SHA

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - production remained on `ed1c4d981314787d76252985b53c14ea1d7886ed`
- Gaps:
  - missing local Coolify webhook URL/secret for fallback trigger
- Inconsistencies:
  - source automation policy surface says primary automation, but runtime did
    not converge within the smoke window
- Architecture constraints:
  - fallback must use the approved webhook helper or UI exception path

### 2. Select One Priority Task
- Selected task:
  - PRJ-938 V1 Deploy Parity Blocked By Source Automation
- Priority rationale:
  - deployment status must not be ambiguous after a failed parity wait
- Why other candidates were deferred:
  - release marker remains blocked until deployment is green

### 3. Plan Implementation
- Files or surfaces to modify:
  - release blocker docs and context only
- Logic:
  - no runtime changes
- Edge cases:
  - do not record secrets

### 4. Execute Implementation
- Implementation notes:
  - recorded exact blocker evidence

### 5. Verify And Test
- Validation performed:
  - production release smoke with deploy parity
  - production health/settings revision checks
- Result:
  - blocked

### 6. Self-Review
- Simpler option considered:
  - waiting longer without new evidence was rejected after the configured
    900-second release-smoke window elapsed
- Technical debt introduced: no
- Scalability assessment:
  - no system changes
- Refinements made:
  - preserved approved fallback path instead of inventing another trigger

### 7. Update Documentation And Knowledge
- Docs updated:
  - release marker blocker
- Context updated:
  - task board and project state
- Learning journal updated: not applicable
