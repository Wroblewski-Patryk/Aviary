# Task

## Header
- ID: PRJ-617
- Title: Sync docs/context for production truth and deploy automation closure
- Status: BACKLOG
- Owner: Product Docs Agent
- Depends on: PRJ-616
- Priority: P1

## Context
After the deploy-parity and Coolify primary-path baseline is real, the same truth must be visible in docs and repository context.

## Goal
Synchronize planning, ops, testing, and context for the final deploy-truth baseline.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Planning docs reflect the deploy-truth and parity contract.
- [ ] Ops/testing guidance reflects the same primary/fallback deploy posture.
- [ ] Repository context reflects the current production-truth baseline.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: doc-and-context sync
- Manual checks: cross-review against live deploy evidence and smoke contract
- Screenshots/logs:
- High-risk checks: avoid leaving old deploy assumptions in planning/context

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/17_logging_and_debugging.md`, `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality/runbook/testing/planning/context

## Review Checklist (mandatory)
- [ ] Architecture alignment confirmed.
- [ ] Existing systems were reused where applicable.
- [ ] No workaround paths were introduced.
- [ ] No logic duplication was introduced.
- [ ] Definition of Done evidence is attached.
- [ ] Relevant validations were run.
- [ ] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
This slice should close the lane, not reopen deploy behavior as an open decision.
