from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_filter_request import ModelsUpdateFilterRequest
from ...models.update_filter_response_200 import UpdateFilterResponse200
from ...models.update_filter_response_400 import UpdateFilterResponse400
from ...models.update_filter_response_401 import UpdateFilterResponse401
from ...models.update_filter_response_404 import UpdateFilterResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    body: ModelsUpdateFilterRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters/{filter_id}".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            filter_id=quote(str(filter_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
    | None
):
    if response.status_code == 200:
        response_200 = UpdateFilterResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateFilterResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateFilterResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateFilterResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
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
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateFilterRequest,
) -> Response[
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
]:
    """Update a filter

     This endpoint updates an existing filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):
        body (ModelsUpdateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFilterResponse200 | UpdateFilterResponse400 | UpdateFilterResponse401 | UpdateFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateFilterRequest,
) -> (
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
    | None
):
    """Update a filter

     This endpoint updates an existing filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):
        body (ModelsUpdateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFilterResponse200 | UpdateFilterResponse400 | UpdateFilterResponse401 | UpdateFilterResponse404
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateFilterRequest,
) -> Response[
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
]:
    """Update a filter

     This endpoint updates an existing filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):
        body (ModelsUpdateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateFilterResponse200 | UpdateFilterResponse400 | UpdateFilterResponse401 | UpdateFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        filter_id=filter_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    filter_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsUpdateFilterRequest,
) -> (
    UpdateFilterResponse200
    | UpdateFilterResponse400
    | UpdateFilterResponse401
    | UpdateFilterResponse404
    | None
):
    """Update a filter

     This endpoint updates an existing filter

    Args:
        project_id (str):
        subscription_id (str):
        filter_id (str):
        body (ModelsUpdateFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateFilterResponse200 | UpdateFilterResponse400 | UpdateFilterResponse401 | UpdateFilterResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            filter_id=filter_id,
            client=client,
            body=body,
        )
    ).parsed
