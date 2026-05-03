# Task

## Header
- ID: PRJ-970
- Title: Add release go/no-go command wrapper
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-956, PRJ-968, PRJ-969
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 970
- Operation Mode: TESTER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

Release checks were available as separate commands: release reality audit,
release smoke, and fallback readiness. Operators needed a single wrapper that
prints a compact GO/HOLD decision while preserving the existing release gates.

## Goal

Add a release go/no-go wrapper that composes the existing release reality audit
and release smoke posture without creating a parallel release gate.

## Scope

- `backend/scripts/run_release_go_no_go.py`
- `backend/scripts/run_release_go_no_go.ps1`
- `backend/tests/test_deployment_trigger_scripts.py`
- `docs/operations/runtime-ops-runbook.md`
- `docs/operations/release-evidence-index.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: release GO/HOLD required stitching multiple command
  outputs by hand.
- Expected product or reliability outcome: one command produces a structured
  release decision from existing proof surfaces.
- How success will be observed: wrapper prints `release_go_no_go_report` with
  `verdict=GO|HOLD`.
- Post-launch learning needed: no

## Deliverable For This Stage

A tested release go/no-go wrapper plus runbook and evidence-index guidance.

## Constraints
- use existing systems and approved mechanisms
- do not create a new release policy owner
- do not silently treat local post-v1 commits as released
- do not force local-HEAD-bound smoke for a historical selected tag unless the
  operator explicitly requests local HEAD parity
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Add a Python wrapper that runs `audit_release_reality.py`.
2. Run release smoke when appropriate for the selected candidate.
3. Skip local-HEAD-bound smoke automatically when a selected historical SHA
   differs from local `HEAD`, and record the skip reason.
4. Add a PowerShell wrapper.
5. Add tests for GO, HOLD, and historical selected-SHA behavior.
6. Update runbook, release index, roadmap, task board, and project state.

## Acceptance Criteria
- Wrapper prints structured `GO` or `HOLD`.
- Audit failures produce `HOLD` and do not run smoke.
- Current-candidate release checks can enforce local HEAD parity.
- Historical selected-tag monitoring does not produce false HOLD only because
  local `HEAD` moved ahead.
- Focused tests pass.

## Definition of Done
- [x] Go/no-go script exists.
- [x] PowerShell wrapper exists.
- [x] Focused tests cover GO/HOLD/skipped-smoke semantics.
- [x] Runbook and release index document commands.
- [x] Task board and project state are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_deployment_trigger_scripts.py -k "release_go_no_go or backend_operator_scripts_expose_help"; Pop-Location`
  - result: `14 passed, 50 deselected`
- Manual checks:
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\run_release_go_no_go.py --base-url https://aviary.luckysparrow.ch --selected-tag v1.0.0 --monitor-mode --output ..\.codex\tmp\release-go-no-go-prj970-full.json; Pop-Location`
  - result: `verdict=GO`; smoke skipped with
    `selected_sha_differs_from_local_head_release_smoke_is_local_head_bound`
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - wrapper does not override existing audit or smoke verdicts
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
  - runbook now documents current-candidate and historical-tag wrapper forms

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: wrapper documents when release smoke is used or skipped
- Rollback note: call audit and release smoke directly
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Review Checklist
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

`run_release_smoke.ps1` is local-HEAD-bound today. The wrapper records this
explicitly when monitoring an already deployed selected tag while local `main`
has moved ahead.

## Production-Grade Required Contract

- Goal: compose existing release checks into one GO/HOLD command.
- Scope: wrapper, tests, docs/context.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: see below.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes, live production audit in manual check
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: yes

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: manual command stitching
- Smallest useful slice: one wrapper over existing audit and smoke
- Success metric or signal: structured `GO` or `HOLD`
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release decision
- SLI: wrapper decision correctness
- SLO: no release claim without audit GO and applicable smoke posture
- Error budget posture: not applicable
- Health/readiness check: production release audit
- Logs, dashboard, or alert route: JSON output
- Smoke command or manual smoke: wrapper invokes release smoke when applicable
- Rollback or disable path: direct audit and smoke commands

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: release metadata only
- Trust boundaries: local operator command and public production health/meta
- Permission or ownership checks: no privileged access used
- Abuse cases: false GO from skipped smoke
- Secret handling: no secrets used
- Security tests or scans: not applicable
- Fail-closed behavior: audit or applicable smoke failure yields `HOLD`
- Residual risk: full production smoke for a historical tag still requires
  checking out that tag or extending smoke to accept an explicit selected SHA

## Result Report

- Task summary: added release go/no-go wrapper.
- Files changed:
  - `backend/scripts/run_release_go_no_go.py`
  - `backend/scripts/run_release_go_no_go.ps1`
  - `backend/tests/test_deployment_trigger_scripts.py`
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - focused deployment-trigger tests
  - live selected-tag monitor wrapper
- What is incomplete:
  - release smoke remains local-HEAD-bound
- Next steps:
  - external blockers remain PRJ-962 Telegram live smoke and PRJ-963 organizer
    provider activation smoke
- Decisions made:
  - selected historical tag monitoring skips local-HEAD-bound smoke and records
    the reason instead of producing a false HOLD

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: release audit and smoke were separate commands.
- Gaps: no compact GO/HOLD wrapper.
- Inconsistencies: local post-v1 commits make historical tag smoke
  local-HEAD-bound.
- Architecture constraints: release proof must reuse existing gates.

### 2. Select One Priority Task
- Selected task: PRJ-970 release go/no-go wrapper.
- Priority rationale: it completes the local release-operability queue.
- Why other candidates were deferred: PRJ-962/963 require external inputs.

### 3. Plan Implementation
- Files or surfaces to modify: scripts, tests, ops docs, context.
- Logic: audit first, smoke only when applicable, structured verdict output.
- Edge cases: historical selected tag differs from local `HEAD`.

### 4. Execute Implementation
- Implementation notes: wrapper uses existing scripts and records smoke skip
  reasons in the output.

### 5. Verify and Test
- Validation performed: focused pytest and live selected-tag monitor command.
- Result: tests passed; live command returned `GO` for deployed `v1.0.0`.

### 6. Self-Review
- Simpler option considered: PowerShell-only wrapper.
- Technical debt introduced: no
- Scalability assessment: wrapper can be extended if release smoke later
  accepts explicit selected SHA.
- Refinements made: fixed false HOLD for historical selected tag monitoring.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
