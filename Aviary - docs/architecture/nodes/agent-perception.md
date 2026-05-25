---
id: "AGENT-PERCEPTION"
name: "Perception Agent"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/agents/perception.py"
related_files: ["backend/app/perception/assessor.py", "backend/app/core/perception_policy.py"]
tags: ["aviary", "agent", "perception"]
---

# Perception Agent

ID: `AGENT-PERCEPTION`

## Summary

Runtime stage agent for perception assessment

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Perception stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-PERCEPTION-PROOF` test verified: Perception agent proof refreshed with focused perception assessor and runtime affective contract checks (`backend/tests/test_perception_assessor.py`). Command: `python -m pytest -q tests/test_perception_assessor.py tests/test_affective_contract.py`.

## Theory Claims

### CLAIM-PERCEPTION-ATTENTION-SALIENCE

The perception stage can be interpreted as an engineered attention and salience boundary that extracts behaviorally relevant signals before context and planning consume the turn.

- status: `reviewed`
- confidence: `medium`
- code expression: `event -> perception -> structured salience and intent schema`
- applicability: Applies to runtime organization, attention-boundary naming, and the separation of perception outputs from downstream planning.
- limitations: The software uses engineered classifiers and schemas; it does not implement neural attention networks or visual saliency maps.
- sources: [SRC-POSNER-PETERSEN-1990-ATTENTION](https://www.annualreviews.org/content/journals/10.1146/annurev.ne.13.030190.000325), [SRC-CORBETTA-SHULMAN-2002-ATTENTION](https://www.nature.com/articles/nrn755), [SRC-ITTI-KOCH-2001-SALIENCE](https://www.nature.com/articles/35058500), [SRC-CLARK-2013-PREDICTIVE](https://pubmed.ncbi.nlm.nih.gov/23663408/)


## Notes

Agent contract covered as part of runtime flow.
