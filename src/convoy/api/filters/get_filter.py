from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_filter_response_200 import GetFilterResponse200
from ...models.get_filter_response_400 import GetFilterResponse400
from ...models.get_filter_response_401 import GetFilterResponse401
from ...models.get_filter_response_404 import GetFilterResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    filter_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters/{filter_id}".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            filter_id=quote(str(filter_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetFilterResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetFilterResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetFilterResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetFilterResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
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
    filter_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
]:
    """Get a filter

     This endpoint retrieves a single filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFilterResponse200 | GetFilterResponse400 | GetFilterResponse401 | GetFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
    | None
):
    """Get a filter

     This endpoint retrieves a single filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFilterResponse200 | GetFilterResponse400 | GetFilterResponse401 | GetFilterResponse404
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
]:
    """Get a filter

     This endpoint retrieves a single filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFilterResponse200 | GetFilterResponse400 | GetFilterResponse401 | GetFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetFilterResponse200
    | GetFilterResponse400
    | GetFilterResponse401
    | GetFilterResponse404
    | None
):
    """Get a filter

     This endpoint retrieves a single filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFilterResponse200 | GetFilterResponse400 | GetFilterResponse401 | GetFilterResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            filter_id=filter_id,
            client=client,
        )
    ).parsed
