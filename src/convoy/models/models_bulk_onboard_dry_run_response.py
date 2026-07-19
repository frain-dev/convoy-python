from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_onboard_validation_error import ModelsOnboardValidationError


T = TypeVar("T", bound="ModelsBulkOnboardDryRunResponse")


@_attrs_define
class ModelsBulkOnboardDryRunResponse:
    """
    Attributes:
        errors (list[ModelsOnboardValidationError] | Unset):
        total_rows (int | Unset):
        valid_count (int | Unset):
    """

    errors: list[ModelsOnboardValidationError] | Unset = UNSET
    total_rows: int | Unset = UNSET
    valid_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        total_rows = self.total_rows

        valid_count = self.valid_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if total_rows is not UNSET:
            field_dict["total_rows"] = total_rows
        if valid_count is not UNSET:
            field_dict["valid_count"] = valid_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_onboard_validation_error import (
            ModelsOnboardValidationError,
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[ModelsOnboardValidationError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ModelsOnboardValidationError.from_dict(errors_item_data)

                errors.append(errors_item)

        total_rows = d.pop("total_rows", UNSET)

        valid_count = d.pop("valid_count", UNSET)

        models_bulk_onboard_dry_run_response = cls(
            errors=errors,
            total_rows=total_rows,
            valid_count=valid_count,
        )

        models_bulk_onboard_dry_run_response.additional_properties = d
        return models_bulk_onboard_dry_run_response

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
