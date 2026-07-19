from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expire_secret_response_200 import ExpireSecretResponse200
from ...models.expire_secret_response_400 import ExpireSecretResponse400
from ...models.expire_secret_response_401 import ExpireSecretResponse401
from ...models.expire_secret_response_404 import ExpireSecretResponse404
from ...models.models_expire_secret import ModelsExpireSecret
from ...types import Response


def _get_kwargs(
    project_id: str,
    endpoint_id: str,
    *,
    body: ModelsExpireSecret,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projects/{project_id}/endpoints/{endpoint_id}/expire_secret".format(
            project_id=quote(str(project_id), safe=""),
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
    | None
):
    if response.status_code == 200:
        response_200 = ExpireSecretResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ExpireSecretResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ExpireSecretResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ExpireSecretResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsExpireSecret,
) -> Response[
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
]:
    """Roll endpoint secret

     This endpoint expires and re-generates the endpoint secret.

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsExpireSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpireSecretResponse200 | ExpireSecretResponse400 | ExpireSecretResponse401 | ExpireSecretResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsExpireSecret,
) -> (
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
    | None
):
    """Roll endpoint secret

     This endpoint expires and re-generates the endpoint secret.

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsExpireSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpireSecretResponse200 | ExpireSecretResponse400 | ExpireSecretResponse401 | ExpireSecretResponse404
    """

    return sync_detailed(
        project_id=project_id,
        endpoint_id=endpoint_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsExpireSecret,
) -> Response[
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
]:
    """Roll endpoint secret

     This endpoint expires and re-generates the endpoint secret.

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsExpireSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpireSecretResponse200 | ExpireSecretResponse400 | ExpireSecretResponse401 | ExpireSecretResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    endpoint_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsExpireSecret,
) -> (
    ExpireSecretResponse200
    | ExpireSecretResponse400
    | ExpireSecretResponse401
    | ExpireSecretResponse404
    | None
):
    """Roll endpoint secret

     This endpoint expires and re-generates the endpoint secret.

    Args:
        project_id (str):
        endpoint_id (str):
        body (ModelsExpireSecret):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpireSecretResponse200 | ExpireSecretResponse400 | ExpireSecretResponse401 | ExpireSecretResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            endpoint_id=endpoint_id,
            client=client,
            body=body,
        )
    ).parsed
