# Task

## Header
- ID: PRJ-1310
- Title: Production incident-evidence bundle and release smoke proof capture
- Task Type: release
- Current Stage: verification
- Status: DONE
- Owner: Ops/Release
- Depends on: PRJ-1309
- Priority: P1
- Mission ID: PRJ-1310-production-incident-evidence-bundle-and-release-smoke-proof
- Mission Status: VERIFIED

## Context
Coolify-first policy is already documented. The next operational closure step is durable artifact capture: incident-evidence bundle + release smoke JSON in repository status space.

## Goal
Produce reproducible production proof artifacts that can be reused by future agents and release audits without rerunning ad hoc checks.

## Definition of Done
- [x] incident-evidence bundle exported to `docs/status`
- [x] release smoke executed against production with bundle verification
- [x] machine-readable smoke output saved in `docs/status`

## Validation Evidence
- Commands:
  - `python backend/scripts/export_incident_evidence_bundle.py --base-url "https://aviary.luckysparrow.ch" --output-root "../docs/status" --capture-mode release_smoke` (from `backend/`)
  - `./backend/scripts/run_release_smoke.ps1 -BaseUrl "https://aviary.luckysparrow.ch" -IncidentEvidenceBundlePath "docs/status/20260524T172450Z_incident-bundle-20260524T172450Z" | Out-File -FilePath "docs/status/release-smoke-prj1310.json" -Encoding utf8`
- Output artifacts:
  - `docs/status/20260524T172450Z_incident-bundle-20260524T172450Z/manifest.json`
  - `docs/status/20260524T172450Z_incident-bundle-20260524T172450Z/incident_evidence.json`
  - `docs/status/20260524T172450Z_incident-bundle-20260524T172450Z/health_snapshot.json`
  - `docs/status/release-smoke-prj1310.json`
- Reality status: verified
