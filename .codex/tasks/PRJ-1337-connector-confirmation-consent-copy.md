# PRJ-1337 Connector Confirmation Consent Copy

## Context

The active mission is `PRJ-1331-backend-capability-to-final-personality-ui`.
The user asked to continue mapping every backend function into a magical,
beautiful, final-feeling UI while coordinating across layers.

Backend review confirmed that connector mutations are confirmation gated
through `POST /app/chat/message` and `POST /app/connectors/confirm`, and
Telegram link setup can enter `link_state: pending_confirmation` after
`POST /app/tools/telegram/link/start`.

## Goal

Make the connector confirmation and Telegram pending-link UI more truthful and
human-readable without changing backend behavior or moving execution authority
into the frontend.

## Constraints

- Preserve backend-owned action execution and confirmation replay boundaries.
- Do not fake connector history; `/app/chat/history` does not expose stored
  pending confirmations.
- Keep Telegram `pending_confirmation` distinct from `linked`.
- Keep copy localized where existing route copy is localized.
- Preserve responsive behavior for `/chat`, `/tools`, and `/integrations`.

## Definition Of Done

- Chat pending confirmation panel renders provider and operation labels as
  user-facing copy instead of raw backend IDs.
- Chat pending confirmation panel keeps the backend reason visible.
- Tools renders Telegram `link_state: pending_confirmation` as a waiting state
  instead of the generic no-code fallback.
- Characterization tests prove pending, submitting, success, error, and
  Telegram pending-link states.
- Responsive route-smoke screenshots for `/chat`, `/tools`, and
  `/integrations` pass on desktop, tablet, and mobile.
- Project source-of-truth state is updated.

## Forbidden

- No backend changes.
- No fake transcript or stored confirmation history.
- No provider credential activation.
- No hidden bypass around confirmation or replay checks.
- No raw provider payloads or env names in primary UI.

## Stage

- Current stage: release
- Stage output: verified frontend slice with task/state records and residual
  risks.

## Implementation Plan

1. Add provider/operation label formatting to the chat pending confirmation
   panel.
2. Surface backend confirmation `reason` in the pending panel.
3. Add localized Tools copy for Telegram pending link confirmation.
4. Teach Tools panel to render `link_state: pending_confirmation` as a waiting
   handoff.
5. Extend characterization fixtures and assertions.
6. Run build, focused characterization tests, responsive route-smoke proof, and
   cleanup checks.

## Acceptance Criteria

- Pending connector action title shows `ClickUp / Update task`, not
  `clickup / update_task`.
- Pending confirmation reason is rendered.
- Browser characterization confirms the raw backend title is not visible.
- Telegram pending link fixture shows waiting copy and does not show
  `No active link code yet`.
- `/chat`, `/tools`, and `/integrations` screenshot gate has zero UI findings.

## Result Report

- Updated `web/src/components/chat.tsx` with connector provider/operation label
  formatting and visible backend reason copy.
- Updated `web/src/index.css` with scoped pending-confirmation reason styling.
- Updated `web/src/components/tools.tsx` and `web/src/App.tsx` so Telegram
  `pending_confirmation` renders as a waiting-for-Telegram state in English,
  Polish, and German copy.
- Updated connector confirmation and Tools characterization scripts to prove
  the refined states.

## Validation

- `node --check scripts\connector-confirmation-render-characterization.mjs` -
  PASS
- `node --check scripts\connector-confirmation-browser-characterization.mjs` -
  PASS
- `node --check scripts\tools-directory-characterization.mjs` - PASS
- `npm run build` - PASS
- `npm run test:connector-confirmation-render` - PASS
- `npm run test:connector-confirmation-browser` - PASS
- `npm run test:tools-directory` - PASS, including `telegram_link_pending`
- `node scripts\route-smoke.mjs --screenshots ..\.codex\artifacts\prj1337-connector-confirmation-consent-copy\screenshots --report ..\.codex\artifacts\prj1337-connector-confirmation-consent-copy\report.json --screenshot-routes /chat,/tools,/integrations --viewports desktop,tablet,mobile --account-proof --fail-on-ui-findings` -
  PASS with `route_count=14`, `status=ok`, `screenshot_count=9`,
  `failed_count=0`, account proof `panel_visible=true`.
- In-app Browser check against `http://127.0.0.1:5174/tools?case=telegram-pending`
  reached the live dev server, showed the unauthenticated login modal, and
  reported no console warnings/errors or framework overlay; authenticated
  contract rendering remains covered by route-smoke and characterization
  harnesses.

## Residual Risk

- Connector confirmation history remains current-turn only in UI because the
  backend history endpoint does not expose pending-confirmation records.
- Provider-specific setup guidance can be made richer in a later Tools or
  Integrations slice.
- Live provider credential activation was not in scope.
