from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_portal_link_response_200 import RevokePortalLinkResponse200
from ...models.revoke_portal_link_response_400 import RevokePortalLinkResponse400
from ...models.revoke_portal_link_response_401 import RevokePortalLinkResponse401
from ...models.revoke_portal_link_response_404 import RevokePortalLinkResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    portal_link_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/portal-links/{portal_link_id}/revoke".format(
            project_id=quote(str(project_id), safe=""),
            portal_link_id=quote(str(portal_link_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
    | None
):
    if response.status_code == 200:
        response_200 = RevokePortalLinkResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RevokePortalLinkResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RevokePortalLinkResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokePortalLinkResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
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
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
]:
    """Revoke a portal link

     This endpoint revokes a portal link

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokePortalLinkResponse200 | RevokePortalLinkResponse400 | RevokePortalLinkResponse401 | RevokePortalLinkResponse404]
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
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
    | None
):
    """Revoke a portal link

     This endpoint revokes a portal link

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokePortalLinkResponse200 | RevokePortalLinkResponse400 | RevokePortalLinkResponse401 | RevokePortalLinkResponse404
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
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
]:
    """Revoke a portal link

     This endpoint revokes a portal link

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokePortalLinkResponse200 | RevokePortalLinkResponse400 | RevokePortalLinkResponse401 | RevokePortalLinkResponse404]
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
    RevokePortalLinkResponse200
    | RevokePortalLinkResponse400
    | RevokePortalLinkResponse401
    | RevokePortalLinkResponse404
    | None
):
    """Revoke a portal link

     This endpoint revokes a portal link

    Args:
        project_id (str):
        portal_link_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokePortalLinkResponse200 | RevokePortalLinkResponse400 | RevokePortalLinkResponse401 | RevokePortalLinkResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            portal_link_id=portal_link_id,
            client=client,
        )
    ).parsed
