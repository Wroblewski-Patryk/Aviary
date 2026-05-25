from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "generate_architecture_graph.py"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_graph_module():
    spec = importlib.util.spec_from_file_location("generate_architecture_graph", SCRIPT_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def node_row(node_id: str = "NODE-TEST") -> dict[str, str]:
    return {
        "id": node_id,
        "name": "Test Node",
        "type": "feature",
        "status": "verified",
        "layer": "test",
        "module": "architecture",
        "feature": "graph",
        "description": "Test node.",
        "file_path": "docs/test.md",
        "related_files": "",
        "parent_id": "",
        "child_ids": "",
        "depends_on": "",
        "used_by": "",
        "ui_related": "",
        "api_related": "",
        "database_related": "",
        "tests_related": "",
        "docs_related": "",
        "agent_related": "",
        "risk_level": "low",
        "completion_percent": "100",
        "last_verified_at": "2026-05-24",
        "verification_status": "verified",
        "notes": "",
        "tags": "#test",
    }


def source_row(source_id: str) -> dict[str, str]:
    return {
        "id": source_id,
        "title": f"Source {source_id}",
        "authors": "Researcher",
        "year": "2026",
        "field": "neuroscience",
        "source_type": "review",
        "publication": "Journal",
        "doi": "10.0000/test",
        "url": f"https://example.test/{source_id}",
        "relevance_summary": "Supports the test claim.",
        "review_status": "reviewed",
        "last_reviewed_at": "2026-05-24",
        "notes": "",
        "tags": "#research",
    }


def theory_claim_row(*, source_ids: str, status: str = "reviewed") -> dict[str, str]:
    return {
        "id": "CLAIM-TEST",
        "node_id": "NODE-TEST",
        "claim": "A reviewed claim needs enough sources.",
        "claim_type": "architecture_theory",
        "status": status,
        "confidence": "medium",
        "source_ids": source_ids,
        "code_expression": "test -> claim",
        "applicability_scope": "Test scope.",
        "limitations": "Test limitation.",
        "last_reviewed_at": "2026-05-24",
        "reviewer": "pytest",
        "notes": "",
        "tags": "#theory",
    }


def registry_with_claim(module, claim: dict[str, str], sources: list[dict[str, str]]):
    return module.Registry(
        nodes=[node_row()],
        relations=[],
        chains=[],
        evidence=[],
        research_sources=sources,
        theory_claims=[claim],
    )


def test_reviewed_theory_claim_requires_at_least_three_research_sources() -> None:
    module = load_graph_module()
    sources = [source_row("SRC-1"), source_row("SRC-2")]
    claim = theory_claim_row(source_ids="SRC-1|SRC-2")

    errors = module.validate_registry(registry_with_claim(module, claim, sources))

    assert any("needs at least 3 research sources" in error for error in errors)


def test_reviewed_theory_claim_accepts_three_existing_research_sources() -> None:
    module = load_graph_module()
    sources = [source_row("SRC-1"), source_row("SRC-2"), source_row("SRC-3")]
    claim = theory_claim_row(source_ids="SRC-1|SRC-2|SRC-3")

    errors = module.validate_registry(registry_with_claim(module, claim, sources))

    assert errors == []


def test_graph_export_includes_research_sources_and_theory_claims(tmp_path: Path) -> None:
    module = load_graph_module()
    sources = [source_row("SRC-1"), source_row("SRC-2"), source_row("SRC-3")]
    claim = theory_claim_row(source_ids="SRC-1|SRC-2|SRC-3")
    registry = registry_with_claim(module, claim, sources)

    module.write_graph_exports(tmp_path, registry)

    graph = json.loads((tmp_path / "docs" / "architecture" / "graphs" / "architecture-graph.json").read_text())
    assert graph["research_sources"] == sources
    assert graph["theory_claims"] == [claim]


def test_current_repository_registry_validates_with_research_layer() -> None:
    module = load_graph_module()

    registry = module.load_registry(module.repo_root())
    errors = module.validate_registry(registry)
    nodes_by_id = {node["id"]: node for node in registry.nodes}
    relations_by_id = {relation["id"]: relation for relation in registry.relations}
    chains_by_id = {chain["id"]: chain for chain in registry.chains}

    assert errors == []
    assert len(registry.nodes) >= 50
    assert len(registry.research_sources) >= 21
    assert len(registry.theory_claims) >= 9
    assert any(claim["id"] == "CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS" for claim in registry.theory_claims)
    assert all(len(module.split_refs(claim["source_ids"])) >= 3 for claim in registry.theory_claims)
    assert nodes_by_id["WORKFLOW-ARCH-GRAPH"]["status"] == "verified"
    assert nodes_by_id["WORKFLOW-ARCH-GRAPH-CI"]["status"] == "verified"
    assert nodes_by_id["DOC-PR-TEMPLATE"]["status"] == "verified"
    assert nodes_by_id["SCRIPT-QUERY-ARCH-GRAPH"]["status"] == "verified"
    assert nodes_by_id["TEST-ARCH-GRAPH-QUERY"]["status"] == "verified"
    assert nodes_by_id["SCRIPT-GENERATE-ARCH-GRAPH"]["status"] == "verified"
    assert nodes_by_id["TEST-ARCH-GRAPH-GENERATOR"]["status"] == "verified"
    assert relations_by_id["REL-EVENT-002"]["target_id"] == "API-EVENT-INGRESS"
    assert chains_by_id["CHAIN-ARCH-GRAPH-WORKFLOW"]["status"] == "verified"
    assert chains_by_id["CHAIN-PROFILE-SETTINGS"]["status"] == "verified"
    assert chains_by_id["CHAIN-APP-AUTH"]["status"] == "verified"
    assert chains_by_id["CHAIN-DATA-MODEL-SCHEMA"]["status"] == "verified"
    assert chains_by_id["CHAIN-TOOLS-OVERVIEW"]["status"] == "verified"
    assert chains_by_id["CHAIN-PERSONALITY-OVERVIEW"]["status"] == "verified"


def test_current_repository_research_rollup_can_be_written_to_temp_dir(tmp_path: Path) -> None:
    module = load_graph_module()
    registry = module.load_registry(module.repo_root())

    module.write_research_rollup(tmp_path, registry)

    rollup = (tmp_path / "docs" / "testing" / "architecture-research-map.md").read_text(encoding="utf-8")
    assert "Architecture Research Map" in rollup
    assert "CLAIM-AFFECTIVE-SIGNAL-INTEGRATION" in rollup
    assert "CLAIM-ROLE-SOCIAL-POSTURE" in rollup
    assert "CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS" in rollup


def test_generated_graph_json_matches_current_registry_counts() -> None:
    module = load_graph_module()
    registry = module.load_registry(module.repo_root())
    graph_path = PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"

    graph = json.loads(graph_path.read_text(encoding="utf-8"))

    assert len(graph["nodes"]) == len(registry.nodes)
    assert len(graph["relations"]) == len(registry.relations)
    assert len(graph["chains"]) == len(registry.chains)
    assert len(graph["evidence"]) == len(registry.evidence)
    assert len(graph["research_sources"]) == len(registry.research_sources)
    assert len(graph["theory_claims"]) == len(registry.theory_claims)


def test_generated_rollups_include_latest_research_and_test_evidence() -> None:
    evidence_map = (PROJECT_ROOT / "docs" / "testing" / "architecture-evidence-map.md").read_text(encoding="utf-8")
    research_map = (PROJECT_ROOT / "docs" / "testing" / "architecture-research-map.md").read_text(encoding="utf-8")

    assert "EVID-APPCHAT-API-PROOF" in evidence_map
    assert "EVID-APPCHAT-EVENT-PROOF" in evidence_map
    assert "EVID-GRAPH-GENERATOR-PYTEST" in evidence_map
    assert "EVID-RESEARCH-UI-CHAT-COGNITIVE-BELT" in evidence_map
    assert "EVID-ARCH-GRAPH-WORKFLOW-CLOSURE" in evidence_map
    assert "EVID-PROFILE-SETTINGS-CHAIN-REFRESH" in evidence_map
    assert "EVID-TOOLS-OVERVIEW-CHAIN-REFRESH" in evidence_map
    assert "EVID-PERSONALITY-OVERVIEW-CHAIN-REFRESH" in evidence_map
    assert "EVID-AUTH-API-CHAIN-REFRESH" in evidence_map
    assert "EVID-DATA-MODEL-SCHEMA-CHAIN" in evidence_map
    assert "EVID-AION-MEMORY-MODEL-PROOF" in evidence_map
    assert "EVID-EVENT-INGRESS-API-PROOF" in evidence_map
    assert "EVID-EVENT-INGRESS-FEATURE-PROOF" in evidence_map
    assert "EVID-DOC-RUNTIME-FLOW" in evidence_map
    assert "EVID-DOC-MEMORY-SYSTEM" in evidence_map
    assert "EVID-PROMPT-OPENAI-RUNTIME-PROOF" in evidence_map
    assert "EVID-SERVICE-RUNTIME-ORCHESTRATOR-PROOF" in evidence_map
    assert "EVID-SERVICE-MEMORY-REPOSITORY-PROOF" in evidence_map
    assert "EVID-TEST-API-ROUTES-PROOF" in evidence_map
    assert "EVID-TEST-MEMORY-REPOSITORY-PROOF" in evidence_map
    assert "EVID-TEST-RUNTIME-PIPELINE-PROOF" in evidence_map
    assert "EVID-TEST-SCHEMA-BASELINE-PROOF" in evidence_map
    assert "EVID-API-TOOLS-OVERVIEW-PROOF" in evidence_map
    assert "EVID-DOC-PIPELINE-APP-CHAT-PROOF" in evidence_map
    assert "EVID-TEST-WEB-ROUTE-SMOKE-PROOF" in evidence_map
    assert "EVID-AGENT-PERCEPTION-PROOF" in evidence_map
    assert "EVID-AGENT-CONTEXT-PROOF" in evidence_map
    assert "EVID-AGENT-PLANNING-PROOF" in evidence_map
    assert "EVID-AGENT-ROLE-PROOF" in evidence_map
    assert "EVID-AGENT-MOTIVATION-PROOF" in evidence_map
    assert "EVID-AGENT-AFFECTIVE-ASSESSMENT-PROOF" in evidence_map
    assert "EVID-API-APP-ME-PROOF" in evidence_map
    assert "EVID-MODEL-AION-PROFILE-PROOF" in evidence_map
    assert "EVID-PAGE-SETTINGS-PROOF" in evidence_map
    assert "EVID-API-PERSONALITY-OVERVIEW-PROOF" in evidence_map
    assert "EVID-PAGE-PERSONALITY-PROOF" in evidence_map
    assert "EVID-COMP-WEB-APP-PROOF" in evidence_map
    assert "EVID-FEAT-TELEGRAM-PROOF" in evidence_map
    assert "EVID-DOC-FRONTEND-ROUTE-MAP-PROOF" in evidence_map
    assert "EVID-DOC-TOOLS-PIPELINE-PROOF" in evidence_map
    assert "EVID-PAGE-DASHBOARD-PROOF" in evidence_map
    assert "EVID-PAGE-TOOLS-PROOF" in evidence_map
    assert "EVID-SERVICE-DELIVERY-ROUTER-PROOF" in evidence_map
    assert "EVID-TEST-ARCH-GRAPH-QUERY-PROOF" in evidence_map
    assert "EVID-TEST-CHAT-TRANSCRIPT-PROOF" in evidence_map
    assert "EVID-TEST-CONNECTOR-POLICY-PROOF" in evidence_map
    assert "EVID-TEST-DELIVERY-ROUTER-PROOF" in evidence_map
    assert "EVID-TEST-PREFERENCES-PROOF" in evidence_map
    assert "EVID-UI-CHAT-COMPOSER-PROOF" in evidence_map
    assert "EVID-ARCH-GRAPH-CI-POLICY" in evidence_map
    assert "EVID-ARCH-PR-TEMPLATE-CHECKLIST" in evidence_map
    assert "EVID-ARCH-GRAPH-QUERY-CLI" in evidence_map
    assert "EVID-ARCH-GRAPH-GAP-AUDIT" in evidence_map
    assert "CLAIM-MOTIVATION-VALUATION-SELECTION" in research_map
    assert "CLAIM-ROLE-SOCIAL-POSTURE" in research_map
    assert "CLAIM-CHAT-COGNITIVE-BELT-LOAD-AWARENESS" in research_map


def test_generated_key_artifacts_match_current_generator_output(tmp_path: Path) -> None:
    module = load_graph_module()
    registry = module.load_registry(module.repo_root())

    module.write_relations_index(tmp_path, registry)
    module.write_chains_index(tmp_path, registry)
    module.write_graph_exports(tmp_path, registry)
    module.write_status_rollup(tmp_path, registry)
    module.write_evidence_rollup(tmp_path, registry)
    module.write_research_rollup(tmp_path, registry)

    artifact_paths = [
        "docs/architecture/graphs/architecture-graph.json",
        "docs/architecture/graphs/architecture-graph.mmd",
        "docs/architecture/relations/index.md",
        "docs/architecture/chains/index.md",
        "docs/status/architecture-map-status.md",
        "docs/testing/architecture-evidence-map.md",
        "docs/testing/architecture-research-map.md",
    ]
    for artifact_path in artifact_paths:
        generated = (tmp_path / artifact_path).read_text(encoding="utf-8")
        committed = (PROJECT_ROOT / artifact_path).read_text(encoding="utf-8")
        assert generated == committed, artifact_path


@pytest.mark.slow
def test_generated_node_pages_match_current_generator_output(tmp_path: Path) -> None:
    module = load_graph_module()
    registry = module.load_registry(module.repo_root())

    module.write_node_pages(tmp_path, registry)

    generated_nodes_dir = tmp_path / "docs" / "architecture" / "nodes"
    committed_nodes_dir = PROJECT_ROOT / "docs" / "architecture" / "nodes"
    generated_files = sorted(path.name for path in generated_nodes_dir.glob("*.md"))
    committed_files = sorted(path.name for path in committed_nodes_dir.glob("*.md"))

    assert generated_files == committed_files
    assert len(committed_files) == len(registry.nodes)

    for filename in generated_files:
        generated = (generated_nodes_dir / filename).read_text(encoding="utf-8")
        committed = (committed_nodes_dir / filename).read_text(encoding="utf-8")
        assert generated == committed, filename
