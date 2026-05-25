---
id: "PROMPT-OPENAI-RUNTIME"
name: "OpenAI Runtime Prompting"
type: "prompt"
status: "verified"
layer: "backend"
module: "openai"
feature: "foreground_runtime"
risk_level: "high"
completion_percent: "85"
last_verified_at: "2026-05-14"
verification_status: "verified"
file_path: "backend/app/integrations/openai/prompting.py"
related_files: ["backend/app/integrations/openai/client.py"]
tags: ["aviary", "prompt", "openai"]
---

# OpenAI Runtime Prompting

ID: `PROMPT-OPENAI-RUNTIME`

## Summary

Prompting contract for AI-assisted runtime replies and classification

## Links

- parent: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- children: none
- depends_on: [[agent-perception|AGENT-PERCEPTION]], [[service-runtime-orchestrator|SERVICE-RUNTIME-ORCHESTRATOR]]
- used_by: [[feat-foreground-runtime|FEAT-FOREGROUND-RUNTIME]]
- ui_related: none
- api_related: [[api-app-chat-message|API-APP-CHAT-MESSAGE]]
- database_related: none
- tests_related: [[test-runtime-pipeline|TEST-RUNTIME-PIPELINE]]
- docs_related: [[doc-runtime-flow|DOC-RUNTIME-FLOW]]
- agent_related: [[agent-perception|AGENT-PERCEPTION]], [[agent-planning|AGENT-PLANNING]]

## Relations

Outgoing: none

Incoming: none

## Chains

- none

## Evidence

- `EVID-PROMPT-OPENAI-RUNTIME-PROOF` test verified: OpenAI runtime prompting proof refreshed with prompt builder response budget policy and API chat reply budget tests (`backend/tests/test_openai_prompting.py`). Command: `python -m pytest -q tests/test_openai_prompting.py tests/test_response_budget_policy.py tests/test_openai_client.py::test_openai_client_generate_reply_uses_api_chat_response_budget`.

## Theory Claims

- none

## Notes

Prompt and budget behavior covered by AI requirement rows.
