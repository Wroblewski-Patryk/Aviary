# Conscious vs Subconscious

## Purpose

This document defines the two operating modes of AION:

- conscious loop
- subconscious loop

They are not separate personalities.
They are two modes of the same system.

---

## Core Principle

AION operates in two temporal modes:

- Conscious -> handles the present turn through the foreground pipeline
- Subconscious -> processes stored episodes to improve future turns

---

## Conscious Loop

### Definition

The conscious loop is the real-time processing layer.

It reacts to incoming events and produces immediate behavior.

---

### Responsibilities

- receive and normalize the event
- assemble or claim the attention turn when needed
- load the runtime baseline (identity, memory, goals, tasks, adaptive state)
- run the canonical foreground stage order:
  `perception -> context -> motivation -> role -> planning -> expression -> action`
- hand off the completed turn to post-action follow-ups:
  episodic memory persistence and reflection enqueue

---

### Flow

event -> normalization -> attention intake -> baseline load -> perception ->
context -> motivation -> role -> planning -> expression -> action -> memory ->
reflection trigger

---

### Characteristics

- fast
- reactive
- visible to the user
- execution-oriented

---

### Constraints

The conscious loop must NOT:

- update identity directly
- perform deep learning
- overfit on single events
- perform heavy reflection

Its job is to complete the current turn correctly, not to evolve the system by
itself.

---

## Subconscious Loop

### Definition

The subconscious loop is the background processing layer.

It runs independently of real-time interaction.

---

### Responsibilities

- analyze stored memory
- detect patterns
- generate conclusions
- update theta and relation state
- refine behavior
- maintain consistency
- prepare proposal-style background outputs for conscious review when needed

---

### Flow

memory -> analysis -> pattern detection -> conclusions -> adaptive updates ->
stored background outputs

---

### Characteristics

- slow
- reflective
- not user-visible
- pattern-oriented

---

## Key Rule

Conscious loop = bounded real-time execution
Subconscious loop = delayed adaptation

This separation is critical.

---

## Why Separation Matters

Without separation:

- the system becomes slow
- learning becomes unstable
- identity becomes chaotic
- responses degrade

With separation:

- real-time stays fast
- learning stays stable
- the system evolves correctly

---

## Shared State

Both loops operate on the same:

- identity
- memory
- theta
- goals
- context

This ensures coherence.

---

## Communication Policy

### Conscious loop

- communicates directly with the user

### Subconscious loop

- does NOT communicate directly
- produces internal updates, conclusions, and proposals

If needed, subconscious insights are passed through the conscious loop.

---

## Triggers

### Conscious triggers

- user message
- API request
- system event
- scheduler wakeup that is admitted through the attention boundary

### Subconscious triggers

- time-based cadence
- queued reflection work
- scheduled maintenance
- explicit background execution owner

---

## Temporal Dynamics

- conscious loop = immediate
- subconscious loop = periodic or deferred

Example:

- live turn handling: immediate
- reflection: scheduled or queue-driven
- deeper background analysis: delayed

---

## Failure Isolation

If subconscious loop fails:

- conscious loop must still work
- the system must still respond
- background work can retry later

---

## Implementation Split

### Conscious

- event ingress (`FastAPI`, Telegram, scheduler-normalized wakeups)
- runtime orchestrator and foreground graph
- expression-to-action handoff
- action-layer side effects
- post-action follow-ups (`memory`, `reflection trigger`)

### Subconscious

- reflection worker
- scheduler and externalized background execution paths
- reflection inference modules
- proposal generation and adaptive-output maintenance

---

## Final Principle

AION works because:

- it acts in the present through the conscious loop
- it learns from the past through the subconscious loop
