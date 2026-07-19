from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deprecate_event_type_response_201 import DeprecateEventTypeResponse201
from ...models.deprecate_event_type_response_400 import DeprecateEventTypeResponse400
from ...models.deprecate_event_type_response_401 import DeprecateEventTypeResponse401
from ...models.deprecate_event_type_response_404 import DeprecateEventTypeResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    event_type_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/event-types/{event_type_id}/deprecate".format(
            project_id=quote(str(project_id), safe=""),
            event_type_id=quote(str(event_type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
    | None
):
    if response.status_code == 201:
        response_201 = DeprecateEventTypeResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = DeprecateEventTypeResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeprecateEventTypeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeprecateEventTypeResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
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
) -> Response[
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
]:
    """Deprecates an event type

     This endpoint deprecates an event type

    Args:
        project_id (str):
        event_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeprecateEventTypeResponse201 | DeprecateEventTypeResponse400 | DeprecateEventTypeResponse401 | DeprecateEventTypeResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_type_id=event_type_id,
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
) -> (
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
    | None
):
    """Deprecates an event type

     This endpoint deprecates an event type

    Args:
        project_id (str):
        event_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeprecateEventTypeResponse201 | DeprecateEventTypeResponse400 | DeprecateEventTypeResponse401 | DeprecateEventTypeResponse404
    """

    return sync_detailed(
        project_id=project_id,
        event_type_id=event_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
]:
    """Deprecates an event type

     This endpoint deprecates an event type

    Args:
        project_id (str):
        event_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeprecateEventTypeResponse201 | DeprecateEventTypeResponse400 | DeprecateEventTypeResponse401 | DeprecateEventTypeResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_type_id=event_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    event_type_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeprecateEventTypeResponse201
    | DeprecateEventTypeResponse400
    | DeprecateEventTypeResponse401
    | DeprecateEventTypeResponse404
    | None
):
    """Deprecates an event type

     This endpoint deprecates an event type

    Args:
        project_id (str):
        event_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeprecateEventTypeResponse201 | DeprecateEventTypeResponse400 | DeprecateEventTypeResponse401 | DeprecateEventTypeResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            event_type_id=event_type_id,
            client=client,
        )
    ).parsed
