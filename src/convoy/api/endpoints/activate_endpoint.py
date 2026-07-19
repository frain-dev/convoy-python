from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_endpoint_response_202 import ActivateEndpointResponse202
from ...models.activate_endpoint_response_400 import ActivateEndpointResponse400
from ...models.activate_endpoint_response_401 import ActivateEndpointResponse401
from ...models.activate_endpoint_response_404 import ActivateEndpointResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    endpoint_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/endpoints/{endpoint_id}/activate".format(
            project_id=quote(str(project_id), safe=""),
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
    | None
):
    if response.status_code == 202:
        response_202 = ActivateEndpointResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ActivateEndpointResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ActivateEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ActivateEndpointResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
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
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
]:
    """Activate endpoint

     Activated an inactive endpoint

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateEndpointResponse202 | ActivateEndpointResponse400 | ActivateEndpointResponse401 | ActivateEndpointResponse404]
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
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
    | None
):
    """Activate endpoint

     Activated an inactive endpoint

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateEndpointResponse202 | ActivateEndpointResponse400 | ActivateEndpointResponse401 | ActivateEndpointResponse404
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
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
]:
    """Activate endpoint

     Activated an inactive endpoint

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateEndpointResponse202 | ActivateEndpointResponse400 | ActivateEndpointResponse401 | ActivateEndpointResponse404]
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
    ActivateEndpointResponse202
    | ActivateEndpointResponse400
    | ActivateEndpointResponse401
    | ActivateEndpointResponse404
    | None
):
    """Activate endpoint

     Activated an inactive endpoint

    Args:
        project_id (str):
        endpoint_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateEndpointResponse202 | ActivateEndpointResponse400 | ActivateEndpointResponse401 | ActivateEndpointResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            endpoint_id=endpoint_id,
            client=client,
        )
    ).parsed
