# Task

## Header
- ID: PRJ-646
- Title: Sync docs for channel-aware delivery
- Status: BACKLOG
- Owner: Product Docs Agent
- Depends on: PRJ-645
- Priority: P2

## Context
After the delivery fix lands, product, runtime, testing, and ops docs should
describe one shared channel-aware delivery contract.

## Goal
Synchronize docs/context for channel-aware delivery limits and formatting.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [ ] Canonical docs describe delivery adaptation as channel-owned behavior under action/delivery.
- [ ] Telegram-specific length and formatting rules are documented without implying the same limit for UI or API.
- [ ] Planning/context truth records this fix as part of the post-core-v1 queue.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests: doc-and-context sync
- Manual checks: cross-review against implementation and proof
- Screenshots/logs:
- High-risk checks: avoid docs that suggest expression should self-truncate to Telegram

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed: `docs/architecture/02_architecture.md`, `docs/architecture/16_agent_contracts.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates: runtime reality, testing, runbook, planning/context

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
The long-term target is channel-aware delivery, not Telegram-first formatting
logic leaking upward.
