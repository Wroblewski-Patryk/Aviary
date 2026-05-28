from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def split_refs(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.replace(';', '|').split('|') if part.strip()]


def load_graph(path: Path) -> dict:
    return json.loads(path.read_text(encoding='utf-8'))


def build_entity_rows(graph: dict) -> list[dict]:
    nodes = graph.get('nodes', [])
    outgoing = Counter()
    incoming = Counter()
    for rel in graph.get('relations', []):
        outgoing[rel.get('source_id', '')] += 1
        incoming[rel.get('target_id', '')] += 1

    rows: list[dict] = []
    for node in nodes:
        node_id = node.get('id', '')
        tests = split_refs(node.get('tests_related', ''))
        docs = split_refs(node.get('docs_related', ''))
        row = {
            'id': node_id,
            'name': node.get('name', ''),
            'type': node.get('type', ''),
            'status': node.get('status', ''),
            'verification_status': node.get('verification_status', ''),
            'layer': node.get('layer', ''),
            'module': node.get('module', ''),
            'feature': node.get('feature', ''),
            'file_path': node.get('file_path', ''),
            'risk_level': node.get('risk_level', ''),
            'last_verified_at': node.get('last_verified_at', ''),
            'tags': node.get('tags', ''),
            'relation_count': outgoing[node_id] + incoming[node_id],
            'outgoing_relations': outgoing[node_id],
            'incoming_relations': incoming[node_id],
            'tests_link_count': len(tests),
            'docs_link_count': len(docs),
            'has_tests_links': len(tests) > 0,
            'has_docs_links': len(docs) > 0,
            'is_auto_inventory': '#auto' in (node.get('tags', '')),
        }
        rows.append(row)
    return rows


def build_function_journey_index(graph: dict) -> dict:
    chains = graph.get('chains', [])
    rows = []
    for chain in chains:
        rows.append(
            {
                'id': chain.get('id', ''),
                'feature': chain.get('feature_id', ''),
                'name': chain.get('name', ''),
                'trigger': chain.get('trigger_node_id', ''),
                'status': chain.get('status', ''),
                'confidence': chain.get('confidence', ''),
                'risk_level': chain.get('risk_level', ''),
                'ordered_node_ids': chain.get('ordered_node_ids', ''),
                'implementation_evidence': chain.get('implementation_evidence', ''),
                'test_evidence': chain.get('test_evidence', ''),
                'behavior_evidence': chain.get('behavior_evidence', ''),
                'connection_evidence': chain.get('connection_evidence', ''),
                'documentation_evidence': chain.get('documentation_evidence', ''),
                'missing_links': chain.get('missing_links', ''),
                'last_verified_at': chain.get('last_verified_at', ''),
                'notes': chain.get('notes', ''),
            }
        )

    gap_counts = Counter('has_gap' if (row.get('missing_links') or '').strip().lower() not in {'', 'none'} else 'no_gap' for row in rows)
    return {
        'summary': {
            'generatedAt': datetime.now(timezone.utc).isoformat(),
            'counts': {
                'chains': len(rows),
                'chainsWithMissingLinks': gap_counts['has_gap'],
            },
        },
        'functionChains': rows,
    }


def build_user_action_index(graph: dict) -> dict:
    nodes = graph.get('nodes', [])
    relations = graph.get('relations', [])
    relation_by_source: dict[str, list[dict]] = {}
    for relation in relations:
        relation_by_source.setdefault(relation.get('source_id', ''), []).append(relation)

    action_types = {'api_route', 'workflow', 'ui_element', 'component', 'event'}
    actions = []
    for node in nodes:
        if node.get('type') not in action_types:
            continue
        node_id = node.get('id', '')
        downstream = relation_by_source.get(node_id, [])
        actions.append(
            {
                'id': node_id,
                'name': node.get('name', ''),
                'type': node.get('type', ''),
                'feature': node.get('feature', ''),
                'module': node.get('module', ''),
                'status': node.get('status', ''),
                'verification_status': node.get('verification_status', ''),
                'file_path': node.get('file_path', ''),
                'downstream_relations': [f"{r.get('relation_type','')}:{r.get('target_id','')}" for r in downstream],
                'risk_level': node.get('risk_level', ''),
                'last_verified_at': node.get('last_verified_at', ''),
            }
        )

    return {
        'summary': {
            'generatedAt': datetime.now(timezone.utc).isoformat(),
            'counts': {
                'actions': len(actions),
                'actionTypes': len({row['type'] for row in actions}),
            },
        },
        'userActions': actions,
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text('', encoding='utf-8')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_graph_markdown(path: Path, graph: dict) -> None:
    nodes = graph.get('nodes', [])
    relations = graph.get('relations', [])
    chains = graph.get('chains', [])
    by_type = Counter(node.get('type', 'unknown') for node in nodes)
    by_status = Counter(node.get('status', 'unknown') for node in nodes)

    lines = [
        '# Architecture Graph',
        '',
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        '',
        '## Summary',
        '',
        f"- Nodes: `{len(nodes)}`",
        f"- Relations: `{len(relations)}`",
        f"- Chains: `{len(chains)}`",
        '',
        '## Node Types',
        '',
        '| Type | Count |',
        '| --- | ---: |',
    ]
    for key, value in sorted(by_type.items()):
        lines.append(f"| {key} | {value} |")

    lines.extend(['', '## Node Status', '', '| Status | Count |', '| --- | ---: |'])
    for key, value in sorted(by_status.items()):
        lines.append(f"| {key} | {value} |")

    lines.extend([
        '',
        '## Render Source',
        '',
        '- Mermaid graph source: `docs/graphs/architecture-graph.mmd`',
        '- Canonical raw graph: `docs/architecture/graphs/architecture-graph.json`',
    ])

    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def write_report(path: Path, entities: list[dict], journeys: dict, actions: dict) -> None:
    by_type = Counter(row.get('type', 'unknown') for row in entities)
    by_status = Counter(row.get('status', 'unknown') for row in entities)

    impl_entities = [row for row in entities if row.get('type') not in {'test', 'documentation'}]
    missing_tests = [row for row in impl_entities if not row.get('has_tests_links')]
    missing_docs = [row for row in impl_entities if not row.get('has_docs_links')]
    disconnected = [row for row in entities if int(row.get('relation_count', 0)) == 0]

    top_missing_tests = missing_tests[:40]
    top_missing_docs = missing_docs[:40]

    lines = [
        '# Architecture Awareness Report',
        '',
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        'Project: Personality',
        f"Root: {repo_root().as_posix()}",
        '',
        '## Counts By Type',
        '',
        '| Type | Count |',
        '| --- | ---: |',
    ]

    for key, value in sorted(by_type.items()):
        lines.append(f"| {key} | {value} |")

    lines.extend(['', '## Counts By Status', '', '| Status | Count |', '| --- | ---: |'])
    for key, value in sorted(by_status.items()):
        lines.append(f"| {key} | {value} |")

    lines.extend([
        '',
        '## Health Signals',
        '',
        f"- Implementation entities without inferred tests: {len(missing_tests)}",
        f"- Implementation entities without inferred docs: {len(missing_docs)}",
        f"- Entities without relation links: {len(disconnected)}",
        f"- Function journey rows: {journeys['summary']['counts']['chains']}",
        f"- User action rows: {actions['summary']['counts']['actions']}",
        '',
        '## Top Missing Test Links',
        '',
    ])

    for row in top_missing_tests:
        lines.append(f"- {row['type']}: {row['name']} ({row['file_path']})")
    if not top_missing_tests:
        lines.append('- none')

    lines.extend(['', '## Top Missing Doc Links', ''])
    for row in top_missing_docs:
        lines.append(f"- {row['type']}: {row['name']} ({row['file_path']})")
    if not top_missing_docs:
        lines.append('- none')

    lines.extend([
        '',
        '## Notes',
        '',
        '- This is a parity export derived from the canonical registry graph under `docs/architecture/graphs`.',
        '- Missing link rows are explicit unknowns; they are not treated as verified behavior.',
        '- `verified` claims still require fresh runtime/test evidence from task-level gates.',
    ])

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main() -> int:
    root = repo_root()
    source_graph = root / 'docs' / 'architecture' / 'graphs' / 'architecture-graph.json'
    source_mmd = root / 'docs' / 'architecture' / 'graphs' / 'architecture-graph.mmd'
    out_graphs = root / 'docs' / 'graphs'

    graph = load_graph(source_graph)
    entities = build_entity_rows(graph)
    journeys = build_function_journey_index(graph)
    actions = build_user_action_index(graph)

    out_graphs.mkdir(parents=True, exist_ok=True)
    (out_graphs / 'architecture-awareness.json').write_text(
        json.dumps({'summary': {'generatedAt': datetime.now(timezone.utc).isoformat(), 'entityCount': len(entities)}, 'entities': entities}, indent=2),
        encoding='utf-8',
    )
    write_csv(out_graphs / 'architecture-awareness.csv', entities)
    write_graph_markdown(out_graphs / 'architecture-graph.md', graph)
    (out_graphs / 'architecture-graph.mmd').write_text(source_mmd.read_text(encoding='utf-8'), encoding='utf-8')
    (out_graphs / 'function-journey-index.json').write_text(json.dumps(journeys, indent=2), encoding='utf-8')
    (out_graphs / 'user-action-index.json').write_text(json.dumps(actions, indent=2), encoding='utf-8')

    write_report(root / 'docs' / 'status' / 'architecture-awareness-report.md', entities, journeys, actions)

    print(f"wrote {out_graphs / 'architecture-awareness.json'}")
    print(f"wrote {out_graphs / 'architecture-awareness.csv'}")
    print(f"wrote {out_graphs / 'architecture-graph.md'}")
    print(f"wrote {out_graphs / 'architecture-graph.mmd'}")
    print(f"wrote {out_graphs / 'function-journey-index.json'}")
    print(f"wrote {out_graphs / 'user-action-index.json'}")
    print(f"wrote {root / 'docs' / 'status' / 'architecture-awareness-report.md'}")
    print(f"entities={len(entities)}")
    print(f"chains={journeys['summary']['counts']['chains']}")
    print(f"actions={actions['summary']['counts']['actions']}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
