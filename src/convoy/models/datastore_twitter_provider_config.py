from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreTwitterProviderConfig")


@_attrs_define
class DatastoreTwitterProviderConfig:
    """
    Attributes:
        crc_verified_at (str | Unset):
    """

    crc_verified_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        crc_verified_at = self.crc_verified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crc_verified_at is not UNSET:
            field_dict["crc_verified_at"] = crc_verified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        crc_verified_at = d.pop("crc_verified_at", UNSET)

        datastore_twitter_provider_config = cls(
            crc_verified_at=crc_verified_at,
        )

        datastore_twitter_provider_config.additional_properties = d
        return datastore_twitter_provider_config

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
