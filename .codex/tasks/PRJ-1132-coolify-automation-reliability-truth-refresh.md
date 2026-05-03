# Task

## Header
- ID: PRJ-1132
- Title: Coolify Automation Reliability Truth Refresh
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1125, PRJ-1128, PRJ-1131
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 1132
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

`v1.0.1` now marks selected SHA
`3b46ed3878a8560c3adb147fcadf064818ccc322`. Production is green and release
smoke passes. The remaining deployment reliability drift is narrower: the
current candidate needed approved Coolify UI fallback after source automation
did not converge during PRJ-1125, while webhook fallback remains blocked
locally by missing operator-provided webhook URL and secret.

## Goal

Refresh Coolify deployment-trigger truth so current v1 release docs distinguish
between achieved release parity and the remaining future-candidate automation
reliability follow-up.

## Scope

- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-deployment-trigger-slo-evidence.md`
- `docs/operations/release-evidence-index.md`
- `docs/operations/runtime-ops-runbook.md`
- `.codex/tasks/PRJ-1132-coolify-automation-reliability-truth-refresh.md`

## Success Signal
- User or operator problem: docs could still imply the release marker is waiting
  on Coolify source/webhook reliability.
- Expected product or reliability outcome: v1 release truth is explicit:
  `v1.0.1` is green, source/webhook automation reliability is a follow-up for
  future candidates.
- How success will be observed: deployment-trigger SLO doc records PRJ-1125,
  PRJ-1128, PRJ-1131, and current fallback readiness evidence.
- Post-launch learning needed: no

## Deliverable For This Stage

Updated release/ops truth docs and validation evidence for current Coolify
automation reliability posture.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it
- do not trigger a deployment
- do not store or print secrets

## Implementation Plan

1. Inspect existing deployment policy, PRJ-930 SLO doc, Coolify fallback
   readiness script, and release evidence docs.
2. Run current selected-tag go/no-go for `v1.0.1`.
3. Run Coolify fallback readiness for the known before/after SHA pair without
   triggering a deploy.
4. Update source-of-truth docs so source automation failure, UI fallback
   success, and webhook fallback blockage are correctly classified.
5. Run diff hygiene.

## Acceptance Criteria
- Docs state `v1.0.1` release parity is achieved and not blocked by this
  follow-up.
- Docs state PRJ-1125 source automation did not converge for the selected SHA.
- Docs state PRJ-1128 UI fallback restored production and is exception-only
  evidence.
- Docs state webhook fallback readiness is currently blocked by missing
  `COOLIFY_DEPLOY_WEBHOOK_URL` and `COOLIFY_DEPLOY_WEBHOOK_SECRET`.
- No deploy trigger runs in this task.

## Definition of Done
- [x] DEFINITION_OF_DONE.md satisfied for a release-doc truth refresh.
- [x] Relevant docs/context updated.
- [x] Current selected-tag go/no-go evidence recorded.
- [x] Fallback readiness evidence recorded.
- [x] Diff hygiene passed.

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
- deployment trigger execution
- secret persistence

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.1 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj1132-v101.json; Pop-Location`
  - result: `verdict=GO`; audit `GO_FOR_SELECTED_SHA`; smoke `exit_code=0`;
    `selected_sha_is_local_head=true`
- Manual checks:
  - `check_coolify_fallback_readiness.py --before-sha 5e64f494e2aac8d29cea532d95f7039ed6029213 --after-sha 3b46ed3878a8560c3adb147fcadf064818ccc322`
  - result: `ready=false`; failed checks: `webhook_url`,
    `webhook_secret_present`, `webhook_secret_length`
  - `git for-each-ref refs/tags/v1.0.1`
  - result: tag object `b016c4f33051805cfa09664f79bbe57f5b30811b`, target
    `3b46ed3878a8560c3adb147fcadf064818ccc322`
- Screenshots/logs: not applicable
- High-risk checks:
  - no deployment trigger was executed
  - no secrets were written
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: not applicable

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/runtime-ops-runbook.md`
  - `backend/app/core/deployment_policy.py`
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
- Remaining mismatches: none
- State checks: not applicable
- Feedback locality checked: not applicable
- Raw technical errors hidden from end users: not applicable
- Responsive checks: not applicable
- Input-mode checks: not applicable
- Accessibility checks: not applicable
- Parity evidence: not applicable

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: yes, SLO doc now points to current `v1.0.1` go/no-go
  and readiness evidence
- Rollback note: no deploy changed; rollback remains redeploy previous
  known-good SHA through canonical Coolify app if needed
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

This task does not fix Coolify source automation inside Coolify. It removes the
repository truth drift and leaves the correct future-candidate action: inspect
Coolify source/webhook configuration or provide webhook fallback inputs before
the next candidate deploy.

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

Runtime tasks must be delivered as a vertical slice: UI -> logic -> API -> DB
-> validation -> error handling -> test. This task is release-doc/ops truth
only and does not change runtime behavior.

## Integration Evidence

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: source automation and fallback posture were
  easy to confuse with current release parity.
- Smallest useful slice: classify current evidence accurately without adding a
  deployment mechanism.
- Success metric or signal: v1 docs state current marker green and automation
  reliability follow-up separately.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release deploy provenance and future candidate deploy
  recovery
- SLI: selected tag production revision parity
- SLO: `v1.0.1` selected tag remains `GO`; future source automation reliability
  remains tracked
- Error budget posture: healthy for current release, follow-up for future
  candidate automation
- Health/readiness check: selected-tag go/no-go
- Logs, dashboard, or alert route: fallback readiness JSON output
- Smoke command or manual smoke:
  `run_release_go_no_go.py --selected-tag v1.0.1 --monitor-mode`
- Rollback or disable path: no deploy changed

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: selected-tag go/no-go

## AI Testing Evidence (required for AI features)

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata and non-secret readiness status
- Trust boundaries: Coolify credentials remain operator-side
- Permission or ownership checks: no deploy trigger executed
- Abuse cases: avoid storing webhook secrets or treating UI fallback as primary
  automation proof
- Secret handling: no secrets used or persisted
- Security tests or scans: not applicable
- Fail-closed behavior: webhook fallback stays blocked until inputs exist
- Residual risk: source/webhook automation needs operator-side configuration
  proof before future candidate deploys can rely on it

- `AI_TESTING_PROTOCOL.md` reviewed: not applicable
- Memory consistency scenarios: not applicable
- Multi-step context scenarios: not applicable
- Adversarial or role-break scenarios: not applicable
- Prompt injection checks: not applicable
- Data leakage and unauthorized access checks: not applicable
- Result: not applicable

## Result Report

- Task summary: refreshed Coolify automation reliability truth after `v1.0.1`.
- Files changed:
  - `.codex/tasks/PRJ-1132-coolify-automation-reliability-truth-refresh.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/operations/runtime-ops-runbook.md`
- How tested:
  - selected-tag go/no-go returned `GO`
  - fallback readiness returned expected blocked state without triggering deploy
  - diff hygiene passed
- What is incomplete:
  - Coolify source/webhook automation reliability still needs operator-side
    inspection or webhook input provisioning before the next selected candidate
    deploy.
- Next steps:
  - run a bounded Coolify automation proof task before the next release
    candidate, or keep UI fallback as documented exception-only recovery.
- Decisions made:
  - current release parity stays green; automation reliability remains a
    future-candidate follow-up, not a `v1.0.1` blocker.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - PRJ-930 SLO doc had stale local proof wording after PRJ-1128/1131.
- Gaps:
  - webhook fallback inputs are still missing locally.
- Inconsistencies:
  - release docs needed clearer separation between current marker success and
    future source/webhook reliability follow-up.
- Architecture constraints:
  - source automation remains primary, webhook/UI fallback remains manual
    exception path.

### 2. Select One Priority Task
- Selected task: refresh Coolify automation reliability truth.
- Priority rationale: it was the next smallest release/ops truth gap after
  `v1.0.1`.
- Why other candidates were deferred:
  - provider activation and AI review are extension/hardening gates, not the
    immediate deployment-truth drift.

### 3. Plan Implementation
- Files or surfaces to modify:
  - deployment SLO doc, release evidence index, runbook, task/context.
- Logic:
  - record current facts and leave future action explicit.
- Edge cases:
  - do not trigger deploy or store secrets.

### 4. Execute Implementation
- Implementation notes:
  - no code behavior changed.
  - source-of-truth docs now reflect current marker and fallback readiness.

### 5. Verify and Test
- Validation performed:
  - selected-tag go/no-go
  - fallback readiness
  - diff hygiene
- Result:
  - passed; fallback readiness correctly blocked without triggering deploy.

### 6. Self-Review
- Simpler option considered:
  - marking automation healthy because production is green; rejected because
    PRJ-1125 showed source automation did not converge for this candidate.
- Technical debt introduced: no
- Scalability assessment:
  - future candidate deploys now have clearer preflight and proof expectations.
- Refinements made:
  - current release parity and future automation reliability were separated.

### 7. Update Documentation and Knowledge
- Docs updated:
  - deployment SLO evidence, release evidence index, runtime ops runbook
- Context updated:
  - task board and project state
- Learning journal updated: not applicable.
