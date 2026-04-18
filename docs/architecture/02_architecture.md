# Architecture

## Core Model

AION is an event-driven backend that keeps state across turns.

The architecture still follows the same high-level loop:

`state -> process -> action boundary -> memory -> update -> next event`

The important rule is not that every stage is already "finished", but that responsibilities stay separated while the runtime grows.

## Current Runtime Architecture

The implemented foreground runtime is:

`event -> state load -> identity -> perception -> context -> motivation -> role -> planning -> expression -> action -> memory -> reflection enqueue`

The intended long-term architecture is still described as:

`event -> perception -> context -> motivation -> role -> planning -> action -> expression -> memory -> reflection`

Current implementation note:

- `expression` is currently computed before `action`
- runtime now creates an explicit `ActionDelivery` handoff from expression into
  action
- only `action` performs side effects
- this is a runtime convenience so integrations can reuse a prepared message payload

## Main Components

The live system already has these concrete parts:

1. API layer
2. Identity snapshot builder
3. Episodic and semantic memory repository
4. Conscious runtime loop
5. Reflection worker and durable queue
6. Goal and task state
7. Lightweight milestone manager
8. Action layer
9. Expression layer
10. Infrastructure and observability

## Stage Ownership And Traceability

To keep architecture drift visible, each runtime stage has one primary code
owner and one primary regression surface:

| Stage | Main code owner | Primary validation surface |
| --- | --- | --- |
| Event normalization | `app/core/events.py`, `app/api/routes.py` | `tests/test_event_normalization.py`, `tests/test_api_routes.py` |
| State load and identity | `app/core/runtime.py`, `app/identity/service.py` | `tests/test_runtime_pipeline.py` |
| Perception | `app/agents/perception.py` | `tests/test_perception_agent.py`, `tests/test_runtime_pipeline.py` |
| Context | `app/agents/context.py` | `tests/test_context_agent.py`, `tests/test_runtime_pipeline.py` |
| Motivation | `app/motivation/engine.py` | `tests/test_motivation_engine.py`, `tests/test_runtime_pipeline.py` |
| Role | `app/agents/role.py` | `tests/test_role_agent.py`, `tests/test_runtime_pipeline.py` |
| Planning | `app/agents/planning.py` | `tests/test_planning_agent.py`, `tests/test_runtime_pipeline.py` |
| Expression | `app/expression/generator.py` | `tests/test_expression_agent.py`, `tests/test_runtime_pipeline.py` |
| Action delivery and side effects | `app/core/runtime.py`, `app/core/action.py`, `app/integrations/delivery_router.py` | `tests/test_action_executor.py`, `tests/test_delivery_router.py`, `tests/test_runtime_pipeline.py`, `tests/test_api_routes.py` |
| Memory persistence | `app/core/action.py`, `app/memory/repository.py` | `tests/test_action_executor.py`, `tests/test_memory_repository.py` |
| Reflection enqueue and worker | `app/core/runtime.py`, `app/reflection/worker.py`, `app/memory/repository.py` | `tests/test_reflection_worker.py`, `tests/test_api_routes.py`, `tests/test_runtime_pipeline.py` |

## Conscious Loop

The conscious loop handles real-time user-facing work:

- normalize input into an event
- load lightweight state
- interpret the event
- build context
- score motivation
- choose a role
- produce a plan
- prepare the reply
- execute side effects
- persist the episode

This loop is synchronous from the user's point of view, even when some stages use OpenAI.

## Reflection Loop

Reflection is no longer only a design idea. The repo now has a real app-local background worker with a durable Postgres-backed queue.

Its current job is to consolidate lightweight state such as:

- semantic user preferences
- theta orientation
- goal execution state
- goal progress snapshots and trends
- milestone state, history, and operational signals

It is still intentionally lightweight:

- in-process rather than external
- retry-based rather than scheduler-heavy
- semantic and heuristic rather than vector or graph-driven

## State Model

The runtime now combines several kinds of state:

- identity and durable profile state
- recent episodic memory
- semantic conclusions
- lightweight theta
- active goals and tasks
- goal progress history
- active milestone objects and milestone history

This is enough to make the runtime meaningfully stateful without pretending that a full autonomous agent society already exists.

## Action Boundary

The action boundary remains the architectural guardrail:

- only the action layer performs side effects
- reasoning stages prepare structure and intent
- memory and reflection updates are persisted through controlled runtime paths rather than ad hoc stage mutation

This is one of the most important constraints in the repo and should survive future refactors.

## Observability

The current architecture is designed to stay inspectable while it evolves.

Today that means:

- structured `RuntimeResult` responses from `POST /event`
- per-stage `stage_timings_ms`
- reflection queue visibility in `GET /health`
- runtime logging keyed by `event_id` and `trace_id`

## Infrastructure Reality

The live repo currently uses:

- FastAPI
- SQLAlchemy async with PostgreSQL
- optional OpenAI Responses API usage
- Telegram Bot API integration
- Docker Compose locally
- Coolify-targeted deployment on a VPS

Still planned rather than implemented:

- vector memory with `pgvector`
- LangGraph or a similar external orchestrator
- a separate reflection worker service
- richer relation and proactive subsystems

## Architectural Principle

The repo should keep making the architecture more real without pretending the later phases are already done.

That means:

- document current behavior honestly
- keep future shape visible
- surface gaps explicitly when code and architecture differ
- prefer small, reversible slices over broad rewrites
