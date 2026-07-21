# convoy-python

Official Convoy Python SDK: an OpenAPI-generated API client plus hand-written webhook signature verification. See the [API Reference](https://getconvoy.io/docs/api-reference/welcome) for endpoint details.

Requires **Python 3.11+**.

## Installation

`1.0.0a1` is a pre-release. Plain `pip install convoy-python` still resolves to `0.2.0` until a final `1.0.0` is published.

```bash
pip install --pre convoy-python
# or pin explicitly:
pip install convoy-python==1.0.0a1
```

If you are upgrading from `0.2.0`, see [MIGRATION.md](./MIGRATION.md) and the release notes for the breaking changes.

## Setup Client

Construct an `AuthenticatedClient` with your instance API root and API key. The project ID is passed per call (it is not embedded in the client).

```python
from convoy import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://us.getconvoy.cloud/api",  # no /v1, no project id
    token="your_api_key",
)
project_id = "your_project_id"
```

Your base URL depends on where your project lives:

- Convoy Cloud (US): `https://us.getconvoy.cloud/api`
- Convoy Cloud (EU): `https://eu.getconvoy.cloud/api`
- Self-hosted: `https://your-instance/api`

## Usage

Each operation lives under `convoy.api.*` and exposes `sync`, `sync_detailed`, `asyncio`, and `asyncio_detailed`. Request bodies use typed models from `convoy.models`.

### Create an Endpoint

```python
from convoy.api.endpoints import create_endpoint
from convoy.models import ModelsCreateEndpoint

result = create_endpoint.sync(
    project_id,
    client=client,
    body=ModelsCreateEndpoint(
        name="default-endpoint",
        url="https://example.com/webhooks/convoy",
        secret="endpoint-secret",
    ),
)
endpoint_id = result.data.uid
```

### Send an Event

```python
from convoy.api.events import create_endpoint_event
from convoy.models import ModelsCreateEvent, ModelsCreateEventDataType0

body = ModelsCreateEvent(
    endpoint_id=endpoint_id,
    event_type="payment.success",
    data=ModelsCreateEventDataType0.from_dict({"status": "Completed"}),
)

result = create_endpoint_event.sync(project_id, client=client, body=body)
# async:
# result = await create_endpoint_event.asyncio(project_id, client=client, body=body)
```

### Verify Webhook Signatures

Verify with the raw request body, before parsing it. `verify_signature` returns a strict `True` / `False` (never a truthy error string).

```python
from convoy.utils.webhook import Webhook

webhook = Webhook(secret="endpoint-secret")

payload = request.body.decode("utf-8")
signature = request.headers.get("X-Convoy-Signature", "")

if not webhook.verify_signature(payload, signature):
    # reject the request
    ...
```

## Testing

```bash
pytest test/
```

## Generated API client

The HTTP API client under `src/convoy/api/` and `src/convoy/models/` is generated from Convoy's OpenAPI spec via [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). **Do not edit generated files by hand**; regenerate with `./scripts/generate.sh` (CI on `frain-dev/convoy` dispatches this when the spec changes).

Webhook signature verification remains hand-written (`src/convoy/utils/webhook.py`) and is covered by shared `test/signature-vectors.json`.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.MD) for details.

## Credits

- [Frain](https://github.com/frain-dev)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
