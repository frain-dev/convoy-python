# convoy-python 1.x migration

## What changed

- The **public HTTP API client** is generated from Convoy's OpenAPI spec (`docs/v3/openapi3.yaml`) via [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
- **Webhook signature verification stays hand-written.** Generators do not own crypto. `src/convoy/utils/webhook.py` and the shared `test/signature-vectors.json` contract remain the source of truth for verify. The generation sync script (`scripts/generate.sh`) never touches `src/convoy/utils/`.

## Generator choice

Generation originally bootstrapped on Speakeasy, but the Speakeasy free tier allows one generated SDK per workspace and `convoy.js` holds that slot. The Speakeasy pipeline is kept **dormant** (`.speakeasy/`, `.genignore`, `.github/workflows/speakeasy_generation.yaml`) so the provider can be switched back without a rebuild; the active pipeline is openapi-python-client (`.github/workflows/sdk_generation.yaml`).

## Breaking change policy

Shipping the generated client is an intentional **1.x** break from the hand-written `0.x` surfaces. Method shapes are **not** silently preserved.

1. This PR wires openapi-python-client generation; the hand-written HTTP client stays removed and verify lives at `src/convoy/utils/webhook.py` (inside the generated module tree, so `from convoy.utils.webhook import Webhook` keeps resolving — `package_name_override: convoy` in `.openapi-python-client.yml`).
2. The first `sdk_generation.yaml` run opens a PR that adds the OpenAPI-generated client and publishes as `1.x`.
3. Consumers pin `0.x` until they migrate call sites.

## Verify (unchanged)

```python
from convoy.utils.webhook import Webhook

webhook = Webhook(secret="endpoint-secret")
payload = request.body.decode("utf-8")
signature = request.headers.get("X-Convoy-Signature", "")

if not webhook.verify_signature(payload, signature):
    raise PermissionError("invalid signature")
```

## Regenerating the API client

CI on `frain-dev/convoy` dispatches `sdk_generation.yaml` when OpenAPI artifacts change. Locally:

```bash
pip install openapi-python-client==0.29.0 ruff==0.15.22
./scripts/generate.sh
```
