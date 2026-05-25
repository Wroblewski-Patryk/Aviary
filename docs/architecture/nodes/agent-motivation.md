---
id: "AGENT-MOTIVATION"
name: "Motivation Engine"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/app/motivation/engine.py"
related_files: ["backend/app/core/adaptive_policy.py", "docs/architecture/06_motivation_engine.md"]
tags: ["aviary", "agent", "motivation", "runtime"]
---

# Motivation Engine

ID: `AGENT-MOTIVATION`

## Summary

Runtime stage that evaluates importance urgency valence and mode before role/planning

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[agent-context|AGENT-CONTEXT]], [[agent-affective-assessment|AGENT-AFFECTIVE-ASSESSMENT]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-motivation|AGENT-MOTIVATION]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Motivation stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-MOTIVATION-PROOF` test verified: Motivation engine proof refreshed with focused motivation evaluation tests (`backend/tests/test_motivation_engine.py`). Command: `python -m pytest -q tests/test_motivation_engine.py`.

## Theory Claims

### CLAIM-MOTIVATION-VALUATION-SELECTION

The motivation stage can be interpreted as an engineered valuation and action-readiness layer that separates importance, urgency, valence, and response mode before role and planning.

- status: `reviewed`
- confidence: `medium`
- code expression: `context + affective cues + goals -> motivation mode/importance/urgency/valence`
- applicability: Applies to the project framing of motivation as a bounded policy stage for prioritization and response mode selection.
- limitations: The app does not implement dopamine systems, reward circuitry, or biological motivation; it uses explicit software fields and policies.
- sources: [SRC-BERRIDGE-ROBINSON-2003-REWARD](https://www.sciencedirect.com/science/article/pii/S0166223603002339), [SRC-DAMASIO-1996-SOMATIC-MARKER](https://pubmed.ncbi.nlm.nih.gov/8941953/), [SRC-FRISTON-2010-FEP](https://www.nature.com/articles/nrn2787)


## Notes

Motivation is implemented as a bounded runtime stage rather than arbitrary emotion.
