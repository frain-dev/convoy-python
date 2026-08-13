from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_endpoint_period_failure_rates_response_200 import (
    GetEndpointPeriodFailureRatesResponse200,
)
from ...models.get_endpoint_period_failure_rates_response_400 import (
    GetEndpointPeriodFailureRatesResponse400,
)
from ...models.get_endpoint_period_failure_rates_response_401 import (
    GetEndpointPeriodFailureRatesResponse401,
)
from ...models.get_endpoint_period_failure_rates_response_404 import (
    GetEndpointPeriodFailureRatesResponse404,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    endpoint_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_endpoint_id: list[str] | Unset = UNSET
    if not isinstance(endpoint_id, Unset):
        json_endpoint_id = endpoint_id

    params["endpointId"] = json_endpoint_id

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/endpoints/period-failure-rates".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
    | None
):
    if response.status_code == 200:
        response_200 = GetEndpointPeriodFailureRatesResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = GetEndpointPeriodFailureRatesResponse400.from_dict(
            response.json()
        )

        return response_400

    if response.status_code == 401:
        response_401 = GetEndpointPeriodFailureRatesResponse401.from_dict(
            response.json()
        )

        return response_401

    if response.status_code == 404:
        response_404 = GetEndpointPeriodFailureRatesResponse404.from_dict(
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
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
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
    endpoint_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> Response[
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
]:
    """Endpoint period failure rates

     Display-only delivery rates for the given endpoint ids over a date range (default last 7 days).
    Independent of the list so a slow COUNT cannot delay the table.

    Args:
        project_id (str):
        endpoint_id (list[str] | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEndpointPeriodFailureRatesResponse200 | GetEndpointPeriodFailureRatesResponse400 | GetEndpointPeriodFailureRatesResponse401 | GetEndpointPeriodFailureRatesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    endpoint_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> (
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
    | None
):
    """Endpoint period failure rates

     Display-only delivery rates for the given endpoint ids over a date range (default last 7 days).
    Independent of the list so a slow COUNT cannot delay the table.

    Args:
        project_id (str):
        endpoint_id (list[str] | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEndpointPeriodFailureRatesResponse200 | GetEndpointPeriodFailureRatesResponse400 | GetEndpointPeriodFailureRatesResponse401 | GetEndpointPeriodFailureRatesResponse404
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        endpoint_id=endpoint_id,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    endpoint_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> Response[
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
]:
    """Endpoint period failure rates

     Display-only delivery rates for the given endpoint ids over a date range (default last 7 days).
    Independent of the list so a slow COUNT cannot delay the table.

    Args:
        project_id (str):
        endpoint_id (list[str] | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetEndpointPeriodFailureRatesResponse200 | GetEndpointPeriodFailureRatesResponse400 | GetEndpointPeriodFailureRatesResponse401 | GetEndpointPeriodFailureRatesResponse404]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        endpoint_id=endpoint_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    endpoint_id: list[str] | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
) -> (
    GetEndpointPeriodFailureRatesResponse200
    | GetEndpointPeriodFailureRatesResponse400
    | GetEndpointPeriodFailureRatesResponse401
    | GetEndpointPeriodFailureRatesResponse404
    | None
):
    """Endpoint period failure rates

     Display-only delivery rates for the given endpoint ids over a date range (default last 7 days).
    Independent of the list so a slow COUNT cannot delay the table.

    Args:
        project_id (str):
        endpoint_id (list[str] | Unset):
        start_date (str | Unset):
        end_date (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetEndpointPeriodFailureRatesResponse200 | GetEndpointPeriodFailureRatesResponse400 | GetEndpointPeriodFailureRatesResponse401 | GetEndpointPeriodFailureRatesResponse404
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            endpoint_id=endpoint_id,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
