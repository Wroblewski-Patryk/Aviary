# Task

## Header
- ID: PRJ-707
- Title: Freeze locale metadata foundation for GUI language UX
- Status: BACKLOG
- Owner: Planning Agent
- Depends on: PRJ-706
- Priority: P1

## Context
`ui_language` is now a valid product contract, but the current selector still
acts as a light proof-of-concept. Future web-to-mobile reuse needs one stable
metadata model for locale label, native label, icon asset posture, and fallback
semantics.

## Goal
Plan a durable locale UX foundation for first-party clients without changing
the runtime-owned conversation-language boundary.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] One locale metadata model is documented for web and later mobile reuse.
- [ ] GUI language remains explicitly separate from runtime-owned conversation language.
- [ ] flag or locale-icon rendering posture is described without relying on implicit system emoji behavior.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: n/a planning slice
- Manual checks: reviewed current `ui_language` contract in frontend and app-facing settings API
- Screenshots/logs: selector evidence from `.codex/artifacts/ux-audit-2026-04-25-round2/`
- High-risk checks: confirm no plan overloads locale selection with conversation-language control

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed: n/a
- Follow-up architecture doc updates: expected in canonical planning and architecture docs if the metadata contract becomes approved

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
This slice is about durable UX metadata planning, not about introducing a new
translation subsystem.
