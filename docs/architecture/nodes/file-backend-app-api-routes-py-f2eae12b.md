---
id: "FILE-BACKEND-APP-API-ROUTES-PY-F2EAE12B"
name: "routes.py"
type: "api_file"
status: "implemented"
layer: "api"
module: "backend"
feature: "api_contracts"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/app/api/routes.py"
related_files: []
tags: ["auto", "api"]
---

# routes.py

ID: `FILE-BACKEND-APP-API-ROUTES-PY-F2EAE12B`

## Summary

Repository file `backend/app/api/routes.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-runtime-from-request-fe129d45|PYFUNC-BACKEND-APP-API-ROUTES-PY-RUNTIME-FROM-REQUEST-FE129D45]]: `backend/app/api/routes.py` contains function `_runtime_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-telegram-from-request-02ed84c7|PYFUNC-BACKEND-APP-API-ROUTES-PY-TELEGRAM-FROM-REQUEST-02ED84C7]]: `backend/app/api/routes.py` contains function `_telegram_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-settings-from-request-256249bb|PYFUNC-BACKEND-APP-API-ROUTES-PY-SETTINGS-FROM-REQUEST-256249BB]]: `backend/app/api/routes.py` contains function `_settings_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-recent-activity-snapshot-6d16e333|PYFUNC-BACKEND-APP-API-ROUTES-PY-RECENT-ACTIVITY-SNAPSHOT-6D16E333]]: `backend/app/api/routes.py` contains function `_recent_activity_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-pending-proposal-snapshot-c6b622b8|PYFUNC-BACKEND-APP-API-ROUTES-PY-PENDING-PROPOSAL-SNAPSHOT-C6B622B8]]: `backend/app/api/routes.py` contains function `_pending_proposal_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-normalize-auth-email-7da5e39b|PYFUNC-BACKEND-APP-API-ROUTES-PY-NORMALIZE-AUTH-EMAIL-7DA5E39B]]: `backend/app/api/routes.py` contains function `_normalize_auth_email`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-hash-password-b9069856|PYFUNC-BACKEND-APP-API-ROUTES-PY-HASH-PASSWORD-B9069856]]: `backend/app/api/routes.py` contains function `_hash_password`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-verify-password-6c208a3f|PYFUNC-BACKEND-APP-API-ROUTES-PY-VERIFY-PASSWORD-6C208A3F]]: `backend/app/api/routes.py` contains function `_verify_password`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-hash-session-token-11319c85|PYFUNC-BACKEND-APP-API-ROUTES-PY-HASH-SESSION-TOKEN-11319C85]]: `backend/app/api/routes.py` contains function `_hash_session_token`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-new-auth-user-id-6acc3ea1|PYFUNC-BACKEND-APP-API-ROUTES-PY-NEW-AUTH-USER-ID-6ACC3EA1]]: `backend/app/api/routes.py` contains function `_new_auth_user_id`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-new-auth-session-id-57277ce6|PYFUNC-BACKEND-APP-API-ROUTES-PY-NEW-AUTH-SESSION-ID-57277CE6]]: `backend/app/api/routes.py` contains function `_new_auth_session_id`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-new-auth-session-token-72d88fed|PYFUNC-BACKEND-APP-API-ROUTES-PY-NEW-AUTH-SESSION-TOKEN-72D88FED]]: `backend/app/api/routes.py` contains function `_new_auth_session_token`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-new-telegram-link-code-24a0c012|PYFUNC-BACKEND-APP-API-ROUTES-PY-NEW-TELEGRAM-LINK-CODE-24A0C012]]: `backend/app/api/routes.py` contains function `_new_telegram_link_code`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-auth-cookie-name-f0620d4b|PYFUNC-BACKEND-APP-API-ROUTES-PY-AUTH-COOKIE-NAME-F0620D4B]]: `backend/app/api/routes.py` contains function `_auth_cookie_name`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-auth-session-ttl-hours-b67ba9d9|PYFUNC-BACKEND-APP-API-ROUTES-PY-AUTH-SESSION-TTL-HOURS-B67BA9D9]]: `backend/app/api/routes.py` contains function `_auth_session_ttl_hours`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-set-auth-cookie-a9d99047|PYFUNC-BACKEND-APP-API-ROUTES-PY-SET-AUTH-COOKIE-A9D99047]]: `backend/app/api/routes.py` contains function `_set_auth_cookie`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-clear-auth-cookie-439f5198|PYFUNC-BACKEND-APP-API-ROUTES-PY-CLEAR-AUTH-COOKIE-439F5198]]: `backend/app/api/routes.py` contains function `_clear_auth_cookie`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-settings-payload-965794e4|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-SETTINGS-PAYLOAD-965794E4]]: `backend/app/api/routes.py` contains function `_app_settings_payload`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-normalized-confirmation-value-c9ab6041|PYFUNC-BACKEND-APP-API-ROUTES-PY-NORMALIZED-CONFIRMATION-VALUE-C9AB6041]]: `backend/app/api/routes.py` contains function `_normalized_confirmation_value`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-confirmation-payload-matches-submissi-5c07b1f6|PYFUNC-BACKEND-APP-API-ROUTES-PY-CONFIRMATION-PAYLOAD-MATCHES-SUBMISSI-5C07B1F6]]: `backend/app/api/routes.py` contains function `_confirmation_payload_matches_submission`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-confirmation-rejection-97396b6a|PYFUNC-BACKEND-APP-API-ROUTES-PY-CONFIRMATION-REJECTION-97396B6A]]: `backend/app/api/routes.py` contains function `_confirmation_rejection`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-replay-snapshot-matches-pending-82495171|PYFUNC-BACKEND-APP-API-ROUTES-PY-REPLAY-SNAPSHOT-MATCHES-PENDING-82495171]]: `backend/app/api/routes.py` contains function `_replay_snapshot_matches_pending`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-build-confirmed-connector-replay-plan-88f0d442|PYFUNC-BACKEND-APP-API-ROUTES-PY-BUILD-CONFIRMED-CONNECTOR-REPLAY-PLAN-88F0D442]]: `backend/app/api/routes.py` contains function `_build_confirmed_connector_replay_plan`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-event-with-user-utc-offset-3d8f07f7|PYFUNC-BACKEND-APP-API-ROUTES-PY-EVENT-WITH-USER-UTC-OFFSET-3D8F07F7]]: `backend/app/api/routes.py` contains function `_event_with_user_utc_offset`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-require-app-auth-44b5ea16|PYFUNC-BACKEND-APP-API-ROUTES-PY-REQUIRE-APP-AUTH-44B5EA16]]: `backend/app/api/routes.py` contains function `_require_app_auth`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-telegram-telemetry-from-request-d8e4c15d|PYFUNC-BACKEND-APP-API-ROUTES-PY-TELEGRAM-TELEMETRY-FROM-REQUEST-D8E4C15D]]: `backend/app/api/routes.py` contains function `_telegram_telemetry_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-memory-repository-from-request-228416c0|PYFUNC-BACKEND-APP-API-ROUTES-PY-MEMORY-REPOSITORY-FROM-REQUEST-228416C0]]: `backend/app/api/routes.py` contains function `_memory_repository_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-resolve-linked-telegram-user-id-0f909f8e|PYFUNC-BACKEND-APP-API-ROUTES-PY-RESOLVE-LINKED-TELEGRAM-USER-ID-0F909F8E]]: `backend/app/api/routes.py` contains function `_resolve_linked_telegram_user_id`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-reflection-worker-from-request-d2e5b963|PYFUNC-BACKEND-APP-API-ROUTES-PY-REFLECTION-WORKER-FROM-REQUEST-D2E5B963]]: `backend/app/api/routes.py` contains function `_reflection_worker_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-scheduler-worker-from-request-8431682d|PYFUNC-BACKEND-APP-API-ROUTES-PY-SCHEDULER-WORKER-FROM-REQUEST-8431682D]]: `backend/app/api/routes.py` contains function `_scheduler_worker_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-attention-coordinator-from-request-df3eaf32|PYFUNC-BACKEND-APP-API-ROUTES-PY-ATTENTION-COORDINATOR-FROM-REQUEST-DF3EAF32]]: `backend/app/api/routes.py` contains function `_attention_coordinator_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-attention-snapshot-from-request-69f0ba35|PYFUNC-BACKEND-APP-API-ROUTES-PY-ATTENTION-SNAPSHOT-FROM-REQUEST-69F0BA35]]: `backend/app/api/routes.py` contains function `_attention_snapshot_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-scheduler-cadence-evidence-from-reque-4bddc622|PYFUNC-BACKEND-APP-API-ROUTES-PY-SCHEDULER-CADENCE-EVIDENCE-FROM-REQUE-4BDDC622]]: `backend/app/api/routes.py` contains function `_scheduler_cadence_evidence_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-memory-retrieval-snapshot-from-settin-80c670b8|PYFUNC-BACKEND-APP-API-ROUTES-PY-MEMORY-RETRIEVAL-SNAPSHOT-FROM-SETTIN-80C670B8]]: `backend/app/api/routes.py` contains function `_memory_retrieval_snapshot_from_settings`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-incident-evidence-from-request-fca2e705|PYFUNC-BACKEND-APP-API-ROUTES-PY-INCIDENT-EVIDENCE-FROM-REQUEST-FCA2E705]]: `backend/app/api/routes.py` contains function `_incident_evidence_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-connectors-snapshot-from-settings-a1289f30|PYFUNC-BACKEND-APP-API-ROUTES-PY-CONNECTORS-SNAPSHOT-FROM-SETTINGS-A1289F30]]: `backend/app/api/routes.py` contains function `_connectors_snapshot_from_settings`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-debug-query-compat-telemetry-from-req-ab6e55b4|PYFUNC-BACKEND-APP-API-ROUTES-PY-DEBUG-QUERY-COMPAT-TELEMETRY-FROM-REQ-AB6E55B4]]: `backend/app/api/routes.py` contains function `_debug_query_compat_telemetry_from_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-enforce-debug-access-3a4608ba|PYFUNC-BACKEND-APP-API-ROUTES-PY-ENFORCE-DEBUG-ACCESS-3A4608BA]]: `backend/app/api/routes.py` contains function `_enforce_debug_access`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-build-learned-state-snapshot-73cf9a24|PYFUNC-BACKEND-APP-API-ROUTES-PY-BUILD-LEARNED-STATE-SNAPSHOT-73CF9A24]]: `backend/app/api/routes.py` contains function `_build_learned_state_snapshot`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-try-handle-telegram-link-command-5114eac8|PYFUNC-BACKEND-APP-API-ROUTES-PY-TRY-HANDLE-TELEGRAM-LINK-COMMAND-5114EAC8]]: `backend/app/api/routes.py` contains function `_try_handle_telegram_link_command`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-handle-event-request-c6dab9a7|PYFUNC-BACKEND-APP-API-ROUTES-PY-HANDLE-EVENT-REQUEST-C6DAB9A7]]: `backend/app/api/routes.py` contains function `_handle_event_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-handle-internal-debug-ingress-aa85eb6e|PYFUNC-BACKEND-APP-API-ROUTES-PY-HANDLE-INTERNAL-DEBUG-INGRESS-AA85EB6E]]: `backend/app/api/routes.py` contains function `_handle_internal_debug_ingress`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-mark-query-debug-compat-headers-430eaf53|PYFUNC-BACKEND-APP-API-ROUTES-PY-MARK-QUERY-DEBUG-COMPAT-HEADERS-430EAF53]]: `backend/app/api/routes.py` contains function `_mark_query_debug_compat_headers`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-is-break-glass-override-request-747a76be|PYFUNC-BACKEND-APP-API-ROUTES-PY-IS-BREAK-GLASS-OVERRIDE-REQUEST-747A76BE]]: `backend/app/api/routes.py` contains function `_is_break_glass_override_request`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-enforce-shared-debug-ingress-policy-b0a1d9d9|PYFUNC-BACKEND-APP-API-ROUTES-PY-ENFORCE-SHARED-DEBUG-INGRESS-POLICY-B0A1D9D9]]: `backend/app/api/routes.py` contains function `_enforce_shared_debug_ingress_policy`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-mark-shared-debug-compat-headers-4a2da701|PYFUNC-BACKEND-APP-API-ROUTES-PY-MARK-SHARED-DEBUG-COMPAT-HEADERS-4A2DA701]]: `backend/app/api/routes.py` contains function `_mark_shared_debug_compat_headers`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-health-21cd7262|PYFUNC-BACKEND-APP-API-ROUTES-PY-HEALTH-21CD7262]]: `backend/app/api/routes.py` contains function `health`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-register-d7ac15ac|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-REGISTER-D7AC15AC]]: `backend/app/api/routes.py` contains function `app_register`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-login-1c99d9a9|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-LOGIN-1C99D9A9]]: `backend/app/api/routes.py` contains function `app_login`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-logout-6c04922b|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-LOGOUT-6C04922B]]: `backend/app/api/routes.py` contains function `app_logout`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-me-c09d9cac|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-ME-C09D9CAC]]: `backend/app/api/routes.py` contains function `app_me`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-patch-me-settings-a09e62ca|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-PATCH-ME-SETTINGS-A09E62CA]]: `backend/app/api/routes.py` contains function `app_patch_me_settings`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-reset-me-data-7c2cf6bf|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-RESET-ME-DATA-7C2CF6BF]]: `backend/app/api/routes.py` contains function `app_reset_me_data`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-chat-history-9610fa36|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-CHAT-HISTORY-9610FA36]]: `backend/app/api/routes.py` contains function `app_chat_history`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-chat-message-18882842|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-CHAT-MESSAGE-18882842]]: `backend/app/api/routes.py` contains function `app_chat_message`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-confirm-connector-action-1ac4ca50|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-CONFIRM-CONNECTOR-ACTION-1AC4CA50]]: `backend/app/api/routes.py` contains function `app_confirm_connector_action`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-personality-overview-05bce018|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-PERSONALITY-OVERVIEW-05BCE018]]: `backend/app/api/routes.py` contains function `app_personality_overview`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-tools-overview-1536c4d4|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-TOOLS-OVERVIEW-1536C4D4]]: `backend/app/api/routes.py` contains function `app_tools_overview`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-patch-tools-preferences-4cbdfd54|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-PATCH-TOOLS-PREFERENCES-4CBDFD54]]: `backend/app/api/routes.py` contains function `app_patch_tools_preferences`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-app-start-telegram-link-eea2a534|PYFUNC-BACKEND-APP-API-ROUTES-PY-APP-START-TELEGRAM-LINK-EEA2A534]]: `backend/app/api/routes.py` contains function `app_start_telegram_link`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-internal-state-inspection-endpoint-8a964d8a|PYFUNC-BACKEND-APP-API-ROUTES-PY-INTERNAL-STATE-INSPECTION-ENDPOINT-8A964D8A]]: `backend/app/api/routes.py` contains function `internal_state_inspection_endpoint`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-event-endpoint-481df852|PYFUNC-BACKEND-APP-API-ROUTES-PY-EVENT-ENDPOINT-481DF852]]: `backend/app/api/routes.py` contains function `event_endpoint`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-event-debug-endpoint-ef2fbbab|PYFUNC-BACKEND-APP-API-ROUTES-PY-EVENT-DEBUG-ENDPOINT-EF2FBBAB]]: `backend/app/api/routes.py` contains function `event_debug_endpoint`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-internal-event-debug-endpoint-5409df78|PYFUNC-BACKEND-APP-API-ROUTES-PY-INTERNAL-EVENT-DEBUG-ENDPOINT-5409DF78]]: `backend/app/api/routes.py` contains function `internal_event_debug_endpoint`.
- `parent_of` -> [[pyfunc-backend-app-api-routes-py-set-webhook-16c00f65|PYFUNC-BACKEND-APP-API-ROUTES-PY-SET-WEBHOOK-16C00F65]]: `backend/app/api/routes.py` contains function `set_webhook`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
