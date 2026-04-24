# Task

## Header
- ID: PRJ-645
- Title: Add proof for long-message and markdown delivery
- Status: BACKLOG
- Owner: QA/Test
- Depends on: PRJ-644
- Priority: P1

## Context
Channel-aware delivery should be proven through tests and release evidence, not
left as a best-effort transport detail.

## Goal
Add behavior and regression proof for long Telegram messages and markdown-safe
rendering.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Regression tests prove Telegram segmentation for content beyond the channel limit.
- [ ] Regression tests prove formatting behavior for markdown-style content.
- [ ] Release or incident evidence records the same delivery adaptation posture.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted pytest plus release-smoke or evidence checks if needed
- Manual checks: local or production verification of formatted Telegram output
- Screenshots/logs:
- High-risk checks: avoid declaring the fix complete on unit tests alone if runtime evidence drifts

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/17_logging_and_debugging.md`, `docs/engineering/testing.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: testing and ops notes

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
If Telegram markdown mode requires escaping rules, that policy should be proven
explicitly.
