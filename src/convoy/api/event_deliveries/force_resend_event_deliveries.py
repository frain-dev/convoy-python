from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.force_resend_event_deliveries_response_200 import (
    ForceResendEventDeliveriesResponse200,
)
from ...models.force_resend_event_deliveries_response_400 import (
    ForceResendEventDeliveriesResponse400,
)
from ...models.force_resend_event_deliveries_response_401 import (
    ForceResendEventDeliveriesResponse401,
)
from ...models.force_resend_event_deliveries_response_404 import (
    ForceResendEventDeliveriesResponse404,
)
from ...models.models_i_ds import ModelsIDs
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsIDs,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/eventdeliveries/forceresend".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ForceResendEventDeliveriesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ForceResendEventDeliveriesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ForceResendEventDeliveriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ForceResendEventDeliveriesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
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
    body: ModelsIDs,
) -> Response[
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
]:
    """Force retry event delivery

     This endpoint enables you retry a previously successful event delivery

    Args:
        project_id (str):
        body (ModelsIDs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForceResendEventDeliveriesResponse200 | ForceResendEventDeliveriesResponse400 | ForceResendEventDeliveriesResponse401 | ForceResendEventDeliveriesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsIDs,
) -> (
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
    | None
):
    """Force retry event delivery

     This endpoint enables you retry a previously successful event delivery

    Args:
        project_id (str):
        body (ModelsIDs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForceResendEventDeliveriesResponse200 | ForceResendEventDeliveriesResponse400 | ForceResendEventDeliveriesResponse401 | ForceResendEventDeliveriesResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsIDs,
) -> Response[
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
]:
    """Force retry event delivery

     This endpoint enables you retry a previously successful event delivery

    Args:
        project_id (str):
        body (ModelsIDs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForceResendEventDeliveriesResponse200 | ForceResendEventDeliveriesResponse400 | ForceResendEventDeliveriesResponse401 | ForceResendEventDeliveriesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsIDs,
) -> (
    ForceResendEventDeliveriesResponse200
    | ForceResendEventDeliveriesResponse400
    | ForceResendEventDeliveriesResponse401
    | ForceResendEventDeliveriesResponse404
    | None
):
    """Force retry event delivery

     This endpoint enables you retry a previously successful event delivery

    Args:
        project_id (str):
        body (ModelsIDs):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForceResendEventDeliveriesResponse200 | ForceResendEventDeliveriesResponse400 | ForceResendEventDeliveriesResponse401 | ForceResendEventDeliveriesResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
