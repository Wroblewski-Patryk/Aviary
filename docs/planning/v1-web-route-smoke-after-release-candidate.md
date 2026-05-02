# V1 Web Route Smoke After Release Candidate

Last updated: 2026-05-03

## Status

`PRJ-913` is DONE.

The local web-v1 route smoke passed after a narrow `/tools` mobile overflow
fix.

## Evidence

Validation commands and results:

- `Push-Location .\web; npm run build; Pop-Location`
  - passed
- bundled Node + Playwright route smoke against local Vite and local backend:
  - `routeChecks=24`
  - `failures=0`
  - `unexpectedConsoleIssueCount=0`
  - `benignConsoleIssueCount=2`
  - `screenshots=8`
- `git diff --check`
  - passed

The two benign console issues were expected unauthenticated `401` responses
from `/app/me` while checking `/login` before local registration.

## Route Coverage

Unauthenticated route:

- `/login`

Authenticated routes checked on desktop and mobile:

- `/dashboard`
- `/chat`
- `/personality`
- `/settings`
- `/tools`
- `/memory`
- `/reflections`
- `/plans`
- `/goals`
- `/insights`
- `/automations`
- `/integrations`

## Fix Shipped

The smoke found a real mobile overflow on `/tools`.

The fix in `web/src/index.css`:

- constrains the Tools canvas and overview bar with `min-width: 0` and
  explicit one-column grid sizing
- allows summary labels and technical detail pills to wrap long text
- clips root horizontal overflow so the intentionally scrollable mobile tabbar
  does not create page-level horizontal scroll

## Evidence Artifacts

Local, uncommitted artifacts:

- `.codex/artifacts/prj913-web-v1-route-smoke/route-smoke-results.json`
- `.codex/artifacts/prj913-web-v1-route-smoke/login-desktop.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/dashboard-desktop.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/chat-desktop.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/personality-desktop.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/dashboard-mobile.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/chat-mobile.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/tools-mobile.png`
- `.codex/artifacts/prj913-web-v1-route-smoke/integrations-mobile.png`

## Notes

The in-app browser plugin path was attempted first, but local `node_repl`
resolved Node `22.13.0` while the plugin requires at least `22.22.0`. The smoke
therefore used the documented bundled Node + Playwright fallback.

This is local route evidence. Production route evidence still requires a fresh
deploy parity smoke after the commit is pushed and deployed.
