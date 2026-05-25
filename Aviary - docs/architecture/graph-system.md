# Architecture Graph Evidence System

Last updated: 2026-05-24

Status: implemented foundation

## Purpose

This system is the Obsidian-first architecture and evidence map for Aviary.
It is not ordinary documentation. It is the machine-readable project nervous
system that lets agents trace a feature from visible UI through API, runtime,
data, tests, and docs before reporting confidence.

The canonical chain for this system is:

`source idea -> node registry -> relation registry -> chain map -> evidence -> generated Obsidian graph -> task/module confidence update`

## Canonical Files

CSV is the source of truth.

| Artifact | Role |
| --- | --- |
| `docs/architecture/registry/nodes.csv` | canonical element registry for features, components, services, routes, models, tests, docs, agents, events, workflows, config, scripts, migrations, and UI elements |
| `docs/architecture/registry/relations.csv` | canonical edge registry between nodes |
| `docs/architecture/registry/chains.csv` | function-chain execution mapping from trigger to effect and proof |
| `docs/architecture/registry/evidence.csv` | implementation, test, behavior, connection, and documentation proof registry |
| `docs/architecture/registry/research_sources.csv` | reviewed neuroscience and cognitive-science source registry |
| `docs/architecture/registry/theory_claims.csv` | code-level theory claims linked to nodes and research sources |
| `docs/architecture/registry/auto_nodes.csv` | generated whole-repository file and symbol inventory |
| `docs/architecture/registry/auto_relations.csv` | generated import, contains, test, and documentation relations |
| `docs/architecture/nodes/*.md` | generated Obsidian node pages |
| `docs/architecture/relations/index.md` | generated relation index |
| `docs/architecture/chains/index.md` | generated function-chain index |
| `docs/architecture/graphs/architecture-graph.json` | generated graph export |
| `docs/architecture/graphs/architecture-graph.mmd` | generated Mermaid graph export |
| `docs/status/architecture-map-status.md` | generated status rollup |
| `docs/testing/architecture-evidence-map.md` | generated evidence rollup |
| `docs/testing/architecture-research-map.md` | generated theory and research support rollup |

Typed CSV files such as `functions.csv`, `components.csv`, `api_routes.csv`,
`tests.csv`, `features.csv`, `workflows.csv`, `events.csv`, `agents.csv`, and
`prompts.csv` are compatibility views for spreadsheet and Obsidian Dataview
workflows. The canonical graph uses `nodes.csv`, `relations.csv`,
`chains.csv`, `evidence.csv`, `research_sources.csv`, `theory_claims.csv`,
and the generated `auto_*.csv` inventory layer.
Auto-discovered rows are broad coverage, not final proof; promote critical
rows into curated CSVs when a feature, release gate, or agent mission depends
on them.

## Node Contract

Every official project element must eventually be represented by a node row.
Absence from the registry means the element is not officially mapped.

Required node columns:

`id,name,type,status,layer,module,feature,description,file_path,related_files,parent_id,child_ids,depends_on,used_by,ui_related,api_related,database_related,tests_related,docs_related,agent_related,risk_level,completion_percent,last_verified_at,verification_status,notes,tags`

Allowed status values:

- `planned`
- `in_progress`
- `implemented`
- `broken`
- `missing`
- `deprecated`
- `tested`
- `verified`
- `blocked`

Allowed verification statuses:

- `missing_evidence`
- `implementation_evidence`
- `test_evidence`
- `behavior_evidence`
- `connection_evidence`
- `documentation_evidence`
- `verified`
- `blocked`

## Relation Contract

Relations must be explicit. Use relation IDs that remain stable across
renames.

Core relation types:

- `depends_on`
- `used_by`
- `calls`
- `renders`
- `routes_to`
- `reads`
- `writes`
- `emits`
- `consumes`
- `tests`
- `documents`
- `verifies`
- `parent_of`
- `child_of`
- `configured_by`
- `generated_from`
- `owned_by`

## Function Chain Contract

Every feature chain should map the whole path, not a local file. A complete
chain should include, when applicable:

`UI trigger -> UI component -> client action -> API request -> backend route -> controller/service -> repository/model -> database/event -> worker/integration -> UI update -> tests -> docs`

Chain confidence rules:

- `complete`: all critical steps have nodes, relations, and proof.
- `partial`: the chain is useful but at least one critical step or proof type
  is missing.
- `blocked`: the chain cannot be verified due to access, environment, product
  decision, or missing dependency.
- `missing`: the feature is claimed but no usable chain exists.

## Evidence Rules

Every feature should carry five evidence classes:

- implementation evidence
- test evidence
- behavior evidence
- connection evidence
- documentation evidence

Missing evidence is a real status, not a note. A mapped feature with missing
proof is considered unreliable until the missing proof is added or explicitly
deferred.

## Research Evidence Rules

Research evidence is separate from runtime evidence. It supports a theory,
metaphor, or architecture claim expressed in code or docs; it does not prove
that the feature works.

Use `research_sources.csv` for reviewed neuroscience or cognitive-science
papers. Use `theory_claims.csv` to link a concrete project node to the claim,
the code expression, the source IDs, applicability scope, and limitations.

Rules:

- A reviewed or mapped theory claim should cite at least 3 research sources.
- A claim must name its `node_id`; no free-floating theory is official.
- A claim must include limitations that prevent overstatement.
- If an agent cannot find adequate sources, the claim status must be
  `needs_sources` and the feature should not be described as research-backed.
- Scientific support never replaces implementation, behavior, test,
  connection, or documentation evidence.

## Agent Workflow

For any new feature, fix, route, component, service, test, prompt, workflow, or
documentation change:

1. Add or update affected rows in `nodes.csv`.
2. Add or update relation rows in `relations.csv`.
3. Add or update execution-chain rows in `chains.csv`.
4. Add or update evidence rows in `evidence.csv`.
5. If the feature expresses a neuroscience-inspired or cognitive-science
   theory, add or update `theory_claims.csv` and link at least 3 reviewed
   source rows from `research_sources.csv`. If sources are missing, set the
   claim to `needs_sources`.
6. Run the generator:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_inventory.py; if ($LASTEXITCODE -eq 0) { ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py }; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

For curated-only regeneration after manual CSV edits:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\generate_architecture_graph.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Fast graph validation for normal registry/research edits:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py -m "not slow"; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Heavy graph validation for pre-release or high-confidence graph work:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python -m pytest -q tests/test_architecture_graph_generator.py; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

The heavy gate regenerates and compares every generated Obsidian node page. It
is intentionally slower than the fast gate.

Local query workflow:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\query_architecture_graph.py --node WORKFLOW-ARCH-GRAPH --show-gaps; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

Use `--search <term>` to find candidate nodes, `--format json` for agent or
automation consumption, and `--show-gaps` when checking missing tests, docs,
evidence, incomplete chains, or unresolved research support. The query CLI
reads `docs/architecture/graphs/architecture-graph.json` as a generated read
model; it does not replace CSV as the source of truth.

For a system-level missing-proof queue:

```powershell
Push-Location .\backend; ..\.venv\Scripts\python .\scripts\query_architecture_graph.py --gaps --limit 20; $exit=$LASTEXITCODE; Pop-Location; exit $exit
```

`--gaps` excludes broad auto-inventory rows by default so the report stays
focused on curated graph promises. Use `--include-auto` only when deliberately
auditing broad repository inventory coverage.

CI policy:

- `.github/workflows/architecture-graph.yml` runs the inventory generator,
  graph generator, committed-artifact diff check, and fast graph pytest gate
  automatically for graph-relevant pull requests and pushes to `main`.
- The same workflow exposes a manual `workflow_dispatch` `heavy` mode for
  all-node page parity before release-level graph confidence.
- Hosted CI evidence is additive. Local graph edits still need the generator
  and fast gate before marking a task done.

7. Review generated Obsidian node pages and graph exports.
8. Update task, requirement, and module-confidence state with the graph
   evidence or missing-proof risk.

## Systemic Analysis Rule

When asked whether a function works, agents must inspect the graph before
answering:

1. find the feature or node,
2. trace dependencies and `used_by`,
3. read the function chain,
4. inspect related UI, API, data, event, worker, tests, docs, and agents,
5. identify missing proof,
6. inspect theory claims and research support when the feature depends on a
   cognitive/neuroscience framing,
7. run or cite the relevant verification,
8. report confidence only from evidence.

Local file-only analysis is not accepted for mapped features.

## Future Extensions

The current foundation is compatible with:

- Obsidian Graph View via `[[node-id]]` links,
- Dataview over YAML frontmatter,
- Breadcrumbs through parent/child fields,
- Juggl and Excalibrain through explicit Markdown links,
- custom graph UI from `architecture-graph.json`,
- dead-function detection from missing `used_by` or orphan nodes,
- test-gap detection from empty `tests_related` or missing evidence,
- impact analysis from reverse relation traversal,
- AI-agent work planning from chain and evidence gaps.
