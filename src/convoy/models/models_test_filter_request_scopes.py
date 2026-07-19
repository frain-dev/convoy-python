from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m import DatastoreM


T = TypeVar("T", bound="ModelsTestFilterRequestScopes")


@_attrs_define
class ModelsTestFilterRequestScopes:
    """
    Attributes:
        body (Any | Unset):
        header (DatastoreM | Unset):
        headers (DatastoreM | Unset):
        path (DatastoreM | Unset):
        query (DatastoreM | Unset):
    """

    body: Any | Unset = UNSET
    header: DatastoreM | Unset = UNSET
    headers: DatastoreM | Unset = UNSET
    path: DatastoreM | Unset = UNSET
    query: DatastoreM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

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
        from ..models.datastore_m import DatastoreM

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        _header = d.pop("header", UNSET)
        header: DatastoreM | Unset
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = DatastoreM.from_dict(_header)

        _headers = d.pop("headers", UNSET)
        headers: DatastoreM | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = DatastoreM.from_dict(_headers)

        _path = d.pop("path", UNSET)
        path: DatastoreM | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = DatastoreM.from_dict(_path)

        _query = d.pop("query", UNSET)
        query: DatastoreM | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DatastoreM.from_dict(_query)

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
