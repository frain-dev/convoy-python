from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.toggle_subscription_status_response_202 import (
    ToggleSubscriptionStatusResponse202,
)
from ...models.toggle_subscription_status_response_400 import (
    ToggleSubscriptionStatusResponse400,
)
from ...models.toggle_subscription_status_response_401 import (
    ToggleSubscriptionStatusResponse401,
)
from ...models.toggle_subscription_status_response_404 import (
    ToggleSubscriptionStatusResponse404,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/toggle_status".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
    | None
):
    if response.status_code == 202:
        response_202 = ToggleSubscriptionStatusResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = ToggleSubscriptionStatusResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ToggleSubscriptionStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ToggleSubscriptionStatusResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
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
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
]:
    """Toggle subscription status

     This endpoint toggles a subscription status. Retained for backward compatibility.

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToggleSubscriptionStatusResponse202 | ToggleSubscriptionStatusResponse400 | ToggleSubscriptionStatusResponse401 | ToggleSubscriptionStatusResponse404]
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
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
    | None
):
    """Toggle subscription status

     This endpoint toggles a subscription status. Retained for backward compatibility.

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToggleSubscriptionStatusResponse202 | ToggleSubscriptionStatusResponse400 | ToggleSubscriptionStatusResponse401 | ToggleSubscriptionStatusResponse404
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
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
]:
    """Toggle subscription status

     This endpoint toggles a subscription status. Retained for backward compatibility.

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToggleSubscriptionStatusResponse202 | ToggleSubscriptionStatusResponse400 | ToggleSubscriptionStatusResponse401 | ToggleSubscriptionStatusResponse404]
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
    ToggleSubscriptionStatusResponse202
    | ToggleSubscriptionStatusResponse400
    | ToggleSubscriptionStatusResponse401
    | ToggleSubscriptionStatusResponse404
    | None
):
    """Toggle subscription status

     This endpoint toggles a subscription status. Retained for backward compatibility.

    Args:
        project_id (str):
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToggleSubscriptionStatusResponse202 | ToggleSubscriptionStatusResponse400 | ToggleSubscriptionStatusResponse401 | ToggleSubscriptionStatusResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
