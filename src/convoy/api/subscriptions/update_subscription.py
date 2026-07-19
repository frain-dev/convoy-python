from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_subscription import ModelsUpdateSubscription
from ...models.update_subscription_response_202 import UpdateSubscriptionResponse202
from ...models.update_subscription_response_400 import UpdateSubscriptionResponse400
from ...models.update_subscription_response_401 import UpdateSubscriptionResponse401
from ...models.update_subscription_response_404 import UpdateSubscriptionResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    *,
    body: ModelsUpdateSubscription,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
    | None
):
    if response.status_code == 202:
        response_202 = UpdateSubscriptionResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UpdateSubscriptionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateSubscriptionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateSubscriptionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
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
    body: ModelsUpdateSubscription,
) -> Response[
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
]:
    """Update a subscription

     This endpoint updates a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsUpdateSubscription):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSubscriptionResponse202 | UpdateSubscriptionResponse400 | UpdateSubscriptionResponse401 | UpdateSubscriptionResponse404]
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
    body: ModelsUpdateSubscription,
) -> (
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
    | None
):
    """Update a subscription

     This endpoint updates a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsUpdateSubscription):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSubscriptionResponse202 | UpdateSubscriptionResponse400 | UpdateSubscriptionResponse401 | UpdateSubscriptionResponse404
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
    body: ModelsUpdateSubscription,
) -> Response[
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
]:
    """Update a subscription

     This endpoint updates a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsUpdateSubscription):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateSubscriptionResponse202 | UpdateSubscriptionResponse400 | UpdateSubscriptionResponse401 | UpdateSubscriptionResponse404]
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
    body: ModelsUpdateSubscription,
) -> (
    UpdateSubscriptionResponse202
    | UpdateSubscriptionResponse400
    | UpdateSubscriptionResponse401
    | UpdateSubscriptionResponse404
    | None
):
    """Update a subscription

     This endpoint updates a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsUpdateSubscription):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateSubscriptionResponse202 | UpdateSubscriptionResponse400 | UpdateSubscriptionResponse401 | UpdateSubscriptionResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
