---
id: "AGENT-CONTEXT"
name: "Context Agent"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/agents/context.py"
related_files: ["backend/app/core/retrieval_policy.py", "backend/app/memory/repository.py"]
tags: ["aviary", "agent", "context"]
---

# Context Agent

ID: `AGENT-CONTEXT`

## Summary

Runtime stage agent for context construction

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]], [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-context|AGENT-CONTEXT]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Context stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-CONTEXT-PROOF` test verified: Context agent proof refreshed with focused context construction tests (`backend/tests/test_context_agent.py`). Command: `python -m pytest -q tests/test_context_agent.py`.

## Theory Claims

- none

## Notes

Context depends on memory retrieval.
