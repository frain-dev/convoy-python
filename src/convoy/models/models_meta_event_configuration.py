from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMetaEventConfiguration")


@_attrs_define
class ModelsMetaEventConfiguration:
    """
    Attributes:
        event_type (list[str] | Unset):
        is_enabled (bool | Unset):
        secret (str | Unset):
        type_ (str | Unset):
        url (str | Unset):
    """

    event_type: list[str] | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    secret: str | Unset = UNSET
    type_: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type: list[str] | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type

        is_enabled = self.is_enabled

        secret = self.secret

        type_ = self.type_

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if secret is not UNSET:
            field_dict["secret"] = secret
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = cast(list[str], d.pop("event_type", UNSET))

        is_enabled = d.pop("is_enabled", UNSET)

        secret = d.pop("secret", UNSET)

        type_ = d.pop("type", UNSET)

        url = d.pop("url", UNSET)

        models_meta_event_configuration = cls(
            event_type=event_type,
            is_enabled=is_enabled,
            secret=secret,
            type_=type_,
            url=url,
        )

        models_meta_event_configuration.additional_properties = d
        return models_meta_event_configuration

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
