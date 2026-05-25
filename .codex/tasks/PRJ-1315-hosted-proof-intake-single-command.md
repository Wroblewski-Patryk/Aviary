# Task

## Header
- ID: PRJ-1315
- Title: Hosted proof intake single-command helper
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1314
- Priority: P1
- Mission ID: PRJ-1315-hosted-proof-intake-single-command
- Mission Status: VERIFIED

## Goal
Allow hosted proof closure without `gh` by providing one local command for downloaded artifact intake.

## Definition of Done
- [x] helper script added
- [x] helper validates fast/heavy artifacts and builds hosted packet
- [x] hosted-proof checklist updated with helper usage

## Validation Evidence
- command:
  - `python backend/scripts/run_architecture_graph_hosted_proof_intake.py --fast-artifact <fast.json> --heavy-artifact <heavy.json> --out-dir <packet-dir>`
- local fixture run:
  - fast/heavy `curated_gap_count=0`, `status=PASSED`
  - packet output generated in `docs/status/prj1315-hosted-intake-packet/`
