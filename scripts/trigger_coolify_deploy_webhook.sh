#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <webhook_url> <webhook_secret> [repository] [branch] [before_sha] [after_sha] [pusher_name]"
  exit 1
fi

WEBHOOK_URL="$1"
WEBHOOK_SECRET="$2"
REPOSITORY="${3:-}"
BRANCH="${4:-main}"
BEFORE_SHA="${5:-}"
AFTER_SHA="${6:-}"
PUSHER_NAME="${7:-codex}"

git_value() {
  git "$@" 2>/dev/null || true
}

if [[ -z "$REPOSITORY" ]]; then
  REMOTE_URL="$(git_value config --get remote.origin.url | tr -d '\r\n')"
  if [[ "$REMOTE_URL" =~ github\.com[:/]([^[:space:]]+?)(\.git)?$ ]]; then
    REPOSITORY="${BASH_REMATCH[1]}"
  fi
fi

if [[ -z "$REPOSITORY" ]]; then
  echo "Could not infer repository name from git remote. Pass repository as owner/name." >&2
  exit 1
fi

if [[ -z "$AFTER_SHA" ]]; then
  AFTER_SHA="$(git_value rev-parse HEAD | tr -d '\r\n')"
fi

if [[ -z "$AFTER_SHA" ]]; then
  echo "Could not determine HEAD commit. Pass after_sha explicitly." >&2
  exit 1
fi

if [[ -z "$BEFORE_SHA" ]]; then
  BEFORE_SHA="$(git_value rev-parse "${AFTER_SHA}^" | tr -d '\r\n')"
fi

if [[ -z "$BEFORE_SHA" ]]; then
  BEFORE_SHA="$AFTER_SHA"
fi

COMMIT_MESSAGE="$(git_value log -1 --pretty=%s "$AFTER_SHA" | tr -d '\r\n')"
if [[ -z "$COMMIT_MESSAGE" ]]; then
  COMMIT_MESSAGE="manual deploy trigger"
fi

REPOSITORY="$REPOSITORY" \
BRANCH="$BRANCH" \
BEFORE_SHA="$BEFORE_SHA" \
AFTER_SHA="$AFTER_SHA" \
COMMIT_MESSAGE="$COMMIT_MESSAGE" \
PUSHER_NAME="$PUSHER_NAME" \
WEBHOOK_SECRET="$WEBHOOK_SECRET" \
WEBHOOK_URL="$WEBHOOK_URL" \
python3 - <<'PY'
import hashlib
import hmac
import json
import os
import sys
import urllib.request

repository = os.environ["REPOSITORY"]
branch = os.environ["BRANCH"]
before_sha = os.environ["BEFORE_SHA"]
after_sha = os.environ["AFTER_SHA"]
commit_message = os.environ["COMMIT_MESSAGE"]
pusher_name = os.environ["PUSHER_NAME"]
webhook_secret = os.environ["WEBHOOK_SECRET"].encode()
webhook_url = os.environ["WEBHOOK_URL"]

payload = {
    "ref": f"refs/heads/{branch}",
    "before": before_sha,
    "after": after_sha,
    "compare": f"https://github.com/{repository}/compare/{before_sha}...{after_sha}",
    "created": False,
    "deleted": False,
    "forced": False,
    "base_ref": None,
    "commits": [
        {
            "id": after_sha,
            "message": commit_message,
            "timestamp": "2026-01-01T00:00:00Z",
            "url": f"https://github.com/{repository}/commit/{after_sha}",
            "author": {"name": pusher_name, "email": ""},
            "committer": {"name": pusher_name, "email": ""},
            "added": [],
            "removed": [],
            "modified": [],
        }
    ],
    "head_commit": {
        "id": after_sha,
        "message": commit_message,
        "timestamp": "2026-01-01T00:00:00Z",
        "url": f"https://github.com/{repository}/commit/{after_sha}",
        "author": {"name": pusher_name, "email": ""},
        "committer": {"name": pusher_name, "email": ""},
        "added": [],
        "removed": [],
        "modified": [],
    },
    "repository": {
        "name": repository.split("/")[-1],
        "full_name": repository,
        "private": False,
        "default_branch": branch,
        "html_url": f"https://github.com/{repository}",
        "clone_url": f"https://github.com/{repository}.git",
        "ssh_url": f"git@github.com:{repository}.git",
        "owner": {
            "name": repository.split("/")[0],
            "login": repository.split("/")[0],
        },
    },
    "pusher": {"name": pusher_name},
    "sender": {"login": pusher_name},
}

body = json.dumps(payload).encode()
signature = "sha256=" + hmac.new(webhook_secret, body, hashlib.sha256).hexdigest()

request = urllib.request.Request(
    webhook_url,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-GitHub-Event": "push",
        "X-Hub-Signature-256": signature,
        "User-Agent": "aion-coolify-webhook-trigger",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=30) as response:
    sys.stdout.write(response.read().decode())
    sys.stdout.write("\n")
PY
