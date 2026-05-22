# Active Mission Packet

Last updated: 2026-05-22

Use this file as the first operational router for `pracuj dalej`, `rob dalej`,
`kontynuuj`, `next`, and similar continuation nudges. Keep it short enough that
a fresh coordinator can choose the next checkpoint without rereading the whole
repository history.

## Current Mission

- Mission ID: PRJ-1232-v12-web-canonical-ui-system
- Status: IN_PROGRESS
- Selected objective: build v1.2 web UI toward the canonical documentation
  references across mobile and desktop, using the web implementation as the
  foundation for the future mobile app. The work must be functional,
  polished, and free of unnecessary decorative or explanatory clutter.
- Why this mission now: v1.1.1 is released; the user explicitly requested v1.2
  frontend improvement with agent coordination, canonical images from docs,
  and all web views supervised across mobile and desktop.
- Release objective or product milestone advanced: v1.2 canonical web UI
  baseline for future native/mobile app transfer.
- First/next checkpoint: continue route-local v1.2 UI polish from the verified
  foundation and public Home batches. Prioritize authenticated shell/sidebar,
  Dashboard density, Chat final pass, Personality final pass, and shared
  module-route consistency.
- Stop conditions: canonical references conflict; a route lacks enough spec to
  claim parity; validation cannot capture desktop/mobile screenshots; broad
  refactor risk exceeds the first batch; production v1.1.1 marker would be
  disturbed.
- Parent validation gate: per batch `npm run build`,
  `npm run audit:ui-responsive`, `npm run audit:ui-navigation`,
  route/account smoke where relevant, visual screenshot comparison against
  canonical assets, and cleanup checks for browser/dev-server leftovers.

## PRJ-1232 Current Evidence

- Branch: `codex/v12-web-canonical-ui`
- Lane status: UX spec, frontend architecture, and QA visual-gate explorer
  lanes completed and integrated into
  `.codex/tasks/PRJ-1232-v12-web-canonical-ui-system.md`.
- Foundation implementation:
  - added `web/src/route-manifest.json` as the shared route/marker source for
    web route contracts and smoke proof
  - derived `ROUTES` and route markers from the manifest in `web/src/routes.ts`
  - updated `web/scripts/route-smoke.mjs` to consume the same manifest and to
    use manifest markers for navigation/account proof
  - improved mobile Chat by replacing the narrow-screen clipped context belt
    with stacked, readable context cards
  - refined route-smoke overflow detection so contained intentional scrollers
    do not mask or misreport document-level overflow checks
  - removed transform scaling from the public landing scenic background so
    `/` and `/login` no longer report decorative out-of-viewport elements
- Validation:
  - `node --check scripts/route-smoke.mjs` in `web/` -> PASS
  - `npm run build` in `web/` -> PASS
  - route smoke -> `route_count=14`, `status=ok`
  - responsive screenshots -> `screenshot_count=18`, `failed_count=0`
  - mobile foundation screenshots for `/chat`, `/settings`, `/dashboard` ->
    `failed_count=0`, `overflowingElementCount=0`
  - navigation proof -> `step_count=4`, `failed_count=0`
  - account proof -> `step_count=1`, `failed_count=0`,
    `panel_visible=true`
  - public Home/Login gate -> `screenshot_count=4`, `failed_count=0`,
    `overflowingElementCount=0` across desktop/mobile `/` and `/login`
- Artifacts:
  - `.codex/artifacts/prj1232-route-smoke/report.json`
  - `.codex/artifacts/prj1232-web-responsive-visual-gate/report.json`
  - `.codex/artifacts/prj1232-mobile-foundation-gate/report.json`
  - `.codex/artifacts/prj1232-navigation-proof/report.json`
  - `.codex/artifacts/prj1232-account-proof/report.json`
  - `.codex/artifacts/prj1232-public-home-gate/report.json`

## Previous Mission

- Mission ID: PRJ-1231-v1-production-candidate-promotion
- Status: COMPLETED
- Selected objective: turn locally verified selected-scope v1 into a real
  production-backed release fact by committing the refreshed candidate,
  publishing it to the deploy source, proving deployed revision parity, running
  production release smoke, and recording the final marker posture.
- Why this mission now: the user asked the coordinator to keep working until
  v1 is fact, and PRJ-1230 proved only local selected-scope readiness. The
  release boundary requires deploy parity and production smoke before any new
  release claim.
- Release objective or product milestone advanced: production-backed v1
  selected-scope marker for the current web-supported candidate.
- First/next checkpoint: v1 selected-scope is released as `v1.1.1`; next work
  should either monitor production or explicitly expand deferred extension
  scope.
- Stop conditions: git push is unavailable; deploy target/source branch cannot
  be confirmed; Coolify webhook/auto-deploy access is unavailable and
  production remains on an older SHA; release smoke fails; backend/web revision
  parity drifts; tag creation would point at an unproven SHA.
- Parent validation gate: completed. Local PRJ-1230 gate remained green;
  pre-push `git diff --check` passed; production release smoke with deploy
  parity passed; release reality audit returned `GO_FOR_SELECTED_SHA`;
  selected-tag go/no-go for `v1.1.1` returned `GO`.

## PRJ-1231 Release Result

- Selected SHA: `df677370f63d2688eb792f9a3a846d2cd40a564b`
- Release tag: `v1.1.1`
- Deploy source: `origin/main`
- Production URL: `https://aviary.luckysparrow.ch`
- Production proof: backend runtime revision and web shell build revision both
  match selected SHA; `release_ready=true`; no release violations; v1 final
  acceptance state `core_v1_bundle_ready`.
- Final verdict: `released`

## Previous Mission

- Mission ID: PRJ-1230-v1-selected-scope-final-readiness-refresh
- Status: COMPLETED
- Selected objective: refresh the selected-scope v1 readiness claim against the
  current workspace, coordinate lane findings, run the parent validation gate,
  and record whether v1 remains `verified`, `partially verified`, or `blocked`.
- Why this mission now: the user asked the coordinator to finish v1 using
  agents; the existing dashboard says selected-scope readiness is `11/11`, but
  the dated evidence is from 2026-05-14 and must not be silently reused for the
  current branch.
- Release objective or product milestone advanced: selected-scope v1 closure
  / web-supported release confidence.
- First/next checkpoint: selected-scope v1 local readiness is refreshed; next
  checkpoint is production candidate promotion only if a deploy target is
  selected.
- Stop conditions: a P0/P1 selected-scope blocker appears; architecture and
  implementation conflict; parent validation fails in a way that requires a
  product or deployment decision; production release parity is requested but
  target credentials/environment are unavailable.
- Parent validation gate: `git diff --check`; full backend pytest; web
  typecheck/build/responsive audit/navigation audit/route smoke; architecture
  dashboard refresh. Production release smoke is required only if this mission
  selects a new deployable release candidate.

## Source Rows

- Task board: latest completed UI slice `PRJ-1229`; next residual Dashboard
  lower-card proportions / first-viewport density.
- Planning: `docs/planning/current-v1-release-boundary.md`;
  `docs/planning/next-iteration-plan.md`.
- Delivery map: selected-scope v1 web-supported closure; native and provider
  extensions remain deferred unless scope is reactivated.
- Requirements: `REQ-UX-001`, `REQ-MOB-001`, `REQ-AI-001..003`.
- Quality scenarios: web route rendering and release readiness gates.
- Risks: deferred provider activation, proactive target sample, deploy
  automation convergence, and native mobile proof are nonblocking selected
  scope rows.
- Module confidence: `AVIARY-WEB-RESP-001`, `AVIARY-STATUS-001`,
  `AVIARY-COGNITIVE-RUNTIME-001`, `AVIARY-MEMORY-001`.
- System health: latest dated evidence from 2026-05-14 needs refresh if this
  branch becomes the active v1 closure basis.
- Architecture / UX / security / ops sources:
  `docs/operations/project-status-dashboard.md`,
  `docs/operations/v1-selected-scope-handoff-2026-05-11.md`,
  `docs/ux/screen-quality-checklist.md`, `docs/ux/design-memory.md`,
  `docs/operations/runtime-ops-runbook.md`.

## Responsibility Lanes

| Lane | Owner | Source docs/state | Owned files/surfaces | Output | Validation/proof | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinator | Active chat | AGENTS, mission control, project memory, state files | Integration, task closure, source-of-truth updates | Mission packet, task contract, final readiness decision | Parent validation gate | COMPLETED |
| Product/Requirements | Coordinator | Current v1 boundary, requirements matrix | Scope, accepted assumptions, exclusions | Selected-scope definition and deferred extension list | Requirements trace review | COMPLETED |
| Architecture | Coordinator | Project status dashboard, architecture audit | Architecture readiness posture | Alignment or mismatch note | Dashboard refresh | COMPLETED |
| Frontend/UX | UX explorer, then coordinator | UX refs, screenshots, web route files | Dashboard lower-row density refresh and route-smoke harness hardening | Web audit/screenshot proof | COMPLETED |
| Backend/API | Coordinator | Runtime confidence rows, backend tests | No backend code planned | Runtime gate status | Full backend pytest | COMPLETED |
| QA/Test | QA explorer, then coordinator | Known issues, system health, module confidence | Read-only gate report | Parent validation command set and blocker posture | Integrated into task evidence | COMPLETED |
| Security/Ops/Docs | Coordinator | Release boundary, ops runbook, security protocol | Release/ops evidence notes and state updates | Candidate versus non-candidate release posture | Smoke/deploy risk note | COMPLETED |
| Documentation/Memory | Coordinator | Task board, project state, ledgers | Active mission, PRJ-1230 task, state summaries | Durable handoff and next checkpoint | Source-of-truth diff review | COMPLETED |

## Delegation Plan

- Lanes kept local: coordination, final integration, shared state updates,
  parent validation, final `DONE`/blocked decision.
- Lanes delegated: QA/Release read-only blocker/gate report; Frontend/UX
  read-only next-slice report.
- Lanes intentionally omitted and why: Data/Migrations, Security deep review,
  and provider Ops smoke are omitted unless validation discovers a selected
  scope change; no schema, secrets, auth, permissions, or provider execution
  change is planned.
- Known overlap risks: avoid editing `.codex/context/PROJECT_STATE.md` over
  existing user governance additions; keep subagents read-only unless a later
  lane is explicitly given a disjoint write set.
- Forbidden files or surfaces: no provider credential activation, no native
  mobile proof work, no new web shell, no architecture rewrite, no temporary
  bypasses.

## Acceptance

- [x] Every important responsibility from source docs has an owner or explicit omission.
- [x] No two write lanes own the same file or shared registry.
- [x] Each lane has expected output and validation/proof.
- [x] Parent validation will run after accepted lane integration.
- [x] Missing or unclear ownership will be recorded in `.agents/state/responsibility-learning.md`.
- [x] Process quality will be evaluated in `.agents/state/agent-evals.md` when
      this mission is broad, repeated, partial, or subagent-heavy.

## Checkpoint Log

| Date | Checkpoint | Result | Evidence | Next action |
| --- | --- | --- | --- | --- |
| 2026-05-22 | Mission opened | Multi-lane coordinator mission created after user asked to finish v1 with agents. | Active mission packet; QA/Release and UX read-only lanes delegated. | Create task contract and run/record parent gate. |
| 2026-05-22 | Lane integration | QA confirmed no selected-scope blockers and UX identified Dashboard lower-row density as the smallest polish slice. | Subagent lane reports; PRJ-1230 task contract. | Patch the focused web slice and harden route-smoke fallback. |
| 2026-05-22 | Parent validation | COMPLETED: selected-scope v1 remains locally verified for this branch. | `git diff --check` PASS with LF/CRLF warnings only; backend `1105 passed`; web build/responsive/navigation/account/route smoke PASS; architecture dashboard `11/11`; screenshot review; cleanup no leftovers. | Promote only after explicit production deploy target/parity smoke. |
