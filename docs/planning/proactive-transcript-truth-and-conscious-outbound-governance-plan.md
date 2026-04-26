# Proactive Transcript Truth And Conscious Outbound Governance Plan

## Purpose

This plan repairs a production-visible drift where scheduler-owned proactive
ticks leak into the user transcript as if they were user-authored messages,
while also tightening the rule for when subconscious or scheduler wakeups are
allowed to produce outward communication.

The goal is not to remove proactive capability.
The goal is to make proactive behavior truthful, conscious, and aligned with
the runtime architecture.

## Planning Basis

Observed from current production evidence, runtime code, and canonical docs:

- proactive cadence is enabled in the Coolify production baseline and defaults
  to `1800` seconds
- proactive candidate generation can synthesize a scheduler event with the
  literal text `time check-in follow up`
- scheduler-originated proactive ticks are allowed to become user-visible
  delivery through the normal `planning -> expression -> action` path
- episodic memory persistence currently records the scheduler event text as the
  turn `event`
- transcript projection currently maps that stored `event` payload to
  `role=user`
- this creates false transcript history and makes system ticks look like user
  chat input

Approved user-direction for the repair:

1. if the user writes to AION, AION must always answer on that source, even if
   the answer is minimal
2. if subconscious or scheduler activity wakes consciousness but there is no
   valuable reason to speak, no user-visible message is required
3. if conscious evaluation concludes that relation maintenance or useful
   follow-up is warranted, proactive delivery is allowed
4. linked-channel escalation after no answer is desirable in principle, but it
   has enough architecture and trust implications that it remains a decision
   gate before implementation

## Fresh Gap Snapshot

The current drift is a combined truth and policy problem:

### 1. Transcript Truth Drift

- scheduler-originated events are stored as if their synthetic `text` were
  equivalent to user-authored input
- transcript projection treats every stored `payload.event` as a `role=user`
  message
- product UI therefore renders internal runtime prompts as visible user turns

### 2. Conscious Outbound Policy Drift

- proactive ticks are allowed to generate outward communication, but the repo
  does not yet freeze the higher-level communication rule that:
  - user-originated turns always deserve an outward reply
  - subconscious or scheduler wakeups do not inherently deserve outward
    delivery
- because that rule is not explicit enough, runtime truth and transcript truth
  can drift together without a clear policy boundary

### 3. Missing Channel-Escalation Decision

- user direction now points toward "retry or escalate via linked channels when
  app silence suggests a message may not have reached the person"
- the current architecture does not yet freeze whether proactive escalation is:
  - never allowed
  - allowed only after bounded delivery-failure evidence
  - allowed after silence windows as a relation-maintenance policy

This must be resolved explicitly before implementation because it affects:

- action ownership
- delivery policy
- user trust and anti-spam posture
- profile or preference ownership for channel priorities

## Repair Strategy

The repair should proceed in four steps:

1. fix transcript truth first
2. freeze the communication-governance rule second
3. repair proactive execution and regression proof third
4. handle cross-channel escalation only after an explicit decision

This order prevents a false quick fix where transcript rendering changes but
the runtime still stores misleading event semantics or still lacks one clear
outbound policy boundary.

## Execution Queue

### PRJ-745 - Freeze transcript truth and communication governance contract

Result:

- one explicit contract defines which runtime-originated events may appear in
  the user transcript and how
- scheduler or subconscious wakeups are distinguished from user-authored input
- the conscious communication rule becomes explicit:
  - user-originated turns always produce an outward reply
  - scheduler or subconscious wakeups may complete with no outward reply
  - proactive outward delivery requires a conscious positive decision, not just
    the existence of a tick
- architecture or runtime-reality docs are updated with the clarified rule

Validation:

- architecture, planning, and transcript-contract cross-review

### PRJ-746 - Repair transcript projection and runtime persistence semantics

Result:

- scheduler-originated synthetic prompts stop appearing as `role=user`
  transcript entries
- runtime persistence either:
  - stores a machine-distinguishable internal event marker
  - or excludes non-user-visible scheduler prompts from transcript projection
- `/app/chat/history` remains a truthful shared transcript across app and
  linked Telegram without leaking internal runtime prompts

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_memory_repository.py tests/test_api_routes.py tests/test_runtime_pipeline.py; Pop-Location`

### PRJ-747 - Tighten proactive wakeup execution and anti-spam behavior

Result:

- proactive ticks may still wake the conscious path for analysis, relation
  checks, or planning
- outward proactive delivery occurs only when the conscious decision path marks
  real user-value in contacting the user
- the fallback "no meaningful outreach" path becomes a clean no-delivery
  outcome rather than a transcript-visible pseudo-user turn
- existing planned-work follow-up behavior remains separate from generic
  proactive time-checkin behavior

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_planning_agent.py tests/test_scheduler_worker.py tests/test_runtime_pipeline.py tests/test_action_executor.py; Pop-Location`

### PRJ-748 - Add regression proof, runbook notes, and context sync

Result:

- regressions pin:
  - user turns still always receive an outward reply
  - scheduler ticks without conscious outreach value stay invisible to the user
  - proactive outreach can still deliver when consciously justified
  - transcript history no longer impersonates the user with scheduler text
- ops guidance records how to triage proactive cadence versus transcript truth
- task board, project state, and learning journal remain synchronized

Validation:

- `Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q; Pop-Location`

## Explicit Decision Gate Before Any Cross-Channel Escalation

The user asked for a later fallback where silence in the first-party app may
lead to outreach through linked communicators. That is reasonable, but the repo
should not implement it without an explicit policy choice because the wrong
choice can feel invasive.

Valid options:

1. conservative
   - no cross-channel escalation
   - proactive delivery stays on the selected originating or preferred channel
2. delivery-failure escalation
   - only escalate when the original channel has bounded delivery-failure
     evidence
   - silence alone is not enough
3. silence-window escalation
   - escalate after a bounded no-reply window plus anti-spam and relation
     checks
   - requires one explicit channel-priority owner and user-preference posture

Recommended current implementation posture:

- execute `PRJ-745..PRJ-748`
- defer cross-channel escalation until the user explicitly chooses between the
  three options above

## Why This Plan Fits The Architecture

- it keeps subconscious or scheduler activity as a wakeup source, not an
  automatic communication owner
- it preserves `planning -> expression -> action` for any user-visible
  delivery that does happen
- it restores transcript truth without creating a second chat store
- it reuses the current shared continuity owner across app and linked Telegram
- it keeps high-risk channel escalation behind an explicit policy decision

## Definition Of Done

This repair lane is complete when:

- internal scheduler prompts no longer appear in product transcript history as
  user-authored turns
- user-authored turns still always receive an outward reply
- scheduler or subconscious wakeups can complete with no outward delivery when
  there is no conscious reason to contact the user
- proactive outreach still works when consciously justified
- docs, tests, and context all describe the same communication boundary
