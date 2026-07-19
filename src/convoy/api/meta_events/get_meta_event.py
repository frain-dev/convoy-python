from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_meta_event_response_200 import GetMetaEventResponse200
from ...models.get_meta_event_response_400 import GetMetaEventResponse400
from ...models.get_meta_event_response_401 import GetMetaEventResponse401
from ...models.get_meta_event_response_404 import GetMetaEventResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    meta_event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/meta-events/{meta_event_id}".format(
            project_id=quote(str(project_id), safe=""),
            meta_event_id=quote(str(meta_event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetMetaEventResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetMetaEventResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetMetaEventResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMetaEventResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    meta_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
]:
    """Retrieve a meta event

     This endpoint retrieves a meta event

    Args:
        project_id (str):
        meta_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetaEventResponse200 | GetMetaEventResponse400 | GetMetaEventResponse401 | GetMetaEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        meta_event_id=meta_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    meta_event_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
    | None
):
    """Retrieve a meta event

     This endpoint retrieves a meta event

    Args:
        project_id (str):
        meta_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetaEventResponse200 | GetMetaEventResponse400 | GetMetaEventResponse401 | GetMetaEventResponse404
    """

    return sync_detailed(
        project_id=project_id,
        meta_event_id=meta_event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    meta_event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
]:
    """Retrieve a meta event

     This endpoint retrieves a meta event

    Args:
        project_id (str):
        meta_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMetaEventResponse200 | GetMetaEventResponse400 | GetMetaEventResponse401 | GetMetaEventResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        meta_event_id=meta_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    meta_event_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetMetaEventResponse200
    | GetMetaEventResponse400
    | GetMetaEventResponse401
    | GetMetaEventResponse404
    | None
):
    """Retrieve a meta event

     This endpoint retrieves a meta event

    Args:
        project_id (str):
        meta_event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMetaEventResponse200 | GetMetaEventResponse400 | GetMetaEventResponse401 | GetMetaEventResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            meta_event_id=meta_event_id,
            client=client,
        )
    ).parsed
