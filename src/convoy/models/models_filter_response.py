from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m_type_0 import DatastoreMType0


T = TypeVar("T", bound="ModelsFilterResponse")


@_attrs_define
class ModelsFilterResponse:
    """
    Attributes:
        body (DatastoreMType0 | None | Unset):
        enabled_at (None | str | Unset):
        event_type (str | Unset):
        headers (DatastoreMType0 | None | Unset):
        path (DatastoreMType0 | None | Unset):
        query (DatastoreMType0 | None | Unset):
        raw_body (DatastoreMType0 | None | Unset):
        raw_headers (DatastoreMType0 | None | Unset):
        raw_path (DatastoreMType0 | None | Unset):
        raw_query (DatastoreMType0 | None | Unset):
        subscription_id (str | Unset):
        uid (str | Unset):
    """

    body: DatastoreMType0 | None | Unset = UNSET
    enabled_at: None | str | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: DatastoreMType0 | None | Unset = UNSET
    path: DatastoreMType0 | None | Unset = UNSET
    query: DatastoreMType0 | None | Unset = UNSET
    raw_body: DatastoreMType0 | None | Unset = UNSET
    raw_headers: DatastoreMType0 | None | Unset = UNSET
    raw_path: DatastoreMType0 | None | Unset = UNSET
    raw_query: DatastoreMType0 | None | Unset = UNSET
    subscription_id: str | Unset = UNSET
    uid: str | Unset = UNSET
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

        enabled_at: None | str | Unset
        if isinstance(self.enabled_at, Unset):
            enabled_at = UNSET
        else:
            enabled_at = self.enabled_at

        event_type = self.event_type

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, DatastoreMType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

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

        raw_body: dict[str, Any] | None | Unset
        if isinstance(self.raw_body, Unset):
            raw_body = UNSET
        elif isinstance(self.raw_body, DatastoreMType0):
            raw_body = self.raw_body.to_dict()
        else:
            raw_body = self.raw_body

        raw_headers: dict[str, Any] | None | Unset
        if isinstance(self.raw_headers, Unset):
            raw_headers = UNSET
        elif isinstance(self.raw_headers, DatastoreMType0):
            raw_headers = self.raw_headers.to_dict()
        else:
            raw_headers = self.raw_headers

        raw_path: dict[str, Any] | None | Unset
        if isinstance(self.raw_path, Unset):
            raw_path = UNSET
        elif isinstance(self.raw_path, DatastoreMType0):
            raw_path = self.raw_path.to_dict()
        else:
            raw_path = self.raw_path

        raw_query: dict[str, Any] | None | Unset
        if isinstance(self.raw_query, Unset):
            raw_query = UNSET
        elif isinstance(self.raw_query, DatastoreMType0):
            raw_query = self.raw_query.to_dict()
        else:
            raw_query = self.raw_query

        subscription_id = self.subscription_id

        uid = self.uid

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
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query
        if raw_body is not UNSET:
            field_dict["raw_body"] = raw_body
        if raw_headers is not UNSET:
            field_dict["raw_headers"] = raw_headers
        if raw_path is not UNSET:
            field_dict["raw_path"] = raw_path
        if raw_query is not UNSET:
            field_dict["raw_query"] = raw_query
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_m_type_0 import DatastoreMType0

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

        def _parse_enabled_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enabled_at = _parse_enabled_at(d.pop("enabled_at", UNSET))

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

        def _parse_raw_body(data: object) -> DatastoreMType0 | None | Unset:
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

        raw_body = _parse_raw_body(d.pop("raw_body", UNSET))

        def _parse_raw_headers(data: object) -> DatastoreMType0 | None | Unset:
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

        raw_headers = _parse_raw_headers(d.pop("raw_headers", UNSET))

        def _parse_raw_path(data: object) -> DatastoreMType0 | None | Unset:
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

        raw_path = _parse_raw_path(d.pop("raw_path", UNSET))

        def _parse_raw_query(data: object) -> DatastoreMType0 | None | Unset:
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

        raw_query = _parse_raw_query(d.pop("raw_query", UNSET))

        subscription_id = d.pop("subscription_id", UNSET)

        uid = d.pop("uid", UNSET)

        models_filter_response = cls(
            body=body,
            enabled_at=enabled_at,
            event_type=event_type,
            headers=headers,
            path=path,
            query=query,
            raw_body=raw_body,
            raw_headers=raw_headers,
            raw_path=raw_path,
            raw_query=raw_query,
            subscription_id=subscription_id,
            uid=uid,
        )

        models_filter_response.additional_properties = d
        return models_filter_response

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
