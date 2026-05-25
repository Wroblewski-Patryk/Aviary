# Architecture Graph Hosted Proof Checklist

Last updated: 2026-05-24

## Purpose

This checklist is an optional hosted supplement for the architecture graph
system. Canonical release gating is local/Coolify-first and does not require
GitHub Actions billing.

## Preconditions

- Local graph gate is green:
  - `python backend/scripts/query_architecture_graph.py --gaps --format json --fail-on-gaps`
- Local graph tests are green:
  - `python -m pytest -q backend/tests/test_architecture_graph_ci_policy.py backend/tests/test_architecture_graph_query.py backend/tests/test_architecture_graph_generator.py -m "not slow"`

## Hosted Proof Steps (Optional)

Use this only when GitHub Actions is available for the repository/account.
If Actions is unavailable (for example billing lock), skip this section and use
the local release gate plus production proof cycle as the required baseline.

Manual UI trigger fallback (when CLI/API auth is unavailable):

- Open:
  - `https://github.com/Wroblewski-Patryk/Aviary/actions/workflows/architecture-graph.yml`
- Click **Run workflow**
- For routine proof choose `validation_mode=fast`
- For release-level parity also run `validation_mode=heavy`

1. Push branch with graph-related changes.
2. Open or update pull request.
3. Wait for workflow:
   - `.github/workflows/architecture-graph.yml`
4. Confirm fast job passed.
5. Download artifact:
   - `architecture-gaps-fast`
6. Verify artifact JSON:
   - `items` is an empty array.
   - optional helper:
     - `python backend/scripts/verify_architecture_gap_artifact.py --artifact <downloaded-artifact.json>`
7. If heavy mode was run manually, also download:
   - `architecture-gaps-heavy`
8. Attach artifact proof to mission/task evidence rows.
9. Optional packet builder:
   - `python backend/scripts/build_architecture_graph_hosted_evidence_packet.py --fast-artifact <architecture-gaps-fast.json> --out-dir <packet-dir>`
   - optional heavy mode:
     - `python backend/scripts/build_architecture_graph_hosted_evidence_packet.py --fast-artifact <architecture-gaps-fast.json> --heavy-artifact <architecture-gaps-heavy.json> --out-dir <packet-dir>`
10. One-command intake helper (verify + packet):
   - `python backend/scripts/run_architecture_graph_hosted_proof_intake.py --fast-artifact <architecture-gaps-fast.json> --out-dir <packet-dir>`
   - optional heavy mode:
     - `python backend/scripts/run_architecture_graph_hosted_proof_intake.py --fast-artifact <architecture-gaps-fast.json> --heavy-artifact <architecture-gaps-heavy.json> --out-dir <packet-dir>`

## Hosted CI Artifacts (Current)

- `architecture-gaps-fast`
- `architecture-hosted-evidence-fast`
- `architecture-gaps-heavy` (manual heavy run only)
- `architecture-hosted-evidence-heavy` (manual heavy run only)

## Failure Handling

- If workflow fails on `--fail-on-gaps`:
  - run local gap audit
  - close reported curated gaps
  - regenerate graph artifacts
  - rerun local tests
  - push again
