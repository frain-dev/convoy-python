from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_filters_response_200 import GetFiltersResponse200
from ...models.get_filters_response_400 import GetFiltersResponse400
from ...models.get_filters_response_401 import GetFiltersResponse401
from ...models.get_filters_response_404 import GetFiltersResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetFiltersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetFiltersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFiltersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetFiltersResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
]:
    """List all filters

     This endpoint fetches all filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFiltersResponse200 | GetFiltersResponse400 | GetFiltersResponse401 | GetFiltersResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
    | None
):
    """List all filters

     This endpoint fetches all filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFiltersResponse200 | GetFiltersResponse400 | GetFiltersResponse401 | GetFiltersResponse404
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
]:
    """List all filters

     This endpoint fetches all filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFiltersResponse200 | GetFiltersResponse400 | GetFiltersResponse401 | GetFiltersResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetFiltersResponse200
    | GetFiltersResponse400
    | GetFiltersResponse401
    | GetFiltersResponse404
    | None
):
    """List all filters

     This endpoint fetches all filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFiltersResponse200 | GetFiltersResponse400 | GetFiltersResponse401 | GetFiltersResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
