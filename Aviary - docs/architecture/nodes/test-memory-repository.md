---
id: "TEST-MEMORY-REPOSITORY"
name: "Memory Repository Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "memory_flow"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_memory_repository.py"
related_files: []
tags: ["aviary", "test", "memory"]
---

# Memory Repository Tests

ID: `TEST-MEMORY-REPOSITORY`

## Summary

Memory repository retrieval persistence and embedding behavior tests

## Links

- parent: [[feat-memory-flow|FEAT-MEMORY-FLOW]]
- children: none
- depends_on: [[service-memory-repository|SERVICE-MEMORY-REPOSITORY]], [[model-aion-memory|MODEL-AION-MEMORY]]
- used_by: [[feat-memory-flow|FEAT-MEMORY-FLOW]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-memory-repository|TEST-MEMORY-REPOSITORY]]
- docs_related: [[doc-memory-system|DOC-MEMORY-SYSTEM]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[model-aion-memory|MODEL-AION-MEMORY]]: Memory repository tests verify structured episodic payload persistence and recent chat transcript projection for AionMemory

Incoming: none

## Chains

- none

## Evidence

- `EVID-TEST-MEMORY-REPOSITORY-PROOF` test verified: Memory repository test node proof refreshed with core persistence and transcript projection checks (`backend/tests/test_memory_repository.py`). Command: `python -m pytest -q tests/test_memory_repository.py::test_memory_repository_persists_structured_episode_payload tests/test_memory_repository.py::test_memory_repository_projects_recent_chat_transcript_in_chronological_order`.

## Theory Claims

- none

## Notes

Memory repository tests back memory confidence row.
