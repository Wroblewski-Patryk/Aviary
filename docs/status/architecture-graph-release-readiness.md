# Architecture Graph Release Readiness

Last updated: 2026-05-24

## Local Gate

- report:
  - `docs/status/architecture-graph-local-release-gate.json`
- overall status:
  - `PASSED`
- fast suite:
  - `39 passed, 1 deselected`
- curated gaps:
  - `items=[]`

## Hosted Proof (Optional Supplement)

- optional workflow:
  - `.github/workflows/architecture-graph.yml`
- optional artifacts:
  - `architecture-gaps-fast`
  - `architecture-hosted-evidence-fast`
  - optional manual heavy:
    - `architecture-gaps-heavy`
    - `architecture-hosted-evidence-heavy`
- verification checklist:
  - `docs/operations/architecture-graph-hosted-proof-checklist.md`
- policy:
  - hosted proof is supplementary and must not block readiness when unavailable
    due to GitHub billing/Actions constraints (`DEC-005`)
