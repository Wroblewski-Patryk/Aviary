# Task

## Header
- ID: PRJ-575
- Title: Post-v1 architecture gap analysis and queue seeding
- Status: DONE
- Owner: Planning Agent
- Depends on: PRJ-574
- Priority: P0

## Context
The no-UI `v1` lane and post-v1 production-hardening queue are complete through
`PRJ-574`. The next execution queue must come from fresh comparison of live
production runtime truth against the canonical architecture, not from legacy
backlog carry-over.

## Goal
Produce one explicit architecture-gap analysis and seed the next detailed
execution queue for the remaining high-value gaps still visible in the current
backend-first product.

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic

## Definition of Done
- [x] canonical architecture docs, runtime reality, and current project truth
      were reviewed together
- [x] live production `/health` was used as evidence instead of planning only
- [x] a new detailed queue with explicit groups, order, and first `READY` task
      was seeded in planning and context files

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval

## Validation Evidence
- Tests:
  - none; planning-only slice
- Manual checks:
  - reviewed `.codex/context/PROJECT_STATE.md`
  - reviewed `.codex/context/TASK_BOARD.md`
  - reviewed `docs/architecture/10_future_vision.md`
  - reviewed `docs/architecture/15_runtime_flow.md`
  - reviewed `docs/architecture/16_agent_contracts.md`
  - reviewed `docs/implementation/runtime-reality.md`
  - reviewed `docs/planning/next-iteration-plan.md`
  - reviewed `docs/planning/open-decisions.md`
  - captured live production snapshot from `https://personality.luckysparrow.ch/health`
- Screenshots/logs:
  - production `/health` snapshot reviewed for `attention`, `proactive`,
    `memory_retrieval`, `connectors`, `learned_state`, `v1_readiness`,
    `api_readiness`, and `conversation_channels.telegram`
- High-risk checks:
  - confirmed Telegram round-trip is healthy before seeding new capability work
  - confirmed reflection and cadence externalization are complete before moving
    attention, proactive, and tooling forward

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/02_architecture.md`
  - `docs/architecture/10_future_vision.md`
  - `docs/architecture/15_runtime_flow.md`
  - `docs/architecture/16_agent_contracts.md`
  - `docs/architecture/17_logging_and_debugging.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
  - not applicable
- Follow-up architecture doc updates:
  - queue seeded for durable attention production cutover, proactive
    activation, retrieval provider alignment, introspection enrichment, and
    organizer-tool production readiness

## Review Checklist (mandatory)
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Fresh production truth after `PRJ-574` shows that the next highest-value gaps
are no longer basic runtime reliability. The main remaining gaps are:

1. attention ownership still runs in `in_process` despite repository-backed
   durable inbox readiness
2. proactive cadence is externalized but production follow-up remains disabled
   by policy
3. retrieval lifecycle target provider baseline remains unaligned
4. learned-state surfaces exist, but they do not yet provide a sufficiently
   rich backend-owned personality-growth bundle for later product UX
5. organizer-tool families exist contractually, but production readiness for
   ClickUp + Google Calendar + Google Drive is still fragmented and mostly
   blocked by missing credential posture
