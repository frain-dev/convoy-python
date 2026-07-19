from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_source_response_201 import CreateSourceResponse201
from ...models.create_source_response_400 import CreateSourceResponse400
from ...models.create_source_response_401 import CreateSourceResponse401
from ...models.create_source_response_404 import CreateSourceResponse404
from ...models.models_create_source import ModelsCreateSource
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsCreateSource,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/sources".format(
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
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
    | None
):
    if response.status_code == 201:
        response_201 = CreateSourceResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateSourceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateSourceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateSourceResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
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
    body: ModelsCreateSource,
) -> Response[
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
]:
    """Create a source

     This endpoint creates a source

    Args:
        project_id (str):
        body (ModelsCreateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSourceResponse201 | CreateSourceResponse400 | CreateSourceResponse401 | CreateSourceResponse404]
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
    body: ModelsCreateSource,
) -> (
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
    | None
):
    """Create a source

     This endpoint creates a source

    Args:
        project_id (str):
        body (ModelsCreateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSourceResponse201 | CreateSourceResponse400 | CreateSourceResponse401 | CreateSourceResponse404
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
    body: ModelsCreateSource,
) -> Response[
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
]:
    """Create a source

     This endpoint creates a source

    Args:
        project_id (str):
        body (ModelsCreateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSourceResponse201 | CreateSourceResponse400 | CreateSourceResponse401 | CreateSourceResponse404]
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
    body: ModelsCreateSource,
) -> (
    CreateSourceResponse201
    | CreateSourceResponse400
    | CreateSourceResponse401
    | CreateSourceResponse404
    | None
):
    """Create a source

     This endpoint creates a source

    Args:
        project_id (str):
        body (ModelsCreateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSourceResponse201 | CreateSourceResponse400 | CreateSourceResponse401 | CreateSourceResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
