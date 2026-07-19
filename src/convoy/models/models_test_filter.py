from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_filter_schema import ModelsFilterSchema


T = TypeVar("T", bound="ModelsTestFilter")


@_attrs_define
class ModelsTestFilter:
    """
    Attributes:
        request (ModelsFilterSchema | Unset):
        schema (ModelsFilterSchema | Unset):
    """

    request: ModelsFilterSchema | Unset = UNSET
    schema: ModelsFilterSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_filter_schema import ModelsFilterSchema

        d = dict(src_dict)
        _request = d.pop("request", UNSET)
        request: ModelsFilterSchema | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = ModelsFilterSchema.from_dict(_request)

        _schema = d.pop("schema", UNSET)
        schema: ModelsFilterSchema | Unset
        if isinstance(_schema, Unset):
            schema = UNSET
        else:
            schema = ModelsFilterSchema.from_dict(_schema)

        models_test_filter = cls(
            request=request,
            schema=schema,
        )

        models_test_filter.additional_properties = d
        return models_test_filter

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
