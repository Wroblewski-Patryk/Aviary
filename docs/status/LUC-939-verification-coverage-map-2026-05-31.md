# LUC-939 Verification Coverage Map for High-Risk Untested Entities

Date: 2026-05-31
Issue: LUC-939
Owner lane: QA Regression Lead
Scope: Evidence mapping only (no implementation/deploy mutation)

## Source Evidence

- `docs/status/architecture-awareness-report.md` (generated 2026-05-29T21:49:36.836Z)
- `docs/graphs/architecture-awareness.json` (timestamp 2026-05-29 21:49:50 UTC)
- `docs/status/LUC-935-known-state-baseline-2026-05-31.md`

Status rubric: `implemented and verified`, `implemented but not verified`, `present in code, behavior unknown`, `missing`, `blocked by error`.

## Prioritized Verification Backlog

| Priority | Entity | Layer | Why high-risk | Current evidence status | Smallest proof | Owner lane |
| --- | --- | --- | --- | --- | --- | --- |
| P0 | `POST /app/auth/login`, `POST /app/auth/register`, `POST /app/auth/logout` | backend api | Entry auth boundary; regressions break all authenticated workflows | present in code, behavior unknown | API integration tests for success/failure/invalid token/logout idempotency | Backend QA |
| P0 | `GET /app/me`, `PATCH /app/me/settings`, `POST /app/me/reset-data` | backend api + data | User profile and destructive reset path; data-loss/security risk | present in code, behavior unknown | API tests + guarded smoke with AI test account confirming reset scope | Backend QA + Security |
| P0 | `POST /app/chat/message`, `GET /app/chat/history` | backend api + runtime | Core product workflow; state continuity and history correctness risk | present in code, behavior unknown | End-to-end API test with deterministic fixture conversation and history assertions | Backend QA |
| P1 | `POST /app/connectors/confirm`, `POST /app/tools/telegram/link/start`, `POST /telegram/set-webhook` | integrations | External integration paths fail silently without coverage; high support cost | present in code, behavior unknown | Contract tests with mocked provider callbacks/webhook payloads | Integrations QA |
| P1 | `PATCH /app/tools/preferences`, `GET /app/tools/overview`, `GET /app/personality/overview` | backend api + domain | User-facing configuration/overview correctness drives trust | present in code, behavior unknown | API tests asserting schema + persisted preference round-trip | Backend QA |
| P1 | `web/src/components/chat.tsx`, `dashboard.tsx`, `personality.tsx`, `settings.tsx`, `tools.tsx`, `shell.tsx` | web ui | Main authenticated UI surfaces have no linked tests | present in code, behavior unknown | Component smoke (render + primary action path) via vitest/react-testing-library | Frontend QA |
| P1 | `mobile/src/ui/chat-screen.tsx`, `home-screen.tsx`, `personality-screen.tsx`, `settings-screen.tsx`, `tools-screen.tsx` | mobile ui | Mobile parity risk against web and API behavior | present in code, behavior unknown | Navigation and render smoke in mobile test harness with mocked API | Mobile QA |
| P2 | `GET /health`, `GET /internal/state/inspect`, `POST /event`, `POST /event/debug` | ops/internal | Release and diagnostics observability paths not verified | present in code, behavior unknown | Non-prod smoke hitting health/internal endpoints with expected status/auth checks | QA + Ops |
| P2 | `GET /`, `GET /{frontend_path:path}`, `web/src/components/public-shell.tsx` | web public shell | Public entry and SPA fallback can regress deploy availability | present in code, behavior unknown | Release-smoke HTTP assertions for static shell and fallback route | QA + Ops |
| P3 | Architecture tooling scripts in report (`backend/scripts/*.py`) | tooling | Impacts evidence quality more than runtime behavior | present in code, behavior unknown | Script smoke run with output-file existence + non-empty checks | Docs/Architecture QA |

## Child-Issue-Ready Breakdown

1. **Auth and account-critical API verification (P0)**
- Owner: Backend QA (+ Security review for reset-data safeguards)
- Scope: auth + account endpoints listed in P0
- Proof contract: API integration tests and AI test-account smoke evidence

2. **Core chat workflow verification (P0)**
- Owner: Backend QA
- Scope: `/app/chat/message`, `/app/chat/history`
- Proof contract: deterministic message/history assertions and regression test artifacts

3. **Integration endpoint contract coverage (P1)**
- Owner: Integrations QA
- Scope: connector confirm + Telegram link/webhook paths
- Proof contract: mocked callback/webhook contract tests

4. **Web UI critical surface smoke suite (P1)**
- Owner: Frontend QA
- Scope: chat/dashboard/personality/settings/tools/shell components
- Proof contract: render+interaction smoke tests tied to architecture entities

5. **Mobile UI critical surface smoke suite (P1)**
- Owner: Mobile QA
- Scope: chat/home/personality/settings/tools screens
- Proof contract: navigation+render smoke with mocked backend responses

6. **Ops/public-entry endpoint smoke guard (P2)**
- Owner: QA + Ops
- Scope: health/internal/event/public shell routes
- Proof contract: non-prod smoke script and expected HTTP/auth behavior evidence

## Coverage-Map Disposition

- Mapping deliverable for LUC-939: `implemented and verified` (evidence table + owner-lane backlog complete).
- Implementation/testing execution for mapped items: `implemented but not verified` (follow-up child lanes required).
