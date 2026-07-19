from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_event_type import ModelsUpdateEventType
from ...models.update_event_type_response_201 import UpdateEventTypeResponse201
from ...models.update_event_type_response_400 import UpdateEventTypeResponse400
from ...models.update_event_type_response_401 import UpdateEventTypeResponse401
from ...models.update_event_type_response_404 import UpdateEventTypeResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    event_type_id: str,
    *,
    body: ModelsUpdateEventType,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/event-types/{event_type_id}".format(
            project_id=quote(str(project_id), safe=""),
            event_type_id=quote(str(event_type_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
    | None
):
    if response.status_code == 201:
        response_201 = UpdateEventTypeResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UpdateEventTypeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateEventTypeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateEventTypeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEventType,
) -> Response[
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
]:
    """Updates an event type

     This endpoint updates an event type

    Args:
        project_id (str):
        event_type_id (str):
        body (ModelsUpdateEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEventTypeResponse201 | UpdateEventTypeResponse400 | UpdateEventTypeResponse401 | UpdateEventTypeResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_type_id=event_type_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEventType,
) -> (
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
    | None
):
    """Updates an event type

     This endpoint updates an event type

    Args:
        project_id (str):
        event_type_id (str):
        body (ModelsUpdateEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEventTypeResponse201 | UpdateEventTypeResponse400 | UpdateEventTypeResponse401 | UpdateEventTypeResponse404
    """

    return sync_detailed(
        project_id=project_id,
        event_type_id=event_type_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEventType,
) -> Response[
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
]:
    """Updates an event type

     This endpoint updates an event type

    Args:
        project_id (str):
        event_type_id (str):
        body (ModelsUpdateEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEventTypeResponse201 | UpdateEventTypeResponse400 | UpdateEventTypeResponse401 | UpdateEventTypeResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_type_id=event_type_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEventType,
) -> (
    UpdateEventTypeResponse201
    | UpdateEventTypeResponse400
    | UpdateEventTypeResponse401
    | UpdateEventTypeResponse404
    | None
):
    """Updates an event type

     This endpoint updates an event type

    Args:
        project_id (str):
        event_type_id (str):
        body (ModelsUpdateEventType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEventTypeResponse201 | UpdateEventTypeResponse400 | UpdateEventTypeResponse401 | UpdateEventTypeResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            event_type_id=event_type_id,
            client=client,
            body=body,
        )
    ).parsed
