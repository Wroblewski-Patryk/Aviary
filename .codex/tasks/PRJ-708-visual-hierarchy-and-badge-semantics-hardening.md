# Task

## Header
- ID: PRJ-708
- Title: Harden visual hierarchy and badge semantics across the shell
- Status: BACKLOG
- Owner: Frontend Builder
- Depends on: PRJ-707
- Priority: P1

## Context
The current visual system is coherent, but too many badges and bordered cards
share similar emphasis. This flattens hierarchy and makes state chips feel more
decorative than semantic.

## Goal
Refine the design system so that emphasis, status, and action are easier to
scan across routes.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] badge usage is reduced or made more semantic across public and authenticated routes.
- [ ] visual hierarchy between title, body, state, and action is clearer across key cards.
- [ ] updated system still fits the existing Tailwind and daisyUI-based stack.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: visual review of shell hierarchy and card scanning behavior
- Screenshots/logs: refreshed browser artifact set across primary routes
- High-risk checks: confirm visual cleanup does not remove necessary status meaning

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
This is a semantic pass, not a theme replacement.
