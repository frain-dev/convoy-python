from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOptionalTime")


@_attrs_define
class ModelsOptionalTime:
    """
    Attributes:
        set_ (bool | Unset):
        time (str | Unset):
    """

    set_: bool | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_ = self.set_

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if set_ is not UNSET:
            field_dict["set"] = set_
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_ = d.pop("set", UNSET)

        time = d.pop("time", UNSET)

        models_optional_time = cls(
            set_=set_,
            time=time,
        )

        models_optional_time.additional_properties = d
        return models_optional_time

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
