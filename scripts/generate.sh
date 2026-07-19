#!/usr/bin/env bash
set -euo pipefail

# Regenerate the API client from Convoy's OpenAPI spec with
# openapi-python-client, then sync it into src/convoy/ without touching
# hand-owned paths (webhook verify, py.typed).
#
# Requires: openapi-python-client, rsync, curl. Run from the repo root.

SPEC_URL="${SPEC_URL:-https://raw.githubusercontent.com/frain-dev/convoy/main/docs/v3/openapi3.yaml}"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

curl -fsSL "$SPEC_URL" -o "$tmp/openapi3.yaml"

# --meta none emits only the package contents; project metadata is hand-owned
# in pyproject.toml.
# --fail-on-warning: a warning means the generator skipped part of the spec;
# never mirror a partial client into src/convoy (rsync --delete would drop
# previously generated modules).
openapi-python-client generate \
  --path "$tmp/openapi3.yaml" \
  --config .openapi-python-client.yml \
  --meta none \
  --fail-on-warning \
  --output-path "$tmp/gen"

# --delete keeps src/convoy an exact mirror of generator output; excluded
# paths are hand-written and never created or removed by this script.
# .ruff_cache is a side effect of the generator's post-processing formatter.
rsync -a --delete \
  --exclude 'utils/' \
  --exclude 'py.typed' \
  --exclude '.ruff_cache/' \
  "$tmp/gen/" src/convoy/

echo "Generated client synced into src/convoy/"
