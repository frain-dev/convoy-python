from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_response_200 import GetProjectsResponse200
from ...models.get_projects_response_400 import GetProjectsResponse400
from ...models.get_projects_response_401 import GetProjectsResponse401
from ...models.get_projects_response_404 import GetProjectsResponse404
from ...types import UNSET, Response


def _get_kwargs(
    *,
    org_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["orgID"] = org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetProjectsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetProjectsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetProjectsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetProjectsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    org_id: str,
) -> Response[
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
]:
    """List all projects

     This endpoint fetches projects for an organisation. Authenticate with a personal API key or JWT and
    pass the organisation id as the orgID query parameter.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectsResponse200 | GetProjectsResponse400 | GetProjectsResponse401 | GetProjectsResponse404]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    org_id: str,
) -> (
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
    | None
):
    """List all projects

     This endpoint fetches projects for an organisation. Authenticate with a personal API key or JWT and
    pass the organisation id as the orgID query parameter.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectsResponse200 | GetProjectsResponse400 | GetProjectsResponse401 | GetProjectsResponse404
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    org_id: str,
) -> Response[
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
]:
    """List all projects

     This endpoint fetches projects for an organisation. Authenticate with a personal API key or JWT and
    pass the organisation id as the orgID query parameter.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectsResponse200 | GetProjectsResponse400 | GetProjectsResponse401 | GetProjectsResponse404]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    org_id: str,
) -> (
    GetProjectsResponse200
    | GetProjectsResponse400
    | GetProjectsResponse401
    | GetProjectsResponse404
    | None
):
    """List all projects

     This endpoint fetches projects for an organisation. Authenticate with a personal API key or JWT and
    pass the organisation id as the orgID query parameter.

    Args:
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectsResponse200 | GetProjectsResponse400 | GetProjectsResponse401 | GetProjectsResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
        )
    ).parsed
