# Task

## Header
- ID: PRJ-1182
- Title: Add v1.5 mobile device proof doctor
- Task Type: verification
- Current Stage: release
- Status: DONE
- Owner: Frontend Builder
- Depends on: PRJ-1181
- Priority: P2
- Module Confidence Rows: AVIARY-MOBILE-UI-001
- Requirement Rows: REQ-MOB-002
- Quality Scenario Rows: QA-MOB-002
- Risk Rows: RISK-MOB-001
- Iteration: 1182
- Operation Mode: BUILDER
- Mission ID: v15-mobile-device-proof-doctor
- Mission Status: VERIFIED_BLOCKED

## Mission Block
- Mission objective: make the remaining native-device proof blocker executable and explicit.
- Included slices: package script, device-proof doctor, blocked report artifact, source-of-truth updates.
- Explicit exclusions: installing Android tooling, launching Expo Go, public hosting, auth transport, live data wiring.
- Handoff expectation: run `npm run doctor:ui-mobile-device` to know whether native proof can proceed.

## Context
The local mobile UI preview is deployed and verified, but native Expo Go or
simulator proof remains blocked in this environment. The blocker should be
detectable through a repeatable repo command instead of hidden terminal
knowledge.

## Goal
Add a device-proof readiness command for v1.5 mobile UI validation.

## Scope
- `mobile/package.json`
- `mobile/scripts/mobile-device-proof-doctor.mjs`
- source-of-truth docs/state files

## Implementation Plan
1. Add `doctor:ui-mobile-device`.
2. Check Android platform tools needed for native proof.
3. Write a JSON report under `.codex/artifacts/prj1182-mobile-device-proof-doctor/`.
4. Keep the command non-destructive and truth-reporting.
5. Validate local preview still passes.

## Acceptance Criteria
- Doctor reports `ready` only when required device tooling exists.
- Current environment reports `blocked` with missing `adb` and `emulator`.
- Doctor writes a durable JSON report.
- TypeScript and preview smoke remain green.
- No product code changes are introduced.

## Validation Evidence
- Tests:
  - `Push-Location .\mobile; npm run doctor:ui-mobile-device; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS; report status `blocked`, missing tools `adb`, `emulator`
  - `Push-Location .\mobile; npm run typecheck; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS
  - `Push-Location .\mobile; npm run smoke:ui-mobile-preview; $exit=$LASTEXITCODE; Pop-Location; exit $exit` -> PASS; `preview_health.ok=true`, `route_count=5`, `viewport_count=2`, `screenshot_count=10`, `failed_count=0`
- High-risk checks:
  - no Android tooling was installed or modified
  - active local preview was not stopped
- Reality status: verified blocked

## Result Report
- Task summary: added a repeatable device-proof readiness doctor and recorded the current native-proof blocker.
- Files changed: `mobile/package.json`, `mobile/scripts/mobile-device-proof-doctor.mjs`, this task file, and source-of-truth docs/state files.
- How tested: device doctor, typecheck, and preview smoke.
- What is incomplete: native Expo Go/simulator proof remains blocked by missing Android tooling.
- Next steps: install Android platform tools or connect a supported device, then run native route proof.

## Autonomous Loop Evidence
### 1. Analyze Current State
- Native proof blocker was known but not executable as a repo check.
### 2. Select One Priority Mission Objective
- Selected task: PRJ-1182.
### 3. Plan Implementation
- Add a non-destructive device readiness command and artifact report.
### 4. Execute Implementation
- Added `doctor:ui-mobile-device` and `mobile-device-proof-doctor.mjs`.
### 5. Verify and Test
- Doctor, typecheck, and preview smoke passed.
### 6. Self-Review
- The task records blocked native readiness without downgrading local-preview proof.
### 7. Update Documentation and Knowledge
- Updated source-of-truth state files and handoff.
