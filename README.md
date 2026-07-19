# convoy-python

This is the official Convoy Python SDK. It contains methods for easily interacting with Convoy's API. Below are examples to get you started. See our [API Reference](https://getconvoy.io/docs/api-reference/welcome) for more.

## Installation

Install convoy-python with

```bash
pip install convoy-python
```

## Setup Client

Import the `convoy` module and set it up with your instance URL, API key, and project ID. Both the API key and project ID are available from your **Project Settings** page.

```python
from convoy import Convoy

convoy = Convoy({
    "api_key": "your_api_key",
    "uri": "https://us.getconvoy.cloud/api/v1",
    "project_id": "your_project_id",
})
```

Your instance URL depends on where your project lives:

- Convoy Cloud (US): `https://us.getconvoy.cloud/api/v1`
- Convoy Cloud (EU): `https://eu.getconvoy.cloud/api/v1`
- Self-hosted: `https://your-instance/api/v1`

## Usage

Each method takes a query dict and returns a `(response, status)` tuple.

### Create an Endpoint

An endpoint represents a target URL to receive events.

```python
endpoint_data = {
    "name": "default-endpoint",
    "url": "https://example.com/webhooks/convoy",
    "description": "Default Endpoint",
    "secret": "endpoint-secret",
}

(response, status) = convoy.endpoint.create({}, endpoint_data)
endpoint_id = response["data"]["uid"]
```

### Create a Subscription

Subscriptions route events from a source to an endpoint.

```python
subscription_data = {
    "name": "event-sub",
    "endpoint_id": endpoint_id,
}

(response, status) = convoy.subscription.create({}, subscription_data)
```

### Send an Event

To send an event, you'll need the `uid` of the endpoint we created earlier.

```python
event_data = {
    "endpoint_id": endpoint_id,
    "event_type": "payment.success",
    "data": {
        "status": "Completed",
        "description": "Transaction Successful",
    },
}

(response, status) = convoy.event.create({}, event_data)
```

To fan an event out to all endpoints with the same `owner_id`, or broadcast to every endpoint in the project:

```python
(response, status) = convoy.event.fanout({}, {"owner_id": "owner-1", "event_type": "payment.success", "data": {}})
(response, status) = convoy.event.broadcast({}, {"event_type": "payment.success", "data": {}})
```

### Verify Webhook Signatures

Verify with the raw request body, before parsing it. `verify_signature` returns `True` for a valid signature and `False` otherwise (it fails closed), so a plain boolean check is safe.

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
pytest test/test.py
```

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.MD) for details.

## Credits

- [Frain](https://github.com/frain-dev)

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

## Generated API client

The HTTP API client is generated from Convoy's OpenAPI spec via [openapi-python-client](https://github.com/openapi-generators/openapi-python-client). **Webhook signature verification remains hand-written** (`convoy/utils/webhook.py`) and is covered by shared `test/signature-vectors.json`. See [MIGRATION.md](./MIGRATION.md).
