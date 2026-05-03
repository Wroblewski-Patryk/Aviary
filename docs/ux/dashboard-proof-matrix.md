# Dashboard Proof Matrix

Last updated: 2026-05-03

This matrix records the current dashboard proof state for the authenticated
web shell. It is a verification map, not a visual redesign brief.

## Scope

- Surface: authenticated `/dashboard`
- Client: `web/`
- Source route: `web/src/App.tsx`
- Source styling: `web/src/index.css`
- Design sources:
  - `docs/ux/aion-visual-motif-system.md`
  - `docs/ux/canonical-web-screen-reference-set.md`
  - `docs/planning/dashboard-foundation-and-personality-visual-system-plan.md`
  - `docs/ux/screen-quality-checklist.md`

## Proof Status

| Area | Current Status | Evidence | Remaining Gap |
| --- | --- | --- | --- |
| Desktop visual proof | VERIFIED | `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-after-1568x1003-v3.png`; `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-desktop-1568x1003.png` | None known for local proof. Deployed parity can still be refreshed after deployment changes. |
| Mobile visual proof | VERIFIED | `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-mobile-after-390x844-v2.png`; `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-mobile-390x844.png` | None known for 390px smoke proof. |
| Tablet visual proof | PARTIAL | Earlier shell work records tablet posture and proof in `.codex/artifacts/prj705-responsive-proof/`; later dashboard-specific artifact search found desktop/mobile dashboard proof, not a dashboard-specific tablet screenshot. | GAP: capture a dashboard-specific tablet screenshot when the next UI proof pass runs. |
| Loading state | VERIFIED | Task-board history records dashboard-local status band styling for live, quiet, failure, loading, and unavailable states; later route smokes passed build and nonblank checks. | GAP: keep a named screenshot artifact for dashboard loading state if the state is visually changed. |
| Empty state | PARTIAL | Later state-system work records product-facing empty-state posture across the shell; dashboard summary smokes removed fake data claims. | GAP: capture dashboard-specific empty-state screenshot with a minimal mocked overview payload. |
| Error/unavailable state | VERIFIED | Task-board history records backend-down `/dashboard` mobile smoke without raw technical leakage or horizontal overflow. | GAP: add a named desktop error screenshot if error presentation changes. |
| Success/live state | VERIFIED | Dashboard canonical screenshots and route smokes cover the normal authenticated success state. | None known for local proof. |
| Pointer interaction | VERIFIED | Desktop route smokes and canonical screenshot passes exercised the pointer-oriented shell layout and route rendering. | GAP: explicit hover/focus-state screenshot is not recorded. |
| Touch interaction | PARTIAL | Mobile dashboard screenshot and route smoke cover 390px layout and overflow behavior. | GAP: no explicit touch-target audit artifact is recorded. |
| Keyboard interaction | PARTIAL | Shell navigation is semantic enough for normal browser focus flow, but the current evidence set does not include a named keyboard traversal log for dashboard. | GAP: add dashboard keyboard traversal evidence in the next proof pass. |
| Horizontal overflow | VERIFIED | Later route smokes record no horizontal overflow at 390px, including authenticated route and backend-down dashboard checks. | None known for 390px proof. |
| Accessibility posture | PARTIAL | The screen-quality checklist is in force and later route smokes check blankness, overflow, and exceptions. | GAP: no dashboard-specific contrast/reduced-motion/keyboard artifact is currently named. |

## Evidence Registry

- `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-desktop-after-1568x1003-v3.png`
- `.codex/artifacts/prj870-dashboard-99-canonical-evidence-pass/dashboard-mobile-after-390x844-v2.png`
- `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-desktop-1568x1003.png`
- `.codex/artifacts/prj875-canonical-ui-final-route-sweep/dashboard-mobile-390x844.png`
- `.codex/artifacts/prj864-dashboard-canonical-pass/dashboard-desktop-1568x1003-v2.png`
- `.codex/artifacts/prj864-dashboard-canonical-pass/dashboard-mobile-390x844-v2.png`
- `.codex/artifacts/prj705-responsive-proof/`

## Required Future Proof Pack

When dashboard visual behavior changes again, capture this minimum pack before
calling the dashboard baseline accepted:

- desktop success screenshot
- tablet success screenshot
- mobile success screenshot
- loading screenshot or deterministic mocked-state artifact
- empty screenshot or deterministic mocked-state artifact
- error/unavailable screenshot
- keyboard traversal note or log
- touch-target and horizontal-overflow note for mobile
- contrast and reduced-motion review note when colors, animation, or decorative
  assets change

## Acceptance Boundary

The dashboard is usable as the current authenticated web baseline, with local
desktop and mobile proof already recorded. It is not yet fully proven as a
complete cross-state/cross-input future-client baseline until the `PARTIAL`
rows above are closed with named evidence.
