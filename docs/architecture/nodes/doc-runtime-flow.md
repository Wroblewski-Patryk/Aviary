---
id: "DOC-RUNTIME-FLOW"
name: "Runtime Flow Doc"
type: "documentation"
status: "verified"
layer: "docs"
module: "runtime"
feature: "foreground_runtime"
risk_level: "high"
completion_percent: "95"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "docs/architecture/15_runtime_flow.md"
related_files: ["docs/architecture/16_agent_contracts.md"]
tags: ["aviary", "docs", "architecture", "runtime"]
---

# Runtime Flow Doc

ID: `DOC-RUNTIME-FLOW`

## Summary

Canonical AION runtime order and stage flow

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: none
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]], [[agent-context|AGENT-CONTEXT]], [[agent-planning|AGENT-PLANNING]]

## Relations

Outgoing: none

Incoming: none

## Chains

- `CHAIN-EVENT-INGRESS` General event ingress runtime chain (verified, high)

## Evidence

- `EVID-DOC-RUNTIME-FLOW` documentation verified: Runtime flow documentation is mapped as the architecture source of truth for canonical AION stage order and event-to-response flow (`docs/architecture/15_runtime_flow.md`).

## Theory Claims

- none

## Notes

Architecture source of truth for pipeline order.
