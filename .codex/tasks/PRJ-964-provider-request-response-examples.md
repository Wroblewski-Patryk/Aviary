# Task

## Header
- ID: PRJ-964
- Title: Add provider request/response examples
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Product Docs Agent
- Depends on: PRJ-960
- Priority: P2
- Coverage Ledger Rows: not applicable
- Iteration: 964
- Operation Mode: BUILDER

## Process Self-Audit
- [x] All seven autonomous loop steps are planned.
- [x] No loop step is being skipped.
- [x] Exactly one priority task is selected.
- [x] Operation mode matches the iteration number.
- [x] The task is aligned with repository source-of-truth documents.

## Context

The provider integration reference mapped live provider-backed operations but
still lacked sanitized request/response examples for operator and agent review.
Live provider smoke remains blocked by credentials, so this task is
documentation hardening, not live provider activation.

## Goal

Document sanitized provider request, success, action-output, and failure shapes
for the provider-backed operations that exist in the current codebase.

## Scope

- `docs/integrations/provider-request-response-examples.md`
- `docs/integrations/index.md`
- `docs/planning/v1-reality-audit-and-roadmap.md`
- `.codex/context/TASK_BOARD.md`
- `.codex/context/PROJECT_STATE.md`

## Implementation Plan

1. Inspect provider clients and action execution owners.
2. Add examples for current provider-backed paths:
   - ClickUp create/list/update task
   - Google Calendar free/busy availability read
   - Google Drive metadata list
   - DuckDuckGo HTML search
   - generic HTTP page read
3. Keep secrets and private payloads redacted.
4. Link the examples from the integration index.
5. Update roadmap and context.

## Acceptance Criteria

- [x] Provider examples exist for current ready/failure paths.
- [x] Examples use placeholders instead of secrets.
- [x] Examples do not include raw provider payload bodies beyond sanitized
  shapes needed to explain the integration contract.
- [x] Integration index and roadmap no longer list this as missing.

## Definition of Done
- [x] `DEFINITION_OF_DONE.md` satisfied for this docs-hardening slice.
- [x] Docs are based on inspected code paths.
- [x] Validation evidence is recorded.
- [x] Task board and project state are synchronized.

## Validation Evidence
- Tests: not applicable; docs-only slice
- Manual checks:
  - provider client/action code inspection
  - markdown link/reference check
  - secret-value placeholder scan
- Screenshots/logs: not applicable
- High-risk checks:
  - no provider tokens or real private data recorded
- Coverage ledger updated: not applicable
- Coverage rows closed or changed: none

## Architecture Evidence
- Architecture source reviewed:
  - `docs/integrations/index.md`
  - `backend/app/core/action.py`
  - provider clients under `backend/app/integrations/`
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
- Rollback note: revert docs if provider implementation changes
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

## Security / Privacy Evidence
- `docs/security/secure-development-lifecycle.md` reviewed: yes
- Data classification: sanitized examples and placeholder IDs
- Trust boundaries: provider API requests, action output, app-facing metadata
- Permission or ownership checks: mutating operations remain documented as
  confirmation-required
- Abuse cases: secret leakage, raw provider payload leakage, mutation without
  confirmation
- Secret handling: placeholders only
- Security tests or scans: manual placeholder scan
- Fail-closed behavior: provider-not-ready shape is documented
- Residual risk: live credential smoke remains blocked externally

## Result Report

- Task summary: added sanitized provider examples and linked them from the
  integration reference.
- Files changed:
  - `docs/integrations/provider-request-response-examples.md`
  - `docs/integrations/index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- How tested: code inspection and markdown/reference checks.
- What is incomplete: live provider activation smoke remains `PRJ-963`.
- Next steps: `PRJ-965` OpenAPI-to-web type sync plan/generator.
- Decisions made: examples cover existing provider-backed paths only; policy-only
  mutations remain excluded from request examples.

## Autonomous Loop Evidence

### 1. Analyze Current State
- Issues: integration docs mapped providers but lacked concrete examples.
- Gaps: request/response examples for ready/failure paths.
- Inconsistencies: none confirmed.
- Architecture constraints: do not document secrets or unsupported live paths.

### 2. Select One Priority Task
- Selected task: `PRJ-964`
- Priority rationale: next unblocked roadmap item after P1 local hardening.
- Why other candidates were deferred: `PRJ-962/963` require operator inputs.

### 3. Plan Implementation
- Files or surfaces to modify: integration docs, roadmap, context.
- Logic: translate inspected provider clients and action outputs into sanitized
  examples.
- Edge cases: mutating operations must show confirmation requirement.

### 4. Execute Implementation
- Implementation notes: created one provider examples reference and linked it
  from the integration index.

### 5. Verify and Test
- Validation performed: code inspection, link/reference check, placeholder scan.
- Result: passed.

### 6. Self-Review
- Simpler option considered: add examples inline to `index.md`.
- Technical debt introduced: no
- Scalability assessment: separate examples file can grow without bloating the
  provider matrix.
- Refinements made: corrected action names to match `backend/app/core/action.py`.

### 7. Update Documentation and Knowledge
- Docs updated:
  - `docs/integrations/provider-request-response-examples.md`
  - `docs/integrations/index.md`
  - `docs/planning/v1-reality-audit-and-roadmap.md`
- Context updated:
  - `.codex/context/TASK_BOARD.md`
  - `.codex/context/PROJECT_STATE.md`
- Learning journal updated: not applicable
