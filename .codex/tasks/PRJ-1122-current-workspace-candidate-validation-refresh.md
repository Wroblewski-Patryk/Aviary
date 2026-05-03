# Task

## Header
- ID: PRJ-1122
- Title: Refresh current workspace candidate validation before PRJ-952 handoff
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-1121
- Priority: P0
- Coverage Ledger Rows: not applicable
- Iteration: 1122
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

PRJ-1121 clarified that PRJ-952 deploy parity cannot move forward until a
selected candidate SHA is frozen and pushed. Before that handoff, the current
workspace needs fresh local validation evidence.

## Goal

Run the relevant local validation gates for the current workspace so the next
operator action can distinguish "ready to package" from "fix local regressions
first."

## Scope

- `.codex/tasks/PRJ-1122-current-workspace-candidate-validation-refresh.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`
- docs/context validation notes only

## Success Signal
- User or operator problem: PRJ-952 cannot proceed safely without knowing
  whether current local work still validates.
- Expected product or reliability outcome: current workspace has fresh backend
  and web validation evidence.
- How success will be observed: validation commands pass or failures are
  recorded as blockers.
- Post-launch learning needed: no

## Deliverable For This Stage

Fresh local validation evidence for the current workspace.

## Constraints
- do not commit or deploy
- do not trigger Coolify fallback
- run validations sequentially where build/smoke ordering matters
- record failures rather than hiding them

## Implementation Plan
1. Run the backend pytest baseline.
2. Run web build.
3. Run focused frontend characterization scripts.
4. Run full route smoke.
5. Run `git diff --check`.
6. Update context/task with results.

## Acceptance Criteria
- Backend baseline result is recorded.
- Web build and route smoke results are recorded.
- Focused frontend characterization results are recorded.
- Candidate state is explicit for PRJ-952 handoff.

## Definition of Done
- [x] Backend validation run.
- [x] Web validation run.
- [x] Diff hygiene run.
- [x] Context updated.
- [x] No deploy or fallback trigger executed.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated release processes
- temporary bypasses or workaround-only paths
- architecture changes without explicit approval
- deployment trigger execution

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`
  - result: `1045 passed`
  - `Push-Location .\web; npm run build; Pop-Location`
  - result: passed
  - `Push-Location .\web; npm run test:tools-directory; Pop-Location`
  - result: `status=ok`
  - `Push-Location .\web; npm run test:chat-transcript; Pop-Location`
  - result: `status=ok`
  - `Push-Location .\web; npm run smoke:routes; Pop-Location`
  - result: `status=ok`, `route_count=14`
  - `git diff --check`
  - result: passed
- Manual checks:
  - not applicable
- Screenshots/logs:
  - route smoke JSON output showed all 14 routes passed
- High-risk checks:
  - no deploy, push, release marker, or Coolify fallback trigger was executed
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-deployment-trigger-slo-evidence.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: release evidence index now records local
  validation without claiming deploy parity

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: not applicable; validation-only
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

Validation-only task. No commit, push, deploy, or fallback trigger.

## Production-Grade Required Contract

- Goal: refresh local validation for the current workspace.
- Scope: validation evidence and context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: complete.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: not applicable
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: covered by backend tests where applicable
- Loading state verified: frontend characterization and route smoke
- Error state verified: frontend characterization and route smoke
- Refresh/restart behavior verified: route smoke
- Regression check performed: backend pytest, web build, focused frontend
  characterizations, route smoke, and `git diff --check`

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator
- Existing workaround or pain: deploy handoff would otherwise lack fresh local
  validation after many local changes.
- Smallest useful slice: run existing validation gates.
- Success metric or signal: all selected commands pass or blockers are explicit.
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: candidate packaging
- SLI: validation pass/fail truthfulness
- SLO: no PRJ-952 handoff without local validation status
- Error budget posture: not applicable
- Health/readiness check: backend tests and web route smoke
- Logs, dashboard, or alert route: command outputs
- Smoke command or manual smoke: web route smoke
- Rollback or disable path: fix failures before candidate packaging

## AI Testing Evidence

Not applicable; no AI behavior changed in this task.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: validation logs only
- Trust boundaries: local tests
- Permission or ownership checks: not applicable
- Abuse cases: false deploy confidence from stale validation
- Secret handling: no secrets used
- Security tests or scans: backend suite includes relevant regressions where
  present
- Fail-closed behavior: failing validation blocks handoff
- Residual risk: production deploy proof remains operator-owned

## Result Report

- Task summary: refreshed local validation for the current workspace before
  PRJ-952 handoff.
- Files changed:
  - `.codex/tasks/PRJ-1122-current-workspace-candidate-validation-refresh.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
  - `docs/operations/release-evidence-index.md`
- How tested:
  - backend pytest baseline
  - web build
  - tools directory characterization
  - chat transcript characterization
  - full route smoke
  - diff hygiene
- What is incomplete:
  - deploy parity remains external; current local work must still be committed,
    pushed, deployed, and smoke-tested before any future release claim.
- Next steps:
  - freeze candidate scope for commit/push, then resolve PRJ-952.
- Decisions made:
  - record local validation as candidate-readiness evidence only, not production
    release evidence.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: current workspace is dirty and local validation needs refresh.
- Gaps: PRJ-952 handoff has deploy preflight but no current validation bundle.
- Inconsistencies: production is green for `v1.0.0`, not current local work.
- Architecture constraints: local validation cannot replace deploy parity.

### 2. Select One Priority Task
- Selected task: PRJ-1122 current workspace candidate validation refresh.
- Priority rationale: it is the next local prerequisite before candidate
  packaging.
- Why other candidates were deferred: actual deploy requires external inputs.

### 3. Plan Implementation
- Files or surfaces to modify: task/context after validation only.
- Logic: run existing backend/web gates.
- Edge cases: route smoke depends on web build completing first.

### 4. Execute Implementation
- Implementation notes: ran existing backend and web gates sequentially,
  keeping route smoke after build.

### 5. Verify and Test
- Validation performed: backend pytest, web build, focused web
  characterizations, route smoke, and diff hygiene.
- Result: passed.

### 6. Self-Review
- Simpler option considered: rely on earlier PRJ-111x validation.
- Technical debt introduced: no
- Scalability assessment: validation command set can be reused before candidate
  packaging.
- Refinements made: release index now distinguishes local validation from
  deploy parity.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/release-evidence-index.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
