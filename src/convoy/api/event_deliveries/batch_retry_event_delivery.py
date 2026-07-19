from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_retry_event_delivery_direction import (
    BatchRetryEventDeliveryDirection,
)
from ...models.batch_retry_event_delivery_response_200 import (
    BatchRetryEventDeliveryResponse200,
)
from ...models.batch_retry_event_delivery_response_400 import (
    BatchRetryEventDeliveryResponse400,
)
from ...models.batch_retry_event_delivery_response_401 import (
    BatchRetryEventDeliveryResponse401,
)
from ...models.batch_retry_event_delivery_response_404 import (
    BatchRetryEventDeliveryResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    direction: BatchRetryEventDeliveryDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    event_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
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

    params["eventId"] = event_id

    params["event_type"] = event_type

    params["idempotencyKey"] = idempotency_key

    params["next_page_cursor"] = next_page_cursor

    params["perPage"] = per_page

    params["prev_page_cursor"] = prev_page_cursor

    params["sort"] = sort

    params["startDate"] = start_date

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["subscriptionId"] = subscription_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/eventdeliveries/batchretry".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
    | None
):
    if response.status_code == 200:
        response_200 = BatchRetryEventDeliveryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BatchRetryEventDeliveryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BatchRetryEventDeliveryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = BatchRetryEventDeliveryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
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
    direction: BatchRetryEventDeliveryDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    event_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
) -> Response[
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
]:
    """Batch retry event delivery

     This endpoint batch retries multiple event deliveries at once.

    Args:
        project_id (str):
        direction (BatchRetryEventDeliveryDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        event_id (str | Unset):
        event_type (str | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):
        start_date (str | Unset):
        status (list[str] | Unset):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchRetryEventDeliveryResponse200 | BatchRetryEventDeliveryResponse400 | BatchRetryEventDeliveryResponse401 | BatchRetryEventDeliveryResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        event_id=event_id,
        event_type=event_type,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
        start_date=start_date,
        status=status,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: BatchRetryEventDeliveryDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    event_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
) -> (
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
    | None
):
    """Batch retry event delivery

     This endpoint batch retries multiple event deliveries at once.

    Args:
        project_id (str):
        direction (BatchRetryEventDeliveryDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        event_id (str | Unset):
        event_type (str | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):
        start_date (str | Unset):
        status (list[str] | Unset):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchRetryEventDeliveryResponse200 | BatchRetryEventDeliveryResponse400 | BatchRetryEventDeliveryResponse401 | BatchRetryEventDeliveryResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        event_id=event_id,
        event_type=event_type,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
        start_date=start_date,
        status=status,
        subscription_id=subscription_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: BatchRetryEventDeliveryDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    event_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
) -> Response[
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
]:
    """Batch retry event delivery

     This endpoint batch retries multiple event deliveries at once.

    Args:
        project_id (str):
        direction (BatchRetryEventDeliveryDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        event_id (str | Unset):
        event_type (str | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):
        start_date (str | Unset):
        status (list[str] | Unset):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchRetryEventDeliveryResponse200 | BatchRetryEventDeliveryResponse400 | BatchRetryEventDeliveryResponse401 | BatchRetryEventDeliveryResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        direction=direction,
        end_date=end_date,
        endpoint_id=endpoint_id,
        event_id=event_id,
        event_type=event_type,
        idempotency_key=idempotency_key,
        next_page_cursor=next_page_cursor,
        per_page=per_page,
        prev_page_cursor=prev_page_cursor,
        sort=sort,
        start_date=start_date,
        status=status,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    direction: BatchRetryEventDeliveryDirection | Unset = UNSET,
    end_date: str | Unset = UNSET,
    endpoint_id: list[str] | Unset = UNSET,
    event_id: str | Unset = UNSET,
    event_type: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    next_page_cursor: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    prev_page_cursor: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    status: list[str] | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
) -> (
    BatchRetryEventDeliveryResponse200
    | BatchRetryEventDeliveryResponse400
    | BatchRetryEventDeliveryResponse401
    | BatchRetryEventDeliveryResponse404
    | None
):
    """Batch retry event delivery

     This endpoint batch retries multiple event deliveries at once.

    Args:
        project_id (str):
        direction (BatchRetryEventDeliveryDirection | Unset):
        end_date (str | Unset):
        endpoint_id (list[str] | Unset):
        event_id (str | Unset):
        event_type (str | Unset):
        idempotency_key (str | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        sort (str | Unset):
        start_date (str | Unset):
        status (list[str] | Unset):
        subscription_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchRetryEventDeliveryResponse200 | BatchRetryEventDeliveryResponse400 | BatchRetryEventDeliveryResponse401 | BatchRetryEventDeliveryResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            direction=direction,
            end_date=end_date,
            endpoint_id=endpoint_id,
            event_id=event_id,
            event_type=event_type,
            idempotency_key=idempotency_key,
            next_page_cursor=next_page_cursor,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            sort=sort,
            start_date=start_date,
            status=status,
            subscription_id=subscription_id,
        )
    ).parsed
