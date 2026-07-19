from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsFilterSchema")


@_attrs_define
class ModelsFilterSchema:
    """
    Attributes:
        body (Any | Unset):
        header (Any | Unset):
        path (Any | Unset):
        query (Any | Unset):
    """

    body: Any | Unset = UNSET
    header: Any | Unset = UNSET
    path: Any | Unset = UNSET
    query: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        header = self.header

        path = self.path

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if header is not UNSET:
            field_dict["header"] = header
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        header = d.pop("header", UNSET)

        path = d.pop("path", UNSET)

        query = d.pop("query", UNSET)

        models_filter_schema = cls(
            body=body,
            header=header,
            path=path,
            query=query,
        )

        models_filter_schema.additional_properties = d
        return models_filter_schema

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
