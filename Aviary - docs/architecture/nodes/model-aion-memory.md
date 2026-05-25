---
id: "MODEL-AION-MEMORY"
name: "AionMemory"
type: "model"
status: "verified"
layer: "database"
module: "memory"
feature: "memory_flow"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/memory/models.py"
related_files: ["backend/migrations/versions/20260416_0001_schema_baseline.py"]
tags: ["aviary", "database", "memory"]
---

# AionMemory

ID: `MODEL-AION-MEMORY`

## Summary

Episodic memory and transcript projection source

## Links

- parent: [[feat-memory-flow|FEAT-MEMORY-FLOW]]
- children: none
- depends_on: [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-schema-baseline|TEST-SCHEMA-BASELINE]], [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing: none

Incoming:
- [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]] -> `writes`: Repository persists episodic memory rows
- [[api-personality-overview|API-PERSONALITY-OVERVIEW]] -> `reads`: Personality overview reads recent activity and learned state
- [[feat-data-model|FEAT-DATA-MODEL]] -> `parent_of`: Data model feature owns AionMemory seed node
- [[test-memory-repository|TEST-MEMORY-REPOSITORY]] -> `verifies`: Memory repository tests verify structured episodic payload persistence and recent chat transcript projection for AionMemory
- [[doc-data-reference|DOC-DATA-REFERENCE]] -> `documents`: Data reference documents AionMemory

## Chains

- `CHAIN-APP-CHAT-MESSAGE` App chat message execution chain (verified, high)
- `CHAIN-DATA-MODEL-SCHEMA` Data model schema proof chain (verified, high)
- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)
- `CHAIN-PERSONALITY-OVERVIEW` Personality learned-state overview chain (verified, high)

## Evidence

- `EVID-AION-MEMORY-MODEL-PROOF` behavior verified: AionMemory model proof refreshed with structured episodic payload persistence recent chat transcript projection and schema payload column tests (`backend/tests/test_memory_repository.py`). Command: `python -m pytest -q tests/test_memory_repository.py::test_memory_repository_persists_structured_episode_payload tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order tests/test_schema_baseline.py::test_schema_baseline_tracks_structured_memory_payload_column`.

## Theory Claims

- none

## Notes

Core durable memory model.
