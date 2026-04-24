# Task

## Header
- ID: PRJ-616
- Title: Harden the Coolify primary deploy path and explicit fallback workflow
- Status: BACKLOG
- Owner: Ops/Release
- Depends on: PRJ-615
- Priority: P0

## Context
The user still observes cases where pushes do not trigger deployment automatically. The operational primary path must become explicit and provable.

## Goal
Make repo-driven deploy the explicit operational default with bounded, visible fallback posture.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Primary Coolify deploy path is explicit and machine-visible.
- [ ] Webhook/UI fallback remains bounded and observable.
- [ ] Live deploy plus release-smoke evidence is attached.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted deploy/observability regression coverage
- Manual checks: live deploy verification in Coolify plus release smoke
- Screenshots/logs: deployment id and target commit evidence
- High-risk checks: keep fallback documented as fallback, not as silent primary behavior

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/26_env_and_config.md`, `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: ops/runbook and planning truth

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
The key rule is that fallback usage must stay explicit in evidence and operator guidance.
