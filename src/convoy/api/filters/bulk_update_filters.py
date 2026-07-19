from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_update_filters_response_200 import BulkUpdateFiltersResponse200
from ...models.bulk_update_filters_response_400 import BulkUpdateFiltersResponse400
from ...models.bulk_update_filters_response_401 import BulkUpdateFiltersResponse401
from ...models.bulk_update_filters_response_404 import BulkUpdateFiltersResponse404
from ...models.models_bulk_update_filter_request import ModelsBulkUpdateFilterRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    *,
    body: list[ModelsBulkUpdateFilterRequest],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters/bulk_update".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
    | None
):
    if response.status_code == 200:
        response_200 = BulkUpdateFiltersResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BulkUpdateFiltersResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BulkUpdateFiltersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = BulkUpdateFiltersResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
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
    body: list[ModelsBulkUpdateFilterRequest],
) -> Response[
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
]:
    """Update multiple subscription filters

     This endpoint updates multiple filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (list[ModelsBulkUpdateFilterRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateFiltersResponse200 | BulkUpdateFiltersResponse400 | BulkUpdateFiltersResponse401 | BulkUpdateFiltersResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        body=body,
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
    body: list[ModelsBulkUpdateFilterRequest],
) -> (
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
    | None
):
    """Update multiple subscription filters

     This endpoint updates multiple filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (list[ModelsBulkUpdateFilterRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateFiltersResponse200 | BulkUpdateFiltersResponse400 | BulkUpdateFiltersResponse401 | BulkUpdateFiltersResponse404
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ModelsBulkUpdateFilterRequest],
) -> Response[
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
]:
    """Update multiple subscription filters

     This endpoint updates multiple filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (list[ModelsBulkUpdateFilterRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpdateFiltersResponse200 | BulkUpdateFiltersResponse400 | BulkUpdateFiltersResponse401 | BulkUpdateFiltersResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: list[ModelsBulkUpdateFilterRequest],
) -> (
    BulkUpdateFiltersResponse200
    | BulkUpdateFiltersResponse400
    | BulkUpdateFiltersResponse401
    | BulkUpdateFiltersResponse404
    | None
):
    """Update multiple subscription filters

     This endpoint updates multiple filters for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (list[ModelsBulkUpdateFilterRequest]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpdateFiltersResponse200 | BulkUpdateFiltersResponse400 | BulkUpdateFiltersResponse401 | BulkUpdateFiltersResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
