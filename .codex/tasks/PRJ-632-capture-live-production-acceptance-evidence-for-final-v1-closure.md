# Task

## Header
- ID: PRJ-632
- Title: Capture live production acceptance evidence for final V1 closure
- Status: BLOCKED
- Owner: Ops/Release
- Depends on: PRJ-631
- Priority: P0

## Context
Final no-UI `v1` closure should not rely only on repo-local evidence. The live system needs its own acceptance evidence bundle.

## Goal
Capture live production evidence for final no-UI `v1` closure.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Live release-smoke evidence is attached for the final acceptance contract.
- [ ] Incident-evidence or bundle artifacts prove the same live posture.
- [ ] Any operator-assisted deployment or credential steps are recorded explicitly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: live release-smoke and artifact checks
- Manual checks: production `/health` and incident-evidence verification
- Screenshots/logs: deployment id, release-smoke result, and artifact location if relevant
- High-risk checks: do not mark `v1` closed on repo-only evidence if live production differs

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/17_logging_and_debugging.md`, `docs/operations/runtime-ops-runbook.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: ops/runbook/planning/context likely

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
This task is intentionally live-production-focused.

This task was superseded on 2026-04-24 by the approved architecture revision
that redefines core no-UI `v1` around:

- stable conversation
- bounded web reading
- tool-grounded learning
- time-aware planned future work

Organizer-tool activation remains a prepared post-`v1` extension and no longer
blocks core `v1` closure.
