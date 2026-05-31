#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from typing import Any


@dataclass
class HttpResult:
    status: int
    body: Any
    raw_text: str


def _request_json(
    method: str,
    url: str,
    payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 30,
) -> HttpResult:
    request_headers = {"Accept": "application/json"}
    if headers:
        request_headers.update(headers)
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json; charset=utf-8"

    req = urllib.request.Request(url=url, method=method, headers=request_headers, data=data)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
            parsed = json.loads(raw) if raw else {}
            return HttpResult(status=response.status, body=parsed, raw_text=raw)
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8") if exc.fp else ""
        parsed = {}
        if raw:
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                parsed = {}
        return HttpResult(status=exc.code, body=parsed, raw_text=raw)


def _request_text(url: str, timeout: int = 30) -> tuple[int, str]:
    req = urllib.request.Request(url=url, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.status, response.read().decode("utf-8")


def _extract_web_revision(index_html: str) -> str:
    match = re.search(
        r'<meta\s+name="aion-web-build-revision"\s+content="(?P<revision>[^"]*)"\s*/?>',
        index_html,
        flags=re.IGNORECASE,
    )
    if not match:
        raise RuntimeError("Public-entry smoke failed: missing aion-web-build-revision meta on '/'.")
    revision = match.group("revision").strip()
    if not revision:
        raise RuntimeError("Public-entry smoke failed: empty aion-web-build-revision meta on '/'.")
    return revision


def run_smoke(base_url: str, text: str, user_id: str, frontend_probe_path: str) -> dict[str, Any]:
    root = base_url.rstrip("/")
    trace_id = str(uuid.uuid4())

    health = _request_json("GET", f"{root}/health")
    if health.status != 200:
        raise RuntimeError(f"Health smoke failed: GET /health returned {health.status}.")
    if not isinstance(health.body, dict) or health.body.get("status") != "ok":
        raise RuntimeError("Health smoke failed: /health does not report status=ok.")

    runtime_policy = health.body.get("runtime_policy") if isinstance(health.body, dict) else None
    if not isinstance(runtime_policy, dict):
        raise RuntimeError("Health smoke failed: /health missing runtime_policy.")
    debug_shared_mode = str(runtime_policy.get("event_debug_shared_ingress_mode", "")).strip()
    if debug_shared_mode not in {"compatibility", "break_glass_only"}:
        raise RuntimeError(
            "Health smoke failed: unsupported event_debug_shared_ingress_mode "
            f"{debug_shared_mode!r}."
        )

    root_status, root_html = _request_text(f"{root}/")
    if root_status != 200:
        raise RuntimeError(f"Public-entry smoke failed: GET / returned {root_status}.")
    web_revision = _extract_web_revision(root_html)

    probe_path = "/" + frontend_probe_path.lstrip("/")
    probe_status, probe_html = _request_text(f"{root}{probe_path}")
    if probe_status != 200:
        raise RuntimeError(f"Public-entry smoke failed: GET {probe_path} returned {probe_status}.")
    if web_revision not in probe_html:
        raise RuntimeError(
            f"Public-entry smoke failed: GET {probe_path} does not carry matching build revision meta."
        )

    inspect_url = f"{root}/internal/state/inspect?{urllib.parse.urlencode({'user_id': user_id})}"
    inspect = _request_json("GET", inspect_url)
    if inspect.status != 200:
        raise RuntimeError(f"Internal health smoke failed: GET /internal/state/inspect returned {inspect.status}.")

    event_payload = {"source": "api", "text": text, "meta": {"user_id": user_id, "trace_id": trace_id}}
    event = _request_json("POST", f"{root}/event", payload=event_payload)
    if event.status != 200:
        raise RuntimeError(f"Event smoke failed: POST /event returned {event.status}.")
    if not isinstance(event.body, dict) or not event.body.get("event_id"):
        raise RuntimeError("Event smoke failed: /event response missing event_id.")

    debug_payload = {"text": "LUC-945 debug smoke", "meta": {"trace_id": trace_id}}
    debug = _request_json("POST", f"{root}/event/debug", payload=debug_payload)
    debug_break_glass = None
    if debug_shared_mode == "compatibility":
        if debug.status != 200:
            raise RuntimeError(
                f"Debug smoke failed: expected /event/debug compatibility 200, got {debug.status}."
            )
    else:
        if debug.status == 200:
            pass
        else:
            if debug.status not in {400, 401, 403, 422}:
                raise RuntimeError(
                    f"Debug smoke failed: unexpected /event/debug status in break-glass mode: {debug.status}."
                )
            debug_break_glass = _request_json(
                "POST",
                f"{root}/event/debug",
                payload=debug_payload,
                headers={"X-AION-Debug-Break-Glass": "true"},
            )
            if debug_break_glass.status != 200:
                raise RuntimeError(
                    "Debug smoke failed: break-glass request to /event/debug did not return 200 "
                    f"(got {debug_break_glass.status})."
                )

    return {
        "kind": "nonprod_entry_health_smoke_report",
        "base_url": root,
        "public_entry": {"root_status": root_status, "probe_path": probe_path, "probe_status": probe_status},
        "health": {"status_code": health.status, "status": health.body.get("status")},
        "internal_state_inspect": {"status_code": inspect.status},
        "event": {"status_code": event.status, "event_id": event.body.get("event_id")},
        "debug": {
            "shared_mode": debug_shared_mode,
            "status_code": debug.status,
            "break_glass_status_code": None if debug_break_glass is None else debug_break_glass.status,
        },
        "web_build_revision": web_revision,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a lightweight non-prod smoke guard for public-entry and internal health surfaces."
    )
    parser.add_argument("--base-url", required=True, help="Base URL, e.g. http://127.0.0.1:8000")
    parser.add_argument("--text", default="LUC-945 smoke event")
    parser.add_argument("--user-id", default="luc-945-smoke")
    parser.add_argument(
        "--frontend-probe-path",
        default="/nonprod-smoke-route",
        help="Path used to verify frontend catch-all route behavior.",
    )
    args = parser.parse_args()

    try:
        report = run_smoke(
            base_url=args.base_url,
            text=args.text,
            user_id=args.user_id,
            frontend_probe_path=args.frontend_probe_path,
        )
    except Exception as exc:  # noqa: BLE001
        print(str(exc), file=sys.stderr)
        return 1

    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
