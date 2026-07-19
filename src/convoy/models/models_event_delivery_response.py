from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_delivery_mode import DatastoreDeliveryMode
from ..models.datastore_event_delivery_status import DatastoreEventDeliveryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_cli_metadata import DatastoreCLIMetadata
    from ..models.datastore_device import DatastoreDevice
    from ..models.datastore_endpoint import DatastoreEndpoint
    from ..models.datastore_event import DatastoreEvent
    from ..models.datastore_metadata import DatastoreMetadata
    from ..models.datastore_source import DatastoreSource
    from ..models.httpheader_http_header import HttpheaderHTTPHeader


T = TypeVar("T", bound="ModelsEventDeliveryResponse")


@_attrs_define
class ModelsEventDeliveryResponse:
    """
    Attributes:
        acknowledged_at (str | Unset):
        cli_metadata (DatastoreCLIMetadata | Unset):
        created_at (str | Unset):
        deleted_at (str | Unset):
        delivery_mode (DatastoreDeliveryMode | Unset):
        description (str | Unset):
        device_id (str | Unset):
        device_metadata (DatastoreDevice | Unset):
        endpoint_id (str | Unset):
        endpoint_metadata (DatastoreEndpoint | Unset):
        event_id (str | Unset):
        event_metadata (DatastoreEvent | Unset):
        event_type (str | Unset):
        headers (HttpheaderHTTPHeader | Unset):
        idempotency_key (str | Unset):
        latency (str | Unset): Deprecated: Latency is deprecated.
        latency_seconds (float | Unset):
        metadata (DatastoreMetadata | Unset):
        project_id (str | Unset):
        source_metadata (DatastoreSource | Unset):
        status (DatastoreEventDeliveryStatus | Unset):
        subscription_id (str | Unset):
        target_url (str | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url_query_params (str | Unset):
    """

    acknowledged_at: str | Unset = UNSET
    cli_metadata: DatastoreCLIMetadata | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    delivery_mode: DatastoreDeliveryMode | Unset = UNSET
    description: str | Unset = UNSET
    device_id: str | Unset = UNSET
    device_metadata: DatastoreDevice | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    endpoint_metadata: DatastoreEndpoint | Unset = UNSET
    event_id: str | Unset = UNSET
    event_metadata: DatastoreEvent | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: HttpheaderHTTPHeader | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    latency: str | Unset = UNSET
    latency_seconds: float | Unset = UNSET
    metadata: DatastoreMetadata | Unset = UNSET
    project_id: str | Unset = UNSET
    source_metadata: DatastoreSource | Unset = UNSET
    status: DatastoreEventDeliveryStatus | Unset = UNSET
    subscription_id: str | Unset = UNSET
    target_url: str | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url_query_params: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged_at = self.acknowledged_at

        cli_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cli_metadata, Unset):
            cli_metadata = self.cli_metadata.to_dict()

        created_at = self.created_at

        deleted_at = self.deleted_at

        delivery_mode: str | Unset = UNSET
        if not isinstance(self.delivery_mode, Unset):
            delivery_mode = self.delivery_mode.value

        description = self.description

        device_id = self.device_id

        device_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_metadata, Unset):
            device_metadata = self.device_metadata.to_dict()

        endpoint_id = self.endpoint_id

        endpoint_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoint_metadata, Unset):
            endpoint_metadata = self.endpoint_metadata.to_dict()

        event_id = self.event_id

        event_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_metadata, Unset):
            event_metadata = self.event_metadata.to_dict()

        event_type = self.event_type

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        idempotency_key = self.idempotency_key

        latency = self.latency

        latency_seconds = self.latency_seconds

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        project_id = self.project_id

        source_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_metadata, Unset):
            source_metadata = self.source_metadata.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        subscription_id = self.subscription_id

        target_url = self.target_url

        uid = self.uid

        updated_at = self.updated_at

        url_query_params = self.url_query_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if cli_metadata is not UNSET:
            field_dict["cli_metadata"] = cli_metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if delivery_mode is not UNSET:
            field_dict["delivery_mode"] = delivery_mode
        if description is not UNSET:
            field_dict["description"] = description
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if device_metadata is not UNSET:
            field_dict["device_metadata"] = device_metadata
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if endpoint_metadata is not UNSET:
            field_dict["endpoint_metadata"] = endpoint_metadata
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if event_metadata is not UNSET:
            field_dict["event_metadata"] = event_metadata
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if latency is not UNSET:
            field_dict["latency"] = latency
        if latency_seconds is not UNSET:
            field_dict["latency_seconds"] = latency_seconds
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if source_metadata is not UNSET:
            field_dict["source_metadata"] = source_metadata
        if status is not UNSET:
            field_dict["status"] = status
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url_query_params is not UNSET:
            field_dict["url_query_params"] = url_query_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_cli_metadata import DatastoreCLIMetadata
        from ..models.datastore_device import DatastoreDevice
        from ..models.datastore_endpoint import DatastoreEndpoint
        from ..models.datastore_event import DatastoreEvent
        from ..models.datastore_metadata import DatastoreMetadata
        from ..models.datastore_source import DatastoreSource
        from ..models.httpheader_http_header import HttpheaderHTTPHeader

        d = dict(src_dict)
        acknowledged_at = d.pop("acknowledged_at", UNSET)

        _cli_metadata = d.pop("cli_metadata", UNSET)
        cli_metadata: DatastoreCLIMetadata | Unset
        if isinstance(_cli_metadata, Unset):
            cli_metadata = UNSET
        else:
            cli_metadata = DatastoreCLIMetadata.from_dict(_cli_metadata)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        _delivery_mode = d.pop("delivery_mode", UNSET)
        delivery_mode: DatastoreDeliveryMode | Unset
        if isinstance(_delivery_mode, Unset):
            delivery_mode = UNSET
        else:
            delivery_mode = DatastoreDeliveryMode(_delivery_mode)

        description = d.pop("description", UNSET)

        device_id = d.pop("device_id", UNSET)

        _device_metadata = d.pop("device_metadata", UNSET)
        device_metadata: DatastoreDevice | Unset
        if isinstance(_device_metadata, Unset):
            device_metadata = UNSET
        else:
            device_metadata = DatastoreDevice.from_dict(_device_metadata)

        endpoint_id = d.pop("endpoint_id", UNSET)

        _endpoint_metadata = d.pop("endpoint_metadata", UNSET)
        endpoint_metadata: DatastoreEndpoint | Unset
        if isinstance(_endpoint_metadata, Unset):
            endpoint_metadata = UNSET
        else:
            endpoint_metadata = DatastoreEndpoint.from_dict(_endpoint_metadata)

        event_id = d.pop("event_id", UNSET)

        _event_metadata = d.pop("event_metadata", UNSET)
        event_metadata: DatastoreEvent | Unset
        if isinstance(_event_metadata, Unset):
            event_metadata = UNSET
        else:
            event_metadata = DatastoreEvent.from_dict(_event_metadata)

        event_type = d.pop("event_type", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: HttpheaderHTTPHeader | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = HttpheaderHTTPHeader.from_dict(_headers)

        idempotency_key = d.pop("idempotency_key", UNSET)

        latency = d.pop("latency", UNSET)

        latency_seconds = d.pop("latency_seconds", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: DatastoreMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DatastoreMetadata.from_dict(_metadata)

        project_id = d.pop("project_id", UNSET)

        _source_metadata = d.pop("source_metadata", UNSET)
        source_metadata: DatastoreSource | Unset
        if isinstance(_source_metadata, Unset):
            source_metadata = UNSET
        else:
            source_metadata = DatastoreSource.from_dict(_source_metadata)

        _status = d.pop("status", UNSET)
        status: DatastoreEventDeliveryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatastoreEventDeliveryStatus(_status)

        subscription_id = d.pop("subscription_id", UNSET)

        target_url = d.pop("target_url", UNSET)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url_query_params = d.pop("url_query_params", UNSET)

        models_event_delivery_response = cls(
            acknowledged_at=acknowledged_at,
            cli_metadata=cli_metadata,
            created_at=created_at,
            deleted_at=deleted_at,
            delivery_mode=delivery_mode,
            description=description,
            device_id=device_id,
            device_metadata=device_metadata,
            endpoint_id=endpoint_id,
            endpoint_metadata=endpoint_metadata,
            event_id=event_id,
            event_metadata=event_metadata,
            event_type=event_type,
            headers=headers,
            idempotency_key=idempotency_key,
            latency=latency,
            latency_seconds=latency_seconds,
            metadata=metadata,
            project_id=project_id,
            source_metadata=source_metadata,
            status=status,
            subscription_id=subscription_id,
            target_url=target_url,
            uid=uid,
            updated_at=updated_at,
            url_query_params=url_query_params,
        )

        models_event_delivery_response.additional_properties = d
        return models_event_delivery_response

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
