# Task

## Header
- ID: PRJ-1115
- Title: Refresh local release-readiness evidence after frontend closure
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1114
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1115
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The frontend presentation extraction lane is closed by PRJ-1114. The next v1
priority remains release reality, but the primary deploy-parity task PRJ-952 is
externally blocked by Coolify source automation or operator fallback evidence.
This task refreshes local and production-observable release evidence using the
existing release scripts without creating a new release gate.

## Goal

Produce a current release-readiness snapshot after frontend closure that
distinguishes deployed `v1.0.0` evidence from local `HEAD` release eligibility.

## Scope

- `.codex/tasks/PRJ-1115-local-release-readiness-evidence-refresh.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/operations/release-evidence-index.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`

## Success Signal
- User or operator problem: after many local frontend changes, release truth can
  drift from production truth.
- Expected product or reliability outcome: operators can see whether current
  local work is release-eligible or still gated by deploy parity.
- How success will be observed: existing release scripts produce current
  structured evidence and docs/context record the result.
- Post-launch learning needed: no

## Deliverable For This Stage

A verified release evidence refresh using existing scripts and updated
source-of-truth notes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new release gates or scripts
- do not claim local `HEAD` is deployed unless production revisions match
- do not trigger deploys or use fallback webhooks without operator secrets
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Run the existing release go/no-go wrapper for the deployed `v1.0.0` marker in
   monitor mode.
2. Run the existing release reality audit for local `HEAD`.
3. Run the existing Coolify fallback readiness check without triggering deploy.
4. Run focused deployment script regressions.
5. Update release index, roadmap, task board, and project state with exact
   evidence and blockers.
6. Run `git diff --check`.

## Acceptance Criteria
- `v1.0.0` monitor evidence is refreshed with the current production revision.
- Local `HEAD` release audit has a clear `GO` or `HOLD` verdict.
- Coolify fallback readiness is explicit and does not expose secrets.
- Focused release-script tests pass.
- Docs/context record that PRJ-952 remains external if deploy parity is not
  achieved.

## Definition of Done
- [x] Existing release checks were run.
- [x] Existing release-script tests passed.
- [x] Release evidence index was refreshed.
- [x] V1 roadmap and context were synchronized.
- [x] No workaround path or duplicate release gate was introduced.

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
- deployment trigger execution without operator approval and secrets

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py; Pop-Location`
  - result: `64 passed`
- Manual checks:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.0 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj1115-v1.json; Pop-Location`
  - result: `verdict=GO`; selected SHA
    `5e64f494e2aac8d29cea532d95f7039ed6029213`; smoke skipped because the
    selected SHA differs from local `HEAD` and release smoke is local-HEAD-bound
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\audit_release_reality.py --base-url https://aviary.luckysparrow.ch --output ..\.codex\tmp\release-reality-audit-prj1115-local-head.json; Pop-Location`
  - result: `verdict=HOLD_REVISION_DRIFT`; local selected SHA
    `5ff12953289bbca680fd5d9f8b3d8780a8f4be55`; production backend and web
    revisions `5e64f494e2aac8d29cea532d95f7039ed6029213`
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\check_coolify_fallback_readiness.py --output ..\.codex\tmp\coolify-fallback-readiness-prj1115.json --print-json; Pop-Location`
  - result: `ready=false`; missing webhook URL and webhook secret
- Screenshots/logs:
  - JSON outputs:
    - `.codex/tmp/release-go-no-go-prj1115-v1.json`
    - `.codex/tmp/release-reality-audit-prj1115-local-head.json`
    - `.codex/tmp/coolify-fallback-readiness-prj1115.json`
- High-risk checks:
  - no deploy trigger was executed
  - fallback readiness redacted secret contents and reported only missing
    secret state
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - release evidence index and v1 roadmap now record the refreshed release
    verdicts

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: release index refreshed with existing commands and
  latest outputs
- Rollback note: docs/context-only release evidence refresh can be reverted
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
- [x] Process self-audit completed before implementation.
- [x] Autonomous loop evidence covers all seven steps.
- [x] Exactly one priority task was selected in this iteration.
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

This task intentionally does not resolve PRJ-952 because production deploy
automation and fallback credentials are operator-owned.

## Production-Grade Required Contract

- Goal: refresh release-readiness evidence after frontend closure.
- Scope: release evidence docs/context and existing release script execution.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: use `DEFINITION_OF_DONE.md` evidence through existing
  release checks and context synchronization.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes, production `/health` and `/settings`
  through existing release scripts
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: yes

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: local hardening work can be mistaken for
  production release evidence.
- Smallest useful slice: run existing release evidence checks and update the
  release truth docs.
- Success metric or signal: structured script outputs and synchronized docs.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release decision
- SLI: release evidence truthfulness
- SLO: no release claim without matching production backend and web revision
- Error budget posture: not applicable
- Health/readiness check: production `/health` and release readiness through
  `audit_release_reality.py`
- Logs, dashboard, or alert route: JSON evidence outputs
- Smoke command or manual smoke:
  - `run_release_go_no_go.py --selected-tag v1.0.0 --monitor-mode`
  - `audit_release_reality.py` for local `HEAD`
  - `check_coolify_fallback_readiness.py --print-json`
- Rollback or disable path: keep PRJ-952 blocked until deploy parity evidence exists

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata only
- Trust boundaries: local operator command, public production health/meta, and
  local secret environment presence checks
- Permission or ownership checks: no privileged action will be taken
- Abuse cases: false release GO for undeployed local commits
- Secret handling: fallback check redacts secret and reports only presence
- Security tests or scans: not applicable
- Fail-closed behavior: release audit HOLD blocks local release claim
- Residual risk: external deploy automation state still requires operator proof

## Result Report

- Task summary: refreshed release readiness after frontend closure using
  existing release scripts.
- Files changed:
  - `.codex/tasks/PRJ-1115-local-release-readiness-evidence-refresh.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- How tested:
  - deployed `v1.0.0` go/no-go monitor wrapper
  - local `HEAD` release reality audit
  - Coolify fallback readiness check
  - deployment trigger script regression suite
- What is incomplete:
  - PRJ-952 remains externally blocked; no current local `HEAD` deploy parity
    exists.
- Next steps:
  - recover Coolify source automation or provide fallback webhook URL and
    secret, then rerun production release smoke for the selected SHA.
- Decisions made:
  - do not claim local `HEAD` as release-ready while production revisions differ.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: frontend confidence improved locally, but deploy parity is still the
  v1 release blocker.
- Gaps: latest release evidence index predates the current local frontend
  closure.
- Inconsistencies: local `HEAD` can be ahead of production while deployed
  `v1.0.0` remains green.
- Architecture constraints: reuse existing release scripts and ops docs.

### 2. Select One Priority Task
- Selected task: PRJ-1115 local release-readiness evidence refresh.
- Priority rationale: it advances v1 truthfulness without requiring blocked
  external deploy inputs.
- Why other candidates were deferred: PRJ-952 requires operator/Coolify action;
  PRJ-962 and PRJ-963 require live credentials.

### 3. Plan Implementation
- Files or surfaces to modify: release docs/context and this task.
- Logic: run existing evidence scripts, classify deployed marker vs local HEAD,
  update source-of-truth files.
- Edge cases: fallback readiness may be blocked by missing secrets; that should
  stay explicit rather than become a workaround.

### 4. Execute Implementation
- Implementation notes: reused `run_release_go_no_go.py`,
  `audit_release_reality.py`, and `check_coolify_fallback_readiness.py`;
  updated release truth docs and context with exact verdicts.

### 5. Verify and Test
- Validation performed: existing release scripts, focused deployment-script
  pytest suite, and diff hygiene.
- Result: deployed marker is green; local `HEAD` is HOLD; fallback readiness is
  blocked by missing operator inputs.

### 6. Self-Review
- Simpler option considered: only update task board without running scripts.
- Technical debt introduced: no
- Scalability assessment: evidence refresh continues to use the existing
  release scripts and can be repeated by operators.
- Refinements made: recorded both deployed-marker and local-HEAD verdicts to
  avoid blending production proof with local work.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
