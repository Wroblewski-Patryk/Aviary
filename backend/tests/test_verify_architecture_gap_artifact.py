from __future__ import annotations

import json
from pathlib import Path

from scripts import verify_architecture_gap_artifact as verifier


def test_verify_gap_artifact_passes_for_empty_items(tmp_path: Path, capsys) -> None:
    artifact = tmp_path / "gaps.json"
    artifact.write_text(json.dumps({"include_auto": False, "items": []}), encoding="utf-8")

    exit_code = verifier.run(["--artifact", str(artifact)])

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "curated_gap_count=0" in output
    assert "status=PASSED" in output


def test_verify_gap_artifact_fails_for_non_empty_items(tmp_path: Path, capsys) -> None:
    artifact = tmp_path / "gaps.json"
    artifact.write_text(
        json.dumps({"include_auto": False, "items": [{"node": {"id": "FEAT-X"}, "gaps": ["no evidence rows"]}]}),
        encoding="utf-8",
    )

    exit_code = verifier.run(["--artifact", str(artifact)])

    output = capsys.readouterr().out
    assert exit_code == 1
    assert "curated_gap_count=1" in output
    assert "status=FAILED" in output
