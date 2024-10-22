# convoy-python
Convoy SDK for Python

This is the Convoy Python SDK. This SDK contains methods for easily interacting with Convoy's API. Below are examples to get you started. See our [API Reference](https://docs.getconvoy.io/api-reference/welcome) for more.


## Installation
Install convoy-python with

```bash
pip install convoy-python
```

## Setup Client
Next, import the `convoy` module and setup with your auth credentials.

```python
from convoy import Convoy
convoy = Convoy({"api_key":"your_api_key", "project_id": "your_project_id"})
```
The SDK also supports authenticating via Basic Auth by defining your username and password.

In the event you're using a self-hosted convoy instance, you can define the `uri` as part of what is passed into the convoy's constructor.

```python
convoy = Convoy({ "api_key": 'your_api_key', "uri": 'self-hosted-instance', "project_id": "your_project_id"})
```

## Usage

### Get all groups

```python
(response, status) = convoy.group.all({ "perPage": 10, "page": 1 })
```

### Create an Endpoint

An endpoint represents a target URL to receive events.

```python
endpointData = {
    "url": "https://0d87-102-89-2-172.ngrok.io",
    "description": "Default Endpoint",
    "secret": "endpoint-secret",
    "events": ["*"],
  }

(response, status) = convoy.endpoint.create({}, endpointData)
endpoint_id = response["data"]["uid"]
```

### Sending an Event

To send an event, you'll need the `uid` we created in the earlier section.

```python
eventData = {
    "endpoint_id": endpoint_id,
    "event_type": "payment.success",
    "data": {
      "event": "payment.success",
      "data": {
        "status": "Completed",
        "description": "Transaction Successful",
        "userID": "test_user_id808",
      },
    },
  }

(response, status) = convoy.event.create({}, eventData)
```

## Testing

```python
pytest ./test/test.py
```

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.MD) for details.


## Credits

- [Frain](https://github.com/frain-dev)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
