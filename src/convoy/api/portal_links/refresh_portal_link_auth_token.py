from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refresh_portal_link_auth_token_response_200 import (
    RefreshPortalLinkAuthTokenResponse200,
)
from ...models.refresh_portal_link_auth_token_response_400 import (
    RefreshPortalLinkAuthTokenResponse400,
)
from ...models.refresh_portal_link_auth_token_response_401 import (
    RefreshPortalLinkAuthTokenResponse401,
)
from ...models.refresh_portal_link_auth_token_response_404 import (
    RefreshPortalLinkAuthTokenResponse404,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    portal_link_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/portal-links/{portal_link_id}/refresh_token".format(
            project_id=quote(str(project_id), safe=""),
            portal_link_id=quote(str(portal_link_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RefreshPortalLinkAuthTokenResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefreshPortalLinkAuthTokenResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RefreshPortalLinkAuthTokenResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RefreshPortalLinkAuthTokenResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    portal_link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
]:
    """Get a portal link auth token

     This endpoint retrieves a portal link auth token

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshPortalLinkAuthTokenResponse200 | RefreshPortalLinkAuthTokenResponse400 | RefreshPortalLinkAuthTokenResponse401 | RefreshPortalLinkAuthTokenResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        portal_link_id=portal_link_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    portal_link_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
    | None
):
    """Get a portal link auth token

     This endpoint retrieves a portal link auth token

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshPortalLinkAuthTokenResponse200 | RefreshPortalLinkAuthTokenResponse400 | RefreshPortalLinkAuthTokenResponse401 | RefreshPortalLinkAuthTokenResponse404
    """

    return sync_detailed(
        project_id=project_id,
        portal_link_id=portal_link_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    portal_link_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
]:
    """Get a portal link auth token

     This endpoint retrieves a portal link auth token

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshPortalLinkAuthTokenResponse200 | RefreshPortalLinkAuthTokenResponse400 | RefreshPortalLinkAuthTokenResponse401 | RefreshPortalLinkAuthTokenResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        portal_link_id=portal_link_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    portal_link_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    RefreshPortalLinkAuthTokenResponse200
    | RefreshPortalLinkAuthTokenResponse400
    | RefreshPortalLinkAuthTokenResponse401
    | RefreshPortalLinkAuthTokenResponse404
    | None
):
    """Get a portal link auth token

     This endpoint retrieves a portal link auth token

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshPortalLinkAuthTokenResponse200 | RefreshPortalLinkAuthTokenResponse400 | RefreshPortalLinkAuthTokenResponse401 | RefreshPortalLinkAuthTokenResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            portal_link_id=portal_link_id,
            client=client,
        )
    ).parsed
