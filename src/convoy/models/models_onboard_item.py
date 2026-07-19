from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOnboardItem")


@_attrs_define
class ModelsOnboardItem:
    """
    Attributes:
        auth_password (str | Unset):
        auth_username (str | Unset):
        event_type (str | Unset):
        name (str | Unset):
        url (str | Unset):
    """

    auth_password: str | Unset = UNSET
    auth_username: str | Unset = UNSET
    event_type: str | Unset = UNSET
    name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_password = self.auth_password

        auth_username = self.auth_username

        event_type = self.event_type

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_password is not UNSET:
            field_dict["auth_password"] = auth_password
        if auth_username is not UNSET:
            field_dict["auth_username"] = auth_username
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_password = d.pop("auth_password", UNSET)

        auth_username = d.pop("auth_username", UNSET)

        event_type = d.pop("event_type", UNSET)

        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        models_onboard_item = cls(
            auth_password=auth_password,
            auth_username=auth_username,
            event_type=event_type,
            name=name,
            url=url,
        )

        models_onboard_item.additional_properties = d
        return models_onboard_item

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
