from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_endpoint import ModelsUpdateEndpoint
from ...models.update_endpoint_response_202 import UpdateEndpointResponse202
from ...models.update_endpoint_response_400 import UpdateEndpointResponse400
from ...models.update_endpoint_response_401 import UpdateEndpointResponse401
from ...models.update_endpoint_response_404 import UpdateEndpointResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    endpoint_id: str,
    *,
    body: ModelsUpdateEndpoint,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/endpoints/{endpoint_id}".format(
            project_id=quote(str(project_id), safe=""),
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
    | None
):
    if response.status_code == 202:
        response_202 = UpdateEndpointResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UpdateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateEndpointResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEndpoint,
) -> Response[
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
]:
    """Update an endpoint

     This endpoint updates an endpoint

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsUpdateEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEndpointResponse202 | UpdateEndpointResponse400 | UpdateEndpointResponse401 | UpdateEndpointResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEndpoint,
) -> (
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
    | None
):
    """Update an endpoint

     This endpoint updates an endpoint

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsUpdateEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEndpointResponse202 | UpdateEndpointResponse400 | UpdateEndpointResponse401 | UpdateEndpointResponse404
    """

    return sync_detailed(
        project_id=project_id,
        endpoint_id=endpoint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEndpoint,
) -> Response[
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
]:
    """Update an endpoint

     This endpoint updates an endpoint

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsUpdateEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateEndpointResponse202 | UpdateEndpointResponse400 | UpdateEndpointResponse401 | UpdateEndpointResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateEndpoint,
) -> (
    UpdateEndpointResponse202
    | UpdateEndpointResponse400
    | UpdateEndpointResponse401
    | UpdateEndpointResponse404
    | None
):
    """Update an endpoint

     This endpoint updates an endpoint

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsUpdateEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateEndpointResponse202 | UpdateEndpointResponse400 | UpdateEndpointResponse401 | UpdateEndpointResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            endpoint_id=endpoint_id,
            client=client,
            body=body,
        )
    ).parsed
