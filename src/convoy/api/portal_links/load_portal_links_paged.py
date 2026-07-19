from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.load_portal_links_paged_direction import LoadPortalLinksPagedDirection
from ...models.load_portal_links_paged_response_200 import (
    LoadPortalLinksPagedResponse200,
)
from ...models.load_portal_links_paged_response_400 import (
    LoadPortalLinksPagedResponse400,
)
from ...models.load_portal_links_paged_response_401 import (
    LoadPortalLinksPagedResponse401,
)
from ...models.load_portal_links_paged_response_404 import (
    LoadPortalLinksPagedResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    direction: LoadPortalLinksPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["next_page_cursor"] = next_page_cursor

    params["ownerId"] = owner_id

    params["perPage"] = per_page

    params["prev_page_cursor"] = prev_page_cursor

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/portal-links".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
    | None
):
    if response.status_code == 200:
        response_200 = LoadPortalLinksPagedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = LoadPortalLinksPagedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = LoadPortalLinksPagedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = LoadPortalLinksPagedResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
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
    direction: LoadPortalLinksPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
]:
    """List all portal links

     This endpoint fetches multiple portal links

    Args:
        project_id (str):
        direction (LoadPortalLinksPagedDirection | Unset):
        next_page_cursor (str | Unset):
        owner_id (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadPortalLinksPagedResponse200 | LoadPortalLinksPagedResponse400 | LoadPortalLinksPagedResponse401 | LoadPortalLinksPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        next_page_cursor=next_page_cursor,
        owner_id=owner_id,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        q=q,
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
    direction: LoadPortalLinksPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
    | None
):
    """List all portal links

     This endpoint fetches multiple portal links

    Args:
        project_id (str):
        direction (LoadPortalLinksPagedDirection | Unset):
        next_page_cursor (str | Unset):
        owner_id (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadPortalLinksPagedResponse200 | LoadPortalLinksPagedResponse400 | LoadPortalLinksPagedResponse401 | LoadPortalLinksPagedResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        direction=direction,
        next_page_cursor=next_page_cursor,
        owner_id=owner_id,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: LoadPortalLinksPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
]:
    """List all portal links

     This endpoint fetches multiple portal links

    Args:
        project_id (str):
        direction (LoadPortalLinksPagedDirection | Unset):
        next_page_cursor (str | Unset):
        owner_id (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LoadPortalLinksPagedResponse200 | LoadPortalLinksPagedResponse400 | LoadPortalLinksPagedResponse401 | LoadPortalLinksPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        next_page_cursor=next_page_cursor,
        owner_id=owner_id,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        q=q,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: LoadPortalLinksPagedDirection | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    owner_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    LoadPortalLinksPagedResponse200
    | LoadPortalLinksPagedResponse400
    | LoadPortalLinksPagedResponse401
    | LoadPortalLinksPagedResponse404
    | None
):
    """List all portal links

     This endpoint fetches multiple portal links

    Args:
        project_id (str):
        direction (LoadPortalLinksPagedDirection | Unset):
        next_page_cursor (str | Unset):
        owner_id (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LoadPortalLinksPagedResponse200 | LoadPortalLinksPagedResponse400 | LoadPortalLinksPagedResponse401 | LoadPortalLinksPagedResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            direction=direction,
            next_page_cursor=next_page_cursor,
            owner_id=owner_id,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            q=q,
            sort=sort,
        )
    ).parsed
