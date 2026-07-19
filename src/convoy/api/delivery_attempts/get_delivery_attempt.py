from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_delivery_attempt_response_200 import GetDeliveryAttemptResponse200
from ...models.get_delivery_attempt_response_400 import GetDeliveryAttemptResponse400
from ...models.get_delivery_attempt_response_401 import GetDeliveryAttemptResponse401
from ...models.get_delivery_attempt_response_404 import GetDeliveryAttemptResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    event_delivery_id: str,
    delivery_attempt_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/eventdeliveries/{event_delivery_id}/deliveryattempts/{delivery_attempt_id}".format(
            project_id=quote(str(project_id), safe=""),
            event_delivery_id=quote(str(event_delivery_id), safe=""),
            delivery_attempt_id=quote(str(delivery_attempt_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetDeliveryAttemptResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetDeliveryAttemptResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetDeliveryAttemptResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetDeliveryAttemptResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    event_delivery_id: str,
    delivery_attempt_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
]:
    """Retrieve a delivery attempt

     This endpoint fetches an app event delivery attempt

    Args:
        project_id (str):
        event_delivery_id (str):
        delivery_attempt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeliveryAttemptResponse200 | GetDeliveryAttemptResponse400 | GetDeliveryAttemptResponse401 | GetDeliveryAttemptResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
        delivery_attempt_id=delivery_attempt_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    event_delivery_id: str,
    delivery_attempt_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
    | None
):
    """Retrieve a delivery attempt

     This endpoint fetches an app event delivery attempt

    Args:
        project_id (str):
        event_delivery_id (str):
        delivery_attempt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeliveryAttemptResponse200 | GetDeliveryAttemptResponse400 | GetDeliveryAttemptResponse401 | GetDeliveryAttemptResponse404
    """

    return sync_detailed(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
        delivery_attempt_id=delivery_attempt_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    event_delivery_id: str,
    delivery_attempt_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
]:
    """Retrieve a delivery attempt

     This endpoint fetches an app event delivery attempt

    Args:
        project_id (str):
        event_delivery_id (str):
        delivery_attempt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDeliveryAttemptResponse200 | GetDeliveryAttemptResponse400 | GetDeliveryAttemptResponse401 | GetDeliveryAttemptResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
        delivery_attempt_id=delivery_attempt_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    event_delivery_id: str,
    delivery_attempt_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetDeliveryAttemptResponse200
    | GetDeliveryAttemptResponse400
    | GetDeliveryAttemptResponse401
    | GetDeliveryAttemptResponse404
    | None
):
    """Retrieve a delivery attempt

     This endpoint fetches an app event delivery attempt

    Args:
        project_id (str):
        event_delivery_id (str):
        delivery_attempt_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDeliveryAttemptResponse200 | GetDeliveryAttemptResponse400 | GetDeliveryAttemptResponse401 | GetDeliveryAttemptResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            event_delivery_id=event_delivery_id,
            delivery_attempt_id=delivery_attempt_id,
            client=client,
        )
    ).parsed
