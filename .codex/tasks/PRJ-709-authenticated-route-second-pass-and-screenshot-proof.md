# Task

## Header
- ID: PRJ-709
- Title: Run one authenticated second-pass route sweep with screenshot proof
- Status: BACKLOG
- Owner: Frontend Builder
- Depends on: PRJ-708
- Priority: P1

## Context
After the second public-entry and shell-quality pass, the product needs one
fresh authenticated route review so the updated shell can act as a better
baseline for later mobile transfer.

## Goal
Perform one deliberate second-pass sweep across authenticated routes:

- `chat`
- `settings`
- `tools`
- `personality`

and capture screenshot evidence across mobile, tablet, and desktop.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] authenticated routes are reviewed after the second UX/UI lane changes land.
- [ ] screenshot evidence exists for mobile, tablet, and desktop across the main routes.
- [ ] final issues are reduced to small polish items rather than product-structure gaps.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: `npm run build` in `web/`
- Manual checks: browser review across authenticated routes and breakpoints
- Screenshots/logs: new screenshot set under `.codex/artifacts/`
- High-risk checks: confirm final route sweep still reflects backend-owned truth rather than mocked client data

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
This task is the acceptance-style visual proof slice for the second lane.
