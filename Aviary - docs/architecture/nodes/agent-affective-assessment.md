---
id: "AGENT-AFFECTIVE-ASSESSMENT"
name: "Affective Assessment Agent"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/app/affective/assessor.py"
related_files: ["backend/app/core/affective_policy.py", "backend/app/core/affective_diagnostics.py", "backend/app/integrations/openai/prompting.py"]
tags: ["aviary", "agent", "affective", "runtime"]
---

# Affective Assessment Agent

ID: `AGENT-AFFECTIVE-ASSESSMENT`

## Summary

Runtime stage for affective signal classification and support need detection

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[agent-perception|AGENT-PERCEPTION]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-affective-assessment|AGENT-AFFECTIVE-ASSESSMENT]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Affective assessment stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-AFFECTIVE-ASSESSMENT-PROOF` test verified: Affective assessment agent proof refreshed with focused affective assessor and contract tests (`backend/tests/test_affective_assessor.py`). Command: `python -m pytest -q tests/test_affective_assessor.py tests/test_affective_contract.py`.

## Theory Claims

### CLAIM-AFFECTIVE-SIGNAL-INTEGRATION

The affective assessment stage can be interpreted as an engineered affective-signal layer that may bias support posture, motivation, planning, and expression without replacing reasoning.

- status: `reviewed`
- confidence: `medium`
- code expression: `perception.affective -> affective assessment -> motivation/role/planning/expression inputs`
- applicability: Applies to the architecture decision to keep affective cues explicit, inspectable, and bounded by policy.
- limitations: The app does not feel emotion and does not implement biological affective systems; affective classification remains software inference with tests and policy gates.
- sources: [SRC-PESSOA-2008-EMOTION-COGNITION](https://www.nature.com/articles/nrn2317), [SRC-DAMASIO-1996-SOMATIC-MARKER](https://pubmed.ncbi.nlm.nih.gov/8941953/), [SRC-PANKSEPP-1998-AFFECTIVE](https://academic.oup.com/book/53534)


## Notes

Affective assessment is part of the canonical runtime graph and is bounded by rollout policy.
