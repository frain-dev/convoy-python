from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.replay_endpoint_event_response_200 import ReplayEndpointEventResponse200
from ...models.replay_endpoint_event_response_400 import ReplayEndpointEventResponse400
from ...models.replay_endpoint_event_response_401 import ReplayEndpointEventResponse401
from ...models.replay_endpoint_event_response_404 import ReplayEndpointEventResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/events/{event_id}/replay".format(
            project_id=quote(str(project_id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ReplayEndpointEventResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ReplayEndpointEventResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ReplayEndpointEventResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ReplayEndpointEventResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
]:
    """Replay event

     This endpoint replays an event afresh assuming it is a new event.

    Args:
        project_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReplayEndpointEventResponse200 | ReplayEndpointEventResponse400 | ReplayEndpointEventResponse401 | ReplayEndpointEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
    | None
):
    """Replay event

     This endpoint replays an event afresh assuming it is a new event.

    Args:
        project_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReplayEndpointEventResponse200 | ReplayEndpointEventResponse400 | ReplayEndpointEventResponse401 | ReplayEndpointEventResponse404
    """

    return sync_detailed(
        project_id=project_id,
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
]:
    """Replay event

     This endpoint replays an event afresh assuming it is a new event.

    Args:
        project_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReplayEndpointEventResponse200 | ReplayEndpointEventResponse400 | ReplayEndpointEventResponse401 | ReplayEndpointEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    ReplayEndpointEventResponse200
    | ReplayEndpointEventResponse400
    | ReplayEndpointEventResponse401
    | ReplayEndpointEventResponse404
    | None
):
    """Replay event

     This endpoint replays an event afresh assuming it is a new event.

    Args:
        project_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReplayEndpointEventResponse200 | ReplayEndpointEventResponse400 | ReplayEndpointEventResponse401 | ReplayEndpointEventResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            event_id=event_id,
            client=client,
        )
    ).parsed
