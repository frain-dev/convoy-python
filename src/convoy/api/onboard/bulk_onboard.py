from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_onboard_response_200 import BulkOnboardResponse200
from ...models.bulk_onboard_response_202 import BulkOnboardResponse202
from ...models.bulk_onboard_response_400 import BulkOnboardResponse400
from ...models.bulk_onboard_response_401 import BulkOnboardResponse401
from ...models.bulk_onboard_response_404 import BulkOnboardResponse404
from ...models.models_bulk_onboard_request import ModelsBulkOnboardRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: ModelsBulkOnboardRequest | Unset = UNSET,
    dry_run: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/onboard".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
    | None
):
    if response.status_code == 200:
        response_200 = BulkOnboardResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = BulkOnboardResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = BulkOnboardResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = BulkOnboardResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = BulkOnboardResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
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
    body: ModelsBulkOnboardRequest | Unset = UNSET,
    dry_run: bool | Unset = UNSET,
) -> Response[
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
]:
    r"""Bulk onboard endpoints with subscriptions

     This endpoint bulk-creates endpoints with subscriptions from a JSON body. A CSV file upload is also
    accepted over raw HTTP as multipart/form-data with a \"file\" field; generated SDK clients only
    expose the JSON body.

    Args:
        project_id (str):
        dry_run (bool | Unset):
        body (ModelsBulkOnboardRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkOnboardResponse200 | BulkOnboardResponse202 | BulkOnboardResponse400 | BulkOnboardResponse401 | BulkOnboardResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        dry_run=dry_run,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsBulkOnboardRequest | Unset = UNSET,
    dry_run: bool | Unset = UNSET,
) -> (
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
    | None
):
    r"""Bulk onboard endpoints with subscriptions

     This endpoint bulk-creates endpoints with subscriptions from a JSON body. A CSV file upload is also
    accepted over raw HTTP as multipart/form-data with a \"file\" field; generated SDK clients only
    expose the JSON body.

    Args:
        project_id (str):
        dry_run (bool | Unset):
        body (ModelsBulkOnboardRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkOnboardResponse200 | BulkOnboardResponse202 | BulkOnboardResponse400 | BulkOnboardResponse401 | BulkOnboardResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        dry_run=dry_run,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsBulkOnboardRequest | Unset = UNSET,
    dry_run: bool | Unset = UNSET,
) -> Response[
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
]:
    r"""Bulk onboard endpoints with subscriptions

     This endpoint bulk-creates endpoints with subscriptions from a JSON body. A CSV file upload is also
    accepted over raw HTTP as multipart/form-data with a \"file\" field; generated SDK clients only
    expose the JSON body.

    Args:
        project_id (str):
        dry_run (bool | Unset):
        body (ModelsBulkOnboardRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkOnboardResponse200 | BulkOnboardResponse202 | BulkOnboardResponse400 | BulkOnboardResponse401 | BulkOnboardResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ModelsBulkOnboardRequest | Unset = UNSET,
    dry_run: bool | Unset = UNSET,
) -> (
    BulkOnboardResponse200
    | BulkOnboardResponse202
    | BulkOnboardResponse400
    | BulkOnboardResponse401
    | BulkOnboardResponse404
    | None
):
    r"""Bulk onboard endpoints with subscriptions

     This endpoint bulk-creates endpoints with subscriptions from a JSON body. A CSV file upload is also
    accepted over raw HTTP as multipart/form-data with a \"file\" field; generated SDK clients only
    expose the JSON body.

    Args:
        project_id (str):
        dry_run (bool | Unset):
        body (ModelsBulkOnboardRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkOnboardResponse200 | BulkOnboardResponse202 | BulkOnboardResponse400 | BulkOnboardResponse401 | BulkOnboardResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            dry_run=dry_run,
        )
    ).parsed
