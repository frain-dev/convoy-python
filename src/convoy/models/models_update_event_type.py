from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_update_event_type_json_schema import (
        ModelsUpdateEventTypeJsonSchema,
    )


T = TypeVar("T", bound="ModelsUpdateEventType")


@_attrs_define
class ModelsUpdateEventType:
    """
    Attributes:
        category (str | Unset): Category is a product-specific grouping for the event type
        description (str | Unset): Description is used to describe what the event type does
        json_schema (ModelsUpdateEventTypeJsonSchema | Unset): JSONSchema is the JSON structure of the event type
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    json_schema: ModelsUpdateEventTypeJsonSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        json_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_schema, Unset):
            json_schema = self.json_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if json_schema is not UNSET:
            field_dict["json_schema"] = json_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_update_event_type_json_schema import (
            ModelsUpdateEventTypeJsonSchema,
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        _json_schema = d.pop("json_schema", UNSET)
        json_schema: ModelsUpdateEventTypeJsonSchema | Unset
        if isinstance(_json_schema, Unset):
            json_schema = UNSET
        else:
            json_schema = ModelsUpdateEventTypeJsonSchema.from_dict(_json_schema)

        models_update_event_type = cls(
            category=category,
            description=description,
            json_schema=json_schema,
        )

        models_update_event_type.additional_properties = d
        return models_update_event_type

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
