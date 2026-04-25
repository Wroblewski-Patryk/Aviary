from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.core.config import get_settings
from app.core.database import Database
from app.core.logging import setup_logging
from app.memory.openai_embedding_client import OpenAIEmbeddingClient
from app.memory.repository import MemoryRepository


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run bounded runtime cleanup while preserving auth identities and profile state."
    )
    parser.add_argument(
        "--mode",
        choices=("single_user_runtime_reset", "runtime_only_preserve_auth"),
        required=True,
    )
    parser.add_argument("--user-id")
    parser.add_argument("--confirm-user-id")
    parser.add_argument("--confirm-runtime-cleanup", action="store_true")
    return parser.parse_args()


async def _run() -> int:
    args = _parse_args()
    settings = get_settings()
    settings.validate_required()
    setup_logging(settings.log_level)

    if args.mode == "single_user_runtime_reset":
        if not str(args.user_id or "").strip() or str(args.confirm_user_id or "").strip() != str(args.user_id).strip():
            print(
                json.dumps(
                    {
                        "status": "blocked_confirmation_required",
                        "mode": args.mode,
                        "user_id": args.user_id,
                    }
                )
            )
            return 2
    elif not bool(args.confirm_runtime_cleanup):
        print(
            json.dumps(
                {
                    "status": "blocked_confirmation_required",
                    "mode": args.mode,
                }
            )
        )
        return 2

    database = Database(settings.database_url)  # type: ignore[arg-type]
    openai_embedding_client = OpenAIEmbeddingClient(api_key=settings.openai_api_key)
    memory_repository = MemoryRepository(
        database.session_factory,
        embedding_provider=str(getattr(settings, "embedding_provider", "deterministic")),
        embedding_model=str(getattr(settings, "embedding_model", "deterministic-v1")),
        embedding_dimensions=int(getattr(settings, "embedding_dimensions", 32)),
        embedding_source_kinds=tuple(
            getattr(
                settings,
                "get_embedding_source_kinds",
                lambda: ("episodic", "semantic", "affective"),
            )()
        ),
        embedding_refresh_mode=str(getattr(settings, "embedding_refresh_mode", "on_write")),
        openai_api_key=settings.openai_api_key,
        openai_embedding_client=openai_embedding_client,
    )
    try:
        if args.mode == "single_user_runtime_reset":
            summary = await memory_repository.reset_user_runtime_data(
                user_id=str(args.user_id).strip()
            )
        else:
            summary = await memory_repository.cleanup_runtime_data_preserving_auth()
    finally:
        await database.dispose()

    print(json.dumps(summary))
    return 0


def main() -> int:
    return asyncio.run(_run())


if __name__ == "__main__":
    raise SystemExit(main())
