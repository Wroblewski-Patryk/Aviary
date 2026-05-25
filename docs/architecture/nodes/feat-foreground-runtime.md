---
id: "FEAT-FOREGROUND-RUNTIME"
name: "Foreground Runtime"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "runtime"
feature: "foreground_runtime"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/pipelines/foreground-runtime.md"
related_files: ["backend/app/core/runtime.py", "backend/app/core/runtime_graph.py", "backend/app/core/contracts.py"]
tags: ["aviary", "feature", "runtime"]
---

# Foreground Runtime

ID: `FEAT-FOREGROUND-RUNTIME`

## Summary

Canonical event to response pipeline through AION runtime stages

## Links

- parent: none
- children: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[event-app-chat-turn|EVENT-APP-CHAT-TURN]], [[agent-perception|AGENT-PERCEPTION]], [[agent-context|AGENT-CONTEXT]], [[agent-planning|AGENT-PLANNING]]
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]], [[feat-event-ingress|FEAT-EVENT-INGRESS]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]], [[agent-context|AGENT-CONTEXT]], [[agent-planning|AGENT-PLANNING]]

## Relations

Outgoing:
- `parent_of` -> [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]: Foreground runtime feature owns orchestrator

Incoming: none

## Chains

- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-RUNTIME-LEDGER` behavior verified: Runtime confidence row is VERIFIED with backend test and production smoke evidence (`.agents/state/module-confidence-ledger.md`).

## Theory Claims

### CLAIM-RUNTIME-PREDICTIVE-ACTION-LOOP

The AION runtime can be interpreted as an engineered perception-context-planning-action loop inspired by predictive processing and active-inference style cognitive architectures.

- status: `reviewed`
- confidence: `medium`
- code expression: `event -> perception -> context -> motivation -> role -> planning -> action -> expression -> memory -> reflection`
- applicability: Applies to architecture language, stage separation, and traceability of perception/action loops.
- limitations: The software is not a biological brain model and does not implement full variational free-energy mathematics or cortical microcircuits.
- sources: [SRC-FRISTON-2010-FEP](https://www.nature.com/articles/nrn2787), [SRC-CLARK-2013-PREDICTIVE](https://pubmed.ncbi.nlm.nih.gov/23663408/), [SRC-BASTOS-2012-MICROCIRCUITS](https://pubmed.ncbi.nlm.nih.gov/23177956/)


## Notes

Core AION pipeline.
