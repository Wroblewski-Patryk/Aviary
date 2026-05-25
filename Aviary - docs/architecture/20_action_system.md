# Action System

## Purpose

This document defines how AION performs real actions in the world.

The Action System is responsible for executing planned side effects.

Without it:

- plans stay theoretical
- decisions never become outcomes
- the system cannot affect anything outside reasoning

The Action System is the execution layer of AION.

---

## Core Principle

Action is separate from cognition.

Reasoning decides:

- what should happen
- why it should happen

Action executes:

- user-visible delivery
- connector or provider calls
- explicit action-layer domain mutations
- other world-facing or policy-gated side effects

This separation is mandatory.

Action sits after expression in the canonical foreground order:

`planning -> expression -> action`

Post-action runtime follow-ups such as episodic memory persistence and
reflection enqueue are adjacent to action, but they are not a reason to move
action earlier in the pipeline.

---

## Responsibilities

The Action System must:

- receive structured handoff from planning and expression
- decide which side effects are required inside the action boundary
- execute them safely under policy and guardrails
- return structured result
- log execution status

---

## What Counts as Action

Examples of valid actions:

- create or update goal/task state through explicit typed intents
- send Telegram message
- call an external API
- execute an authorized connector operation
- persist other action-owned typed intent results

Examples of non-actions:

- analyzing context
- generating plan
- choosing tone
- persisting episodic memory after the turn
- enqueueing reflection after persistence
- reflecting on patterns

Those belong to other layers.

---

## Action Input

The Action System receives:

- event
- plan
- expression handoff
- action requirements
- user_id
- trace_id

Example:

```json
{
  "event": {},
  "plan": {
    "goal": "Create task for follow-up",
    "steps": ["Create task", "Notify user"],
    "needs_action": true,
    "needs_response": true
  },
  "expression": {
    "delivery": {}
  },
  "meta": {
    "user_id": "uuid",
    "trace_id": "uuid"
  }
}
```

---

## Action Output

The Action System must return structured output.

Example:

```json
{
  "action_result": {
    "status": "success",
    "actions": ["task_created", "telegram_sent"],
    "notes": "Task created and user notified"
  }
}
```

Possible statuses:

- success
- partial
- fail
- noop

---

## Core Rule

Only the Action System may perform planned turn side effects.

No reasoning stage may:

- call external services directly
- send user messages directly
- execute action-owned durable mutations directly

If this rule breaks, architecture becomes chaotic.

Adjacent follow-up rule:

- runtime-owned post-action stages may persist the finished episode and enqueue
  reflection only after action output exists
- those follow-ups do not give earlier reasoning stages permission to perform
  side effects directly

---

## Action Categories

### 1. Action-Owned Domain Mutation

Used for:

- goal/task updates through explicit typed intents
- relation or proactive-state maintenance when owned by typed action intents
- other durable domain mutations explicitly delegated to action

These actions affect internal state through the action boundary.

---

### 2. User Communication

Used for:

- sending Telegram messages
- future app notifications
- reminders
- proactive check-ins when the conscious loop authorizes delivery

These actions affect the user directly.

Transport adaptation rule:

- action may adapt one canonical assistant reply to fit transport limits or
  formatting constraints
- adaptation may split a message into ordered segments, but it must preserve
  semantic completeness relative to the canonical app-owned reply
- action must not silently replace the canonical reply with a materially
  different transport-specific rewrite

---

### 3. External Tool Actions

Used for:

- HTTP requests
- API integrations
- external services
- authorized connector execution

These actions affect outside systems.

---

### 4. Runtime Triggers

Used for:

- policy-gated wakeups or runtime dispatches that are explicitly action-owned

These actions affect internal execution flow.

---

## Post-Action Runtime Follow-Ups

These are not part of the Action System, but they run after action completes:

- episodic memory persistence
- reflection enqueue

They remain runtime-orchestrator responsibilities because they happen after the
foreground action result exists and should stay separate from cognitive stages.

---

## Action Decision Model

Not every plan requires action.

Possible outcomes:

### Noop

Nothing action-owned should happen.

Example:

- internal reasoning only
- response handled without side effects
- no durable domain mutation needed

---

### Domain Mutation Only

Example:

- create task
- update goal status

---

### Communication Only

Example:

- send Telegram message

---

### Combined Action

Example:

- create task
- notify user
- execute an authorized connector operation

---

## Safety Boundary

The Action System must never:

- reinterpret cognition from scratch
- invent side effects that were not authorized by the upstream plan/policy
- bypass connector guardrails
- hide failures behind success-shaped output

Action is an executor, not a second planner.
