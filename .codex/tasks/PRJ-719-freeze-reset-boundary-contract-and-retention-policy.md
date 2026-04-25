# Task

## Header
- ID: PRJ-719
- Title: Freeze the reset boundary contract and retention policy
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-718
- Priority: P1

## Context
Fresh planning for the destructive-data lane already established the safe split
between:

- operator-only production cleanup
- authenticated self-service per-user runtime reset

What remained open before implementation was the exact retention and session
contract. The repo already has the right ownership boundaries:

- backend-owned auth/session
- profile-owned linked-channel and shell settings continuity
- per-user runtime continuity keyed by `user_id`

This task freezes the contract before `PRJ-720` adds any shared cleanup owner
or delete logic, so later implementation does not blur runtime reset with
account deletion, session handling, or production-wide cleanup.

## Goal
Freeze one explicit destructive-data contract for the repo that defines:

- what self-service reset clears
- what self-service reset preserves
- what happens to auth sessions after reset
- how self-service reset differs from operator-only production cleanup

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] the self-service reset retention boundary is explicit in repo truth
- [x] session posture after reset is resolved instead of remaining implicit
- [x] source-of-truth docs and context align on the same destructive boundary

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - none; contract and context freeze only
- Manual checks:
  - cross-review of architecture, planning, reset lane plan, and current
    auth/profile/runtime ownership boundaries
- Screenshots/logs:
  - none
- High-risk checks:
  - self-service reset must stay distinct from account deletion
  - production-wide cleanup must stay outside product UI
  - preserved settings and linked integrations must not be pulled into the
    destructive scope
  - session posture must be explicit before backend implementation begins

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/26_env_and_config.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - none
- Follow-up architecture doc updates:
  - the reset-boundary contract is now recorded in
    `docs/architecture/16_agent_contracts.md`

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
Frozen session posture for the first implementation:

- self-service reset revokes all auth sessions, including the current session
- the auth account, profile settings, linked integrations, and linked channels
  remain intact
- the user signs in again into a clean runtime-continuity state after reset

This keeps the destructive boundary explicit and avoids ambiguous mixed-state
posture across multiple active sessions while still preserving configuration.
