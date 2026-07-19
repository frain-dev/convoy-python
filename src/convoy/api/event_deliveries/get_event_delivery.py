from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_delivery_response_200 import GetEventDeliveryResponse200
from ...models.get_event_delivery_response_400 import GetEventDeliveryResponse400
from ...models.get_event_delivery_response_401 import GetEventDeliveryResponse401
from ...models.get_event_delivery_response_404 import GetEventDeliveryResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    event_delivery_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/eventdeliveries/{event_delivery_id}".format(
            project_id=quote(str(project_id), safe=""),
            event_delivery_id=quote(str(event_delivery_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetEventDeliveryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetEventDeliveryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetEventDeliveryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetEventDeliveryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
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
    *,
    client: AuthenticatedClient,
) -> Response[
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
]:
    """Retrieve an event delivery

     This endpoint fetches an event delivery.

    Args:
        project_id (str):
        event_delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventDeliveryResponse200 | GetEventDeliveryResponse400 | GetEventDeliveryResponse401 | GetEventDeliveryResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    event_delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
    | None
):
    """Retrieve an event delivery

     This endpoint fetches an event delivery.

    Args:
        project_id (str):
        event_delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventDeliveryResponse200 | GetEventDeliveryResponse400 | GetEventDeliveryResponse401 | GetEventDeliveryResponse404
    """

    return sync_detailed(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    event_delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
]:
    """Retrieve an event delivery

     This endpoint fetches an event delivery.

    Args:
        project_id (str):
        event_delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEventDeliveryResponse200 | GetEventDeliveryResponse400 | GetEventDeliveryResponse401 | GetEventDeliveryResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        event_delivery_id=event_delivery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    event_delivery_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    GetEventDeliveryResponse200
    | GetEventDeliveryResponse400
    | GetEventDeliveryResponse401
    | GetEventDeliveryResponse404
    | None
):
    """Retrieve an event delivery

     This endpoint fetches an event delivery.

    Args:
        project_id (str):
        event_delivery_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEventDeliveryResponse200 | GetEventDeliveryResponse400 | GetEventDeliveryResponse401 | GetEventDeliveryResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            event_delivery_id=event_delivery_id,
            client=client,
        )
    ).parsed
