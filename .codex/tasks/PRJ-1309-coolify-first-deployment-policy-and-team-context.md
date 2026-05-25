# Task

## Header
- ID: PRJ-1309
- Title: Coolify-first deployment policy and team-context recovery
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1308
- Priority: P1
- Coverage Ledger Rows: not applicable
- Module Confidence Rows: deployment runbooks (ops docs)
- Requirement Rows: release/deploy operator baseline continuity
- Quality Scenario Rows: operability, maintainability
- Risk Rows: deployment context drift, toolchain assumption drift
- Iteration: 1
- Operation Mode: BUILDER
- Mission ID: PRJ-1309-coolify-first-deployment-policy-and-team-context
- Mission Status: VERIFIED

## Context
User confirmed a hard operator constraint: no paid GitHub extensions and production app hosted on VPS with Coolify. Existing docs covered Coolify deployment, but did not explicitly lock this as a durable policy across decision/state files or document team-context recovery as a first troubleshooting step.

## Goal
Persist the deployment constraint and eliminate ambiguity so future agents and operators follow a Coolify-first release path without paid GitHub extension assumptions.

## Constraints
- reuse existing deployment/runbook systems
- no new deployment framework
- no secret material stored in repo docs/state

## Definition of Done
- [x] durable decision row recorded in decision register
- [x] Coolify team-context recovery step added to deployment guide
- [x] runtime ops runbook reflects Coolify control plane and no-paid-extension policy

## Validation Evidence
- Tests: `./backend/scripts/run_release_smoke.ps1 -BaseUrl "https://aviary.luckysparrow.ch"` (PASS, `release_ready=true`, `release_violations=[]`)
- Manual checks: reviewed updated docs for policy consistency and step order
- Reality status: verified

## Result Report
- Added decision `DEC-004` in `.agents/state/decision-register.md`.
- Updated `docs/architecture/28_local_windows_and_coolify_deploy.md` with mandatory team-switch check when app/resource is not visible and explicit no-paid-extension note.
- Updated `docs/operations/runtime-ops-runbook.md` with canonical Coolify control-plane URL, no-paid-extension deployment policy, and team-context troubleshooting section.
