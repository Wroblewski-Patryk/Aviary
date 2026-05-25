---
id: "DOC-TOOLS-PIPELINE"
name: "Tools Pipeline Doc"
type: "documentation"
status: "verified"
layer: "docs"
module: "tools"
feature: "tools"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-11"
verification_status: "verified"
file_path: "docs/pipelines/tools.md"
related_files: []
tags: ["aviary", "docs", "tools"]
---

# Tools Pipeline Doc

ID: `DOC-TOOLS-PIPELINE`

## Summary

Dedicated app tools connector readiness preference Telegram link and permission-gate map

## Links

- parent: [[feat-tools|FEAT-TOOLS]]
- children: none
- depends_on: [[feat-tools|FEAT-TOOLS]]
- used_by: [[page-tools|PAGE-TOOLS]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- ui_related: [[page-tools|PAGE-TOOLS]]
- api_related: [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-connector-policy|TEST-CONNECTOR-POLICY]]
- docs_related: [[doc-tools-pipeline|DOC-TOOLS-PIPELINE]]
- agent_related: none

## Relations

Outgoing:
- `documents` -> [[feat-telegram|FEAT-TELEGRAM]]: Tools pipeline documents Telegram link and readiness path

Incoming: none

## Chains

- `CHAIN-TELEGRAM-LINK-DELIVERY` Telegram link and delivery chain (verified, high)
- `CHAIN-TOOLS-OVERVIEW` Tools overview execution chain (verified, high)

## Evidence

- `EVID-DOC-TOOLS-PIPELINE-PROOF` documentation verified: Tools pipeline doc proof refreshed for tools readiness preferences and Telegram link flow mapping (`docs/pipelines/tools.md`).

## Theory Claims

- none

## Notes

Tools pipeline doc is graph-linked.
