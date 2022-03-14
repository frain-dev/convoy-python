# convoy-python
Convoy SDK for Python

This is the Convoy Python SDK. This SDK contains methods for easily interacting with Convoy's API. Below are examples to get you started. For additional examples, please see our official documentation at (https://convoy.readme.io/reference)


## Installation
Install convoy-python with

```bash
pip install convoy-python
```

## Setup Client
Next, import the `convoy` module and setup with your auth credentials.

```python
from convoy import Convoy
convoy = Convoy({"api_key":"your_api_key"})
```
The SDK also supports authenticating via Basic Auth by defining your username and password.

```python
convoy = Convoy({"username":"default", "password":"default"})
```

In the event you're using a self hosted convoy instance, you can define the url as part of what is passed into convoy's constructor.

```python
convoy = Convoy({ "api_key": 'your_api_key', "uri": 'self-hosted-instance' })
```

## Usage

```python
content, status = convoy.group.all({ "perPage": 10, "page": 1 })

## Testing

```python
pytest ./test/test.py
```

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.


## Credits

- [Frain](https://github.com/frain-dev)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.