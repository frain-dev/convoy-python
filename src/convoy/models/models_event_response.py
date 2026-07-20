from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_event_status import DatastoreEventStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_endpoint import DatastoreEndpoint
    from ..models.datastore_source import DatastoreSource
    from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0
    from ..models.models_event_response_data_type_0 import ModelsEventResponseDataType0


T = TypeVar("T", bound="ModelsEventResponse")


@_attrs_define
class ModelsEventResponse:
    """
    Attributes:
        acknowledged_at (None | str | Unset):
        app_id (str | Unset): Deprecated
        created_at (str | Unset):
        data (ModelsEventResponseDataType0 | None | Unset): Data is an arbitrary JSON value that gets sent as the body
            of the
            webhook to the endpoints
        deleted_at (None | str | Unset):
        endpoint_metadata (list[DatastoreEndpoint] | Unset):
        endpoints (list[str] | Unset):
        event_type (str | Unset):
        headers (HttpheaderHTTPHeaderType0 | None | Unset):
        idempotency_key (str | Unset):
        is_duplicate_event (bool | Unset):
        metadata (str | Unset):
        project_id (str | Unset):
        raw (str | Unset):
        source_id (str | Unset):
        source_metadata (DatastoreSource | None | Unset):
        status (DatastoreEventStatus | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url_path (str | Unset):
        url_query_params (str | Unset):
    """

    acknowledged_at: None | str | Unset = UNSET
    app_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    data: ModelsEventResponseDataType0 | None | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    endpoint_metadata: list[DatastoreEndpoint] | Unset = UNSET
    endpoints: list[str] | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: HttpheaderHTTPHeaderType0 | None | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    is_duplicate_event: bool | Unset = UNSET
    metadata: str | Unset = UNSET
    project_id: str | Unset = UNSET
    raw: str | Unset = UNSET
    source_id: str | Unset = UNSET
    source_metadata: DatastoreSource | None | Unset = UNSET
    status: DatastoreEventStatus | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url_path: str | Unset = UNSET
    url_query_params: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_source import DatastoreSource
        from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0
        from ..models.models_event_response_data_type_0 import (
            ModelsEventResponseDataType0,
        )

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        app_id = self.app_id

        created_at = self.created_at

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ModelsEventResponseDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        endpoint_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.endpoint_metadata, Unset):
            endpoint_metadata = []
            for endpoint_metadata_item_data in self.endpoint_metadata:
                endpoint_metadata_item = endpoint_metadata_item_data.to_dict()
                endpoint_metadata.append(endpoint_metadata_item)

        endpoints: list[str] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints

        event_type = self.event_type

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, HttpheaderHTTPHeaderType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        idempotency_key = self.idempotency_key

        is_duplicate_event = self.is_duplicate_event

        metadata = self.metadata

        project_id = self.project_id

        raw = self.raw

        source_id = self.source_id

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

        uid = self.uid

        updated_at = self.updated_at

        url_path = self.url_path

        url_query_params = self.url_query_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if data is not UNSET:
            field_dict["data"] = data
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if endpoint_metadata is not UNSET:
            field_dict["endpoint_metadata"] = endpoint_metadata
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if is_duplicate_event is not UNSET:
            field_dict["is_duplicate_event"] = is_duplicate_event
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if raw is not UNSET:
            field_dict["raw"] = raw
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if source_metadata is not UNSET:
            field_dict["source_metadata"] = source_metadata
        if status is not UNSET:
            field_dict["status"] = status
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url_path is not UNSET:
            field_dict["url_path"] = url_path
        if url_query_params is not UNSET:
            field_dict["url_query_params"] = url_query_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_endpoint import DatastoreEndpoint
        from ..models.datastore_source import DatastoreSource
        from ..models.httpheader_http_header_type_0 import HttpheaderHTTPHeaderType0
        from ..models.models_event_response_data_type_0 import (
            ModelsEventResponseDataType0,
        )

        d = dict(src_dict)

        def _parse_acknowledged_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        app_id = d.pop("app_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        def _parse_data(data: object) -> ModelsEventResponseDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ModelsEventResponseDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsEventResponseDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        _endpoint_metadata = d.pop("endpoint_metadata", UNSET)
        endpoint_metadata: list[DatastoreEndpoint] | Unset = UNSET
        if _endpoint_metadata is not UNSET:
            endpoint_metadata = []
            for endpoint_metadata_item_data in _endpoint_metadata:
                endpoint_metadata_item = DatastoreEndpoint.from_dict(
                    endpoint_metadata_item_data
                )

                endpoint_metadata.append(endpoint_metadata_item)

        endpoints = cast(list[str], d.pop("endpoints", UNSET))

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

        is_duplicate_event = d.pop("is_duplicate_event", UNSET)

        metadata = d.pop("metadata", UNSET)

        project_id = d.pop("project_id", UNSET)

        raw = d.pop("raw", UNSET)

        source_id = d.pop("source_id", UNSET)

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
        status: DatastoreEventStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatastoreEventStatus(_status)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url_path = d.pop("url_path", UNSET)

        url_query_params = d.pop("url_query_params", UNSET)

        models_event_response = cls(
            acknowledged_at=acknowledged_at,
            app_id=app_id,
            created_at=created_at,
            data=data,
            deleted_at=deleted_at,
            endpoint_metadata=endpoint_metadata,
            endpoints=endpoints,
            event_type=event_type,
            headers=headers,
            idempotency_key=idempotency_key,
            is_duplicate_event=is_duplicate_event,
            metadata=metadata,
            project_id=project_id,
            raw=raw,
            source_id=source_id,
            source_metadata=source_metadata,
            status=status,
            uid=uid,
            updated_at=updated_at,
            url_path=url_path,
            url_query_params=url_query_params,
        )

        models_event_response.additional_properties = d
        return models_event_response

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
