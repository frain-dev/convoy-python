from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.models_function_request import ModelsFunctionRequest
from ...models.post_v1_projects_project_id_sources_test_function_response_200 import (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200,
)
from ...models.post_v1_projects_project_id_sources_test_function_response_400 import (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse400,
)
from ...models.post_v1_projects_project_id_sources_test_function_response_401 import (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse401,
)
from ...models.post_v1_projects_project_id_sources_test_function_response_404 import (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse404,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsFunctionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/sources/test_function".format(
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
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
    | None
):
    if response.status_code == 200:
        response_200 = PostV1ProjectsProjectIDSourcesTestFunctionResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = PostV1ProjectsProjectIDSourcesTestFunctionResponse400.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 401:
        response_401 = PostV1ProjectsProjectIDSourcesTestFunctionResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 404:
        response_404 = PostV1ProjectsProjectIDSourcesTestFunctionResponse404.from_dict(
            response.json()
        )

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
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
    body: ModelsFunctionRequest,
) -> Response[
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
]:
    """Validate source function

     This endpoint validates that a filter will match a certain payload structure.

    Args:
        project_id (str):
        body (ModelsFunctionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV1ProjectsProjectIDSourcesTestFunctionResponse200 | PostV1ProjectsProjectIDSourcesTestFunctionResponse400 | PostV1ProjectsProjectIDSourcesTestFunctionResponse401 | PostV1ProjectsProjectIDSourcesTestFunctionResponse404]
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
    body: ModelsFunctionRequest,
) -> (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
    | None
):
    """Validate source function

     This endpoint validates that a filter will match a certain payload structure.

    Args:
        project_id (str):
        body (ModelsFunctionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV1ProjectsProjectIDSourcesTestFunctionResponse200 | PostV1ProjectsProjectIDSourcesTestFunctionResponse400 | PostV1ProjectsProjectIDSourcesTestFunctionResponse401 | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
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
    body: ModelsFunctionRequest,
) -> Response[
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
]:
    """Validate source function

     This endpoint validates that a filter will match a certain payload structure.

    Args:
        project_id (str):
        body (ModelsFunctionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV1ProjectsProjectIDSourcesTestFunctionResponse200 | PostV1ProjectsProjectIDSourcesTestFunctionResponse400 | PostV1ProjectsProjectIDSourcesTestFunctionResponse401 | PostV1ProjectsProjectIDSourcesTestFunctionResponse404]
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
    body: ModelsFunctionRequest,
) -> (
    PostV1ProjectsProjectIDSourcesTestFunctionResponse200
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse400
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse401
    | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
    | None
):
    """Validate source function

     This endpoint validates that a filter will match a certain payload structure.

    Args:
        project_id (str):
        body (ModelsFunctionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV1ProjectsProjectIDSourcesTestFunctionResponse200 | PostV1ProjectsProjectIDSourcesTestFunctionResponse400 | PostV1ProjectsProjectIDSourcesTestFunctionResponse401 | PostV1ProjectsProjectIDSourcesTestFunctionResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
