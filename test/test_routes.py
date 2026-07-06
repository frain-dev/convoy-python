import json

import pytest

from convoy import Convoy

BASE = "https://us.getconvoy.cloud/api/v1/projects/test-project-id"


class FakeResponse:
    status_code = 200

    def json(self):
        return {"status": True, "message": "ok", "data": None}


@pytest.fixture
def calls(monkeypatch):
    """Capture every outgoing request the client makes."""
    captured = []

    def recorder(method):
        def fake(url, headers=None, params=None, data=None):
            captured.append({
                "method": method,
                "url": url,
                "params": params,
                "body": json.loads(data) if data else None,
            })
            return FakeResponse()
        return fake

    monkeypatch.setattr("requests.get", recorder("GET"))
    monkeypatch.setattr("requests.post", recorder("POST"))
    monkeypatch.setattr("requests.put", recorder("PUT"))
    monkeypatch.setattr("requests.delete", recorder("DELETE"))
    return captured


@pytest.fixture
def convoy():
    return Convoy({
        "api_key": "test-api-key",
        "uri": "https://us.getconvoy.cloud/api/v1",
        "project_id": "test-project-id",
    })


def test_batch_retry_posts_empty_body_with_query_filters(convoy, calls):
    convoy.event_delivery.batchresend({"status": ["Failure"]})
    call = calls[0]
    assert call["method"] == "POST"
    assert call["url"] == BASE + "/eventdeliveries/batchretry"
    assert call["params"] == {"status": ["Failure"]}
    assert call["body"] == {}


def test_force_resend_posts_ids_body(convoy, calls):
    convoy.event_delivery.forceresend({}, {"ids": ["ed-1", "ed-2"]})
    call = calls[0]
    assert call["method"] == "POST"
    assert call["url"] == BASE + "/eventdeliveries/forceresend"
    assert call["body"] == {"ids": ["ed-1", "ed-2"]}


def test_endpoint_pause_uses_put_with_empty_body(convoy, calls):
    convoy.endpoint.pause("ep-1")
    call = calls[0]
    assert call["method"] == "PUT"
    assert call["url"] == BASE + "/endpoints/ep-1/pause"
    assert call["body"] == {}


def test_endpoint_expire_secret_uses_put(convoy, calls):
    convoy.endpoint.expire_secret("ep-1", {"expiration": 24})
    call = calls[0]
    assert call["method"] == "PUT"
    assert call["url"] == BASE + "/endpoints/ep-1/expire_secret"
    assert call["body"] == {"expiration": 24}


def test_endpoint_find_targets_single_endpoint(convoy, calls):
    convoy.endpoint.find("ep-1", {})
    assert calls[0]["url"] == BASE + "/endpoints/ep-1"


def test_event_fanout_posts_to_fanout(convoy, calls):
    convoy.event.fanout({}, {"owner_id": "owner-1", "event_type": "x", "data": {}})
    call = calls[0]
    assert call["method"] == "POST"
    assert call["url"] == BASE + "/events/fanout"


def test_event_broadcast_posts_to_broadcast(convoy, calls):
    convoy.event.broadcast({}, {"event_type": "x", "data": {}})
    call = calls[0]
    assert call["method"] == "POST"
    assert call["url"] == BASE + "/events/broadcast"


def test_event_replay_posts_to_replay(convoy, calls):
    convoy.event.replay("ev-1")
    call = calls[0]
    assert call["method"] == "PUT"
    assert call["url"] == BASE + "/events/ev-1/replay"


def test_project_find_targets_project_root(convoy, calls):
    convoy.project.find({})
    assert calls[0]["url"] == BASE
