# Canonical Multi-Channel Conversation And Relational Outreach Plan

## Purpose

This plan freezes how AION should behave when the same user can interact
through the internal authenticated app chat and linked transports such as
Telegram.

The goal is not to build a parallel messaging platform.
The goal is to keep one canonical conversation owner, propagate meaning
correctly across linked channels, and let relational memory shape constructive
outreach without spam or architecture drift.

## User-Approved Behavioral Baseline

The user has now approved the following product posture:

1. the internal authenticated app chat is the canonical conversation surface
2. linked channels such as Telegram are transport mirrors over the same user
   continuity after explicit registration and linking
3. if the user writes on Telegram, AION should:
   - ingest the message into canonical shared conversation continuity
   - answer canonically in the internal chat
   - propagate that same answer back to Telegram
4. if the user writes in the app, AION must always answer on that turn even if
   the minimal answer is `...`
5. scheduler or subconscious wakeups may stay silent when they have nothing
   valuable to say
6. proactive outreach may happen after delivery failure or relationally
   interpreted silence, but the timing should adapt per user rather than use
   one hard global timeout
7. sleep posture, channel preference, response cadence, and interruption
   tolerance should be inferred and adapted by the personality
8. any user-authored message on any linked channel counts as contact
9. the user should not see transport-attempt bookkeeping in the chat history
10. Telegram and future linked channels may adapt transport formatting or
    segmentation, but they must preserve the same meaning as the canonical app
    reply

## Current Repo Analysis

### Strengths Already Present

The repo already has several pieces we should reuse:

- one backend-owned shared transcript contract for `/app/chat/history`
- linked Telegram identity through explicit link-code onboarding
- one shared runtime `user_id` continuity owner across app and linked Telegram
- one action-owned delivery router with Telegram segmentation support
- one proactive runtime with relation-aware interruption and delivery posture
- relation and preference surfaces already influencing runtime behavior
- runtime truth and observability around Telegram round-trip posture

Concrete implementation anchors:

- canonical transcript projection:
  - `backend/app/memory/repository.py`
- first-party app conversation routes:
  - `backend/app/api/routes.py`
- Telegram link and ingress handling:
  - `backend/app/api/routes.py`
- delivery and segmentation:
  - `backend/app/integrations/delivery_router.py`
- proactive and relation-aware interruption logic:
  - `backend/app/proactive/engine.py`
  - `backend/app/agents/planning.py`
  - `backend/app/reflection/relation_signals.py`

### Gaps Still Open

The repo does not yet fully implement the newly approved behavior:

1. canonical cross-channel mirroring is only partial
   - app and linked Telegram share user continuity, but the repo does not yet
     freeze a full canonical "reply once, mirror outward" contract end to end
2. channel-fit inference is too narrow
   - current relation signals emphasize delivery reliability and collaboration,
     but not explicit channel preference, sleep posture, or response cadence
3. proactive escalation policy is still under-specified in code
   - proactive logic is relation-aware, but it does not yet own channel-choice
     inference for "app only" versus "app plus Telegram"
4. transcript truth is fixed for scheduler impersonation, but not yet fully
   modeled for one canonical reply versus multi-segment transport mirrors
5. tooling and settings surfaces do not yet expose a complete explicit posture
   for user-stated channel preferences versus inferred channel behavior

### Architectural Constraints

The implementation must preserve:

- one canonical app-facing transcript
- one cognitive pipeline regardless of channel
- one expression output per turn
- action-owned propagation and segmentation
- no transport-specific second planner
- no new separate messaging store

## Delivery Strategy

The safest order is:

1. freeze architecture and product truth for canonical multi-channel behavior
2. add bounded relation and preference primitives for channel-fit inference
3. route inbound linked-channel turns into one canonical reply + mirrored
   outbound delivery posture
4. teach proactive routing when to stay in app versus propagate to linked
   channels
5. add observability, tests, and runbook proof

## Execution Groups

### Group A - Freeze Canonical Multi-Channel Contracts

Purpose:

- ensure architecture and planning docs describe exactly one conversation owner
  and one propagation rule

Tasks:

- `PRJ-750` Freeze canonical multi-channel conversation contract
  - define app chat as source-of-truth
  - define linked channels as ingress/egress mirrors
  - define canonical reply versus transport adaptation
- `PRJ-751` Freeze relational outreach governance contract
  - define obligatory replies to user-authored turns
  - define silent scheduler wakeups
  - define adaptive silence and channel-choice policy

### Group B - Add Channel-Fit Memory And Preference Inputs

Purpose:

- give runtime enough structured truth to infer where and when outreach should
  happen

Tasks:

- `PRJ-752` Add channel-affinity and response-cadence adaptive outputs
  - infer whether the user prefers app, Telegram, or mixed contact
  - infer approximate response tempo and tolerance
- `PRJ-753` Add sleep and quiet-pattern inference boundary
  - model likely sleep windows or night silence safely
  - keep this lightweight and continuity-owned, not a new scheduling subsystem
- `PRJ-754` Add explicit user channel-preference posture
  - allow stated preferences to coexist with inferred ones
  - define precedence between explicit preference and inferred adaptation

### Group C - Implement Canonical Reply And Linked-Channel Propagation

Purpose:

- ensure one canonical answer can mirror correctly across channels

Tasks:

- `PRJ-755` Canonicalize linked-channel ingress into app-owned conversation continuity
  - Telegram inbound becomes one canonical shared turn
  - app transcript stays complete regardless of source
- `PRJ-756` Mirror linked-channel replies from one canonical assistant answer
  - preserve one canonical transcript row
  - propagate semantically equivalent delivery to Telegram
- `PRJ-757` Preserve canonical-message semantics during transport segmentation
  - reuse existing Telegram splitting
  - verify that segmentation remains ordered and semantically complete
  - keep segmentation metadata out of app chat history

### Group D - Implement Relational Proactive Channel Choice

Purpose:

- teach proactive delivery to choose app only versus app plus linked channels
  constructively

Tasks:

- `PRJ-758` Add channel-choice policy for proactive outreach
  - choose whether proactive delivery stays in app or propagates to Telegram
  - base the decision on relation, channel affinity, and recent contact
- `PRJ-759` Add adaptive silence interpretation
  - treat any user message on any linked channel as contact
  - avoid panicking during likely sleep windows
  - allow different cadence by user without fixed global timeout
- `PRJ-760` Preserve mandatory reply posture for user-authored turns
  - user-originated turns must always get at least minimal reply
  - this must hold across app and linked Telegram ingress

### Group E - Observability, Testing, And Rollout Proof

Purpose:

- make the new behavior measurable and safe to roll out

Tasks:

- `PRJ-761` Expand tests for canonical multi-channel continuity
  - inbound Telegram -> canonical transcript -> mirrored Telegram reply
  - app inbound -> canonical reply -> optional propagation posture
  - silent proactive wakeup with no user-visible delivery
- `PRJ-762` Expand observability for channel-fit and propagation posture
  - keep transcript clean
  - expose channel-decision and propagation summaries in debug/health surfaces
- `PRJ-763` Update runbook, planning truth, and learning journal
  - add rollout notes
  - add incident triage posture
  - sync source-of-truth artifacts

## Detailed Task Breakdown

### PRJ-750 - Freeze canonical multi-channel conversation contract

Current-stage goal:

- document the final rules for source-of-truth chat, linked ingress, mirrored
  egress, and canonical-message semantics

Implementation notes:

- architecture docs first
- no code changes in this slice

### PRJ-751 - Freeze relational outreach governance contract

Current-stage goal:

- document the user-approved rules for:
  - always reply to user-authored turns
  - allow silent internal wakeups
  - infer silence windows and channel fit relationally

Implementation notes:

- architecture and planning truth first
- no code changes in this slice

### PRJ-752 - Add channel-affinity and response-cadence adaptive outputs

Current-stage goal:

- add bounded adaptive outputs or relation records describing:
  - preferred interaction channel
  - mixed-channel comfort
  - approximate response cadence

Repo fit analysis:

- best extension points are existing relation or conclusion owners
- avoid adding a second preference system outside current runtime memory

Validation target:

- relation signal tests
- runtime loading and debug-surface tests

### PRJ-753 - Add sleep and quiet-pattern inference boundary

Current-stage goal:

- infer likely sleep/quiet posture from light continuity signals without
  inventing a full scheduler/calendar subsystem

Repo fit analysis:

- likely reuse profile `utc_offset`, recent contact timestamps, and adaptive
  outputs
- keep this bounded and heuristic

Validation target:

- proactive policy tests
- runtime behavior tests for night silence

### PRJ-754 - Add explicit user channel-preference posture

Current-stage goal:

- define where explicit user channel preferences live and how they interact
  with inference

Repo fit analysis:

- likely belongs beside existing app-facing user preferences and tools settings
- must not duplicate identity and conclusion ownership without policy

Validation target:

- API route tests
- runtime preference precedence tests

### PRJ-755 - Canonicalize linked-channel ingress into app-owned conversation continuity

Current-stage goal:

- ensure Telegram inbound turns always persist into canonical app transcript
  under the linked `user_id`

Repo fit analysis:

- Telegram ingress already resolves linked profiles in `routes.py`
- transcript storage already reuses episodic memory
- likely needs explicit canonical-channel metadata rather than a new store

Validation target:

- `/event` Telegram ingress tests
- `/app/chat/history` transcript continuity tests

### PRJ-756 - Mirror linked-channel replies from one canonical assistant answer

Current-stage goal:

- preserve one canonical assistant reply while propagating the same meaning
  back to the source channel

Repo fit analysis:

- current action/delivery boundary is the correct owner
- likely needs bounded propagation metadata in action/delivery, not a second
  expression path

Validation target:

- action executor tests
- runtime pipeline tests for linked Telegram

### PRJ-757 - Preserve canonical-message semantics during transport segmentation

Current-stage goal:

- guarantee that Telegram segmentation remains a transport adaptation only

Repo fit analysis:

- existing `DeliveryRouter` already splits long Telegram messages
- likely work is mostly tests and explicit metadata/contract alignment

Validation target:

- delivery-router tests
- transcript tests proving no transport-segment leakage into canonical chat

### PRJ-758 - Add channel-choice policy for proactive outreach

Current-stage goal:

- let runtime choose app only versus app plus Telegram based on relation and
  channel affinity

Repo fit analysis:

- natural owners are proactive planning and delivery guardrails
- must not bypass action or transcript contracts

Validation target:

- proactive engine tests
- planning-agent tests
- runtime behavior tests

### PRJ-759 - Add adaptive silence interpretation

Current-stage goal:

- treat silence as a contextual signal rather than a fixed timeout

Repo fit analysis:

- reuse recent memory, linked-channel contact, adaptive outputs, and existing
  relation-aware proactive logic
- avoid a rigid global threshold subsystem

Validation target:

- memory repository tests
- proactive policy tests
- end-to-end behavior scenarios

### PRJ-760 - Preserve mandatory reply posture for user-authored turns

Current-stage goal:

- guarantee that inbound user turns across app and Telegram always get at
  least a minimal reply

Repo fit analysis:

- planning and action already distinguish `needs_response`; this slice should
  make the guarantee explicit and testable across channels

Validation target:

- API route tests
- runtime pipeline tests
- behavior scenarios

### PRJ-761 - Expand tests for canonical multi-channel continuity

Current-stage goal:

- cover mirrored inbound/outbound and transcript truth end to end

Validation target:

- targeted pytest modules
- final full backend suite

### PRJ-762 - Expand observability for channel-fit and propagation posture

Current-stage goal:

- expose enough runtime truth to debug:
  - why a proactive was silent
  - why Telegram propagation happened
  - which channel was preferred

Validation target:

- health route tests
- debug payload tests

### PRJ-763 - Update runbook, planning truth, and learning journal

Current-stage goal:

- record rollout posture and operator triage paths

Validation target:

- doc/context cross-review

## Recommended Execution Order

1. `PRJ-750`
2. `PRJ-751`
3. `PRJ-752`
4. `PRJ-753`
5. `PRJ-754`
6. `PRJ-755`
7. `PRJ-756`
8. `PRJ-757`
9. `PRJ-758`
10. `PRJ-759`
11. `PRJ-760`
12. `PRJ-761`
13. `PRJ-762`
14. `PRJ-763`

Why this order:

- freeze contracts first
- add memory and preference truth before behavior chooses channels
- wire canonical ingress and mirrored egress before relational proactive
  routing
- only then deepen observability and release proof

## Definition Of Done

This lane is complete when:

- the app remains the canonical conversation owner
- linked-channel ingress and egress mirror that same truth
- one canonical reply can propagate across linked channels without semantic
  drift
- user-authored turns always receive a reply
- silent internal wakeups remain silent
- proactive propagation becomes relation-aware and context-aware
- tests, docs, and operator runbook all describe the same behavior
