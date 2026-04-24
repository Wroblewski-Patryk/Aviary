# Task

## Header
- ID: PRJ-624
- Title: Add release and behavior evidence for capability-record truthfulness
- Status: DONE
- Owner: QA/Test
- Depends on: PRJ-623
- Priority: P1

## Context
Once capability records are visible, evidence must prove that the backend truthfully distinguishes described guidance from executable/authorized behavior.

## Goal
Pin the capability-record truthfulness contract through regression and release evidence.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] Regression coverage proves catalog truthfulness semantics.
- [x] Release or incident evidence consumes the same contract.
- [x] Behavior-level proof exists for at least one described-versus-authorized distinction.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `.\.venv\Scripts\python -m pytest -q tests/test_runtime_pipeline.py tests/test_deployment_trigger_scripts.py` -> `131 passed`
- Manual checks: release-smoke contract cross-review in `scripts/run_release_smoke.ps1` against capability-catalog truthfulness semantics
- Screenshots/logs:
- High-risk checks: avoid evidence that only checks shape while ignoring truthfulness semantics

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/29_runtime_behavior_testing.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing guidance and ops notes likely

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
The catalog must not imply that a durable skill description equals live tool authority.
