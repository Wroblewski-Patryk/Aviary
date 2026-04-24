# Task

## Header
- ID: PRJ-615
- Title: Add machine-visible repo-vs-production truth and deploy-parity evidence
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-614
- Priority: P0

## Context
Deploy provenance exists, but the user still needs clearer evidence that live production actually matches the intended repository baseline for the current no-UI `v1` slice.

## Goal
Expose machine-visible parity evidence for repository-intended versus live deployed baseline.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Existing health or observability surfaces expose deploy-parity truth.
- [ ] Release evidence consumes the same parity contract.
- [ ] Regression coverage pins the new evidence path.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest coverage for health/observability/deploy scripts
- Manual checks: live release-smoke verification after deploy
- Screenshots/logs:
- High-risk checks: do not invent a second deployment-truth system separate from existing deployment/observability owners

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/17_logging_and_debugging.md`, `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: likely runtime reality/runbook/testing if the contract widens

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
The target is operator-readable parity evidence, not a new deployment controller.
