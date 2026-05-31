from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from scripts.run_nonprod_entry_health_smoke import run_smoke


def _make_handler(debug_mode: str) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def _send_json(self, code: int, payload: dict[str, Any]) -> None:
            encoded = json.dumps(payload).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def _send_html(self, code: int, html: str) -> None:
            encoded = html.encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)

        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/health":
                self._send_json(
                    200,
                    {
                        "status": "ok",
                        "runtime_policy": {
                            "event_debug_shared_ingress_mode": debug_mode,
                        },
                    },
                )
                return
            if self.path == "/" or self.path.startswith("/nonprod-smoke-route"):
                self._send_html(
                    200,
                    '<html><head><meta name="aion-web-build-revision" content="abc123" /></head></html>',
                )
                return
            if self.path.startswith("/internal/state/inspect?"):
                self._send_json(200, {"ok": True})
                return
            self._send_json(404, {"detail": "not found"})

        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers.get("Content-Length", "0"))
            _ = self.rfile.read(length) if length > 0 else b""
            if self.path == "/event":
                self._send_json(200, {"event_id": "evt-1", "reply": {"message": "ok"}})
                return
            if self.path == "/event/debug":
                if debug_mode == "compatibility":
                    self._send_json(200, {"debug": {"ok": True}})
                    return
                if self.headers.get("X-AION-Debug-Break-Glass", "").lower() == "true":
                    self._send_json(200, {"debug": {"ok": True}})
                    return
                self._send_json(403, {"detail": "break glass required"})
                return
            self._send_json(404, {"detail": "not found"})

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A003
            return

    return Handler


def _run_server(debug_mode: str):
    server = ThreadingHTTPServer(("127.0.0.1", 0), _make_handler(debug_mode))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def test_nonprod_smoke_compatibility_mode_passes() -> None:
    server, thread = _run_server("compatibility")
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        report = run_smoke(
            base_url=base_url,
            text="compatibility smoke",
            user_id="u-1",
            frontend_probe_path="/nonprod-smoke-route",
        )
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()

    assert report["health"]["status"] == "ok"
    assert report["event"]["status_code"] == 200
    assert report["debug"]["shared_mode"] == "compatibility"
    assert report["debug"]["status_code"] == 200


def test_nonprod_smoke_break_glass_mode_uses_header_retry() -> None:
    server, thread = _run_server("break_glass_only")
    try:
        base_url = f"http://127.0.0.1:{server.server_address[1]}"
        report = run_smoke(
            base_url=base_url,
            text="break glass smoke",
            user_id="u-2",
            frontend_probe_path="/nonprod-smoke-route",
        )
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()

    assert report["debug"]["shared_mode"] == "break_glass_only"
    assert report["debug"]["status_code"] == 403
    assert report["debug"]["break_glass_status_code"] == 200
