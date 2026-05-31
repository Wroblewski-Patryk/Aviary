# Task Synchronization Report

Generated: 2026-05-31T10:24:35.780Z

## Contract

Every task should identify the feature/module it changes, dependency expectations, affected files, test requirements, docs requirements, and proof links.

## Signals

- Tasks without architecture links: 0
- Implementation entities without task links: 701
- Verified entities without proof evidence: 0

## Tasks Without Architecture Links


## Implementation Without Task Links

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
- feature: check_coolify_fallback_readiness.py (backend/scripts/check_coolify_fallback_readiness.py)
- feature: check_production_revision_parity.py (backend/scripts/check_production_revision_parity.py)
- feature: check_web_api_openapi_sync.py (backend/scripts/check_web_api_openapi_sync.py)
- feature: export_data_model_reference.py (backend/scripts/export_data_model_reference.py)
- feature: export_incident_evidence_bundle.py (backend/scripts/export_incident_evidence_bundle.py)
- feature: generate_architecture_graph.py (backend/scripts/generate_architecture_graph.py)
- feature: generate_architecture_inventory.py (backend/scripts/generate_architecture_inventory.py)
- feature: generate_project_status_dashboard.py (backend/scripts/generate_project_status_dashboard.py)
- feature: query_architecture_graph.py (backend/scripts/query_architecture_graph.py)
- feature: report_architecture_coverage.py (backend/scripts/report_architecture_coverage.py)
- feature: run_ai_red_team_scenarios.py (backend/scripts/run_ai_red_team_scenarios.py)
- feature: run_architecture_graph_hosted_proof_intake.py (backend/scripts/run_architecture_graph_hosted_proof_intake.py)
- feature: run_architecture_graph_local_release_gate.py (backend/scripts/run_architecture_graph_local_release_gate.py)
- feature: run_behavior_validation.py (backend/scripts/run_behavior_validation.py)
- feature: run_communication_boundary_backfill_once.py (backend/scripts/run_communication_boundary_backfill_once.py)
- feature: run_coolify_deploy_watchdog.py (backend/scripts/run_coolify_deploy_watchdog.py)
- feature: run_maintenance_tick_once.py (backend/scripts/run_maintenance_tick_once.py)
- feature: run_nonprod_entry_health_smoke.py (backend/scripts/run_nonprod_entry_health_smoke.py)
- feature: run_proactive_tick_once.py (backend/scripts/run_proactive_tick_once.py)
- feature: run_reflection_queue_once.py (backend/scripts/run_reflection_queue_once.py)
- feature: run_release_go_no_go.py (backend/scripts/run_release_go_no_go.py)
- feature: run_user_data_cleanup.py (backend/scripts/run_user_data_cleanup.py)
- feature: sync_release_evidence_index_from_latest_summary.py (backend/scripts/sync_release_evidence_index_from_latest_summary.py)
- feature: trigger_coolify_deploy_webhook.py (backend/scripts/trigger_coolify_deploy_webhook.py)
- feature: verify_architecture_gap_artifact.py (backend/scripts/verify_architecture_gap_artifact.py)
- feature: main.js (docs/.obsidian/plugins/dataview/main.js)
- feature: main.js (docs/.obsidian/plugins/note-toolbar/main.js)
- feature: main.js (docs/.obsidian/plugins/obsidian-excalidraw-plugin/main.js)
- feature: main.js (docs/.obsidian/plugins/obsidian-git/main.js)
- feature: main.js (docs/.obsidian/plugins/obsidian-tasks-plugin/main.js)
- feature: main.js (docs/.obsidian/plugins/omnisearch/main.js)
- feature: main.js (docs/.obsidian/plugins/table-editor-obsidian/main.js)
- feature: main.js (docs/.obsidian/plugins/templater-obsidian/main.js)
- feature: entry-cbd0d4352ad3efd1c5b4821730cc408d.js (mobile/.expo-web-export/_expo/static/js/web/entry-cbd0d4352ad3efd1c5b4821730cc408d.js)
- feature: expo-env.d.ts (mobile/expo-env.d.ts)
- feature: mobile-device-proof-doctor.mjs (mobile/scripts/mobile-device-proof-doctor.mjs)
- feature: mobile-preview-smoke.mjs (mobile/scripts/mobile-preview-smoke.mjs)
- feature: mobile-ui-audit.mjs (mobile/scripts/mobile-ui-audit.mjs)
- feature: serve-mobile-preview.mjs (mobile/scripts/serve-mobile-preview.mjs)
- feature: theme.ts (mobile/src/theme.ts)