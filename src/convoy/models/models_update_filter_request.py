from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m_type_0 import DatastoreMType0
    from ..models.models_optional_time import ModelsOptionalTime


T = TypeVar("T", bound="ModelsUpdateFilterRequest")


@_attrs_define
class ModelsUpdateFilterRequest:
    """
    Attributes:
        body (DatastoreMType0 | None | Unset):
        enabled_at (ModelsOptionalTime | Unset):
        event_type (str | Unset): Type of event this filter applies to (optional)
        headers (DatastoreMType0 | None | Unset):
        is_flattened (bool | Unset): Whether the filter uses flattened JSON paths (optional)
        path (DatastoreMType0 | None | Unset):
        query (DatastoreMType0 | None | Unset):
    """

    body: DatastoreMType0 | None | Unset = UNSET
    enabled_at: ModelsOptionalTime | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: DatastoreMType0 | None | Unset = UNSET
    is_flattened: bool | Unset = UNSET
    path: DatastoreMType0 | None | Unset = UNSET
    query: DatastoreMType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_m_type_0 import DatastoreMType0

        body: dict[str, Any] | None | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        elif isinstance(self.body, DatastoreMType0):
            body = self.body.to_dict()
        else:
            body = self.body

        enabled_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enabled_at, Unset):
            enabled_at = self.enabled_at.to_dict()

        event_type = self.event_type

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, DatastoreMType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        is_flattened = self.is_flattened

        path: dict[str, Any] | None | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        elif isinstance(self.path, DatastoreMType0):
            path = self.path.to_dict()
        else:
            path = self.path

        query: dict[str, Any] | None | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, DatastoreMType0):
            query = self.query.to_dict()
        else:
            query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if enabled_at is not UNSET:
            field_dict["enabled_at"] = enabled_at
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if is_flattened is not UNSET:
            field_dict["is_flattened"] = is_flattened
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_m_type_0 import DatastoreMType0
        from ..models.models_optional_time import ModelsOptionalTime

        d = dict(src_dict)

        def _parse_body(data: object) -> DatastoreMType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_m_type_0 = DatastoreMType0.from_dict(data)

                return componentsschemasdatastore_m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMType0 | None | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        _enabled_at = d.pop("enabled_at", UNSET)
        enabled_at: ModelsOptionalTime | Unset
        if isinstance(_enabled_at, Unset):
            enabled_at = UNSET
        else:
            enabled_at = ModelsOptionalTime.from_dict(_enabled_at)

        event_type = d.pop("event_type", UNSET)

        def _parse_headers(data: object) -> DatastoreMType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_m_type_0 = DatastoreMType0.from_dict(data)

                return componentsschemasdatastore_m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMType0 | None | Unset, data)

        headers = _parse_headers(d.pop("headers", UNSET))

        is_flattened = d.pop("is_flattened", UNSET)

        def _parse_path(data: object) -> DatastoreMType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_m_type_0 = DatastoreMType0.from_dict(data)

                return componentsschemasdatastore_m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMType0 | None | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_query(data: object) -> DatastoreMType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_m_type_0 = DatastoreMType0.from_dict(data)

                return componentsschemasdatastore_m_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMType0 | None | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        models_update_filter_request = cls(
            body=body,
            enabled_at=enabled_at,
            event_type=event_type,
            headers=headers,
            is_flattened=is_flattened,
            path=path,
            query=query,
        )

        models_update_filter_request.additional_properties = d
        return models_update_filter_request

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
