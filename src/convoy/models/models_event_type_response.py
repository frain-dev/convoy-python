from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_event_type_response_json_schema import (
        ModelsEventTypeResponseJsonSchema,
    )


T = TypeVar("T", bound="ModelsEventTypeResponse")


@_attrs_define
class ModelsEventTypeResponse:
    """
    Attributes:
        category (str | Unset):
        deprecated_at (str | Unset):
        description (str | Unset):
        json_schema (ModelsEventTypeResponseJsonSchema | Unset):
        name (str | Unset):
        uid (str | Unset):
    """

    category: str | Unset = UNSET
    deprecated_at: str | Unset = UNSET
    description: str | Unset = UNSET
    json_schema: ModelsEventTypeResponseJsonSchema | Unset = UNSET
    name: str | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        deprecated_at = self.deprecated_at

        description = self.description

        json_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_schema, Unset):
            json_schema = self.json_schema.to_dict()

        name = self.name

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if deprecated_at is not UNSET:
            field_dict["deprecated_at"] = deprecated_at
        if description is not UNSET:
            field_dict["description"] = description
        if json_schema is not UNSET:
            field_dict["json_schema"] = json_schema
        if name is not UNSET:
            field_dict["name"] = name
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_event_type_response_json_schema import (
            ModelsEventTypeResponseJsonSchema,
        )

        d = dict(src_dict)
        category = d.pop("category", UNSET)

        deprecated_at = d.pop("deprecated_at", UNSET)

        description = d.pop("description", UNSET)

        _json_schema = d.pop("json_schema", UNSET)
        json_schema: ModelsEventTypeResponseJsonSchema | Unset
        if isinstance(_json_schema, Unset):
            json_schema = UNSET
        else:
            json_schema = ModelsEventTypeResponseJsonSchema.from_dict(_json_schema)

        name = d.pop("name", UNSET)

        uid = d.pop("uid", UNSET)

        models_event_type_response = cls(
            category=category,
            deprecated_at=deprecated_at,
            description=description,
            json_schema=json_schema,
            name=name,
            uid=uid,
        )

        models_event_type_response.additional_properties = d
        return models_event_type_response

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
