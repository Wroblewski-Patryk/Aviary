---
id: "AGENT-ROLE"
name: "Role Agent"
type: "agent"
status: "verified"
layer: "backend"
module: "agents"
feature: "foreground_runtime"
risk_level: "medium"
completion_percent: "85"
last_verified_at: "2026-05-24"
verification_status: "verified"
file_path: "backend/app/agents/role.py"
related_files: ["backend/app/core/role_selection_policy.py", "backend/app/core/role_skill_policy.py", "backend/app/core/skill_registry.py"]
tags: ["aviary", "agent", "role", "runtime"]
---

# Role Agent

ID: `AGENT-ROLE`

## Summary

Runtime stage that selects the behavioral role and skill posture for the turn

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]], [[agent-motivation|AGENT-MOTIVATION]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-event-ingress|API-EVENT-INGRESS]]
- database_related: [[model-aion-memory|MODEL-AION-MEMORY]]
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-role|AGENT-ROLE]]

## Relations

Outgoing: none

Incoming:
- [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]] -> `owned_by`: Role stage participates in runtime pipeline

## Chains

- none

## Evidence

- `EVID-AGENT-ROLE-PROOF` test verified: Role agent proof refreshed with focused role selection and skill posture tests (`backend/tests/test_role_agent.py`). Command: `python -m pytest -q tests/test_role_agent.py`.

## Theory Claims

### CLAIM-ROLE-SOCIAL-POSTURE

The role-selection stage can be interpreted as an engineered social-posture and perspective-taking boundary that chooses an interaction stance before planning and expression.

- status: `reviewed`
- confidence: `medium`
- code expression: `motivation + context + preferences -> selected role + selected skills`
- applicability: Applies to role selection as interaction posture metadata that shapes planning/expression without creating a second persona or granting execution authority.
- limitations: The app does not possess social cognition or theory of mind; role selection is a constrained software policy and prompt/skill posture.
- sources: [SRC-AMODIO-FRITH-2006-SOCIAL](https://cir.nii.ac.jp/crid/1363107368466543232), [SRC-FRITH-FRITH-2006-MENTALIZING](https://www.sciencedirect.com/science/article/pii/S0896627306003448), [SRC-ADOLPHS-1999-SOCIAL](https://cir.nii.ac.jp/crid/1360574096537462784), [SRC-MILLER-COHEN-2001-PFC](https://www.annualreviews.org/doi/10.1146/annurev.neuro.24.1.167)


## Notes

Role selection shapes planning and expression but does not grant action authority.
