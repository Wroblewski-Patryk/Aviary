# Task

## Header
- ID: PRJ-703
- Title: Reframe login around product value, trust, and fast session entry
- Status: READY
- Owner: Frontend Builder
- Depends on: PRJ-691
- Priority: P0

## Context
The current `/login` screen is cleaner than the original shell, but it still
uses too much first-viewport space on architecture-oriented hero content and
secondary descriptive cards. This weakens trust and delays the real primary
action on mobile.

## Goal
Make the public entry route feel like a product, not a system overview:

- bring session entry and value closer together
- remove architecture-facing promotional copy
- remove or demote user-visible build chrome
- keep login/register trustworthy and lightweight on mobile

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] `/login` leads with product value and session entry instead of system framing.
- [ ] `build` revision no longer appears as user-facing primary chrome on the public route.
- [ ] mobile, tablet, and desktop login screenshots show clearer first-viewport action hierarchy.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: browser review of `/login` on mobile, tablet, and desktop
- Screenshots/logs: refresh `.codex/artifacts/ux-audit-2026-04-25-round2/` or later follow-up set
- High-risk checks: confirm public-route simplification does not imply client-owned auth logic

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/16_agent_contracts.md`
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
Public product surfaces should not lead with backend or contract terminology.
