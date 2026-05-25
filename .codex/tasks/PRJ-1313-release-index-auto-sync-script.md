# Task

## Header
- ID: PRJ-1313
- Title: Release index auto-sync script from latest production summary
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1312
- Priority: P1
- Mission ID: PRJ-1313-release-index-auto-sync-script
- Mission Status: VERIFIED

## Goal
Automate updating `docs/operations/release-evidence-index.md` from the latest production summary JSON.

## Definition of Done
- [x] sync script added
- [x] script executed successfully on current repository state
- [x] runbook includes the sync command

## Validation Evidence
- script:
  - `backend/scripts/sync_release_evidence_index_from_latest_summary.py`
- command:
  - `python backend/scripts/sync_release_evidence_index_from_latest_summary.py --date 2026-05-24`
- output:
  - updated `docs/operations/release-evidence-index.md` with latest summary block
