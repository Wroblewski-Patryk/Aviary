---
id: "AGENT-PLANNING"
name: "Planning Agent"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/agents/planning.py"
related_files: ["backend/app/core/planning_governance.py"]
tags: ["aviary", "agent", "planning"]
---

# Planning Agent

ID: `AGENT-PLANNING`

## Summary

Runtime stage agent for plan generation

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
- agent_related: [[agent-planning|AGENT-PLANNING]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Planning stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-PLANNING-PROOF` test verified: Planning agent proof refreshed with focused planning agent tests (`backend/tests/test_planning_agent.py`). Command: `python -m pytest -q tests/test_planning_agent.py`.

## Theory Claims

### CLAIM-PLANNING-EXECUTIVE-POLICY

The planning stage can be interpreted as an engineered executive-control and policy-selection boundary that proposes goals or next actions without owning side effects.

- status: `reviewed`
- confidence: `medium`
- code expression: `role -> planning -> expression -> action boundary`
- applicability: Applies to the architecture separation between planning, expression, and action ownership.
- limitations: The app does not implement prefrontal cortex function or formal policy optimization; action authority remains a software safety boundary.
- sources: [SRC-MILLER-COHEN-2001-PFC](https://www.annualreviews.org/doi/10.1146/annurev.neuro.24.1.167), [SRC-FRISTON-2010-FEP](https://www.nature.com/articles/nrn2787), [SRC-CLARK-2013-PREDICTIVE](https://pubmed.ncbi.nlm.nih.gov/23663408/)


## Notes

Planning remains before action boundary.
