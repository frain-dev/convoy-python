from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_endpoint_fanout_event_response_201 import (
    CreateEndpointFanoutEventResponse201,
)
from ...models.create_endpoint_fanout_event_response_400 import (
    CreateEndpointFanoutEventResponse400,
)
from ...models.create_endpoint_fanout_event_response_401 import (
    CreateEndpointFanoutEventResponse401,
)
from ...models.create_endpoint_fanout_event_response_404 import (
    CreateEndpointFanoutEventResponse404,
)
from ...models.models_fanout_event import ModelsFanoutEvent
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsFanoutEvent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/events/fanout".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
    | None
):
    if response.status_code == 201:
        response_201 = CreateEndpointFanoutEventResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateEndpointFanoutEventResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateEndpointFanoutEventResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateEndpointFanoutEventResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsFanoutEvent,
) -> Response[
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
]:
    """Fan out an event

     This endpoint uses the owner_id to fan out an event to multiple endpoints.

    Args:
        project_id (str):
        body (ModelsFanoutEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEndpointFanoutEventResponse201 | CreateEndpointFanoutEventResponse400 | CreateEndpointFanoutEventResponse401 | CreateEndpointFanoutEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsFanoutEvent,
) -> (
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
    | None
):
    """Fan out an event

     This endpoint uses the owner_id to fan out an event to multiple endpoints.

    Args:
        project_id (str):
        body (ModelsFanoutEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEndpointFanoutEventResponse201 | CreateEndpointFanoutEventResponse400 | CreateEndpointFanoutEventResponse401 | CreateEndpointFanoutEventResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsFanoutEvent,
) -> Response[
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
]:
    """Fan out an event

     This endpoint uses the owner_id to fan out an event to multiple endpoints.

    Args:
        project_id (str):
        body (ModelsFanoutEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateEndpointFanoutEventResponse201 | CreateEndpointFanoutEventResponse400 | CreateEndpointFanoutEventResponse401 | CreateEndpointFanoutEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsFanoutEvent,
) -> (
    CreateEndpointFanoutEventResponse201
    | CreateEndpointFanoutEventResponse400
    | CreateEndpointFanoutEventResponse401
    | CreateEndpointFanoutEventResponse404
    | None
):
    """Fan out an event

     This endpoint uses the owner_id to fan out an event to multiple endpoints.

    Args:
        project_id (str):
        body (ModelsFanoutEvent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateEndpointFanoutEventResponse201 | CreateEndpointFanoutEventResponse400 | CreateEndpointFanoutEventResponse401 | CreateEndpointFanoutEventResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
