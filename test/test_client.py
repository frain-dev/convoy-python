import pytest

from convoy import Convoy
from convoy.client import Client


def make_config(**overrides):
    config = {
        "api_key": "test-api-key",
        "uri": "https://us.getconvoy.cloud/api/v1",
        "project_id": "test-project-id",
    }
    config.update(overrides)
    return config


def test_client_builds_project_scoped_base_uri():
    client = Client(make_config())
    assert client.get_base_url() == "https://us.getconvoy.cloud/api/v1/projects/test-project-id"


def test_client_strips_trailing_slash_from_uri():
    client = Client(make_config(uri="https://us.getconvoy.cloud/api/v1/"))
    assert client.get_base_url() == "https://us.getconvoy.cloud/api/v1/projects/test-project-id"


def test_client_builds_resource_paths():
    client = Client(make_config())
    assert client.build_path("/endpoints") == "https://us.getconvoy.cloud/api/v1/projects/test-project-id/endpoints"
    assert client.build_path("") == "https://us.getconvoy.cloud/api/v1/projects/test-project-id"


def test_client_sets_bearer_authorization_header():
    client = Client(make_config())
    assert client.headers["Authorization"] == "Bearer test-api-key"


@pytest.mark.parametrize("missing", ["api_key", "uri", "project_id"])
def test_client_requires_config_values(missing):
    config = make_config()
    config[missing] = ""
    with pytest.raises(ValueError):
        Client(config)


@pytest.mark.parametrize("uri", [
    "https://us.getconvoy.cloud/api/v1/projects/test-project-id",
    "https://us.getconvoy.cloud/api/v1/projects",
    "https://us.getconvoy.cloud/api/v1/projects/",
])
def test_client_rejects_project_scoped_uri(uri):
    with pytest.raises(ValueError):
        Client(make_config(uri=uri))


def test_convoy_exposes_project_scoped_resources():
    convoy = Convoy(make_config())
    for resource in ["project", "endpoint", "event", "event_delivery", "delivery_attempt", "source", "subscription", "webhook"]:
        assert hasattr(convoy, resource)
    assert not hasattr(convoy, "group")
