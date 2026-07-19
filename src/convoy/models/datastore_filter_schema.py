from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m import DatastoreM


T = TypeVar("T", bound="DatastoreFilterSchema")


@_attrs_define
class DatastoreFilterSchema:
    """
    Attributes:
        body (DatastoreM | Unset):
        headers (DatastoreM | Unset):
        is_flattened (bool | Unset):
        path (DatastoreM | Unset):
        query (DatastoreM | Unset):
    """

    body: DatastoreM | Unset = UNSET
    headers: DatastoreM | Unset = UNSET
    is_flattened: bool | Unset = UNSET
    path: DatastoreM | Unset = UNSET
    query: DatastoreM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        is_flattened = self.is_flattened

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
        from ..models.datastore_m import DatastoreM

        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: DatastoreM | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = DatastoreM.from_dict(_body)

        _headers = d.pop("headers", UNSET)
        headers: DatastoreM | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = DatastoreM.from_dict(_headers)

        is_flattened = d.pop("is_flattened", UNSET)

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

        datastore_filter_schema = cls(
            body=body,
            headers=headers,
            is_flattened=is_flattened,
            path=path,
            query=query,
        )

        datastore_filter_schema.additional_properties = d
        return datastore_filter_schema

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
