# Task

## Header
- ID: PRJ-961
- Title: Add strict-mode incident sentinel regression
- Task Type: feature
- Current Stage: verification
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-933, PRJ-960
- Priority: P1
- Coverage Ledger Rows: not applicable
- Iteration: 961
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The strict-mode incident bundle helper falls back to `/health`-derived evidence
when debug payload export is disabled. `PRJ-961` pins that this fallback does
not write debug payload text or synthetic provider payload sentinels into the
bundle files.

## Goal

Add a regression that proves strict-mode incident evidence keeps policy-safe
health-derived evidence and excludes debug payload bodies.

## Scope

- `backend/tests/test_incident_evidence_bundle_script.py`
- `docs/security/v1-provider-payload-leakage-audit.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan

1. Reuse the existing incident bundle script test server with debug payload
   disabled.
2. Pass synthetic provider payload sentinels through the debug request text.
3. Assert the strict-mode fallback bundle records
   `capture_source=health_snapshot_strict_mode` and
   `debug_payload_included=false`.
4. Assert `manifest.json`, `incident_evidence.json`, and `health_snapshot.json`
   do not contain the debug text sentinels or debug user id.
5. Update docs and context.

## Acceptance Criteria

- [x] Strict-mode fallback still exports a canonical bundle.
- [x] The bundle marks debug payload inclusion as false.
- [x] Synthetic provider payload sentinel strings are absent from committed
  bundle outputs.
- [x] Focused incident bundle tests pass.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for this regression slice.
- [x] Focused tests pass.
- [x] Planning/security docs and context are synchronized.

## Validation Evidence
- Tests:
  - `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_incident_evidence_bundle_script.py; Pop-Location`
  - result: `3 passed`
- Manual checks: not applicable
- Screenshots/logs: not applicable
- High-risk checks: strict-mode incident evidence privacy
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/operations/runtime-ops-runbook.md`
  - `docs/security/v1-provider-payload-leakage-audit.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: not applicable
- Follow-up architecture doc updates: none

## Deployment / Ops Evidence
- Deploy impact: none
- Env or secret changes: none
- Health-check impact: none
- Smoke steps updated: no
- Rollback note: remove the added test/docs if superseded by a deeper bundle
  verifier
- Observability or alerting impact: none
- Staged rollout or feature flag: not applicable

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: synthetic provider/debug sentinel strings
- Trust boundaries: debug request payload versus strict-mode health-derived
  incident evidence
- Permission or ownership checks: not applicable for local script fixture
- Abuse cases: debug payload or raw provider text written into incident bundle
- Secret handling: no real secrets used
- Security tests or scans: focused incident bundle regression
- Fail-closed behavior: sentinel presence fails the test
- Residual risk: live provider credential smoke remains externally blocked

## Result Report

- Task summary: added strict-mode incident bundle sentinel regression.
- Files changed:
  - `backend/tests/test_incident_evidence_bundle_script.py`
  - `docs/security/v1-provider-payload-leakage-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested: focused incident bundle test file.
- What is incomplete: live provider activation smoke remains blocked by
  credentials.
- Next steps: `PRJ-964` provider request/response examples, or unblock
  external `PRJ-962/PRJ-963` when operator credentials are available.
- Decisions made: this is kept as script-level regression because the strict
  fallback behavior is owned by the incident bundle helper.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: strict-mode fallback was documented and tested structurally, but not
  against debug/provider payload sentinels.
- Gaps: no explicit sentinel absence check for exported bundle files.
- Inconsistencies: none confirmed.
- Architecture constraints: strict-mode fallback must use health policy
  surfaces only.

### 2. Select One Priority Task
- Selected task: `PRJ-961`
- Priority rationale: next READY P1 after provider payload sentinel coverage.
- Why other candidates were deferred: live Telegram/provider smokes require
  operator inputs.

### 3. Plan Implementation
- Files or surfaces to modify: incident bundle tests and docs/context.
- Logic: export strict-mode bundle with debug disabled, then inspect generated
  JSON file text.
- Edge cases: sentinels must be absent from all bundle outputs, including
  manifest and health snapshot.

### 4. Execute Implementation
- Implementation notes: added one focused test to the existing script test
  module.

### 5. Verify and Test
- Validation performed: focused incident bundle tests.
- Result: passed.

### 6. Self-Review
- Simpler option considered: only documenting the existing fallback behavior.
- Technical debt introduced: no
- Scalability assessment: additional sentinels can be added to the same test.
- Refinements made: checked all three generated JSON files.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/security/v1-provider-payload-leakage-audit.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
