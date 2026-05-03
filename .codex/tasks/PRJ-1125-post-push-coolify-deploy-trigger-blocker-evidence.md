# Task

## Header
- ID: PRJ-1125
- Title: Post-Push Coolify Deploy Trigger Blocker Evidence
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1124
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1125
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1124 packaged and pushed the current post-v1 candidate to `origin/main`.
PRJ-952 remained the next release blocker until production proved deploy parity
for the selected SHA.

Selected pushed candidate:

`3b46ed3878a8560c3adb147fcadf064818ccc322`

Production stayed on the previous released revision:

`5e64f494e2aac8d29cea532d95f7039ed6029213`

## Goal

Capture machine-visible evidence that Coolify source automation did not bring
production to the pushed candidate within the approved bounded wait, and keep
the next operator action exact without introducing a workaround.

## Success Signal
- User or operator problem: a pushed candidate needs a clear deploy blocker and
  next action.
- Expected product or reliability outcome: the release lane cannot accidentally
  mark the new candidate as deployed while production still serves the old SHA.
- How success will be observed: release evidence records `HOLD_REVISION_DRIFT`,
  bounded wait timeout, and blocked fallback inputs.
- Post-launch learning needed: yes

## Deliverable For This Stage

An evidence-only release task and source-of-truth updates that preserve the
selected SHA and identify the missing operator-owned deploy trigger inputs.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not create another candidate commit for deploy evidence only, because that
  would move the selected SHA again

## Scope

- `.codex/tasks/PRJ-1125-post-push-coolify-deploy-trigger-blocker-evidence.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `.codex/context/LEARNING_JOURNAL.md`
- `docs/operations/release-evidence-index.md`

## Implementation Plan

1. Verify local `main` and `origin/main` both point at the selected candidate.
2. Run release reality audit against production for the selected SHA.
3. Run bounded deploy parity wait through the existing release smoke script.
4. Run read-only Coolify fallback readiness for the same before/after SHAs.
5. Update task, context, release evidence, and learning journal with the
   observed blocker and next action.

## Acceptance Criteria

- Exact selected SHA is recorded.
- Production revision drift is recorded.
- Bounded wait evidence is recorded.
- Fallback readiness blocker is recorded without exposing secrets.
- No deploy workaround or manual trigger is introduced.

## Definition of Done
- [x] Evidence uses existing release audit, smoke, and fallback readiness tools.
- [x] The selected candidate SHA remains explicit.
- [x] The task records residual blocker and next action.
- [x] Relevant source-of-truth docs are updated.
- [x] `DEFINITION_OF_DONE.md` is satisfied for this evidence-only release task.

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
  - PRJ-1122 local validation remains current:
    - backend `1045 passed`
    - web build passed
    - tools directory characterization `status=ok`
    - chat transcript characterization `status=ok`
    - route smoke `status=ok`, `route_count=14`
- Manual checks:
  - `git log -1 --oneline --decorate`
    - `3b46ed3 (HEAD -> main, origin/main, origin/HEAD) release: package post-v1 candidate`
  - `git status --short --branch`
    - `## main...origin/main`
    - only `.codex/tmp/` and `artifacts/` remain untracked
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - `audit_release_reality.py --selected-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
    - `verdict=HOLD_REVISION_DRIFT`
    - production backend and web revisions:
      `5e64f494e2aac8d29cea532d95f7039ed6029213`
  - `run_release_smoke.ps1 -WaitForDeployParity -DeployParityMaxWaitSeconds 900`
    - failed after 900 seconds because production runtime revision stayed on
      `5e64f494e2aac8d29cea532d95f7039ed6029213`
  - `check_coolify_fallback_readiness.py --before-sha 5e64f494e2aac8d29cea532d95f7039ed6029213 --after-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
    - `ready=false`
    - missing `webhook_url`, `webhook_secret_present`, and
      `webhook_secret_length`
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## UX/UI Evidence (required for UX tasks)
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
- Screenshot comparison pass completed: not applicable
- Remaining mismatches: not applicable
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: high
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: release evidence refreshed; no script change
- Rollback note: production remains on `v1.0.0` target
  `5e64f494e2aac8d29cea532d95f7039ed6029213`; do not move a new marker until
  deploy parity is proven for `3b46ed3878a8560c3adb147fcadf064818ccc322`.
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

## Notes

This task intentionally does not trigger a webhook or UI redeploy. The approved
fallback requires operator-owned `COOLIFY_DEPLOY_WEBHOOK_URL` and
`COOLIFY_DEPLOY_WEBHOOK_SECRET`, and neither value is available in the current
environment.

## Production-Grade Required Contract

Every task must include these mandatory sections before it can move to `READY`
or `IN_PROGRESS`:

- `Goal`
- `Scope` with exact files, modules, routes, APIs, schemas, docs, or runtime
  surfaces
- `Implementation Plan` with step-by-step execution and validation
- `Acceptance Criteria` with testable conditions
- `Definition of Done` using `DEFINITION_OF_DONE.md`
- `Result Report`

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: production can stay healthy while deploy parity
  remains behind the pushed candidate.
- Smallest useful slice: record exact blocker evidence and next command.
- Success metric or signal: no false release marker for the new candidate.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: verify production deploy parity after
  operator redeploy/fallback.

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not
  applicable; no runtime code or observability behavior changed.
- Critical user journey: release candidate deployment
- SLI: deploy parity for backend and web revisions
- SLO: selected SHA visible in production before release marker
- Error budget posture: burning
- Health/readiness check: `/health` and `/settings` remain healthy but stale.
- Logs, dashboard, or alert route: Coolify deployment history is
  operator-owned.
- Smoke command or manual smoke:
  - `.\backend\scripts\run_release_smoke.ps1 -BaseUrl "https://aviary.luckysparrow.ch" -WaitForDeployParity -DeployParityMaxWaitSeconds 900 -DeployParityPollSeconds 30 -HealthRetryMaxAttempts 10 -HealthRetryDelaySeconds 10`
- Rollback or disable path: stay on deployed `v1.0.0` until parity is proven.

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable; evidence-only release
  task.
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: release audit and smoke parity wait

## AI Testing Evidence (required for AI features)

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable; no
  code or permission behavior changed.
- Data classification: non-secret release metadata
- Trust boundaries: operator-owned Coolify webhook credentials remain outside
  the repo and were not fabricated.
- Permission or ownership checks: fallback trigger was not run without
  operator inputs.
- Abuse cases: avoid leaking or inventing deployment secrets.
- Secret handling: missing secret state recorded, no secret values printed.
- Security tests or scans: not applicable
- Fail-closed behavior: release marker remains blocked by deploy parity.
- Residual risk: production auto-deploy source may still be misconfigured or
  delayed outside local control.

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: recorded that pushed candidate
  `3b46ed3878a8560c3adb147fcadf064818ccc322` did not reach production within
  the approved bounded wait.
- Files changed:
  - `.codex/tasks/PRJ-1125-post-push-coolify-deploy-trigger-blocker-evidence.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - release reality audit
  - release smoke deploy parity wait
  - fallback readiness check
  - `git diff --check`
- What is incomplete: external deploy trigger recovery remains blocked until
  Coolify source automation is fixed or operator provides fallback inputs.
- Next steps: operator redeploy/fallback for selected after SHA
  `3b46ed3878a8560c3adb147fcadf064818ccc322`, then rerun PRJ-953 production
  release smoke.
- Decisions made: do not create another candidate commit just to record deploy
  evidence, because that would move the selected SHA.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: production still reports `5e64f494e2aac8d29cea532d95f7039ed6029213`
  after `origin/main` moved to `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Gaps: no local Coolify webhook URL or secret is available.
- Inconsistencies: production is healthy and release-ready for `v1.0.0`, but
  not deployed to the new candidate.
- Architecture constraints: source automation is primary; webhook/UI fallback
  is exception-only and operator-owned.

### 2. Select One Priority Task
- Selected task: PRJ-1125 post-push Coolify deploy trigger blocker evidence.
- Priority rationale: release deployment is the active P0 blocker after
  candidate packaging.
- Why other candidates were deferred: feature work cannot produce a truthful
  release marker while deploy parity is blocked.

### 3. Plan Implementation
- Files or surfaces to modify: task/context/release evidence/learning journal.
- Logic: preserve exact selected SHA, record audit and fallback states, avoid
  manual trigger without approved inputs.
- Edge cases: do not move candidate SHA by creating another release candidate
  commit for evidence only.

### 4. Execute Implementation
- Implementation notes: evidence captured with existing scripts only.

### 5. Verify and Test
- Validation performed:
  - release reality audit: `HOLD_REVISION_DRIFT`
  - release smoke parity wait: timed out after 900 seconds
  - fallback readiness: blocked by missing webhook URL and secret
  - `git diff --check`: passed

### 6. Self-Review
- Architecture alignment: yes; source automation remains primary and fallback
  remains operator-owned.
- Duplication/workaround check: no new deploy mechanism or bypass added.
- Risk: production still needs external Coolify recovery.

### 7. Update Documentation and Knowledge
- Updated:
  - task board
  - project state
  - release evidence index
  - learning journal
