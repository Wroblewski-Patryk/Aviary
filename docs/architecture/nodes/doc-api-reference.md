---
id: "DOC-API-REFERENCE"
name: "API Reference"
type: "documentation"
status: "verified"
layer: "docs"
module: "api"
feature: "api_contracts"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-11"
verification_status: "verified"
file_path: "docs/api/index.md"
related_files: ["docs/api/openapi.json"]
tags: ["aviary", "docs", "api"]
---

# API Reference

ID: `DOC-API-REFERENCE`

## Summary

Endpoint purpose auth posture schemas side effects frontend callers tests and pipelines

## Links

- parent: none
- children: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- depends_on: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- used_by: [[feat-app-chat|FEAT-APP-CHAT]], [[feat-profile-settings|FEAT-PROFILE-SETTINGS]], [[feat-tools|FEAT-TOOLS]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]], [[api-app-me|API-APP-ME]], [[api-tools-overview|API-TOOLS-OVERVIEW]]
- database_related: none
- tests_related: [[test-api-routes|TEST-API-ROUTES]]
- docs_related: [[doc-api-reference|DOC-API-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `documents` -> [[api-app-auth|API-APP-AUTH]]: API reference documents authenticated app endpoint posture
- `documents` -> [[api-app-chat-message|API-APP-CHAT-MESSAGE]]: API reference documents chat route

Incoming: none

## Chains

- `CHAIN-APP-AUTH` App auth session execution chain (verified, high)

## Evidence

- `EVID-API-DOCS` documentation verified: API reference maps endpoint purpose auth schemas side effects tests and pipelines (`docs/api/index.md`).

## Theory Claims

- none

## Notes

Existing API reference becomes graph-linked docs evidence.
