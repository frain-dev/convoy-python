from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOnboardValidationError")


@_attrs_define
class ModelsOnboardValidationError:
    """
    Attributes:
        field (str | Unset):
        message (str | Unset):
        row (int | Unset):
    """

    field: str | Unset = UNSET
    message: str | Unset = UNSET
    row: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        message = self.message

        row = self.row

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        message = d.pop("message", UNSET)

        row = d.pop("row", UNSET)

        models_onboard_validation_error = cls(
            field=field,
            message=message,
            row=row,
        )

        models_onboard_validation_error.additional_properties = d
        return models_onboard_validation_error

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
