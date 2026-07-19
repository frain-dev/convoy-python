from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsCustomResponse")


@_attrs_define
class ModelsCustomResponse:
    """
    Attributes:
        body (str | Unset):
        content_type (str | Unset):
    """

    body: str | Unset = UNSET
    content_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        content_type = d.pop("content_type", UNSET)

        models_custom_response = cls(
            body=body,
            content_type=content_type,
        )

        models_custom_response.additional_properties = d
        return models_custom_response

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
