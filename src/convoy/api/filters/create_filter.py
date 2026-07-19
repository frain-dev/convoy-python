from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_filter_response_201 import CreateFilterResponse201
from ...models.create_filter_response_400 import CreateFilterResponse400
from ...models.create_filter_response_401 import CreateFilterResponse401
from ...models.create_filter_response_404 import CreateFilterResponse404
from ...models.models_create_filter_request import ModelsCreateFilterRequest
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    *,
    body: ModelsCreateFilterRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters".format(
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
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
    | None
):
    if response.status_code == 201:
        response_201 = CreateFilterResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateFilterResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateFilterResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateFilterResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
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
    body: ModelsCreateFilterRequest,
) -> Response[
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
]:
    """Create a new filter

     This endpoint creates a new filter for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsCreateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFilterResponse201 | CreateFilterResponse400 | CreateFilterResponse401 | CreateFilterResponse404]
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
    body: ModelsCreateFilterRequest,
) -> (
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
    | None
):
    """Create a new filter

     This endpoint creates a new filter for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsCreateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFilterResponse201 | CreateFilterResponse400 | CreateFilterResponse401 | CreateFilterResponse404
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
    body: ModelsCreateFilterRequest,
) -> Response[
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
]:
    """Create a new filter

     This endpoint creates a new filter for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsCreateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateFilterResponse201 | CreateFilterResponse400 | CreateFilterResponse401 | CreateFilterResponse404]
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
    body: ModelsCreateFilterRequest,
) -> (
    CreateFilterResponse201
    | CreateFilterResponse400
    | CreateFilterResponse401
    | CreateFilterResponse404
    | None
):
    """Create a new filter

     This endpoint creates a new filter for a subscription

    Args:
        project_id (str):
        subscription_id (str):
        body (ModelsCreateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateFilterResponse201 | CreateFilterResponse400 | CreateFilterResponse401 | CreateFilterResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
