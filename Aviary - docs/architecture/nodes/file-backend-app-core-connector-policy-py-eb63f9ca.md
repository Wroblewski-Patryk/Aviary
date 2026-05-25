---
id: "FILE-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-EB63F9CA"
name: "connector_policy.py"
type: "backend_file"
status: "implemented"
layer: "backend"
module: "backend"
feature: "backend"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/app/core/connector_policy.py"
related_files: []
tags: ["auto", "backend"]
---

# connector_policy.py

ID: `FILE-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-EB63F9CA`

## Summary

Repository file `backend/app/core/connector_policy.py` auto-discovered for architecture graph inventory.

## Links

- parent: none
- children: none
- depends_on: none
- used_by: none
- ui_related: none
- api_related: none
- database_related: none
- tests_related: none
- docs_related: none
- agent_related: none

## Relations

Outgoing:
- `parent_of` -> [[pyclass-backend-app-core-connector-policy-py-connectoroperationpolicy-052106f2|PYCLASS-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-CONNECTOROPERATIONPOLICY-052106F2]]: `backend/app/core/connector_policy.py` contains class `ConnectorOperationPolicy`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-resolve-connector-operatio-617b29ef|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-RESOLVE-CONNECTOR-OPERATIO-617B29EF]]: `backend/app/core/connector_policy.py` contains function `resolve_connector_operation_policy`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-resolve-connector-capabili-786229af|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-RESOLVE-CONNECTOR-CAPABILI-786229AF]]: `backend/app/core/connector_policy.py` contains function `resolve_connector_capability_discovery_policy`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-build-connector-permission-b53db928|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-BUILD-CONNECTOR-PERMISSION-B53DB928]]: `backend/app/core/connector_policy.py` contains function `build_connector_permission_gate`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-resolve-policy-for-connect-4459552b|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-RESOLVE-POLICY-FOR-CONNECT-4459552B]]: `backend/app/core/connector_policy.py` contains function `resolve_policy_for_connector_intent`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-connector-authorization-ma-7543d34f|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-CONNECTOR-AUTHORIZATION-MA-7543D34F]]: `backend/app/core/connector_policy.py` contains function `connector_authorization_matrix_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-connector-capability-propo-7c370ce3|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-CONNECTOR-CAPABILITY-PROPO-7C370CE3]]: `backend/app/core/connector_policy.py` contains function `connector_capability_proposal_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-connector-guardrail-snapsh-e4539e7d|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-CONNECTOR-GUARDRAIL-SNAPSH-E4539E7D]]: `backend/app/core/connector_policy.py` contains function `connector_guardrail_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-connector-intent-policy-vi-65c2a3d6|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-CONNECTOR-INTENT-POLICY-VI-65C2A3D6]]: `backend/app/core/connector_policy.py` contains function `connector_intent_policy_violation`.
- `parent_of` -> [[pyfunc-backend-app-core-connector-policy-py-permission-gate-reason-dcfe293b|PYFUNC-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-PERMISSION-GATE-REASON-DCFE293B]]: `backend/app/core/connector_policy.py` contains function `_permission_gate_reason`.

Incoming:
- [[file-backend-tests-test-connector-policy-py-f801f586|FILE-BACKEND-TESTS-TEST-CONNECTOR-POLICY-PY-F801F586]] -> `verifies`: Test file `backend/tests/test_connector_policy.py` appears to verify `FILE-BACKEND-APP-CORE-CONNECTOR-POLICY-PY-EB63F9CA`.

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
