from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "query_architecture_graph.py"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_query_module():
    spec = importlib.util.spec_from_file_location("query_architecture_graph", SCRIPT_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sample_graph() -> dict:
    return {
        "generated_at": "2026-05-24",
        "nodes": [
            {
                "id": "FEAT-SAMPLE",
                "name": "Sample Feature",
                "type": "feature",
                "status": "verified",
                "layer": "cross_layer",
                "module": "sample",
                "feature": "sample_feature",
                "description": "A sample mapped feature.",
                "file_path": "docs/sample.md",
                "related_files": "",
                "parent_id": "",
                "child_ids": "UI-SAMPLE",
                "depends_on": "DOC-SAMPLE",
                "used_by": "",
                "ui_related": "UI-SAMPLE",
                "api_related": "",
                "database_related": "",
                "tests_related": "TEST-SAMPLE",
                "docs_related": "DOC-SAMPLE",
                "agent_related": "",
                "risk_level": "medium",
                "completion_percent": "95",
                "last_verified_at": "2026-05-24",
                "verification_status": "verified",
                "notes": "",
                "tags": "#sample #feature",
            },
            {
                "id": "UI-SAMPLE",
                "name": "Sample UI",
                "type": "ui_element",
                "status": "implemented",
                "layer": "frontend",
                "module": "sample",
                "feature": "sample_feature",
                "description": "A sample UI element.",
                "file_path": "web/src/sample.tsx",
                "related_files": "",
                "parent_id": "FEAT-SAMPLE",
                "child_ids": "",
                "depends_on": "FEAT-SAMPLE",
                "used_by": "",
                "ui_related": "",
                "api_related": "",
                "database_related": "",
                "tests_related": "",
                "docs_related": "",
                "agent_related": "",
                "risk_level": "medium",
                "completion_percent": "50",
                "last_verified_at": "2026-05-24",
                "verification_status": "implementation_evidence",
                "notes": "",
                "tags": "#sample #ui",
            },
            {
                "id": "TEST-SAMPLE",
                "name": "Sample Test",
                "type": "test",
                "status": "verified",
                "layer": "test",
                "module": "sample",
                "feature": "sample_feature",
                "description": "A sample test.",
                "file_path": "backend/tests/test_sample.py",
                "related_files": "",
                "parent_id": "FEAT-SAMPLE",
                "child_ids": "",
                "depends_on": "FEAT-SAMPLE",
                "used_by": "",
                "ui_related": "",
                "api_related": "",
                "database_related": "",
                "tests_related": "TEST-SAMPLE",
                "docs_related": "DOC-SAMPLE",
                "agent_related": "",
                "risk_level": "low",
                "completion_percent": "100",
                "last_verified_at": "2026-05-24",
                "verification_status": "verified",
                "notes": "",
                "tags": "#sample #test",
            },
            {
                "id": "FILE-AUTO-SAMPLE",
                "name": "auto_sample.py",
                "type": "file",
                "status": "implemented",
                "layer": "backend",
                "module": "sample",
                "feature": "inventory",
                "description": "Auto row with missing proof.",
                "file_path": "backend/auto_sample.py",
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
                "risk_level": "medium",
                "completion_percent": "70",
                "last_verified_at": "2026-05-24",
                "verification_status": "implementation_evidence",
                "notes": "",
                "tags": "#auto",
            },
        ],
        "relations": [
            {
                "id": "REL-SAMPLE-001",
                "source_id": "FEAT-SAMPLE",
                "relation_type": "parent_of",
                "target_id": "UI-SAMPLE",
                "status": "verified",
                "description": "Feature owns the UI element.",
                "evidence": "docs/sample.md",
                "notes": "",
                "tags": "#sample",
            },
            {
                "id": "REL-SAMPLE-002",
                "source_id": "TEST-SAMPLE",
                "relation_type": "verifies",
                "target_id": "FEAT-SAMPLE",
                "status": "verified",
                "description": "Test verifies the feature.",
                "evidence": "backend/tests/test_sample.py",
                "notes": "",
                "tags": "#sample",
            },
        ],
        "chains": [
            {
                "id": "CHAIN-SAMPLE",
                "name": "Sample execution chain",
                "feature_id": "FEAT-SAMPLE",
                "status": "verified",
                "confidence": "high",
                "trigger_node_id": "UI-SAMPLE",
                "ordered_node_ids": "UI-SAMPLE>FEAT-SAMPLE>TEST-SAMPLE",
                "implementation_evidence": "docs/sample.md",
                "test_evidence": "backend/tests/test_sample.py",
                "behavior_evidence": "pytest",
                "connection_evidence": "REL-SAMPLE-001..002",
                "documentation_evidence": "DOC-SAMPLE",
                "missing_links": "none",
                "risk_level": "low",
                "last_verified_at": "2026-05-24",
                "notes": "",
                "tags": "#sample",
            }
        ],
        "evidence": [
            {
                "id": "EVID-SAMPLE",
                "node_id": "FEAT-SAMPLE",
                "evidence_type": "behavior",
                "status": "verified",
                "evidence_path": "backend/tests/test_sample.py",
                "command": "python -m pytest",
                "last_verified_at": "2026-05-24",
                "summary": "Sample feature is verified.",
                "notes": "",
                "tags": "#sample",
            }
        ],
        "research_sources": [],
        "theory_claims": [
            {
                "id": "CLAIM-SAMPLE",
                "node_id": "FEAT-SAMPLE",
                "claim": "Sample claim.",
                "claim_type": "architecture_theory",
                "status": "reviewed",
                "confidence": "medium",
                "source_ids": "SRC-1|SRC-2|SRC-3",
                "code_expression": "sample",
                "applicability_scope": "Test.",
                "limitations": "Test only.",
                "last_reviewed_at": "2026-05-24",
                "reviewer": "pytest",
                "notes": "",
                "tags": "#sample",
            }
        ],
    }


def test_query_node_includes_impact_chain_evidence_and_theory_claims() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    result = module.query_node(indexes, "FEAT-SAMPLE")

    assert result["node"]["name"] == "Sample Feature"
    assert [relation["id"] for relation in result["outgoing_relations"]] == ["REL-SAMPLE-001"]
    assert [relation["id"] for relation in result["incoming_relations"]] == ["REL-SAMPLE-002"]
    assert [chain["id"] for chain in result["chains"]] == ["CHAIN-SAMPLE"]
    assert [item["id"] for item in result["evidence"]] == ["EVID-SAMPLE"]
    assert [claim["id"] for claim in result["theory_claims"]] == ["CLAIM-SAMPLE"]
    assert result["gaps"] == []


def test_search_nodes_matches_description_and_tags() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    matches = module.search_nodes(indexes, "sample")

    match_ids = [node["id"] for node in matches]
    assert {"FEAT-SAMPLE", "TEST-SAMPLE", "UI-SAMPLE"}.issubset(match_ids)
    assert match_ids.index("FILE-AUTO-SAMPLE") > match_ids.index("UI-SAMPLE")


def test_gap_detection_flags_missing_proof_for_incomplete_ui_node() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    result = module.query_node(indexes, "UI-SAMPLE")

    assert "node status is implemented" in result["gaps"]
    assert "verification status is implementation_evidence" in result["gaps"]
    assert "tests_related is empty" in result["gaps"]
    assert "docs_related is empty" in result["gaps"]
    assert "no evidence rows" in result["gaps"]


def test_operational_gap_mode_ignores_strict_proof_requirements_for_auto_nodes() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    strict_result = module.query_node(indexes, "FILE-AUTO-SAMPLE", gap_mode="strict")
    operational_result = module.query_node(indexes, "FILE-AUTO-SAMPLE", gap_mode="operational")

    assert "tests_related is empty" in strict_result["gaps"]
    assert "docs_related is empty" in strict_result["gaps"]
    assert "no evidence rows" in strict_result["gaps"]
    assert operational_result["gaps"] == []


def test_chain_missing_links_do_not_overreport_on_model_nodes() -> None:
    module = load_query_module()
    graph = sample_graph()
    graph["nodes"][0]["type"] = "model"
    graph["chains"][0]["missing_links"] = "Future API work"
    indexes = module.build_indexes(graph)

    result = module.query_node(indexes, "FEAT-SAMPLE")

    assert "CHAIN-SAMPLE missing links: Future API work" not in result["gaps"]


def test_gap_report_excludes_auto_inventory_rows_by_default() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    report = module.gap_report(indexes)

    reported_ids = {item["node"]["id"] for item in report}
    assert "UI-SAMPLE" in reported_ids
    assert "FILE-AUTO-SAMPLE" not in reported_ids


def test_gap_report_can_include_auto_inventory_rows() -> None:
    module = load_query_module()
    indexes = module.build_indexes(sample_graph())

    report = module.gap_report(indexes, include_auto=True)

    assert "FILE-AUTO-SAMPLE" in {item["node"]["id"] for item in report}


def test_cli_json_output_for_known_node(tmp_path: Path, capsys) -> None:
    module = load_query_module()
    graph_path = tmp_path / "architecture-graph.json"
    graph_path.write_text(json.dumps(sample_graph()), encoding="utf-8")

    exit_code = module.run(["--graph", str(graph_path), "--node", "FEAT-SAMPLE", "--format", "json"])

    output = json.loads(capsys.readouterr().out)
    assert exit_code == 0
    assert output["node"]["id"] == "FEAT-SAMPLE"
    assert output["chains"][0]["id"] == "CHAIN-SAMPLE"


def test_cli_gap_report_json_output_excludes_auto_rows_by_default(tmp_path: Path, capsys) -> None:
    module = load_query_module()
    graph_path = tmp_path / "architecture-graph.json"
    graph_path.write_text(json.dumps(sample_graph()), encoding="utf-8")

    exit_code = module.run(["--graph", str(graph_path), "--gaps", "--format", "json"])

    output = json.loads(capsys.readouterr().out)
    reported_ids = {item["node"]["id"] for item in output["items"]}
    assert exit_code == 0
    assert output["include_auto"] is False
    assert "UI-SAMPLE" in reported_ids
    assert "FILE-AUTO-SAMPLE" not in reported_ids


def test_cli_fail_on_gaps_returns_nonzero_when_gaps_exist(tmp_path: Path, capsys) -> None:
    module = load_query_module()
    graph_path = tmp_path / "architecture-graph.json"
    graph_path.write_text(json.dumps(sample_graph()), encoding="utf-8")

    exit_code = module.run(["--graph", str(graph_path), "--gaps", "--fail-on-gaps", "--format", "json"])

    output = json.loads(capsys.readouterr().out)
    assert output["items"]
    assert exit_code == 1


def test_cli_fail_on_gaps_returns_zero_when_no_gaps_exist(tmp_path: Path, capsys) -> None:
    module = load_query_module()
    graph = sample_graph()
    graph["nodes"][1]["status"] = "verified"
    graph["nodes"][1]["verification_status"] = "verified"
    graph["nodes"][1]["tests_related"] = "TEST-SAMPLE"
    graph["nodes"][1]["docs_related"] = "DOC-SAMPLE"
    graph["evidence"].append(
        {
            "id": "EVID-UI-SAMPLE",
            "node_id": "UI-SAMPLE",
            "evidence_type": "behavior",
            "status": "verified",
            "evidence_path": "web/src/sample.tsx",
            "command": "",
            "last_verified_at": "2026-05-24",
            "summary": "UI sample is verified.",
            "notes": "",
            "tags": "#sample",
        }
    )
    graph["evidence"].append(
        {
            "id": "EVID-TEST-SAMPLE",
            "node_id": "TEST-SAMPLE",
            "evidence_type": "behavior",
            "status": "verified",
            "evidence_path": "backend/tests/test_sample.py",
            "command": "python -m pytest",
            "last_verified_at": "2026-05-24",
            "summary": "Test sample is verified.",
            "notes": "",
            "tags": "#sample",
        }
    )
    graph_path = tmp_path / "architecture-graph.json"
    graph_path.write_text(json.dumps(graph), encoding="utf-8")

    exit_code = module.run(["--graph", str(graph_path), "--gaps", "--fail-on-gaps", "--format", "json"])

    output = json.loads(capsys.readouterr().out)
    assert output["items"] == []
    assert exit_code == 0


def test_cli_missing_node_returns_nonzero_with_suggestions(tmp_path: Path, capsys) -> None:
    module = load_query_module()
    graph_path = tmp_path / "architecture-graph.json"
    graph_path.write_text(json.dumps(sample_graph()), encoding="utf-8")

    exit_code = module.run(["--graph", str(graph_path), "--node", "FEAT-UNKNOWN"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Unknown architecture node" in captured.err
    assert "FEAT-SAMPLE" in captured.err


def test_current_graph_query_smoke_for_architecture_workflow() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    result = module.query_node(indexes, "WORKFLOW-ARCH-GRAPH")

    assert result["node"]["status"] == "verified"
    assert any(chain["id"] == "CHAIN-ARCH-GRAPH-WORKFLOW" for chain in result["chains"])
    assert any(item["id"] == "EVID-ARCH-GRAPH-WORKFLOW-CLOSURE" for item in result["evidence"])


def test_current_graph_gap_audit_smoke_returns_curated_rows_or_zero_gap_state() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    report = module.gap_report(indexes, limit=10)

    assert all("#auto" not in item["node"]["tags"] for item in report)


def test_current_graph_event_ingress_has_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    result = module.query_node(indexes, "API-EVENT-INGRESS")

    assert any(item["id"] == "EVID-EVENT-INGRESS-API-PROOF" for item in result["evidence"])
    assert result["gaps"] == []


def test_current_graph_app_chat_api_and_event_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    api_result = module.query_node(indexes, "API-APP-CHAT-MESSAGE")
    event_result = module.query_node(indexes, "EVENT-APP-CHAT-TURN")

    assert any(item["id"] == "EVID-APPCHAT-API-PROOF" for item in api_result["evidence"])
    assert any(item["id"] == "EVID-APPCHAT-EVENT-PROOF" for item in event_result["evidence"])
    assert api_result["gaps"] == []
    assert event_result["gaps"] == []


def test_current_graph_runtime_memory_docs_and_features_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "DOC-MEMORY-SYSTEM",
        "DOC-RUNTIME-FLOW",
        "FEAT-EVENT-INGRESS",
        "FEAT-FOREGROUND-RUNTIME",
        "FEAT-MEMORY-FLOW",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_service_test_prompt_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "PROMPT-OPENAI-RUNTIME",
        "SERVICE-MEMORY-REPOSITORY",
        "SERVICE-RUNTIME-ORCHESTRATOR",
        "TEST-API-ROUTES",
        "TEST-MEMORY-REPOSITORY",
        "TEST-RUNTIME-PIPELINE",
        "TEST-SCHEMA-BASELINE",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_curated_medium_risk_cleanup_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "API-TOOLS-OVERVIEW",
        "DOC-PIPELINE-APP-CHAT",
        "TEST-WEB-ROUTE-SMOKE",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_runtime_agent_stage_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "AGENT-AFFECTIVE-ASSESSMENT",
        "AGENT-CONTEXT",
        "AGENT-MOTIVATION",
        "AGENT-PERCEPTION",
        "AGENT-PLANNING",
        "AGENT-ROLE",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_profile_settings_direct_proof_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "API-APP-ME",
        "MODEL-AION-PROFILE",
        "PAGE-SETTINGS",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_personality_overview_direct_proof_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "API-PERSONALITY-OVERVIEW",
        "PAGE-PERSONALITY",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_web_shell_component_node_has_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    result = module.query_node(indexes, "COMP-WEB-APP")
    assert result["gaps"] == []


def test_current_graph_telegram_feature_node_has_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    result = module.query_node(indexes, "FEAT-TELEGRAM")
    assert result["gaps"] == []


def test_current_graph_docs_pages_service_and_test_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "DOC-FRONTEND-ROUTE-MAP",
        "DOC-TOOLS-PIPELINE",
        "PAGE-DASHBOARD",
        "PAGE-TOOLS",
        "SERVICE-DELIVERY-ROUTER",
        "TEST-ARCH-GRAPH-QUERY",
        "TEST-CHAT-TRANSCRIPT",
        "TEST-CONNECTOR-POLICY",
        "TEST-DELIVERY-ROUTER",
        "TEST-PREFERENCES",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []


def test_current_graph_ui_and_workflow_nodes_have_no_gaps() -> None:
    module = load_query_module()
    indexes = module.build_indexes(module.load_graph(PROJECT_ROOT / "docs" / "architecture" / "graphs" / "architecture-graph.json"))

    for node_id in [
        "UI-CHAT-COMPOSER",
        "UI-CHAT-COGNITIVE-BELT",
        "WORKFLOW-ARCH-GRAPH",
        "WORKFLOW-ARCH-GRAPH-CI",
        "WORKFLOW-RESEARCH-EVIDENCE",
    ]:
        result = module.query_node(indexes, node_id)
        assert result["gaps"] == []
