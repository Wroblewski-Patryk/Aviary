---
id: "FILE-BACKEND-APP-API-SCHEMAS-PY-06232F12"
name: "schemas.py"
type: "api_file"
status: "implemented"
layer: "api"
module: "backend"
feature: "api_contracts"
risk_level: "medium"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "backend/app/api/schemas.py"
related_files: []
tags: ["auto", "api"]
---

# schemas.py

ID: `FILE-BACKEND-APP-API-SCHEMAS-PY-06232F12`

## Summary

Repository file `backend/app/api/schemas.py` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-eventreplyresponse-85bcd107|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-EVENTREPLYRESPONSE-85BCD107]]: `backend/app/api/schemas.py` contains class `EventReplyResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-eventruntimeresponse-f529076b|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-EVENTRUNTIMERESPONSE-F529076B]]: `backend/app/api/schemas.py` contains class `EventRuntimeResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-eventqueueresponse-a2eb11bb|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-EVENTQUEUERESPONSE-A2EB11BB]]: `backend/app/api/schemas.py` contains class `EventQueueResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-pendingconnectorconfirmationresponse-47ab9c28|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-PENDINGCONNECTORCONFIRMATIONRESPONSE-47AB9C28]]: `backend/app/api/schemas.py` contains class `PendingConnectorConfirmationResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-eventresponse-fcbcbde4|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-EVENTRESPONSE-FCBCBDE4]]: `backend/app/api/schemas.py` contains class `EventResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-setwebhookrequest-53b65cd6|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-SETWEBHOOKREQUEST-53B65CD6]]: `backend/app/api/schemas.py` contains class `SetWebhookRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appregisterrequest-f56ccf92|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPREGISTERREQUEST-F56CCF92]]: `backend/app/api/schemas.py` contains class `AppRegisterRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-apploginrequest-f4c9ce91|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPLOGINREQUEST-F4C9CE91]]: `backend/app/api/schemas.py` contains class `AppLoginRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appsettingspatchrequest-996738fc|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPSETTINGSPATCHREQUEST-996738FC]]: `backend/app/api/schemas.py` contains class `AppSettingsPatchRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appresetdatarequest-f0071d50|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPRESETDATAREQUEST-F0071D50]]: `backend/app/api/schemas.py` contains class `AppResetDataRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appchatmessagerequest-0cef3709|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCHATMESSAGEREQUEST-0CEF3709]]: `backend/app/api/schemas.py` contains class `AppChatMessageRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appconnectorconfirmationrequest-98214940|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCONNECTORCONFIRMATIONREQUEST-98214940]]: `backend/app/api/schemas.py` contains class `AppConnectorConfirmationRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appauthuserresponse-8035ab64|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPAUTHUSERRESPONSE-8035AB64]]: `backend/app/api/schemas.py` contains class `AppAuthUserResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appsettingsresponse-6c08196c|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPSETTINGSRESPONSE-6C08196C]]: `backend/app/api/schemas.py` contains class `AppSettingsResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appresetdataresponse-5f646cfa|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPRESETDATARESPONSE-5F646CFA]]: `backend/app/api/schemas.py` contains class `AppResetDataResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appmeresponse-b511655d|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPMERESPONSE-B511655D]]: `backend/app/api/schemas.py` contains class `AppMeResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appchathistoryentry-b91ee2ed|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCHATHISTORYENTRY-B91EE2ED]]: `backend/app/api/schemas.py` contains class `AppChatHistoryEntry`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appchathistoryresponse-e727512d|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCHATHISTORYRESPONSE-E727512D]]: `backend/app/api/schemas.py` contains class `AppChatHistoryResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appchatmessageresponse-f194e7e8|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCHATMESSAGERESPONSE-F194E7E8]]: `backend/app/api/schemas.py` contains class `AppChatMessageResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-appconnectorconfirmationresponse-d4b30530|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPCONNECTORCONFIRMATIONRESPONSE-D4B30530]]: `backend/app/api/schemas.py` contains class `AppConnectorConfirmationResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-apppersonalityoverviewresponse-f44719c9|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPPERSONALITYOVERVIEWRESPONSE-F44719C9]]: `backend/app/api/schemas.py` contains class `AppPersonalityOverviewResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-apptoolsoverviewresponse-29eef1bd|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPTOOLSOVERVIEWRESPONSE-29EEF1BD]]: `backend/app/api/schemas.py` contains class `AppToolsOverviewResponse`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-apptoolspreferencespatchrequest-c55e8de0|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPTOOLSPREFERENCESPATCHREQUEST-C55E8DE0]]: `backend/app/api/schemas.py` contains class `AppToolsPreferencesPatchRequest`.
- `parent_of` -> [[pyclass-backend-app-api-schemas-py-apptelegramlinkstartresponse-207960a2|PYCLASS-BACKEND-APP-API-SCHEMAS-PY-APPTELEGRAMLINKSTARTRESPONSE-207960A2]]: `backend/app/api/schemas.py` contains class `AppTelegramLinkStartResponse`.

Incoming: none

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
