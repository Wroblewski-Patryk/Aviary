# Task

## Header
- ID: PRJ-705
- Title: Freeze responsive tier rules for mobile, tablet, and desktop
- Status: BACKLOG
- Owner: Frontend Builder
- Depends on: PRJ-704
- Priority: P1

## Context
The current shell is clearly mobile-first, but tablet still behaves mostly as a
scaled phone layout. The next iteration needs explicit tier rules so later
visual changes do not regress into one-size-fits-all responsive behavior.

## Goal
Make responsive behavior deliberate:

- define tablet-specific layout posture
- align spacing and typography per tier
- prevent desktop or mobile assumptions from dominating the intermediate tier

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] One explicit responsive posture is defined and implemented for mobile, tablet, and desktop.
- [ ] tablet is no longer only a scaled mobile view.
- [ ] the chosen tier rules are screenshot-proven across the main routes.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: viewport review across main routes on mobile, tablet, and desktop
- Screenshots/logs: refreshed multi-viewport artifact set
- High-risk checks: confirm tier rules do not introduce route-specific layout forks that duplicate shell logic

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: n/a
- Follow-up architecture doc updates: none expected

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
Treat `tablet` as its own product tier, not just an interpolation between two extremes.
