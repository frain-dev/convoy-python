from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pause_endpoint_response_202 import PauseEndpointResponse202
from ...models.pause_endpoint_response_400 import PauseEndpointResponse400
from ...models.pause_endpoint_response_401 import PauseEndpointResponse401
from ...models.pause_endpoint_response_404 import PauseEndpointResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    endpoint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/endpoints/{endpoint_id}/pause".format(
            project_id=quote(str(project_id), safe=""),
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
    | None
):
    if response.status_code == 202:
        response_202 = PauseEndpointResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = PauseEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PauseEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = PauseEndpointResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
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
) -> Response[
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
]:
    """Pause endpoint

     Toggles an endpoint's status between active and paused states

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PauseEndpointResponse202 | PauseEndpointResponse400 | PauseEndpointResponse401 | PauseEndpointResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
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
) -> (
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
    | None
):
    """Pause endpoint

     Toggles an endpoint's status between active and paused states

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PauseEndpointResponse202 | PauseEndpointResponse400 | PauseEndpointResponse401 | PauseEndpointResponse404
    """

    return sync_detailed(
        project_id=project_id,
        endpoint_id=endpoint_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
]:
    """Pause endpoint

     Toggles an endpoint's status between active and paused states

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PauseEndpointResponse202 | PauseEndpointResponse400 | PauseEndpointResponse401 | PauseEndpointResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    PauseEndpointResponse202
    | PauseEndpointResponse400
    | PauseEndpointResponse401
    | PauseEndpointResponse404
    | None
):
    """Pause endpoint

     Toggles an endpoint's status between active and paused states

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PauseEndpointResponse202 | PauseEndpointResponse400 | PauseEndpointResponse401 | PauseEndpointResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            endpoint_id=endpoint_id,
            client=client,
        )
    ).parsed
