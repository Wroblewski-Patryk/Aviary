# Architecture Awareness Report

Generated: 2026-05-29T21:49:36.836Z
Project: Aviary
Root: C:/Personal/Projekty/Aplikacje/Aviary

## Counts By Type

| Type | Count |
| --- | ---: |
| agent | 52 |
| api_endpoint | 20 |
| component | 16 |
| document | 11343 |
| feature | 55 |
| function | 830 |
| migration | 27 |
| model | 298 |
| module | 21 |
| project | 1 |
| route | 130 |
| test | 59 |

## Counts By Status

| Status | Count |
| --- | ---: |
| blocked | 1 |
| deprecated | 3 |
| implemented | 12788 |
| in_progress | 1 |
| tested | 59 |

## Health Signals

- Implementation entities without inferred tests: 921
- Implementation entities without inferred docs: 519
- Entities without owner attribution: 0
- Disconnected entities: 0

## Top Missing Test Links

- api_endpoint: POST /app/auth/login (backend/app/api/routes.py#/app/auth/login)
- api_endpoint: POST /app/auth/logout (backend/app/api/routes.py#/app/auth/logout)
- api_endpoint: POST /app/auth/register (backend/app/api/routes.py#/app/auth/register)
- api_endpoint: GET /app/chat/history (backend/app/api/routes.py#/app/chat/history)
- api_endpoint: POST /app/chat/message (backend/app/api/routes.py#/app/chat/message)
- api_endpoint: POST /app/connectors/confirm (backend/app/api/routes.py#/app/connectors/confirm)
- api_endpoint: GET /app/me (backend/app/api/routes.py#/app/me)
- api_endpoint: POST /app/me/reset-data (backend/app/api/routes.py#/app/me/reset-data)
- api_endpoint: PATCH /app/me/settings (backend/app/api/routes.py#/app/me/settings)
- api_endpoint: GET /app/personality/overview (backend/app/api/routes.py#/app/personality/overview)
- api_endpoint: GET /app/tools/overview (backend/app/api/routes.py#/app/tools/overview)
- api_endpoint: PATCH /app/tools/preferences (backend/app/api/routes.py#/app/tools/preferences)
- api_endpoint: POST /app/tools/telegram/link/start (backend/app/api/routes.py#/app/tools/telegram/link/start)
- api_endpoint: POST /event (backend/app/api/routes.py#/event)
- api_endpoint: POST /event/debug (backend/app/api/routes.py#/event/debug)
- api_endpoint: GET /health (backend/app/api/routes.py#/health)
- api_endpoint: GET /internal/state/inspect (backend/app/api/routes.py#/internal/state/inspect)
- api_endpoint: POST /telegram/set-webhook (backend/app/api/routes.py#/telegram/set-webhook)
- api_endpoint: GET / (backend/app/main.py#/)
- api_endpoint: GET /{frontend_path:path} (backend/app/main.py#/{frontend_path:path})
- component: chat-screen.tsx (mobile/src/ui/chat-screen.tsx)
- component: home-screen.tsx (mobile/src/ui/home-screen.tsx)
- component: personality-screen.tsx (mobile/src/ui/personality-screen.tsx)
- component: primitives.tsx (mobile/src/ui/primitives.tsx)
- component: settings-screen.tsx (mobile/src/ui/settings-screen.tsx)
- component: tools-screen.tsx (mobile/src/ui/tools-screen.tsx)
- component: App.tsx (web/src/App.tsx)
- component: app-icons.tsx (web/src/components/app-icons.tsx)
- component: chat.tsx (web/src/components/chat.tsx)
- component: dashboard.tsx (web/src/components/dashboard.tsx)
- component: personality.tsx (web/src/components/personality.tsx)
- component: public-shell.tsx (web/src/components/public-shell.tsx)
- component: settings.tsx (web/src/components/settings.tsx)
- component: shared.tsx (web/src/components/shared.tsx)
- component: shell.tsx (web/src/components/shell.tsx)
- component: tools.tsx (web/src/components/tools.tsx)
- feature: audit_architecture_implementation_map.py (backend/scripts/audit_architecture_implementation_map.py)
- feature: audit_release_reality.py (backend/scripts/audit_release_reality.py)
- feature: build_architecture_awareness_pack.py (backend/scripts/build_architecture_awareness_pack.py)
- feature: build_architecture_graph_hosted_evidence_packet.py (backend/scripts/build_architecture_graph_hosted_evidence_packet.py)

## Top Missing Doc Links

- api_endpoint: POST /app/auth/login (backend/app/api/routes.py#/app/auth/login)
- api_endpoint: POST /app/auth/logout (backend/app/api/routes.py#/app/auth/logout)
- api_endpoint: POST /app/auth/register (backend/app/api/routes.py#/app/auth/register)
- api_endpoint: GET /app/chat/history (backend/app/api/routes.py#/app/chat/history)
- api_endpoint: POST /app/chat/message (backend/app/api/routes.py#/app/chat/message)
- api_endpoint: POST /app/connectors/confirm (backend/app/api/routes.py#/app/connectors/confirm)
- api_endpoint: GET /app/me (backend/app/api/routes.py#/app/me)
- api_endpoint: POST /app/me/reset-data (backend/app/api/routes.py#/app/me/reset-data)
- api_endpoint: PATCH /app/me/settings (backend/app/api/routes.py#/app/me/settings)
- api_endpoint: GET /app/personality/overview (backend/app/api/routes.py#/app/personality/overview)
- api_endpoint: GET /app/tools/overview (backend/app/api/routes.py#/app/tools/overview)
- api_endpoint: PATCH /app/tools/preferences (backend/app/api/routes.py#/app/tools/preferences)
- api_endpoint: POST /app/tools/telegram/link/start (backend/app/api/routes.py#/app/tools/telegram/link/start)
- api_endpoint: POST /event (backend/app/api/routes.py#/event)
- api_endpoint: POST /event/debug (backend/app/api/routes.py#/event/debug)
- api_endpoint: GET /health (backend/app/api/routes.py#/health)
- api_endpoint: GET /internal/state/inspect (backend/app/api/routes.py#/internal/state/inspect)
- api_endpoint: POST /telegram/set-webhook (backend/app/api/routes.py#/telegram/set-webhook)
- api_endpoint: GET / (backend/app/main.py#/)
- api_endpoint: GET /{frontend_path:path} (backend/app/main.py#/{frontend_path:path})
- component: chat-screen.tsx (mobile/src/ui/chat-screen.tsx)
- component: home-screen.tsx (mobile/src/ui/home-screen.tsx)
- component: personality-screen.tsx (mobile/src/ui/personality-screen.tsx)
- component: primitives.tsx (mobile/src/ui/primitives.tsx)
- component: settings-screen.tsx (mobile/src/ui/settings-screen.tsx)
- component: tools-screen.tsx (mobile/src/ui/tools-screen.tsx)
- component: App.tsx (web/src/App.tsx)
- component: app-icons.tsx (web/src/components/app-icons.tsx)
- component: chat.tsx (web/src/components/chat.tsx)
- component: dashboard.tsx (web/src/components/dashboard.tsx)
- component: personality.tsx (web/src/components/personality.tsx)
- component: public-shell.tsx (web/src/components/public-shell.tsx)
- component: settings.tsx (web/src/components/settings.tsx)
- component: shared.tsx (web/src/components/shared.tsx)
- component: shell.tsx (web/src/components/shell.tsx)
- component: tools.tsx (web/src/components/tools.tsx)
- feature: audit_architecture_implementation_map.py (backend/scripts/audit_architecture_implementation_map.py)
- feature: audit_release_reality.py (backend/scripts/audit_release_reality.py)
- feature: build_architecture_awareness_pack.py (backend/scripts/build_architecture_awareness_pack.py)
- feature: build_architecture_graph_hosted_evidence_packet.py (backend/scripts/build_architecture_graph_hosted_evidence_packet.py)

## Notes

- This is an inferred baseline. CTO/Docs Memory must promote or correct important relations.
- Override input: `C:/Personal/Projekty/Aplikacje/Aviary/docs/architecture/scanner-overrides.json` (entity entries: 0, relation entries: 0).
- Override summary: excluded files 0, entity overrides 0, relation overrides 0, critical entities tagged 0.
- `verified` still requires fresh command/browser/deploy evidence, not only file presence.