# Architecture Registry

CSV files in this directory are the canonical source for the architecture graph
evidence system.

Start with:

- `nodes.csv`
- `relations.csv`
- `chains.csv`
- `evidence.csv`
- `research_sources.csv`
- `theory_claims.csv`

The remaining typed CSV files are compatibility views for spreadsheet filters
and Obsidian Dataview workflows. When in doubt, update the canonical files
first, then mirror the row into a typed view if the element belongs there.

Use `research_sources.csv` and `theory_claims.csv` when a feature, prompt,
agent, runtime stage, memory behavior, reflection behavior, or UX metaphor
claims neuroscience or cognitive-science grounding. A reviewed/mapped claim
must cite at least three source IDs and include limitations. If suitable
sources are not found, keep the claim as `needs_sources`; do not describe the
feature as research-backed.

`auto_nodes.csv` and `auto_relations.csv` are generated whole-repository
inventory layers. They are still CSV graph inputs, but they are marked as
auto-discovered evidence. Promote rows into curated CSVs when they become
release-critical or need richer feature-chain proof.

Regenerate the automatic inventory with:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Regenerate graph artifacts with:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Run the fast graph validation gate with:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Run the heavy graph validation gate before release-level graph confidence with:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

GitHub Actions policy:

- `.github/workflows/architecture-graph.yml` runs inventory regeneration,
  graph regeneration, a committed-artifact diff check, and the fast pytest gate
  for graph-relevant pull requests and pushes to `main`.
- Run the same workflow manually with `validation_mode=heavy` before
  release-level graph confidence when all generated Obsidian node pages should
  be compared.
