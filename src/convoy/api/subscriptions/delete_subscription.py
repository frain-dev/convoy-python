from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_subscription_response_200 import DeleteSubscriptionResponse200
from ...models.delete_subscription_response_400 import DeleteSubscriptionResponse400
from ...models.delete_subscription_response_401 import DeleteSubscriptionResponse401
from ...models.delete_subscription_response_404 import DeleteSubscriptionResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteSubscriptionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteSubscriptionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteSubscriptionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = DeleteSubscriptionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
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
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
]:
    """Delete subscription

     This endpoint deletes a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionResponse200 | DeleteSubscriptionResponse400 | DeleteSubscriptionResponse401 | DeleteSubscriptionResponse404]
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
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
    | None
):
    """Delete subscription

     This endpoint deletes a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSubscriptionResponse200 | DeleteSubscriptionResponse400 | DeleteSubscriptionResponse401 | DeleteSubscriptionResponse404
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
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
]:
    """Delete subscription

     This endpoint deletes a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteSubscriptionResponse200 | DeleteSubscriptionResponse400 | DeleteSubscriptionResponse401 | DeleteSubscriptionResponse404]
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
    DeleteSubscriptionResponse200
    | DeleteSubscriptionResponse400
    | DeleteSubscriptionResponse401
    | DeleteSubscriptionResponse404
    | None
):
    """Delete subscription

     This endpoint deletes a subscription

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteSubscriptionResponse200 | DeleteSubscriptionResponse400 | DeleteSubscriptionResponse401 | DeleteSubscriptionResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
