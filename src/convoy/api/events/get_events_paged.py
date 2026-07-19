from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_events_paged_direction import GetEventsPagedDirection
from ...models.get_events_paged_response_200 import GetEventsPagedResponse200
from ...models.get_events_paged_response_400 import GetEventsPagedResponse400
from ...models.get_events_paged_response_401 import GetEventsPagedResponse401
from ...models.get_events_paged_response_404 import GetEventsPagedResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    direction: GetEventsPagedDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    source_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params["endDate"] = end_date

    json_endpoint_id: list[str] | Unset = UNSET
    if not isinstance(endpoint_id, Unset):
        json_endpoint_id = endpoint_id

    params["endpointId"] = json_endpoint_id

    params["idempotencyKey"] = idempotency_key

    params["next_page_cursor"] = next_page_cursor

    params["perPage"] = per_page

    params["prev_page_cursor"] = prev_page_cursor

    params["query"] = query

    params["sort"] = sort

    json_source_id: list[str] | Unset = UNSET
    if not isinstance(source_id, Unset):
        json_source_id = source_id

    params["sourceId"] = json_source_id

    params["startDate"] = start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/events".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetEventsPagedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEventsPagedResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetEventsPagedResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetEventsPagedResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
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
    direction: GetEventsPagedDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    source_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> Response[
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
]:
    """List all events

     This endpoint fetches app events with pagination

    Args:
        project_id (str):
        direction (GetEventsPagedDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        query (str | Unset):
        sort (str | Unset):
        source_id (list[str] | Unset):
        start_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsPagedResponse200 | GetEventsPagedResponse400 | GetEventsPagedResponse401 | GetEventsPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        query=query,
        sort=sort,
        source_id=source_id,
        start_date=start_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetEventsPagedDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    source_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> (
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
    | None
):
    """List all events

     This endpoint fetches app events with pagination

    Args:
        project_id (str):
        direction (GetEventsPagedDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        query (str | Unset):
        sort (str | Unset):
        source_id (list[str] | Unset):
        start_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsPagedResponse200 | GetEventsPagedResponse400 | GetEventsPagedResponse401 | GetEventsPagedResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        query=query,
        sort=sort,
        source_id=source_id,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetEventsPagedDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    source_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> Response[
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
]:
    """List all events

     This endpoint fetches app events with pagination

    Args:
        project_id (str):
        direction (GetEventsPagedDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        query (str | Unset):
        sort (str | Unset):
        source_id (list[str] | Unset):
        start_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventsPagedResponse200 | GetEventsPagedResponse400 | GetEventsPagedResponse401 | GetEventsPagedResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        query=query,
        sort=sort,
        source_id=source_id,
        start_date=start_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: GetEventsPagedDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    query: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    source_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
) -> (
    GetEventsPagedResponse200
    | GetEventsPagedResponse400
    | GetEventsPagedResponse401
    | GetEventsPagedResponse404
    | None
):
    """List all events

     This endpoint fetches app events with pagination

    Args:
        project_id (str):
        direction (GetEventsPagedDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        query (str | Unset):
        sort (str | Unset):
        source_id (list[str] | Unset):
        start_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventsPagedResponse200 | GetEventsPagedResponse400 | GetEventsPagedResponse401 | GetEventsPagedResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            direction=direction,
            end_date=end_date,
            endpoint_id=endpoint_id,
            idempotency_key=idempotency_key,
            next_page_cursor=next_page_cursor,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            query=query,
            sort=sort,
            source_id=source_id,
            start_date=start_date,
        )
    ).parsed
