from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_create_event_type_json_schema_type_0 import (
        ModelsCreateEventTypeJsonSchemaType0,
    )


T = TypeVar("T", bound="ModelsCreateEventType")


@_attrs_define
class ModelsCreateEventType:
    """
    Attributes:
        category (str | Unset): Category is a product-specific grouping for the event type
        description (str | Unset): Description is used to describe what the event type does
        json_schema (ModelsCreateEventTypeJsonSchemaType0 | None | Unset): JSONSchema is the JSON structure of the event
            type
        name (str | Unset): Name is the event type name. E.g., invoice.created
    """

    category: str | Unset = UNSET
    description: str | Unset = UNSET
    json_schema: ModelsCreateEventTypeJsonSchemaType0 | None | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.models_create_event_type_json_schema_type_0 import (
            ModelsCreateEventTypeJsonSchemaType0,
        )

        category = self.category

        description = self.description

        json_schema: dict[str, Any] | None | Unset
        if isinstance(self.json_schema, Unset):
            json_schema = UNSET
        elif isinstance(self.json_schema, ModelsCreateEventTypeJsonSchemaType0):
            json_schema = self.json_schema.to_dict()
        else:
            json_schema = self.json_schema

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if json_schema is not UNSET:
            field_dict["json_schema"] = json_schema
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_create_event_type_json_schema_type_0 import (
            ModelsCreateEventTypeJsonSchemaType0,
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        def _parse_json_schema(
            data: object,
        ) -> ModelsCreateEventTypeJsonSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                json_schema_type_0 = ModelsCreateEventTypeJsonSchemaType0.from_dict(
                    data
                )

                return json_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsCreateEventTypeJsonSchemaType0 | None | Unset, data)

        json_schema = _parse_json_schema(d.pop("json_schema", UNSET))

        name = d.pop("name", UNSET)

        models_create_event_type = cls(
            category=category,
            description=description,
            json_schema=json_schema,
            name=name,
        )

        models_create_event_type.additional_properties = d
        return models_create_event_type

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
