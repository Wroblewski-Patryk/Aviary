# V1 Selected-Scope Handoff

## Header

- Date: 2026-05-11
- Author role: Codex
- Related task IDs: `PRJ-931`, `PRJ-932`, `PRJ-933`
- Current branch: local workspace
- Current stage: release
- Operation mode: ARCHITECT

## Current Source Of Truth

- Product: `docs/planning/current-v1-release-boundary.md`
- Architecture: `docs/operations/architecture-implementation-audit-2026-05-10.md`
- Planning: `docs/planning/v1-core-acceptance-bundle.md`
- Task board: `.codex/context/TASK_BOARD.md`
- Deployment/ops: `docs/operations/project-status-dashboard.md`
- State: `.agents/state/current-focus.md`, `.agents/state/module-confidence-ledger.md`

## What Changed

- Summary: the selected core/web-supported v1 architecture scope is now
  evidence-complete in the generated radar.
- Product behavior changed: no.
- Architecture changed: no new architecture; the generated radar was aligned
  with existing release-boundary decisions.
- UX changed: no product UX redesign; `PRJ-931` added a chat composer
  accessible name and route-state smoke coverage.
- Deployment changed: no.

## Validation

- Commands run:
  - `Push-Location .\web; npm exec -- tsc -b --pretty false; if ($LASTEXITCODE -eq 0) { npm exec -- vite build }; if ($LASTEXITCODE -eq 0) { npm run smoke:routes }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
  - `Push-Location .\backend; ..\.venv\Scripts\python .\scripts\audit_architecture_implementation_map.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_project_status_dashboard.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit`
  - `git diff --check`
- Manual checks:
  - `docs/operations/project-status-dashboard.md` reports selected-scope
    readiness `11/11` and no active blockers or evidence gaps.
  - `docs/planning/v1-core-acceptance-bundle.md` reports core no-UI v1 GO and
    current selected release marker `v1.0.1`.
- Checks not run:
  - no fresh production deploy smoke was run in this final sync because no
    runtime, deploy, secret, provider, or production candidate changed.

## Risks And Assumptions

- Residual risks:
  - deferred extension rows remain visible for organizer provider activation,
    proactive target sampling, future-candidate source/webhook deploy
    convergence, and mobile restart.
  - every later commit that changes release content needs fresh candidate
    validation and deploy parity.
- Assumptions made:
  - the selected scope follows `docs/planning/current-v1-release-boundary.md`.
  - extension rows should not block the achieved core/web-supported marker
    unless release scope is explicitly expanded.
- Known blockers:
  - none for selected scope.
- Open decisions:
  - none required to claim selected-scope readiness.

## Next Tiny Task

- Recommended next task: preserve evidence; do not start a new feature unless
  the release scope changes.
- Why next: the generated radar has no selected-scope blocker or evidence gap.
- Suggested owner: Planning + QA/Test.
- Files or surfaces likely touched: dashboard/audit/state files only unless a
  deferred extension trigger appears.
- Validation to run: audit/dashboard regeneration and the row-specific command
  pack for any changed row.

## Resume Instructions

- Read first:
  - `docs/operations/project-status-dashboard.md`
  - `docs/planning/current-v1-release-boundary.md`
  - `docs/planning/v1-core-acceptance-bundle.md`
  - `.agents/state/current-focus.md`
- Do not touch:
  - deferred extension rows without credentials, launch-scope expansion, a new
    release candidate, or explicit mobile product scope.
- Watch out for:
  - treating organizer/provider credentials as a local implementation defect.
  - claiming future candidates inherit v1 evidence without fresh deploy parity.
- If blocked:
  - record the blocker in `.agents/state/known-issues.md` and keep the
    dashboard selected-scope semantics explicit.
