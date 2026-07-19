from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_test_filter_request import ModelsTestFilterRequest
from ...models.test_filter_response_200 import TestFilterResponse200
from ...models.test_filter_response_400 import TestFilterResponse400
from ...models.test_filter_response_401 import TestFilterResponse401
from ...models.test_filter_response_404 import TestFilterResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    subscription_id: str,
    event_type: str,
    *,
    body: ModelsTestFilterRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/subscriptions/{subscription_id}/filters/test/{event_type}".format(
            project_id=quote(str(project_id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
            event_type=quote(str(event_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
    | None
):
    if response.status_code == 200:
        response_200 = TestFilterResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TestFilterResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TestFilterResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = TestFilterResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
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
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: ModelsTestFilterRequest,
) -> Response[
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
]:
    """Test a filter

     This endpoint tests a filter against a payload

    Args:
        project_id (str):
        subscription_id (str):
        event_type (str):
        body (ModelsTestFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestFilterResponse200 | TestFilterResponse400 | TestFilterResponse401 | TestFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        event_type=event_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    subscription_id: str,
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: ModelsTestFilterRequest,
) -> (
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
    | None
):
    """Test a filter

     This endpoint tests a filter against a payload

    Args:
        project_id (str):
        subscription_id (str):
        event_type (str):
        body (ModelsTestFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestFilterResponse200 | TestFilterResponse400 | TestFilterResponse401 | TestFilterResponse404
    """

    return sync_detailed(
        project_id=project_id,
        subscription_id=subscription_id,
        event_type=event_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    subscription_id: str,
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: ModelsTestFilterRequest,
) -> Response[
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
]:
    """Test a filter

     This endpoint tests a filter against a payload

    Args:
        project_id (str):
        subscription_id (str):
        event_type (str):
        body (ModelsTestFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestFilterResponse200 | TestFilterResponse400 | TestFilterResponse401 | TestFilterResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        subscription_id=subscription_id,
        event_type=event_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    subscription_id: str,
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: ModelsTestFilterRequest,
) -> (
    TestFilterResponse200
    | TestFilterResponse400
    | TestFilterResponse401
    | TestFilterResponse404
    | None
):
    """Test a filter

     This endpoint tests a filter against a payload

    Args:
        project_id (str):
        subscription_id (str):
        event_type (str):
        body (ModelsTestFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestFilterResponse200 | TestFilterResponse400 | TestFilterResponse401 | TestFilterResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            subscription_id=subscription_id,
            event_type=event_type,
            client=client,
            body=body,
        )
    ).parsed
