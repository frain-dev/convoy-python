from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_project_response_200 import DeleteProjectResponse200
from ...models.delete_project_response_400 import DeleteProjectResponse400
from ...models.delete_project_response_401 import DeleteProjectResponse401
from ...models.delete_project_response_403 import DeleteProjectResponse403
from ...models.delete_project_response_404 import DeleteProjectResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/projects/{project_id}".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
    | None
):
    if response.status_code == 200:
        response_200 = DeleteProjectResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DeleteProjectResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DeleteProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
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
) -> Response[
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
]:
    """Delete a project

     This endpoint deletes a project

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectResponse200 | DeleteProjectResponse400 | DeleteProjectResponse401 | DeleteProjectResponse403 | DeleteProjectResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
    | None
):
    """Delete a project

     This endpoint deletes a project

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectResponse200 | DeleteProjectResponse400 | DeleteProjectResponse401 | DeleteProjectResponse403 | DeleteProjectResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
]:
    """Delete a project

     This endpoint deletes a project

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectResponse200 | DeleteProjectResponse400 | DeleteProjectResponse401 | DeleteProjectResponse403 | DeleteProjectResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    DeleteProjectResponse200
    | DeleteProjectResponse400
    | DeleteProjectResponse401
    | DeleteProjectResponse403
    | DeleteProjectResponse404
    | None
):
    """Delete a project

     This endpoint deletes a project

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectResponse200 | DeleteProjectResponse400 | DeleteProjectResponse401 | DeleteProjectResponse403 | DeleteProjectResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
