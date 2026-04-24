# Task

## Header
- ID: PRJ-619
- Title: Implement operator-visible website-reading readiness and guardrails
- Status: DONE
- Owner: Backend Builder
- Depends on: PRJ-618
- Priority: P0

## Context
The workflow needs runtime truth: what provider path is selected, what bounded page-read semantics are allowed, and what blocks live website reading in production.

## Goal
Expose one truthful readiness and guardrail surface for website reading.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] Existing health/debug surfaces expose website-reading readiness and blocker posture.
- [x] The same surfaces encode bounded read semantics and allowed provider path.
- [x] Regression coverage pins the new guardrail contract.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `.\.venv\Scripts\python -m pytest -q tests/test_api_routes.py tests/test_runtime_pipeline.py` -> `187 passed`
- Manual checks: `/health.connectors` plus internal inspection/debug checks
- Screenshots/logs:
- High-risk checks: do not add a second browser/search subsystem outside connector/action ownership

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/17_logging_and_debugging.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality/testing/ops if visibility widens

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [x] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The operator should be able to tell whether "read my site" is available, bounded, and safe.

Completion notes:

- `/health.connectors.web_knowledge_tools` now exposes
  `website_reading_workflow`
- `system_debug.adaptive_state["web_knowledge_tools"]` exposes the same
  readiness or blocker contract for turn-level traces
- the workflow now reports:
  - direct URL review availability
  - search-first review availability
  - allowed entry modes
  - bounded read semantics
  - selected provider path
  - blockers and next actions
- next slice `PRJ-620` should prove the same contract through behavior and
  release evidence
