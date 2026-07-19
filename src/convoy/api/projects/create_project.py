from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_response_201 import CreateProjectResponse201
from ...models.create_project_response_400 import CreateProjectResponse400
from ...models.create_project_response_401 import CreateProjectResponse401
from ...models.create_project_response_402 import CreateProjectResponse402
from ...models.create_project_response_403 import CreateProjectResponse403
from ...models.create_project_response_404 import CreateProjectResponse404
from ...models.models_create_project import ModelsCreateProject
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: ModelsCreateProject,
    org_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["orgID"] = org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
    | None
):
    if response.status_code == 201:
        response_201 = CreateProjectResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = CreateProjectResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = CreateProjectResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreateProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsCreateProject,
    org_id: str,
) -> Response[
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
]:
    """Create a project

     This endpoint creates a project. Authenticate with a personal API key or JWT and pass the
    organisation id as the orgID query parameter. The response includes the project and a one-time
    project API key.

    Args:
        org_id (str):
        body (ModelsCreateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse201 | CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse402 | CreateProjectResponse403 | CreateProjectResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ModelsCreateProject,
    org_id: str,
) -> (
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
    | None
):
    """Create a project

     This endpoint creates a project. Authenticate with a personal API key or JWT and pass the
    organisation id as the orgID query parameter. The response includes the project and a one-time
    project API key.

    Args:
        org_id (str):
        body (ModelsCreateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse201 | CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse402 | CreateProjectResponse403 | CreateProjectResponse404
    """

    return sync_detailed(
        client=client,
        body=body,
        org_id=org_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ModelsCreateProject,
    org_id: str,
) -> Response[
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
]:
    """Create a project

     This endpoint creates a project. Authenticate with a personal API key or JWT and pass the
    organisation id as the orgID query parameter. The response includes the project and a one-time
    project API key.

    Args:
        org_id (str):
        body (ModelsCreateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse201 | CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse402 | CreateProjectResponse403 | CreateProjectResponse404]
    """

    kwargs = _get_kwargs(
        body=body,
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ModelsCreateProject,
    org_id: str,
) -> (
    CreateProjectResponse201
    | CreateProjectResponse400
    | CreateProjectResponse401
    | CreateProjectResponse402
    | CreateProjectResponse403
    | CreateProjectResponse404
    | None
):
    """Create a project

     This endpoint creates a project. Authenticate with a personal API key or JWT and pass the
    organisation id as the orgID query parameter. The response includes the project and a one-time
    project API key.

    Args:
        org_id (str):
        body (ModelsCreateProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse201 | CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse402 | CreateProjectResponse403 | CreateProjectResponse404
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            org_id=org_id,
        )
    ).parsed
