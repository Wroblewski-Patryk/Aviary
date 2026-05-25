---
id: "FEAT-EVENT-INGRESS"
name: "General Event Ingress"
type: "feature"
status: "verified"
layer: "cross_layer"
module: "runtime"
feature: "event_ingress"
risk_level: "high"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/pipelines/index.md"
related_files: ["backend/app/api/routes.py"]
tags: ["aviary", "feature", "event"]
---

# General Event Ingress

ID: `FEAT-EVENT-INGRESS`

## Summary

External event path into runtime pipeline

## Links

- parent: none
- children: [[api-event-ingress|API-EVENT-INGRESS]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- depends_on: [[api-event-ingress|API-EVENT-INGRESS]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-api-routes|TEST-API-ROUTES]], [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]], [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: none

## Relations

Outgoing: none

Incoming: none

## Chains

- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-EVENT-INGRESS-FEATURE-PROOF` behavior verified: Event ingress feature proof is backed by explicit API event evidence and the verified event ingress runtime chain (`.codex/tasks/PRJ-1289-event-ingress-api-gap-closure.md`).

## Theory Claims

- none

## Notes

Part of selected core runtime evidence.
