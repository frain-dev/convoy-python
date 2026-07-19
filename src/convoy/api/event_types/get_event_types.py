from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_types_response_200 import GetEventTypesResponse200
from ...models.get_event_types_response_400 import GetEventTypesResponse400
from ...models.get_event_types_response_401 import GetEventTypesResponse401
from ...models.get_event_types_response_404 import GetEventTypesResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/event-types".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetEventTypesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEventTypesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetEventTypesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetEventTypesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
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
) -> Response[
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
]:
    """Retrieves a project's event types

     This endpoint fetches the project's event types

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventTypesResponse200 | GetEventTypesResponse400 | GetEventTypesResponse401 | GetEventTypesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
    | None
):
    """Retrieves a project's event types

     This endpoint fetches the project's event types

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventTypesResponse200 | GetEventTypesResponse400 | GetEventTypesResponse401 | GetEventTypesResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
]:
    """Retrieves a project's event types

     This endpoint fetches the project's event types

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventTypesResponse200 | GetEventTypesResponse400 | GetEventTypesResponse401 | GetEventTypesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetEventTypesResponse200
    | GetEventTypesResponse400
    | GetEventTypesResponse401
    | GetEventTypesResponse404
    | None
):
    """Retrieves a project's event types

     This endpoint fetches the project's event types

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventTypesResponse200 | GetEventTypesResponse400 | GetEventTypesResponse401 | GetEventTypesResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
