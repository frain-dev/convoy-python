from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.import_open_api_spec_response_200 import ImportOpenApiSpecResponse200
from ...models.import_open_api_spec_response_400 import ImportOpenApiSpecResponse400
from ...models.import_open_api_spec_response_401 import ImportOpenApiSpecResponse401
from ...models.import_open_api_spec_response_404 import ImportOpenApiSpecResponse404
from ...models.models_import_open_api_spec import ModelsImportOpenAPISpec
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsImportOpenAPISpec,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/event-types/import".format(
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
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ImportOpenApiSpecResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ImportOpenApiSpecResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ImportOpenApiSpecResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ImportOpenApiSpecResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
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
    body: ModelsImportOpenAPISpec,
) -> Response[
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
]:
    """Import event types from OpenAPI spec

     This endpoint imports event types from an OpenAPI specification

    Args:
        project_id (str):
        body (ModelsImportOpenAPISpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportOpenApiSpecResponse200 | ImportOpenApiSpecResponse400 | ImportOpenApiSpecResponse401 | ImportOpenApiSpecResponse404]
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
    body: ModelsImportOpenAPISpec,
) -> (
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
    | None
):
    """Import event types from OpenAPI spec

     This endpoint imports event types from an OpenAPI specification

    Args:
        project_id (str):
        body (ModelsImportOpenAPISpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportOpenApiSpecResponse200 | ImportOpenApiSpecResponse400 | ImportOpenApiSpecResponse401 | ImportOpenApiSpecResponse404
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
    body: ModelsImportOpenAPISpec,
) -> Response[
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
]:
    """Import event types from OpenAPI spec

     This endpoint imports event types from an OpenAPI specification

    Args:
        project_id (str):
        body (ModelsImportOpenAPISpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportOpenApiSpecResponse200 | ImportOpenApiSpecResponse400 | ImportOpenApiSpecResponse401 | ImportOpenApiSpecResponse404]
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
    body: ModelsImportOpenAPISpec,
) -> (
    ImportOpenApiSpecResponse200
    | ImportOpenApiSpecResponse400
    | ImportOpenApiSpecResponse401
    | ImportOpenApiSpecResponse404
    | None
):
    """Import event types from OpenAPI spec

     This endpoint imports event types from an OpenAPI specification

    Args:
        project_id (str):
        body (ModelsImportOpenAPISpec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportOpenApiSpecResponse200 | ImportOpenApiSpecResponse400 | ImportOpenApiSpecResponse401 | ImportOpenApiSpecResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
