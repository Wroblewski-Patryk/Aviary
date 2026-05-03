# Task

## Header
- ID: PRJ-968
- Title: Add release evidence index
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-956
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 968
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The v1 lane now has release smoke, a release reality audit, archive rules, and
task evidence, but operators still needed one index that states what is
currently deployed, what local work is ahead, which blockers remain, and what
the next release action is.

## Goal

Create a committed release evidence index that summarizes current production
revision parity, v1 readiness, blockers, proof sources, and refresh commands.

## Scope

- `docs/operations/release-evidence-index.md`
- `docs/planning/v1-release-evidence-archive-standard.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Success Signal
- User or operator problem: release truth was spread across several task and
  planning documents.
- Expected product or reliability outcome: one operator-facing index shows the
  current production SHA, release tag target, blockers, and next action.
- How success will be observed: operators can refresh the index using the
  commands recorded in the document.
- Post-launch learning needed: no

## Deliverable For This Stage

A committed release evidence index grounded in live production health and web
meta revision checks.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new release gates
- do not mark undeployed local commits as released
- do not commit generated evidence artifacts
- stay within the declared current stage unless explicit approval changes it

## Implementation Plan
1. Inspect local `HEAD`, branch relation, and `v1.0.0` tag target.
2. Verify production `/health` and `/settings` web meta revision.
3. Create `docs/operations/release-evidence-index.md`.
4. Link the index from the release archive standard and v1 roadmap.
5. Update task board and project state.
6. Validate docs with `git diff --check`.

## Acceptance Criteria
- The index records production backend revision and web meta revision.
- The index distinguishes deployed `v1.0.0` from newer local commits.
- The index records blocker and next-action state.
- Existing release evidence docs point at the index.
- Generated local artifacts remain untracked and unstaged.

## Definition of Done
- [x] Release evidence index exists.
- [x] Production revision evidence is recorded.
- [x] Blockers and next actions are explicit.
- [x] Docs/context are synchronized.
- [x] Validation evidence is recorded.

## Validation Evidence
- Tests:
  - `git diff --check`
  - result: passed with CRLF normalization warnings only
- Manual checks:
  - `git rev-parse HEAD`
  - `git for-each-ref refs/tags/v1.0.0 --format='%(objectname) %(objecttype) %(*objectname)'`
  - `Invoke-RestMethod -Uri 'https://aviary.luckysparrow.ch/health' -TimeoutSec 30`
  - `curl.exe -s -L --max-time 30 https://aviary.luckysparrow.ch/settings`
- Screenshots/logs:
  - not applicable
- High-risk checks:
  - index explicitly says newer local commits do not inherit the deployed
    `v1.0.0` acceptance claim
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-release-evidence-archive-standard.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - release archive standard now points at the index

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: remove the index if release evidence is consolidated elsewhere
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

The index intentionally keeps generated evidence directories out of git and
uses committed docs as pointers.

## Production-Grade Required Contract

- Goal: create one release-truth index.
- Scope: docs/context only.
- Implementation Plan: see above.
- Acceptance Criteria: see above.
- Definition of Done: see above.
- Result Report: see below.

## Integration Evidence

- `INTEGRATION_CHECKLIST.md` reviewed: not applicable
- Real API/service path used: yes, read-only production `/health` and web
  `/settings`
- Endpoint and client contract match: not applicable
- DB schema and migrations verified: not applicable
- Loading state verified: not applicable
- Error state verified: not applicable
- Refresh/restart behavior verified: not applicable
- Regression check performed: doc validation only

## Product / Discovery Evidence
- Problem validated: yes
- User or operator affected: release operator and future agents
- Existing workaround or pain: release truth required reading multiple files
- Smallest useful slice: one index with proof links and refresh commands
- Success metric or signal: operator can determine current release posture
  without reconstructing it from task history
- Feature flag, staged rollout, or disable path: not applicable
- Post-launch feedback or metric check: no

## Reliability / Observability Evidence
- `docs/operations/service-reliability-and-observability.md` reviewed: not applicable
- Critical user journey: release decision and rollback orientation
- SLI: release evidence freshness
- SLO: refresh before every candidate or release marker decision
- Error budget posture: not applicable
- Health/readiness check: production `/health`
- Logs, dashboard, or alert route: not applicable
- Smoke command or manual smoke: read-only production revision checks
- Rollback or disable path: not applicable

## AI Testing Evidence

Not applicable; no AI behavior changed.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: not applicable
- Data classification: public health and release metadata only
- Trust boundaries: production read-only public health/meta surfaces
- Permission or ownership checks: no privileged access used
- Abuse cases: not applicable
- Secret handling: no secrets used
- Security tests or scans: not applicable
- Fail-closed behavior: index records blockers instead of waiving them
- Residual risk: index freshness depends on manual refresh until automated
  release evidence publication exists

## Result Report

- Task summary: added a release evidence index for current production and v1
  marker truth.
- Files changed:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-release-evidence-archive-standard.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested:
  - read-only production checks
  - `git diff --check`
- What is incomplete:
  - no automated publishing of external release artifacts
- Next steps:
  - `PRJ-969` Coolify fallback secret/runbook readiness check
  - `PRJ-970` release go/no-go wrapper
- Decisions made:
  - local post-v1 commits are explicitly not treated as released until fresh
    deploy parity evidence exists

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: release truth existed but was distributed across docs and task
  records.
- Gaps: no one-page operator index.
- Inconsistencies: local `main` is ahead of deployed `v1.0.0` production.
- Architecture constraints: release markers require deployed revision parity.

### 2. Select One Priority Task
- Selected task: PRJ-968 release evidence index.
- Priority rationale: it improves release-operability without requiring
  external credentials.
- Why other candidates were deferred: PRJ-969/970 build on this index, while
  PRJ-962/963 are externally blocked.

### 3. Plan Implementation
- Files or surfaces to modify: release docs and context.
- Logic: capture local and production SHA evidence, blockers, proof sources,
  and refresh commands.
- Edge cases: avoid claiming unreleased local commits as production-ready.

### 4. Execute Implementation
- Implementation notes: created the index under `docs/operations/` because it
  is an operator-facing release surface.

### 5. Verify and Test
- Validation performed: production health/meta checks and `git diff --check`.
- Result: production remains coherent with `v1.0.0`; local branch is ahead.

### 6. Self-Review
- Simpler option considered: only update the roadmap.
- Technical debt introduced: no
- Scalability assessment: the index can be refreshed for each new candidate.
- Refinements made: documented that the index commit itself advances local
  `HEAD`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/operations/release-evidence-index.md`
  - `docs/planning/v1-release-evidence-archive-standard.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable.
