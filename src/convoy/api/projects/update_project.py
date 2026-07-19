from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_update_project import ModelsUpdateProject
from ...models.update_project_response_202 import UpdateProjectResponse202
from ...models.update_project_response_400 import UpdateProjectResponse400
from ...models.update_project_response_401 import UpdateProjectResponse401
from ...models.update_project_response_403 import UpdateProjectResponse403
from ...models.update_project_response_404 import UpdateProjectResponse404
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsUpdateProject,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}".format(
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
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
    | None
):
    if response.status_code == 202:
        response_202 = UpdateProjectResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = UpdateProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UpdateProjectResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UpdateProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
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
    body: ModelsUpdateProject,
) -> Response[
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
]:
    """Update a project

     This endpoint updates a project's name, logo, and config

    Args:
        project_id (str):
        body (ModelsUpdateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProjectResponse202 | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse403 | UpdateProjectResponse404]
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
    body: ModelsUpdateProject,
) -> (
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
    | None
):
    """Update a project

     This endpoint updates a project's name, logo, and config

    Args:
        project_id (str):
        body (ModelsUpdateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProjectResponse202 | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse403 | UpdateProjectResponse404
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
    body: ModelsUpdateProject,
) -> Response[
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
]:
    """Update a project

     This endpoint updates a project's name, logo, and config

    Args:
        project_id (str):
        body (ModelsUpdateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProjectResponse202 | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse403 | UpdateProjectResponse404]
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
    body: ModelsUpdateProject,
) -> (
    UpdateProjectResponse202
    | UpdateProjectResponse400
    | UpdateProjectResponse401
    | UpdateProjectResponse403
    | UpdateProjectResponse404
    | None
):
    """Update a project

     This endpoint updates a project's name, logo, and config

    Args:
        project_id (str):
        body (ModelsUpdateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProjectResponse202 | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse403 | UpdateProjectResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
