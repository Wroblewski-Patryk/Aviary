# Task

## Header
- ID: PRJ-1128
- Title: Coolify UI redeploy and release smoke recovery
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1124, PRJ-1125, PRJ-1126, PRJ-1127
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1128
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Production returned `503 Service Unavailable` with body `no available server`
after the pushed post-v1 candidate
`3b46ed3878a8560c3adb147fcadf064818ccc322` failed to converge through the
initial Coolify webhook deployment. The user provided explicit Coolify access,
so the approved UI manual fallback path could be used for the canonical
Coolify application.

## Goal

Restore the canonical production app through the existing Coolify UI path,
prove production deploy parity for the selected candidate SHA, and capture
release evidence without moving the selected SHA.

## Scope

- Coolify canonical app:
  - project `icmgqml9uw3slzch9m9ok23z`
  - environment `qxooi9coxat272krzjx221fv`
  - application `jr1oehwlzl8tcn3h8gh2vvih`
- Production URL: `https://aviary.luckysparrow.ch`
- Candidate SHA: `3b46ed3878a8560c3adb147fcadf064818ccc322`
- Repository evidence only:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/operations/runtime-ops-runbook.md`

## Success Signal
- User or operator problem: production had no available app server after the
  candidate deployment attempt.
- Expected product or reliability outcome: public production returns healthy
  responses and reports the selected backend and web build revision.
- How success will be observed: release reality audit returns
  `GO_FOR_SELECTED_SHA`, and release smoke passes.
- Post-launch learning needed: yes

## Deliverable For This Stage

Release recovery evidence for the canonical Coolify UI redeploy and production
smoke result.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not write Coolify credentials or secrets to repository files
- do not push evidence-only changes that would move the selected deploy SHA

## Implementation Plan
1. Inspect the canonical Coolify app, deployment history, and logs.
2. Use the existing Coolify UI `Deploy` action for the canonical app.
3. Watch the new deployment until it reaches a terminal state.
4. Run production release reality audit for the selected SHA.
5. Run production release smoke with deploy parity.
6. Export a release-smoke incident evidence bundle.
7. Update task/context/evidence docs without changing runtime code.

## Acceptance Criteria
- Coolify deployment history shows a successful manual deployment for
  `3b46ed3`.
- Public `/health` returns HTTP `200`.
- Production backend revision equals
  `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Production web build revision equals
  `3b46ed3878a8560c3adb147fcadf064818ccc322`.
- Release reality audit verdict is `GO_FOR_SELECTED_SHA`.
- Release smoke exits successfully.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for this release evidence slice.
- [x] Production redeploy and parity evidence captured.
- [x] Release smoke evidence captured.
- [x] Relevant source-of-truth docs updated.

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
- storing or echoing Coolify credentials in repo artifacts

## Validation Evidence
- Tests:
  - not rerun; this task changed no runtime code and relies on PRJ-1122 local
    validation plus production release smoke
- Manual checks:
  - Coolify app page: `aviary (localhost)` under Root Team
  - Coolify deployment page: latest manual deployment for commit `3b46ed3`
    succeeded, started `2026-05-03 22:57:33 UTC`, ended
    `2026-05-03 22:59:10 UTC`, duration `01m 37s`
  - `Invoke-WebRequest https://aviary.luckysparrow.ch/health` -> HTTP `200`
- Screenshots/logs:
  - `.codex/tmp/coolify-after-deploy-click.png`
  - `.codex/tmp/coolify-deployment-after-redeploy-watch.png`
  - `.codex/tmp/release-reality-audit-after-coolify-ui.json`
  - `.codex/tmp/incident-evidence-after-coolify-ui/20260503T230011Z_incident-bundle-20260503T230011Z/`
- High-risk checks:
  - release reality audit:
    `verdict=GO_FOR_SELECTED_SHA`
  - `release_marker_allowed=true`
  - production backend revision:
    `3b46ed3878a8560c3adb147fcadf064818ccc322`
  - production web build revision:
    `3b46ed3878a8560c3adb147fcadf064818ccc322`
  - release smoke with deploy parity exited successfully
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/architecture/26_env_and_config.md`
  - `docs/architecture/27_codex_instructions.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: high
- Env or secret changes: none made
- Health-check impact: restored public health from `503 no available server`
  to HTTP `200`
- Smoke steps updated: release evidence index and runbook updated
- Rollback note: Coolify rollback remains the operator-owned rollback path for
  the canonical app if the selected candidate regresses
- Observability or alerting impact: release-smoke incident evidence bundle can
  now be exported again from public production
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

The first failed Coolify deployment for the selected SHA imported the correct
repository commit and failed after removing old containers and starting the new
application. The manual UI redeploy for the same canonical app and same SHA
completed successfully. This supports the existing manual UI fallback as an
operator exception path, not a new deployment mechanism.

## Production-Grade Required Contract

Every task must include Goal, Scope, Implementation Plan, Acceptance Criteria,
Definition of Done, and Result Report. This task includes all required sections.

Runtime vertical slice note: no runtime behavior was changed in this task; the
slice was deployment recovery and production evidence only.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: production operator and v1 users
- Existing workaround or pain: public production returned `503 no available server`
- Smallest useful slice: approved Coolify UI redeploy for the canonical app
- Success metric or signal: production health and release smoke green for the
  selected SHA
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: heartbeat deploy-parity recheck remains
  active

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: public production availability and v1 readiness
- SLI: `/health` availability and backend/web deploy parity
- SLO: deployment trigger SLO documented in release evidence index
- Error budget posture: healthy after recovery
- Health/readiness check: `/health` HTTP `200`, `release_ready=true`
- Logs, dashboard, or alert route: Coolify deployment history plus release
  smoke output
- Smoke command or manual smoke:
  - `run_release_smoke.ps1 -BaseUrl https://aviary.luckysparrow.ch -WaitForDeployParity`
- Rollback or disable path: Coolify rollback for canonical app

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: yes
- DB schema and migrations verified: via production health/readiness surfaces
- Loading state verified: not applicable
- Error state verified: public `503` before recovery, HTTP `200` after recovery
- Refresh/restart behavior verified: Coolify manual redeploy succeeded
- Regression check performed: release smoke with deploy parity

## AI Testing Evidence (required for AI features)

Not applicable. This task changed no AI behavior.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: operational deployment metadata
- Trust boundaries: Coolify UI session and public production endpoints
- Permission or ownership checks: user provided explicit Coolify access
- Abuse cases: credentials must not be committed or echoed into repo docs
- Secret handling: credentials were used only for login/session; no secret
  values were written into tracked files
- Security tests or scans: not applicable
- Fail-closed behavior: no environment or secret changes were made
- Residual risk: the automatic webhook/source deployment trigger still needs
  follow-up reliability evidence because manual UI fallback was used

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: no secret persistence in repo
- Result: pass for this ops-only slice

## Result Report

- Task summary: restored production availability and deploy parity by using the
  approved Coolify UI manual redeploy fallback for the canonical app.
- Files changed:
  - `.codex/tasks/PRJ-1128-coolify-ui-redeploy-release-smoke-recovery.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `.codex/context/LEARNING_JOURNAL.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/operations/runtime-ops-runbook.md`
- How tested:
  - Coolify deployment watch
  - production `/health`
  - release reality audit
  - release smoke with deploy parity
  - release-smoke incident bundle export
- What is incomplete:
  - Coolify automatic source/webhook trigger reliability still needs a separate
    follow-up if manual fallback exception rate is to be reduced
  - organizer provider activation remains an extension blocker, not a core v1
    blocker
- Next steps:
  - create a narrow follow-up for Coolify source automation evidence if needed
  - do not move release marker or selected SHA unless a new candidate is chosen
- Decisions made:
  - used the existing Coolify UI manual fallback after explicit user-provided
    access and canonical app confirmation

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - production was unavailable with `503 no available server`
  - first deployment for selected SHA failed in Coolify
- Gaps:
  - no webhook fallback credentials were available locally
- Inconsistencies:
  - local Coolify-shape smoke passed while production app was exited
- Architecture constraints:
  - use existing deployment mechanisms and preserve action boundaries

### 2. Select One Priority Task
- Selected task: PRJ-1128 Coolify UI redeploy and release smoke recovery
- Priority rationale: public production availability and selected-SHA parity are
  P0 release blockers
- Why other candidates were deferred: provider activation and automation SLO
  follow-up are lower priority after restoring production

### 3. Plan Implementation
- Files or surfaces to modify: source-of-truth docs only
- Logic: no runtime logic changes
- Edge cases:
  - avoid storing credentials
  - avoid pushing evidence-only commits that move the selected SHA

### 4. Execute Implementation
- Implementation notes:
  - switched Coolify to Root Team
  - confirmed canonical Aviary app IDs
  - inspected deployment history and app logs
  - triggered the canonical app `Deploy` UI action

### 5. Verify and Test
- Validation performed:
  - Coolify deployment watch
  - production health check
  - release reality audit
  - release smoke with deploy parity
  - incident evidence bundle export
- Result: passed

### 6. Self-Review
- Simpler option considered: rerun release audit only
- Technical debt introduced: no
- Scalability assessment: manual fallback is acceptable as an exception path;
  source automation reliability should be tracked separately
- Refinements made: captured Root Team/Coolify access pitfall in learning
  journal

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/release-evidence-index.md`
  - `docs/operations/runtime-ops-runbook.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: yes
