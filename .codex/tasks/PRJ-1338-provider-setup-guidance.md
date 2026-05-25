# PRJ-1338 - Provider Setup Guidance

Last updated: 2026-05-25

## Context

The backend-capability-to-final-personality-UI mission is mapping backend-owned
capabilities into truthful, polished web surfaces. After `PRJ-1336` made
Integrations an external-only provider map and `PRJ-1337` improved connector
consent/link-state copy, Tools still needed a safer user-facing bridge from
`/app/tools/overview.next_actions` to setup guidance.

## Goal

Show a compact setup guide on non-integral Tools provider cards when the backend
reports missing provider configuration, link-required state, or next actions,
without adding credential entry, provider execution, or frontend-owned
authority.

## Constraints

- Use `/app/tools/overview` fields as the UI contract.
- Keep secrets, raw env names, raw provider payloads, and execution internals out
  of primary UI.
- Keep detailed setup guidance in Tools; Integrations remains a provider map.
- Preserve desktop, tablet, and mobile route stability.
- Keep connector execution and confirmation authority in the backend action
  layer.

## Definition Of Done

- Tools renders provider setup guides for Telegram, ClickUp, Google Calendar,
  and Google Drive when blocked/link-required.
- Integral tools do not render setup guides.
- Telegram `pending_confirmation` renders as an explicit pending state.
- Friendly setup action copy is used instead of raw env/secret names.
- Build, characterization, and responsive route-smoke proof pass.
- Relevant state, requirement, risk, quality, and module ledgers are updated.

## Forbidden

- Do not expose credential names or token values in user-facing setup copy.
- Do not add provider credential forms.
- Do not make frontend toggles execute provider actions.
- Do not claim a provider is connected when the backend only reports provider
  readiness or pending link confirmation.

## Stage

- Stage: verification
- Output expected from this stage: task packet plus proof-linked source-of-truth
  updates.

## Scope

- `web/src/components/tools.tsx`
- `web/src/lib/tool-formatting.ts`
- `web/src/App.tsx`
- `web/src/index.css`
- `web/scripts/tools-directory-characterization.mjs`
- `web/scripts/route-smoke.mjs`
- project state and quality ledgers

## Implementation Plan

1. Add localized setup-guide labels and pending link-state copy.
2. Map backend next-action IDs to friendly product copy, including Telegram
   pending confirmation and Google provider readiness/configuration variants.
3. Render a three-step setup guide only on non-integral Tools cards that need
   provider setup, user action, or link confirmation.
4. Add responsive CSS for the setup guide.
5. Extend Tools characterization and route-smoke to assert setup guides,
   no env-name leaks, and route stability.

## Acceptance Criteria

- `npm run test:tools-directory` reports `setupGuideCount=4`,
  `integralSetupGuideCount=0`, `hasSetupBoundary=true`, provider setup copy
  present, Telegram pending state present, and `leaksEnvNames=false`.
- Strict route-smoke screenshot gate for `/tools,/integrations` passes across
  desktop, tablet, and mobile with `setupGuideCount=4` on `/tools` and no
  credential-name leaks.
- No backend behavior changes are required.

## Result Report

`PRJ-1338` is verified. Tools now renders backend-derived setup guides for the
four external provider/channel cards that need configuration or link action:
Telegram, ClickUp, Google Calendar, and Google Drive. Each guide separates
provider state, next safe action, and the execution boundary. Integral tools
remain guide-free, and Integrations remains an external provider map rather than
a setup flow.

## Validation

- `node --check scripts\tools-directory-characterization.mjs` in `web/` -> PASS
- `node --check scripts\route-smoke.mjs` in `web/` -> PASS
- `npm run build` in `web/` -> PASS
- `CHROME_PATH=C:\Program Files\Microsoft\Edge\Application\msedge.exe npm run test:tools-directory` in `web/` -> PASS:
  - `groupCount=4`
  - `itemCount=7`
  - `toggleCount=4`
  - `capabilityChipCount=21`
  - `setupGuideCount=4`
  - `integralSetupGuideCount=0`
  - `technicalDetailsCount=7`
  - `hasSetupBoundary=true`
  - `hasClickUpSetup=true`
  - `hasCalendarSetup=true`
  - `hasDriveSetup=true`
  - `leaksEnvNames=false`
  - `telegram_link_pending.hasPendingCopy=true`
  - `telegram_link_pending.hasPendingState=true`
  - `telegram_link_pending.hasNoCodeFallback=false`
- Strict route-smoke screenshot/account gate in `web/` -> PASS:
  - report: `.codex/artifacts/prj1338-provider-setup-guidance/report.json`
  - screenshots: `.codex/artifacts/prj1338-provider-setup-guidance/screenshots/*.png`
  - `route_count=14`
  - `status=ok`
  - `screenshot_count=6`
  - `failed_count=0`
  - `/tools` desktop/tablet/mobile `setupGuideCount=4`
  - `/tools` desktop/tablet/mobile `leakedCredentialNames=false`
  - account proof `panel_visible=true`

## Residual Risk

- Live provider credential activation remains deferred until credentials and
  operator acceptance are in scope.
- Provider setup guidance is informational only; credential entry and mutation
  execution remain backend/ops concerns.
- Default Chrome CDP characterization on this Windows machine can occasionally
  time out on `Page.enable`; Edge via `CHROME_PATH` was used for the successful
  local characterization rerun.
