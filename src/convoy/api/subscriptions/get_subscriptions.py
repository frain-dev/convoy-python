from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscriptions_direction import GetSubscriptionsDirection
from ...models.get_subscriptions_response_200 import GetSubscriptionsResponse200
from ...models.get_subscriptions_response_400 import GetSubscriptionsResponse400
from ...models.get_subscriptions_response_401 import GetSubscriptionsResponse401
from ...models.get_subscriptions_response_404 import GetSubscriptionsResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    direction: GetSubscriptionsDirection | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_endpoint_id: list[str] | Unset = UNSET
    if not isinstance(endpoint_id, Unset):
        json_endpoint_id = endpoint_id

    params["endpointId"] = json_endpoint_id

    params["name"] = name

    params["next_page_cursor"] = next_page_cursor

    params["perPage"] = per_page

    params["prev_page_cursor"] = prev_page_cursor

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/subscriptions".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetSubscriptionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSubscriptionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetSubscriptionsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSubscriptionsResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
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
    direction: GetSubscriptionsDirection | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
]:
    """List all subscriptions

     This endpoint fetches all the subscriptions

    Args:
        project_id (str):
        direction (GetSubscriptionsDirection | Unset):
        endpoint_id (list[str] | Unset):
        name (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionsResponse200 | GetSubscriptionsResponse400 | GetSubscriptionsResponse401 | GetSubscriptionsResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        endpoint_id=endpoint_id,
        name=name,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetSubscriptionsDirection | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
    | None
):
    """List all subscriptions

     This endpoint fetches all the subscriptions

    Args:
        project_id (str):
        direction (GetSubscriptionsDirection | Unset):
        endpoint_id (list[str] | Unset):
        name (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionsResponse200 | GetSubscriptionsResponse400 | GetSubscriptionsResponse401 | GetSubscriptionsResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        direction=direction,
        endpoint_id=endpoint_id,
        name=name,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetSubscriptionsDirection | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
]:
    """List all subscriptions

     This endpoint fetches all the subscriptions

    Args:
        project_id (str):
        direction (GetSubscriptionsDirection | Unset):
        endpoint_id (list[str] | Unset):
        name (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionsResponse200 | GetSubscriptionsResponse400 | GetSubscriptionsResponse401 | GetSubscriptionsResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        endpoint_id=endpoint_id,
        name=name,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetSubscriptionsDirection | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    name: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    GetSubscriptionsResponse200
    | GetSubscriptionsResponse400
    | GetSubscriptionsResponse401
    | GetSubscriptionsResponse404
    | None
):
    """List all subscriptions

     This endpoint fetches all the subscriptions

    Args:
        project_id (str):
        direction (GetSubscriptionsDirection | Unset):
        endpoint_id (list[str] | Unset):
        name (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionsResponse200 | GetSubscriptionsResponse400 | GetSubscriptionsResponse401 | GetSubscriptionsResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            direction=direction,
            endpoint_id=endpoint_id,
            name=name,
            next_page_cursor=next_page_cursor,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            sort=sort,
        )
    ).parsed
