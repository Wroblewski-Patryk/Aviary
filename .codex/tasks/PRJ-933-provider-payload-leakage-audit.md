# Task

## Header
- ID: PRJ-933
- Title: Provider Payload Leakage Audit
- Task Type: release
- Current Stage: release
- Status: DONE
- Owner: Security
- Depends on: PRJ-931, PRJ-932
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 933
- Operation Mode: ARCHITECT

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context
The public-launch hardening queue required a provider payload leakage audit
after the AI red-team scenario pack and cross-user/session isolation audit.
The relevant surfaces are app overview routes, health policy surfaces,
incident evidence, chat transcript projection, durable memory storage, and
tool/provider overview metadata.

## Goal
Confirm and tighten the boundary so raw web page, task, calendar, drive,
Telegram, memory, or proposal payloads are not exposed through public app
overview, health, incident evidence, or UI-consumed overview routes.

## Scope
- `backend/app/api/routes.py`
- `backend/tests/test_api_routes.py`
- `docs/security/v1-provider-payload-leakage-audit.md`
- `docs/planning/v1-release-audit-and-execution-plan.md`
- `docs/planning/v1-core-acceptance-bundle.md`
- `docs/engineering/testing.md`
- `docs/architecture/16_agent_contracts.md`
- `docs/README.md`
- `docs/index.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan
1. Inspect provider, memory, app overview, tools overview, health, incident
   evidence, and transcript projection paths.
2. Fix the only confirmed leak candidate: raw subconscious proposal `payload`
   in learned-state planning snapshots.
3. Add a regression that provider-like proposal payload bodies stay out of
   `/app/personality/overview`.
4. Record the audit result, remaining gaps, validation, and next task.

## Acceptance Criteria
- `planning_state.pending_proposals` no longer returns raw proposal `payload`
  through overview/inspection snapshots.
- Existing runtime and repository proposal payload contracts remain intact for
  conscious runtime handoff.
- Audit documentation records verified surfaces and residual gaps.
- Focused route tests pass.

## Definition of Done
- [x] Code builds without syntax errors.
- [x] Affected API behavior is covered by focused regression evidence.
- [x] No workaround path or duplicated runtime contract was introduced.
- [x] Relevant source-of-truth docs and context files were updated.
- [x] Residual risks and next steps are recorded.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_api_routes.py -k "personality_overview or tools_overview or internal_state or incident or raw_payload"; Pop-Location`
  - result: `8 passed, 111 deselected`
- Manual checks:
  - code inspection of `backend/app/api/routes.py`
  - code inspection of `backend/app/core/app_tools_policy.py`
  - code inspection of `backend/app/core/observability_policy.py`
  - code inspection of `backend/app/memory/repository.py`
  - docs and frontend search for `pending_proposals` usage
- Screenshots/logs: not applicable
- High-risk checks: no raw proposal payload in public planning snapshot
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/architecture/16_agent_contracts.md`
  - `docs/security/secure-development-lifecycle.md`
  - `DEFINITION_OF_DONE.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates:
  - learned-state planning snapshots now explicitly use proposal metadata and
    payload-key disclosure only, not raw proposal payload bodies.

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: provider payloads, memory payloads, Telegram payloads,
  and proposal payloads can contain user data or third-party content.
- Trust boundaries: public authenticated app routes, debug-gated internal
  routes, health policy surfaces, incident evidence bundles, durable memory.
- Permission or ownership checks: app overview and tools overview require
  authenticated app sessions; internal state inspection requires debug access.
- Abuse cases: user or attacker attempts to read raw provider response bodies,
  raw memory payloads, or proposal payload internals through overview routes.
- Secret handling: no secret values added.
- Security tests or scans: focused route regression.
- Fail-closed behavior: debug/inspection access remains blocked when debug
  payloads are disabled or tokens are missing.
- Residual risk: the AI red-team scenario pack still needs executed pass/fail
  evidence for prompt-level exfiltration attempts.

## Result Report
- Task summary:
  - audited provider and memory payload exposure paths
  - found and fixed raw proposal payload exposure in learned-state planning
    snapshots
  - recorded verified surfaces and remaining evidence gaps
- Files changed:
  - listed in Scope
- How tested:
  - focused `pytest` route selection: `8 passed, 111 deselected`
  - markdown/reference checks
  - `git diff --check` passed with existing CRLF normalization warnings only
- What is incomplete:
  - live provider credential smoke remains blocked by operator credentials
  - PRJ-931 scenario pack has not yet been executed as pass/fail red-team
    evidence
- Next steps:
  - add broader explicit no-raw-provider-payload route regressions once live
    provider fixtures are available
  - continue with PRJ-930 deployment trigger SLO evidence or PRJ-934 go/no-go
    review when remaining hardening evidence is acceptable
- Decisions made:
  - keep durable repository/runtime proposal payloads intact
  - sanitize only the overview/inspection projection boundary

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues:
  - release plan still listed provider payload leakage audit as open
  - `recent_activity` was bounded, but `pending_proposals` reused repository
    serialization including raw `payload`
- Gaps:
  - executed AI red-team evidence remains open
  - live provider payload smoke remains blocked by credentials
- Inconsistencies:
  - public planning snapshot was broader than the bounded learned-state
    inspection language implied
- Architecture constraints:
  - preserve action boundary and runtime proposal payload contracts

### 2. Select One Priority Task
- Selected task: PRJ-933 Provider Payload Leakage Audit
- Priority rationale: first non-blocked P1 security hardening item after
  PRJ-932
- Why other candidates were deferred: provider activation smoke remains
  credential-blocked; final go/no-go depends on this audit

### 3. Plan Implementation
- Files or surfaces to modify:
  - API snapshot projection, tests, security docs, release docs, context docs
- Logic:
  - convert pending proposals to a safe metadata snapshot before returning the
    learned-state overview
- Edge cases:
  - non-dict proposals are ignored
  - empty payloads expose `payload_present=false`
  - payload key names are disclosed, not payload values

### 4. Execute Implementation
- Added `_pending_proposal_snapshot(...)`.
- Updated learned-state snapshot to use sanitized proposals.
- Added provider-like raw payload regression in personality overview test.

### 5. Verify And Test
- Focused route tests were run: `8 passed, 111 deselected`.
- Diff whitespace check passed with CRLF normalization warnings only.

### 6. Self-Review
- Existing repository/runtime proposal payload contracts remain unchanged.
- Public app overview now exposes metadata only for proposal payload state.
- No new system, workaround, or duplicate runtime path was introduced.

### 7. Update Documentation And Knowledge
- Added audit source document.
- Updated architecture, testing, release plan, acceptance bundle, docs index,
  task board, and project state.
