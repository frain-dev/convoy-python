from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_source import ModelsUpdateSource
from ...models.update_source_response_202 import UpdateSourceResponse202
from ...models.update_source_response_400 import UpdateSourceResponse400
from ...models.update_source_response_401 import UpdateSourceResponse401
from ...models.update_source_response_404 import UpdateSourceResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    source_id: str,
    *,
    body: ModelsUpdateSource,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/sources/{source_id}".format(
            project_id=quote(str(project_id), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
    | None
):
    if response.status_code == 202:
        response_202 = UpdateSourceResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UpdateSourceResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateSourceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateSourceResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
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
    body: ModelsUpdateSource,
) -> Response[
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
]:
    """Update a source

     This endpoint updates a source

    Args:
        project_id (str):
        source_id (str):
        body (ModelsUpdateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSourceResponse202 | UpdateSourceResponse400 | UpdateSourceResponse401 | UpdateSourceResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        body=body,
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
    body: ModelsUpdateSource,
) -> (
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
    | None
):
    """Update a source

     This endpoint updates a source

    Args:
        project_id (str):
        source_id (str):
        body (ModelsUpdateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSourceResponse202 | UpdateSourceResponse400 | UpdateSourceResponse401 | UpdateSourceResponse404
    """

    return sync_detailed(
        project_id=project_id,
        source_id=source_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateSource,
) -> Response[
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
]:
    """Update a source

     This endpoint updates a source

    Args:
        project_id (str):
        source_id (str):
        body (ModelsUpdateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSourceResponse202 | UpdateSourceResponse400 | UpdateSourceResponse401 | UpdateSourceResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        source_id=source_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    source_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateSource,
) -> (
    UpdateSourceResponse202
    | UpdateSourceResponse400
    | UpdateSourceResponse401
    | UpdateSourceResponse404
    | None
):
    """Update a source

     This endpoint updates a source

    Args:
        project_id (str):
        source_id (str):
        body (ModelsUpdateSource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSourceResponse202 | UpdateSourceResponse400 | UpdateSourceResponse401 | UpdateSourceResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            source_id=source_id,
            client=client,
            body=body,
        )
    ).parsed
