---
id: "SERVICE-MEMORY-REPOSITORY"
name: "MemoryRepository"
type: "service"
status: "verified"
layer: "backend"
module: "memory"
feature: "memory_flow"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/memory/repository.py"
related_files: ["backend/app/memory/models.py", "backend/app/memory/embeddings.py"]
tags: ["aviary", "memory", "repository"]
---

# MemoryRepository

ID: `SERVICE-MEMORY-REPOSITORY`

## Summary

Repository boundary for episodic memory retrieval writes profiles conclusions relations and reflection inputs

## Links

- parent: [[feat-memory-flow|FEAT-MEMORY-FLOW]]
- children: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[model-aion-memory|MODEL-AION-MEMORY]]
- used_by: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]], [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-memory-system|DOC-MEMORY-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `writes` -> [[model-aion-memory|MODEL-AION-MEMORY]]: Repository persists episodic memory rows

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `calls`: Runtime retrieves and writes memory through repository boundary

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)
- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)

## Evidence

- `EVID-SERVICE-MEMORY-REPOSITORY-PROOF` test verified: Memory repository proof refreshed with structured episodic payload persistence and recent chat transcript projection tests (`backend/tests/test_memory_repository.py`). Command: `python -m pytest -q tests/test_memory_repository.py::test_memory_repository_persists_structured_episode_payload tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order`.

## Theory Claims

- none

## Notes

Memory flow is verified in AVIARY-MEMORY-001.
