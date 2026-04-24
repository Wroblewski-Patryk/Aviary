# Task

## Header
- ID: PRJ-644
- Title: Implement channel-aware Telegram segmentation and formatting
- Status: BACKLOG
- Owner: Backend Builder
- Depends on: PRJ-643
- Priority: P1

## Context
Telegram has a hard message-length ceiling and a specific parse/render model,
but current delivery sends one raw message without channel-aware adaptation.

## Goal
Implement channel-aware Telegram delivery that can segment long messages and
apply safe markdown rendering without hardcoding the same limits into other
channels.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Telegram delivery segments long outbound content according to a channel-owned limit.
- [ ] Telegram rendering uses an explicit formatting policy instead of raw literal markdown passing through by accident.
- [ ] API and future UI channels remain free to use different limits and formatting capabilities.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: targeted delivery-router and Telegram client coverage
- Manual checks: verify multi-part Telegram delivery and formatting behavior
- Screenshots/logs:
- High-risk checks: avoid moving channel constraints into planning or expression-stage heuristics

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/16_agent_contracts.md`, `docs/architecture/17_logging_and_debugging.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality, testing, runbook

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
This should land as delivery-layer adaptation, not as prompt-shaping pressure on
expression output.
