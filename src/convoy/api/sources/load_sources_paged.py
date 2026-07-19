from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.load_sources_paged_direction import LoadSourcesPagedDirection
from ...models.load_sources_paged_response_200 import LoadSourcesPagedResponse200
from ...models.load_sources_paged_response_400 import LoadSourcesPagedResponse400
from ...models.load_sources_paged_response_401 import LoadSourcesPagedResponse401
from ...models.load_sources_paged_response_404 import LoadSourcesPagedResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    direction: LoadSourcesPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["next_page_cursor"] = next_page_cursor

    params["perPage"] = per_page

    params["prev_page_cursor"] = prev_page_cursor

    params["provider"] = provider

    params["sort"] = sort

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/sources".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
    | None
):
    if response.status_code == 200:
        response_200 = LoadSourcesPagedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LoadSourcesPagedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LoadSourcesPagedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = LoadSourcesPagedResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
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
    direction: LoadSourcesPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
]:
    """List all sources

     This endpoint fetches multiple sources

    Args:
        project_id (str):
        direction (LoadSourcesPagedDirection | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        provider (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadSourcesPagedResponse200 | LoadSourcesPagedResponse400 | LoadSourcesPagedResponse401 | LoadSourcesPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        provider=provider,
        sort=sort,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: LoadSourcesPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> (
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
    | None
):
    """List all sources

     This endpoint fetches multiple sources

    Args:
        project_id (str):
        direction (LoadSourcesPagedDirection | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        provider (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadSourcesPagedResponse200 | LoadSourcesPagedResponse400 | LoadSourcesPagedResponse401 | LoadSourcesPagedResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        direction=direction,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        provider=provider,
        sort=sort,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: LoadSourcesPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
]:
    """List all sources

     This endpoint fetches multiple sources

    Args:
        project_id (str):
        direction (LoadSourcesPagedDirection | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        provider (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadSourcesPagedResponse200 | LoadSourcesPagedResponse400 | LoadSourcesPagedResponse401 | LoadSourcesPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        provider=provider,
        sort=sort,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: LoadSourcesPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> (
    LoadSourcesPagedResponse200
    | LoadSourcesPagedResponse400
    | LoadSourcesPagedResponse401
    | LoadSourcesPagedResponse404
    | None
):
    """List all sources

     This endpoint fetches multiple sources

    Args:
        project_id (str):
        direction (LoadSourcesPagedDirection | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        provider (str | Unset):
        sort (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadSourcesPagedResponse200 | LoadSourcesPagedResponse400 | LoadSourcesPagedResponse401 | LoadSourcesPagedResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            direction=direction,
            next_page_cursor=next_page_cursor,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            provider=provider,
            sort=sort,
            type_=type_,
        )
    ).parsed
