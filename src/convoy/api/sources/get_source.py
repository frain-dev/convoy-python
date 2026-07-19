from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_source_response_200 import GetSourceResponse200
from ...models.get_source_response_400 import GetSourceResponse400
from ...models.get_source_response_401 import GetSourceResponse401
from ...models.get_source_response_404 import GetSourceResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    source_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/sources/{source_id}".format(
            project_id=quote(str(project_id), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSourceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSourceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSourceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSourceResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
]:
    """Retrieve a source

     This endpoint retrieves a source by its id

    Args:
        project_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSourceResponse200 | GetSourceResponse400 | GetSourceResponse401 | GetSourceResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
    | None
):
    """Retrieve a source

     This endpoint retrieves a source by its id

    Args:
        project_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSourceResponse200 | GetSourceResponse400 | GetSourceResponse401 | GetSourceResponse404
    """

    return sync_detailed(
        project_id=project_id,
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
]:
    """Retrieve a source

     This endpoint retrieves a source by its id

    Args:
        project_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSourceResponse200 | GetSourceResponse400 | GetSourceResponse401 | GetSourceResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetSourceResponse200
    | GetSourceResponse400
    | GetSourceResponse401
    | GetSourceResponse404
    | None
):
    """Retrieve a source

     This endpoint retrieves a source by its id

    Args:
        project_id (str):
        source_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSourceResponse200 | GetSourceResponse400 | GetSourceResponse401 | GetSourceResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            source_id=source_id,
            client=client,
        )
    ).parsed
