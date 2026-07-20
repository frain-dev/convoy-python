from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m_type_0 import DatastoreMType0


T = TypeVar("T", bound="ModelsTestFilterRequestScopes")


@_attrs_define
class ModelsTestFilterRequestScopes:
    """
    Attributes:
        body (Any | Unset):
        header (DatastoreMType0 | None | Unset):
        headers (DatastoreMType0 | None | Unset):
        path (DatastoreMType0 | None | Unset):
        query (DatastoreMType0 | None | Unset):
    """

    body: Any | Unset = UNSET
    header: DatastoreMType0 | None | Unset = UNSET
    headers: DatastoreMType0 | None | Unset = UNSET
    path: DatastoreMType0 | None | Unset = UNSET
    query: DatastoreMType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_m_type_0 import DatastoreMType0

        body = self.body

        header: dict[str, Any] | None | Unset
        if isinstance(self.header, Unset):
            header = UNSET
        elif isinstance(self.header, DatastoreMType0):
            header = self.header.to_dict()
        else:
            header = self.header

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if header is not UNSET:
            field_dict["header"] = header
        if headers is not UNSET:
            field_dict["headers"] = headers
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_m_type_0 import DatastoreMType0

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        def _parse_header(data: object) -> DatastoreMType0 | None | Unset:
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

        header = _parse_header(d.pop("header", UNSET))

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

        models_test_filter_request_scopes = cls(
            body=body,
            header=header,
            headers=headers,
            path=path,
            query=query,
        )

        models_test_filter_request_scopes.additional_properties = d
        return models_test_filter_request_scopes

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
