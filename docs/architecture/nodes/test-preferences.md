---
id: "TEST-PREFERENCES"
name: "Preferences Tests"
type: "test"
status: "verified"
layer: "test"
module: "backend"
feature: "profile_settings"
risk_level: "medium"
completion_percent: "90"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/tests/test_preferences.py"
related_files: []
tags: ["aviary", "test", "profile"]
---

# Preferences Tests

ID: `TEST-PREFERENCES`

## Summary

Preference parsing and persistence posture tests

## Links

- parent: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- children: none
- depends_on: [[api-app-me|API-APP-ME]], [[model-aion-profile|MODEL-AION-PROFILE]]
- used_by: [[feat-profile-settings|FEAT-PROFILE-SETTINGS]]
- ui_related: none
- api_related: [[api-app-me|API-APP-ME]]
- database_related: [[model-aion-profile|MODEL-AION-PROFILE]]
- tests_related: [[test-preferences|TEST-PREFERENCES]]
- docs_related: [[doc-data-reference|DOC-DATA-REFERENCE]]
- agent_related: none

## Relations

Outgoing:
- `verifies` -> [[model-aion-profile|MODEL-AION-PROFILE]]: Preferences tests verify profile preference parsing/persistence

Incoming: none

## Chains

- `CHAIN-PROFILE-SETTINGS` Profile settings execution chain (verified, high)

## Evidence

- `EVID-TEST-PREFERENCES-PROOF` test verified: Preferences tests proof refreshed with profile preference parsing and persistence helper contract coverage (`backend/tests/test_preferences.py`). Command: `python -m pytest -q tests/test_preferences.py`.

## Theory Claims

- none

## Notes

Preference tests are owned in test ledger.
