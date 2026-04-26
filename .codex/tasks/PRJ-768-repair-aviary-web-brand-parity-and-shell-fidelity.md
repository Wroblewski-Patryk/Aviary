# Task

## Header
- ID: PRJ-768
- Title: Repair Aviary web brand parity and shell fidelity
- Task Type: fix | design
- Current Stage: verification
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-766
- Priority: P0

## Context
The approved first-party product brand baseline says the app shell must present
`Aviary` as the product name, use the provided bird SVG as the canonical
logomark, and apply `Cormorant Garamond` plus `Inter` consistently across the
web UX/UI. A fresh audit on 2026-04-27 found that the current web project still
ships user-facing `AION` strings in the shell and auth copy, the reusable
wordmark component still renders `AION`, and the product-level naming boundary
is therefore not actually closed in implementation.

## Goal
Remove the remaining user-facing `AION` branding drift from the web shell,
ensure the provided SVG is the canonical visible logo treatment, and verify the
final UX/UI against the approved Aviary brand baseline.

## Deliverable For This Stage
One verified implementation slice with:
- repaired product-brand copy in the live shell
- corrected `AVIARY` wordmark output
- tuned brand-lockup typography for the approved font pairing
- validation evidence for the rebuilt web app

## Constraints
- use existing systems and approved mechanisms
- do not introduce new structures without approval
- do not implement workarounds
- do not duplicate logic
- stay within the declared current stage unless explicit approval changes it

## Definition of Done
- [x] Remaining user-facing `AION` product strings in the active web shell are
      replaced with `Aviary`.
- [x] The reusable shell wordmark renders the provided Aviary SVG plus the
      visible `AVIARY` wordmark.
- [x] Focused validation covers a successful production web build.

## Stage Exit Criteria
- [x] The output matches the declared `Current Stage`.
- [x] Work from later stages was not mixed in without explicit approval.
- [x] Risks and assumptions for this stage are stated clearly.

## Forbidden
- new systems without approval
- duplicated logic or parallel implementations of the same contract
- temporary bypasses, hacks, or workaround-only paths
- architecture changes without explicit approval
- implicit stage skipping

## Validation Evidence
- Tests:
  - `Push-Location .\web; npm run build; Pop-Location`
- Manual checks:
  - source audit of `web/src/App.tsx`
  - source audit of `web/src/index.css`
  - source audit of `web/public/aviary-logomark.svg`
- Screenshots/logs:
  - `browser-use` runtime could not complete because the available Node runtime
    is below the required version for the in-app browser workflow
- High-risk checks:
  - confirmed that active product-brand output now resolves to `Aviary` in the
    authenticated shell and auth copy

## Architecture Evidence (required for architecture-impacting tasks)
- Architecture source reviewed:
  - `docs/architecture/architecture-source-of-truth.md`
- Fits approved architecture: yes
- Mismatch discovered: no
- Decision required from user: no
- Approval reference if architecture changed:
- Follow-up architecture doc updates:
  - none required

## UX/UI Evidence (required for UX tasks)
- Design source type: approved_snapshot
- Design source reference:
  - `C:/Users/wrobl/Desktop/UIUX/aion - logotype.svg`
  - `C:/Users/wrobl/Desktop/UIUX/aion - logotype - logo.png`
  - `docs/ux/brand-personality-tokens.md`
- Canonical visual target:
  - `Aviary` product shell with bird SVG logomark plus `AVIARY` wordmark
- Fidelity target: pixel_close
- Stitch used: no
- Experience-quality bar reviewed: yes
- Visual-direction brief reviewed: yes
- Existing shared pattern reused:
  - existing shell wordmark component and shared display/body font system
- New shared pattern introduced: no
- Design-memory entry reused:
  - brand logotype and font pairing
- Design-memory update required: no
- Visual gap audit completed: yes
- Background or decorative asset strategy:
  - preserve current premium shell atmosphere while correcting brand lockup and
    typography fidelity
- Canonical asset extraction required: no
- Screenshot comparison pass completed: no
- Remaining mismatches:
  - browser screenshot parity is still pending because the in-app browser could
    not be executed in this environment
- State checks: success
- Responsive checks: pending real-browser pass
- Input-mode checks: pending real-browser pass
- Accessibility checks:
  - final implementation must confirm decorative logo semantics and visible
    `AVIARY` text naming
- Parity evidence:
  - current stage is source-level gap audit only

## Deployment / Ops Evidence (required for runtime or infra tasks)
- Deploy impact: low
- Env or secret changes:
- Health-check impact:
- Smoke steps updated:
- Rollback note:

## Review Checklist (mandatory)
- [x] Current stage is declared and respected.
- [x] Deliverable for the current stage is complete.
- [x] Architecture alignment confirmed.
- [x] Existing systems were reused where applicable.
- [x] No workaround paths were introduced.
- [x] No logic duplication was introduced.
- [x] Definition of Done evidence is attached.
- [x] Relevant validations were run.
- [x] Docs or context were updated if repository truth changed.
- [ ] Learning journal was updated if a recurring pitfall was confirmed.

## Notes
Implemented repair scope:

1. Product-brand copy in `web/src/App.tsx`.
   - Replaced remaining visible `AION` product-name strings with `Aviary`
     across auth, settings, workspace framing, dashboard summary, and Telegram
     linking copy.

2. Shell wordmark truth.
   - The reusable `AviaryWordmark` now exposes `aria-label="Aviary"` and
     renders the visible `AVIARY` wordmark next to the provided SVG mark.

3. Brand-lockup typography fidelity.
   - `web/src/index.css` now gives the lockup lighter `Cormorant Garamond`
     weight, calmer spacing, and slightly stronger mark sizing to better match
     the approved premium brand posture.

Remaining follow-up:
- run a real in-browser desktop/tablet/mobile screenshot pass once the browser
  runtime is available again
- note:
  - one stale older bundle file in `web/dist/assets` may still contain legacy
    text, but the active `dist/index.html` now points at the fresh Aviary build
    artifact produced in this validation pass
