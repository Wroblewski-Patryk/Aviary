---
id: "FILE-WEB-SRC-LIB-API-TS-19A6B5EA"
name: "api.ts"
type: "frontend_file"
status: "implemented"
layer: "frontend"
module: "web"
feature: "web_shell"
risk_level: "low"
completion_percent: "70"
last_verified_at: "2026-05-24"
verification_status: "implementation_evidence"
file_path: "web/src/lib/api.ts"
related_files: []
tags: ["auto", "frontend"]
---

# api.ts

ID: `FILE-WEB-SRC-LIB-API-TS-19A6B5EA`

## Summary

Repository file `web/src/lib/api.ts` auto-discovered for architecture graph inventory.

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
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apierror-919a4c60|TSFUNC-WEB-SRC-LIB-API-TS-APIERROR-919A4C60]]: `web/src/lib/api.ts` contains symbol `ApiError`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appauthuser-9eb67275|TSFUNC-WEB-SRC-LIB-API-TS-APPAUTHUSER-9EB67275]]: `web/src/lib/api.ts` contains symbol `AppAuthUser`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appsettings-84b68c13|TSFUNC-WEB-SRC-LIB-API-TS-APPSETTINGS-84B68C13]]: `web/src/lib/api.ts` contains symbol `AppSettings`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appmeresponse-e997ba33|TSFUNC-WEB-SRC-LIB-API-TS-APPMERESPONSE-E997BA33]]: `web/src/lib/api.ts` contains symbol `AppMeResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appresetdataresponse-d81291cb|TSFUNC-WEB-SRC-LIB-API-TS-APPRESETDATARESPONSE-D81291CB]]: `web/src/lib/api.ts` contains symbol `AppResetDataResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appchathistoryentry-7a4a6532|TSFUNC-WEB-SRC-LIB-API-TS-APPCHATHISTORYENTRY-7A4A6532]]: `web/src/lib/api.ts` contains symbol `AppChatHistoryEntry`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appchathistoryresponse-c42525db|TSFUNC-WEB-SRC-LIB-API-TS-APPCHATHISTORYRESPONSE-C42525DB]]: `web/src/lib/api.ts` contains symbol `AppChatHistoryResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appchatmessageresponse-9a0ed2ce|TSFUNC-WEB-SRC-LIB-API-TS-APPCHATMESSAGERESPONSE-9A0ED2CE]]: `web/src/lib/api.ts` contains symbol `AppChatMessageResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apppendingconnectorconfirmation-4934a09b|TSFUNC-WEB-SRC-LIB-API-TS-APPPENDINGCONNECTORCONFIRMATION-4934A09B]]: `web/src/lib/api.ts` contains symbol `AppPendingConnectorConfirmation`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appconnectorconfirmationresponse-368feebe|TSFUNC-WEB-SRC-LIB-API-TS-APPCONNECTORCONFIRMATIONRESPONSE-368FEEBE]]: `web/src/lib/api.ts` contains symbol `AppConnectorConfirmationResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apprecentactivityitem-59cd952d|TSFUNC-WEB-SRC-LIB-API-TS-APPRECENTACTIVITYITEM-59CD952D]]: `web/src/lib/api.ts` contains symbol `AppRecentActivityItem`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apppendingproposalsnapshot-6e60bace|TSFUNC-WEB-SRC-LIB-API-TS-APPPENDINGPROPOSALSNAPSHOT-6E60BACE]]: `web/src/lib/api.ts` contains symbol `AppPendingProposalSnapshot`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apppersonalityoverviewresponse-74f3886c|TSFUNC-WEB-SRC-LIB-API-TS-APPPERSONALITYOVERVIEWRESPONSE-74F3886C]]: `web/src/lib/api.ts` contains symbol `AppPersonalityOverviewResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptoolprovider-fc8eec90|TSFUNC-WEB-SRC-LIB-API-TS-APPTOOLPROVIDER-FC8EEC90]]: `web/src/lib/api.ts` contains symbol `AppToolProvider`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptoolusercontrol-a6e440ef|TSFUNC-WEB-SRC-LIB-API-TS-APPTOOLUSERCONTROL-A6E440EF]]: `web/src/lib/api.ts` contains symbol `AppToolUserControl`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-appskilltoolbinding-98d2e917|TSFUNC-WEB-SRC-LIB-API-TS-APPSKILLTOOLBINDING-98D2E917]]: `web/src/lib/api.ts` contains symbol `AppSkillToolBinding`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptoolitem-54a0f8fb|TSFUNC-WEB-SRC-LIB-API-TS-APPTOOLITEM-54A0F8FB]]: `web/src/lib/api.ts` contains symbol `AppToolItem`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptoolgroup-81453c09|TSFUNC-WEB-SRC-LIB-API-TS-APPTOOLGROUP-81453C09]]: `web/src/lib/api.ts` contains symbol `AppToolGroup`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptoolsoverviewresponse-78cb8475|TSFUNC-WEB-SRC-LIB-API-TS-APPTOOLSOVERVIEWRESPONSE-78CB8475]]: `web/src/lib/api.ts` contains symbol `AppToolsOverviewResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apptelegramlinkstartresponse-e9ac3c26|TSFUNC-WEB-SRC-LIB-API-TS-APPTELEGRAMLINKSTARTRESPONSE-E9AC3C26]]: `web/src/lib/api.ts` contains symbol `AppTelegramLinkStartResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apphealthtelegramchannel-9b2a3376|TSFUNC-WEB-SRC-LIB-API-TS-APPHEALTHTELEGRAMCHANNEL-9B2A3376]]: `web/src/lib/api.ts` contains symbol `AppHealthTelegramChannel`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-apphealthresponse-f8ff0753|TSFUNC-WEB-SRC-LIB-API-TS-APPHEALTHRESPONSE-F8FF0753]]: `web/src/lib/api.ts` contains symbol `AppHealthResponse`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-jsonbody-58ce556d|TSFUNC-WEB-SRC-LIB-API-TS-JSONBODY-58CE556D]]: `web/src/lib/api.ts` contains symbol `JsonBody`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-parsejsonifpossible-c37fde4c|TSFUNC-WEB-SRC-LIB-API-TS-PARSEJSONIFPOSSIBLE-C37FDE4C]]: `web/src/lib/api.ts` contains symbol `parseJsonIfPossible`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-trimmed-a7f41a49|TSFUNC-WEB-SRC-LIB-API-TS-TRIMMED-A7F41A49]]: `web/src/lib/api.ts` contains symbol `trimmed`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-requestjson-ad67f8cd|TSFUNC-WEB-SRC-LIB-API-TS-REQUESTJSON-AD67F8CD]]: `web/src/lib/api.ts` contains symbol `requestJson`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-response-f8d4309a|TSFUNC-WEB-SRC-LIB-API-TS-RESPONSE-F8D4309A]]: `web/src/lib/api.ts` contains symbol `response`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-text-b63f426d|TSFUNC-WEB-SRC-LIB-API-TS-TEXT-B63F426D]]: `web/src/lib/api.ts` contains symbol `text`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-payload-8eed6b3b|TSFUNC-WEB-SRC-LIB-API-TS-PAYLOAD-8EED6B3B]]: `web/src/lib/api.ts` contains symbol `payload`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-detail-96b6159a|TSFUNC-WEB-SRC-LIB-API-TS-DETAIL-96B6159A]]: `web/src/lib/api.ts` contains symbol `detail`.
- `parent_of` -> [[tsfunc-web-src-lib-api-ts-api-559ad4b5|TSFUNC-WEB-SRC-LIB-API-TS-API-559AD4B5]]: `web/src/lib/api.ts` contains symbol `api`.

Incoming:
- [[file-architecture-api-md-de44016d|FILE-ARCHITECTURE-API-MD-DE44016D]] -> `documents`: Doc `architecture/api.md` appears to document `FILE-WEB-SRC-LIB-API-TS-19A6B5EA`.
- [[file-web-src-app-tsx-32c2b18b|FILE-WEB-SRC-APP-TSX-32C2B18B]] -> `depends_on`: `web/src/App.tsx` imports `./lib/api`.
- [[file-web-src-lib-chat-transcript-ts-53433054|FILE-WEB-SRC-LIB-CHAT-TRANSCRIPT-TS-53433054]] -> `depends_on`: `web/src/lib/chat-transcript.ts` imports `./api`.

## Chains

- none

## Evidence

- missing

## Theory Claims

- none

## Notes

Auto-discovered inventory row. Promote to curated registry row when it becomes feature-critical.
