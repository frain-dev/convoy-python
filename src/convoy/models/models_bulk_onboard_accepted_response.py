from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsBulkOnboardAcceptedResponse")


@_attrs_define
class ModelsBulkOnboardAcceptedResponse:
    """
    Attributes:
        batch_count (int | Unset):
        message (str | Unset):
        total_items (int | Unset):
    """

    batch_count: int | Unset = UNSET
    message: str | Unset = UNSET
    total_items: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_count = self.batch_count

        message = self.message

        total_items = self.total_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_count is not UNSET:
            field_dict["batch_count"] = batch_count
        if message is not UNSET:
            field_dict["message"] = message
        if total_items is not UNSET:
            field_dict["total_items"] = total_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        batch_count = d.pop("batch_count", UNSET)

        message = d.pop("message", UNSET)

        total_items = d.pop("total_items", UNSET)

        models_bulk_onboard_accepted_response = cls(
            batch_count=batch_count,
            message=message,
            total_items=total_items,
        )

        models_bulk_onboard_accepted_response.additional_properties = d
        return models_bulk_onboard_accepted_response

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
