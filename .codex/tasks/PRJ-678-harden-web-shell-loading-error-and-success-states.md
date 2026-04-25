# Task

## Header
- ID: PRJ-678
- Title: Harden web-shell loading, error, empty, and success states across the current routes
- Status: READY
- Owner: Frontend Builder
- Depends on: PRJ-677
- Priority: P1

## Context
Once backend route health and route loading are repaired, the shell still needs
one consistent UX pass so errors do not bleed across screens, loading states do
not persist without end, and success states remain understandable for the
current product surface.

## Goal
Polish the existing web shell so auth, chat, settings, tools, and personality
have coherent user-visible state handling aligned with backend truth.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Each current route has a truthful loading, error, empty, and success
      state where applicable.
- [ ] Stale global errors do not incorrectly dominate later healthy screens.
- [ ] The repaired shell feels coherent without inventing new product
      subsystems or UI-only truth.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
- Manual checks:
- Screenshots/logs:
- High-risk checks:

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: docs/architecture/16_agent_contracts.md;
  docs/overview.md
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:

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
This is a polish pass only after the current broken product paths are restored.
