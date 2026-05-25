---
id: "TEST-CONNECTOR-POLICY"
name: "Connector Policy Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "tools"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_connector_policy.py"
related_files: []
tags: ["aviary", "test", "connectors"]
---

# Connector Policy Tests

ID: `TEST-CONNECTOR-POLICY`

## Summary

Connector operation and permission policy tests

## Links

- parent: [[feat-tools|FEAT-TOOLS]]
- children: none
- depends_on: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- used_by: [[feat-tools|FEAT-TOOLS]]
- ui_related: none
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-connector-policy|TEST-CONNECTOR-POLICY]]
- docs_related: [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[api-tools-overview|API-TOOLS-OVERVIEW]]: Connector policy tests verify tools permission posture

Incoming: none

## Chains

- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- missing

## Theory Claims

- none

## Notes

Provider policies covered locally; live credentials remain scope-dependent.
