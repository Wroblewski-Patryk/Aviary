# Task

## Header
- ID: PRJ-1121
- Title: Add Coolify deploy parity operator preflight for PRJ-952
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1120
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1121
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-952 remains the active v1 release-reality blocker. Existing scripts can
check fallback readiness and trigger the approved Coolify webhook fallback, but
operators need an explicit preflight that prevents triggering deploy for a SHA
that does not include the intended local work.

## Goal

Document the exact PRJ-952 preflight sequence: select/commit the candidate,
verify fallback inputs, trigger only with operator secrets, then rerun release
smoke with deploy parity.

## Scope

- `.codex/tasks/PRJ-1121-coolify-deploy-parity-operator-preflight.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- `docs/planning/v1-deployment-trigger-slo-evidence.md`
- `docs/operations/release-evidence-index.md`

## Success Signal
- User or operator problem: deploy fallback can target the wrong SHA if the
  current working tree is dirty.
- Expected product or reliability outcome: PRJ-952 has a clear operator
  preflight that preserves release truth.
- How success will be observed: docs say not to trigger fallback until the
  selected SHA is explicit and pushed.
- Post-launch learning needed: no

## Deliverable For This Stage

A docs-only PRJ-952 operator preflight update plus context updates.

## Constraints
- reuse existing Coolify fallback scripts
- do not introduce a new deploy mechanism
- do not trigger deploy without operator secrets
- do not claim local `HEAD` is deployable while the intended scope is uncommitted

## Implementation Plan
1. Add a PRJ-952 preflight section to deployment-trigger SLO evidence.
2. Update release evidence index with the current candidate-packaging caution.
3. Update task board and project state.
4. Run `git diff --check`.

## Acceptance Criteria
- Docs explicitly require a selected pushed SHA before fallback trigger.
- Docs preserve source automation as primary and webhook/UI as exception-only.
- Docs list the existing readiness, trigger, and smoke commands.
- Context records that PRJ-952 remains external.

## Definition of Done
- [x] PRJ-952 preflight documented.
- [x] Release evidence index updated.
- [x] Context updated.
- [x] `git diff --check` passes.
- [x] No release process or architecture change was introduced.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated release processes
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- deploying without operator approval and secrets

## Validation Evidence
- Tests:
  - not applicable; docs-only operator preflight update
- Manual checks:
  - reviewed existing fallback readiness and trigger script parameters
  - reviewed deployment SLO and release evidence index after edit
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - no deploy was triggered
  - no webhook secret was requested, inferred, or written
  - source automation remains primary and fallback remains exception-only
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
  - `backend/scripts/check_coolify_fallback_readiness.py`
  - `backend/scripts/trigger_coolify_deploy_webhook.py`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: deployment SLO evidence and release index
  now include the PRJ-952 selected-SHA preflight

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: docs only
- Rollback note: revert docs/context update
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
- [x] Learning journal was updated if a recurring pitfall is confirmed.

## Notes

Docs-only preflight update. No deploy was triggered.

## Production-Grade Required Contract

- Goal: document PRJ-952 operator preflight.
- Scope: deployment SLO evidence, release index, context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: fallback trigger command exists but can be run
  before candidate SHA is frozen.
- Smallest useful slice: preflight wording in existing SLO evidence.
- Success metric or signal: operator cannot miss selected-SHA precondition.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: deploy parity recovery
- SLI: selected SHA is the same SHA deployed and smoked
- SLO: no release claim without backend/web revision parity
- Error budget posture: not applicable
- Health/readiness check: release smoke after deploy
- Logs, dashboard, or alert route: Coolify history and JSON fallback evidence
- Smoke command or manual smoke: documented existing release smoke
- Rollback or disable path: keep PRJ-952 blocked until operator evidence exists

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata and secret-presence checks only
- Trust boundaries: local operator, Coolify webhook, public production health
- Permission or ownership checks: operator secrets required
- Abuse cases: deploying wrong SHA; leaking webhook secret
- Secret handling: docs require secret placeholders; readiness check redacts
  secret contents
- Security tests or scans: not applicable
- Fail-closed behavior: missing webhook URL/secret keeps fallback blocked
- Residual risk: external deploy proof remains operator-owned

## Result Report

- Task summary: added a PRJ-952 operator preflight for Coolify deploy parity.
- Files changed:
  - `.codex/tasks/PRJ-1121-coolify-deploy-parity-operator-preflight.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - `git diff --check`
- What is incomplete:
  - actual PRJ-952 deploy parity remains external because it requires a selected
    pushed candidate and Coolify source automation or operator webhook inputs.
- Next steps:
  - select and push the intended candidate SHA, then recover source automation
    or run the approved fallback and PRJ-953 release smoke.
- Decisions made:
  - explicitly block deploy fallback for inferred `HEAD` when intended release
    work is still uncommitted.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: PRJ-952 is blocked and local worktree is dirty.
- Gaps: operator preflight does not explicitly forbid deploying an unfrozen
  candidate.
- Inconsistencies: fallback readiness can infer `HEAD`, but intended work may
  still be uncommitted.
- Architecture constraints: source automation remains primary; fallback is
  exception-only.

### 2. Select One Priority Task
- Selected task: PRJ-1121 Coolify deploy parity operator preflight.
- Priority rationale: this is the closest local work to unblocking PRJ-952
  without operator secrets.
- Why other candidates were deferred: actual deploy requires external Coolify
  source automation or webhook inputs.

### 3. Plan Implementation
- Files or surfaces to modify: deployment SLO evidence, release index, context.
- Logic: selected SHA first, readiness check second, trigger third, smoke last.
- Edge cases: dirty working tree means `HEAD` may not include intended work.

### 4. Execute Implementation
- Implementation notes: added selected-SHA preflight, readiness command,
  fallback trigger command, and deploy-parity smoke command to the existing SLO
  evidence doc.

### 5. Verify and Test
- Validation performed: `git diff --check`.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only rely on `trigger_command_hint`.
- Technical debt introduced: no
- Scalability assessment: future deploy recovery can reuse the same preflight
  for any selected SHA.
- Refinements made: documented the dirty-worktree risk directly in release
  evidence.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
  - `docs/operations/release-evidence-index.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
