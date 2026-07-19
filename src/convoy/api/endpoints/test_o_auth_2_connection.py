from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_test_o_auth_2_request import ModelsTestOAuth2Request
from ...models.test_o_auth_2_connection_response_200 import (
    TestOAuth2ConnectionResponse200,
)
from ...models.test_o_auth_2_connection_response_400 import (
    TestOAuth2ConnectionResponse400,
)
from ...models.test_o_auth_2_connection_response_401 import (
    TestOAuth2ConnectionResponse401,
)
from ...models.test_o_auth_2_connection_response_404 import (
    TestOAuth2ConnectionResponse404,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsTestOAuth2Request,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/endpoints/oauth2/test".format(
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
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
    | None
):
    if response.status_code == 200:
        response_200 = TestOAuth2ConnectionResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TestOAuth2ConnectionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = TestOAuth2ConnectionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = TestOAuth2ConnectionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
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
    body: ModelsTestOAuth2Request,
) -> Response[
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
]:
    """Test OAuth2 connection

     This endpoint tests the OAuth2 connection by attempting to exchange a token

    Args:
        project_id (str):
        body (ModelsTestOAuth2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestOAuth2ConnectionResponse200 | TestOAuth2ConnectionResponse400 | TestOAuth2ConnectionResponse401 | TestOAuth2ConnectionResponse404]
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
    body: ModelsTestOAuth2Request,
) -> (
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
    | None
):
    """Test OAuth2 connection

     This endpoint tests the OAuth2 connection by attempting to exchange a token

    Args:
        project_id (str):
        body (ModelsTestOAuth2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestOAuth2ConnectionResponse200 | TestOAuth2ConnectionResponse400 | TestOAuth2ConnectionResponse401 | TestOAuth2ConnectionResponse404
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
    body: ModelsTestOAuth2Request,
) -> Response[
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
]:
    """Test OAuth2 connection

     This endpoint tests the OAuth2 connection by attempting to exchange a token

    Args:
        project_id (str):
        body (ModelsTestOAuth2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TestOAuth2ConnectionResponse200 | TestOAuth2ConnectionResponse400 | TestOAuth2ConnectionResponse401 | TestOAuth2ConnectionResponse404]
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
    body: ModelsTestOAuth2Request,
) -> (
    TestOAuth2ConnectionResponse200
    | TestOAuth2ConnectionResponse400
    | TestOAuth2ConnectionResponse401
    | TestOAuth2ConnectionResponse404
    | None
):
    """Test OAuth2 connection

     This endpoint tests the OAuth2 connection by attempting to exchange a token

    Args:
        project_id (str):
        body (ModelsTestOAuth2Request):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TestOAuth2ConnectionResponse200 | TestOAuth2ConnectionResponse400 | TestOAuth2ConnectionResponse401 | TestOAuth2ConnectionResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
