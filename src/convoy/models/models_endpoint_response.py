from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_endpoint_status import DatastoreEndpointStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_endpoint_authentication import (
        DatastoreEndpointAuthentication,
    )
    from ..models.datastore_mtls_client_cert import DatastoreMtlsClientCert
    from ..models.datastore_secret import DatastoreSecret


T = TypeVar("T", bound="ModelsEndpointResponse")


@_attrs_define
class ModelsEndpointResponse:
    """
    Attributes:
        advanced_signatures (bool | Unset):
        authentication (DatastoreEndpointAuthentication | Unset):
        cb_state (str | Unset): CBState is the circuit breaker state ("open", "half-open", "closed") so the UI
            can reflect a tripped breaker on the endpoint status. Nil when CB is
            off/unlicensed or has no sample for this endpoint.
        content_type (str | Unset):
        created_at (str | Unset):
        deleted_at (str | Unset):
        description (str | Unset):
        events (int | Unset):
        failure_count (int | Unset):
        failure_rate (float | Unset): FailureRate is the circuit breaker's rolling failure rate for this endpoint.
            It is a pointer so the API can return null when no rate was computed (circuit
            breaker feature off, or sampler not running), distinct from a genuine 0%.
        http_timeout (int | Unset):
        mtls_client_cert (DatastoreMtlsClientCert | Unset):
        name (str | Unset):
        owner_id (str | Unset):
        period_failure_rate (float | Unset): PeriodFailureRate is the period failure rate from event_deliveries,
            (Failure+Retry)/(Success+Failure+Retry). Retry counts as failed-so-far.
            Nil when the range has no counted deliveries; sibling counts are transient.
        project_id (str | Unset):
        rate_limit (int | Unset):
        rate_limit_duration (int | Unset):
        retry_count (int | Unset):
        secrets (list[DatastoreSecret] | Unset):
        slack_webhook_url (str | Unset):
        status (DatastoreEndpointStatus | Unset):
        success_count (int | Unset):
        support_email (str | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    advanced_signatures: bool | Unset = UNSET
    authentication: DatastoreEndpointAuthentication | Unset = UNSET
    cb_state: str | Unset = UNSET
    content_type: str | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    description: str | Unset = UNSET
    events: int | Unset = UNSET
    failure_count: int | Unset = UNSET
    failure_rate: float | Unset = UNSET
    http_timeout: int | Unset = UNSET
    mtls_client_cert: DatastoreMtlsClientCert | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    period_failure_rate: float | Unset = UNSET
    project_id: str | Unset = UNSET
    rate_limit: int | Unset = UNSET
    rate_limit_duration: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    secrets: list[DatastoreSecret] | Unset = UNSET
    slack_webhook_url: str | Unset = UNSET
    status: DatastoreEndpointStatus | Unset = UNSET
    success_count: int | Unset = UNSET
    support_email: str | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advanced_signatures = self.advanced_signatures

        authentication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        cb_state = self.cb_state

        content_type = self.content_type

        created_at = self.created_at

        deleted_at = self.deleted_at

        description = self.description

        events = self.events

        failure_count = self.failure_count

        failure_rate = self.failure_rate

        http_timeout = self.http_timeout

        mtls_client_cert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mtls_client_cert, Unset):
            mtls_client_cert = self.mtls_client_cert.to_dict()

        name = self.name

        owner_id = self.owner_id

        period_failure_rate = self.period_failure_rate

        project_id = self.project_id

        rate_limit = self.rate_limit

        rate_limit_duration = self.rate_limit_duration

        retry_count = self.retry_count

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        slack_webhook_url = self.slack_webhook_url

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        success_count = self.success_count

        support_email = self.support_email

        uid = self.uid

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advanced_signatures is not UNSET:
            field_dict["advanced_signatures"] = advanced_signatures
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if cb_state is not UNSET:
            field_dict["cb_state"] = cb_state
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if failure_rate is not UNSET:
            field_dict["failure_rate"] = failure_rate
        if http_timeout is not UNSET:
            field_dict["http_timeout"] = http_timeout
        if mtls_client_cert is not UNSET:
            field_dict["mtls_client_cert"] = mtls_client_cert
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if period_failure_rate is not UNSET:
            field_dict["period_failure_rate"] = period_failure_rate
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit
        if rate_limit_duration is not UNSET:
            field_dict["rate_limit_duration"] = rate_limit_duration
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if slack_webhook_url is not UNSET:
            field_dict["slack_webhook_url"] = slack_webhook_url
        if status is not UNSET:
            field_dict["status"] = status
        if success_count is not UNSET:
            field_dict["success_count"] = success_count
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_endpoint_authentication import (
            DatastoreEndpointAuthentication,
        )
        from ..models.datastore_mtls_client_cert import DatastoreMtlsClientCert
        from ..models.datastore_secret import DatastoreSecret

        d = dict(src_dict)
        advanced_signatures = d.pop("advanced_signatures", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: DatastoreEndpointAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = DatastoreEndpointAuthentication.from_dict(_authentication)

        cb_state = d.pop("cb_state", UNSET)

        content_type = d.pop("content_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        description = d.pop("description", UNSET)

        events = d.pop("events", UNSET)

        failure_count = d.pop("failure_count", UNSET)

        failure_rate = d.pop("failure_rate", UNSET)

        http_timeout = d.pop("http_timeout", UNSET)

        _mtls_client_cert = d.pop("mtls_client_cert", UNSET)
        mtls_client_cert: DatastoreMtlsClientCert | Unset
        if isinstance(_mtls_client_cert, Unset):
            mtls_client_cert = UNSET
        else:
            mtls_client_cert = DatastoreMtlsClientCert.from_dict(_mtls_client_cert)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        period_failure_rate = d.pop("period_failure_rate", UNSET)

        project_id = d.pop("project_id", UNSET)

        rate_limit = d.pop("rate_limit", UNSET)

        rate_limit_duration = d.pop("rate_limit_duration", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        _secrets = d.pop("secrets", UNSET)
        secrets: list[DatastoreSecret] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = DatastoreSecret.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        slack_webhook_url = d.pop("slack_webhook_url", UNSET)

        _status = d.pop("status", UNSET)
        status: DatastoreEndpointStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatastoreEndpointStatus(_status)

        success_count = d.pop("success_count", UNSET)

        support_email = d.pop("support_email", UNSET)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        models_endpoint_response = cls(
            advanced_signatures=advanced_signatures,
            authentication=authentication,
            cb_state=cb_state,
            content_type=content_type,
            created_at=created_at,
            deleted_at=deleted_at,
            description=description,
            events=events,
            failure_count=failure_count,
            failure_rate=failure_rate,
            http_timeout=http_timeout,
            mtls_client_cert=mtls_client_cert,
            name=name,
            owner_id=owner_id,
            period_failure_rate=period_failure_rate,
            project_id=project_id,
            rate_limit=rate_limit,
            rate_limit_duration=rate_limit_duration,
            retry_count=retry_count,
            secrets=secrets,
            slack_webhook_url=slack_webhook_url,
            status=status,
            success_count=success_count,
            support_email=support_email,
            uid=uid,
            updated_at=updated_at,
            url=url,
        )

        models_endpoint_response.additional_properties = d
        return models_endpoint_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
