from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
    from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0


T = TypeVar("T", bound="ModelsEventDeliveryResponse")


@_attrs_define
class ModelsEventDeliveryResponse:
    """
    Attributes:
        acknowledged_at (None | str | Unset):
        cli_metadata (DatastoreCLIMetadata | None | Unset):
        created_at (str | Unset):
        deleted_at (None | str | Unset):
        delivery_mode (DatastoreDeliveryMode | Unset):
        description (str | Unset):
        device_id (str | Unset):
        device_metadata (DatastoreDevice | None | Unset):
        endpoint_id (str | Unset):
        endpoint_metadata (DatastoreEndpoint | None | Unset):
        event_id (str | Unset):
        event_metadata (DatastoreEvent | None | Unset):
        event_type (str | Unset):
        headers (HttpheaderHTTPHeaderType0 | None | Unset):
        idempotency_key (str | Unset):
        latency (str | Unset): Deprecated: Latency is deprecated.
        latency_seconds (float | Unset):
        metadata (DatastoreMetadata | None | Unset):
        project_id (str | Unset):
        source_metadata (DatastoreSource | None | Unset):
        status (DatastoreEventDeliveryStatus | Unset):
        subscription_id (str | Unset):
        target_url (str | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url_query_params (str | Unset):
    """

    acknowledged_at: None | str | Unset = UNSET
    cli_metadata: DatastoreCLIMetadata | None | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    delivery_mode: DatastoreDeliveryMode | Unset = UNSET
    description: str | Unset = UNSET
    device_id: str | Unset = UNSET
    device_metadata: DatastoreDevice | None | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    endpoint_metadata: DatastoreEndpoint | None | Unset = UNSET
    event_id: str | Unset = UNSET
    event_metadata: DatastoreEvent | None | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: HttpheaderHTTPHeaderType0 | None | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    latency: str | Unset = UNSET
    latency_seconds: float | Unset = UNSET
    metadata: DatastoreMetadata | None | Unset = UNSET
    project_id: str | Unset = UNSET
    source_metadata: DatastoreSource | None | Unset = UNSET
    status: DatastoreEventDeliveryStatus | Unset = UNSET
    subscription_id: str | Unset = UNSET
    target_url: str | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url_query_params: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_cli_metadata import DatastoreCLIMetadata
        from ..models.datastore_device import DatastoreDevice
        from ..models.datastore_endpoint import DatastoreEndpoint
        from ..models.datastore_event import DatastoreEvent
        from ..models.datastore_metadata import DatastoreMetadata
        from ..models.datastore_source import DatastoreSource
        from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        cli_metadata: dict[str, Any] | None | Unset
        if isinstance(self.cli_metadata, Unset):
            cli_metadata = UNSET
        elif isinstance(self.cli_metadata, DatastoreCLIMetadata):
            cli_metadata = self.cli_metadata.to_dict()
        else:
            cli_metadata = self.cli_metadata

        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        delivery_mode: str | Unset = UNSET
        if not isinstance(self.delivery_mode, Unset):
            delivery_mode = self.delivery_mode.value

        description = self.description

        device_id = self.device_id

        device_metadata: dict[str, Any] | None | Unset
        if isinstance(self.device_metadata, Unset):
            device_metadata = UNSET
        elif isinstance(self.device_metadata, DatastoreDevice):
            device_metadata = self.device_metadata.to_dict()
        else:
            device_metadata = self.device_metadata

        endpoint_id = self.endpoint_id

        endpoint_metadata: dict[str, Any] | None | Unset
        if isinstance(self.endpoint_metadata, Unset):
            endpoint_metadata = UNSET
        elif isinstance(self.endpoint_metadata, DatastoreEndpoint):
            endpoint_metadata = self.endpoint_metadata.to_dict()
        else:
            endpoint_metadata = self.endpoint_metadata

        event_id = self.event_id

        event_metadata: dict[str, Any] | None | Unset
        if isinstance(self.event_metadata, Unset):
            event_metadata = UNSET
        elif isinstance(self.event_metadata, DatastoreEvent):
            event_metadata = self.event_metadata.to_dict()
        else:
            event_metadata = self.event_metadata

        event_type = self.event_type

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, HttpheaderHTTPHeaderType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        idempotency_key = self.idempotency_key

        latency = self.latency

        latency_seconds = self.latency_seconds

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DatastoreMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        project_id = self.project_id

        source_metadata: dict[str, Any] | None | Unset
        if isinstance(self.source_metadata, Unset):
            source_metadata = UNSET
        elif isinstance(self.source_metadata, DatastoreSource):
            source_metadata = self.source_metadata.to_dict()
        else:
            source_metadata = self.source_metadata

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
        from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0

        d = dict(src_dict)

        def _parse_acknowledged_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_cli_metadata(data: object) -> DatastoreCLIMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cli_metadata_type_1 = DatastoreCLIMetadata.from_dict(data)

                return cli_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreCLIMetadata | None | Unset, data)

        cli_metadata = _parse_cli_metadata(d.pop("cli_metadata", UNSET))

        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        _delivery_mode = d.pop("delivery_mode", UNSET)
        delivery_mode: DatastoreDeliveryMode | Unset
        if isinstance(_delivery_mode, Unset):
            delivery_mode = UNSET
        else:
            delivery_mode = DatastoreDeliveryMode(_delivery_mode)

        description = d.pop("description", UNSET)

        device_id = d.pop("device_id", UNSET)

        def _parse_device_metadata(data: object) -> DatastoreDevice | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_metadata_type_1 = DatastoreDevice.from_dict(data)

                return device_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreDevice | None | Unset, data)

        device_metadata = _parse_device_metadata(d.pop("device_metadata", UNSET))

        endpoint_id = d.pop("endpoint_id", UNSET)

        def _parse_endpoint_metadata(data: object) -> DatastoreEndpoint | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_metadata_type_1 = DatastoreEndpoint.from_dict(data)

                return endpoint_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreEndpoint | None | Unset, data)

        endpoint_metadata = _parse_endpoint_metadata(d.pop("endpoint_metadata", UNSET))

        event_id = d.pop("event_id", UNSET)

        def _parse_event_metadata(data: object) -> DatastoreEvent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                event_metadata_type_1 = DatastoreEvent.from_dict(data)

                return event_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreEvent | None | Unset, data)

        event_metadata = _parse_event_metadata(d.pop("event_metadata", UNSET))

        event_type = d.pop("event_type", UNSET)

        def _parse_headers(data: object) -> HttpheaderHTTPHeaderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemashttpheader_http_header_type_0 = (
                    HttpheaderHTTPHeaderType0.from_dict(data)
                )

                return componentsschemashttpheader_http_header_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpheaderHTTPHeaderType0 | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        idempotency_key = d.pop("idempotency_key", UNSET)

        latency = d.pop("latency", UNSET)

        latency_seconds = d.pop("latency_seconds", UNSET)

        def _parse_metadata(data: object) -> DatastoreMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = DatastoreMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        project_id = d.pop("project_id", UNSET)

        def _parse_source_metadata(data: object) -> DatastoreSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_metadata_type_1 = DatastoreSource.from_dict(data)

                return source_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreSource | None | Unset, data)

        source_metadata = _parse_source_metadata(d.pop("source_metadata", UNSET))

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
