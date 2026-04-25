# Task

## Header
- ID: PRJ-706
- Title: Normalize product-facing loading, empty, error, and success states
- Status: BACKLOG
- Owner: Frontend Builder
- Depends on: PRJ-705
- Priority: P1

## Context
The current routes already have loading and error affordances, but their tone
still feels system-first. Product quality now depends on making these states
clear, brief, and supportive instead of merely truthful transport feedback.

## Goal
Create one coherent product-state system across the shell while keeping current
backend-owned behavior and error truth.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] loading, empty, success, and error states share a consistent product posture across routes.
- [ ] state messaging is shorter and more user-facing without hiding truthful failure detail.
- [ ] route states remain thin wrappers over current backend-owned contracts.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: route-state review for login, chat, settings, tools, and personality
- Screenshots/logs: refreshed state screenshots and local route evidence
- High-risk checks: confirm better copy does not mask real operational failures

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/17_logging_and_debugging.md`
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
Truthful failure detail stays available, but the first line of feedback should
help the user recover.
