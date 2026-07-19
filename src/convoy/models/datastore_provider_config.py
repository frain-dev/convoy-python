from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_twitter_provider_config import (
        DatastoreTwitterProviderConfig,
    )


T = TypeVar("T", bound="DatastoreProviderConfig")


@_attrs_define
class DatastoreProviderConfig:
    """
    Attributes:
        twitter (DatastoreTwitterProviderConfig | Unset):
    """

    twitter: DatastoreTwitterProviderConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        twitter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.twitter, Unset):
            twitter = self.twitter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if twitter is not UNSET:
            field_dict["twitter"] = twitter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_twitter_provider_config import (
            DatastoreTwitterProviderConfig,
        )

        d = dict(src_dict)
        _twitter = d.pop("twitter", UNSET)
        twitter: DatastoreTwitterProviderConfig | Unset
        if isinstance(_twitter, Unset):
            twitter = UNSET
        else:
            twitter = DatastoreTwitterProviderConfig.from_dict(_twitter)

        datastore_provider_config = cls(
            twitter=twitter,
        )

        datastore_provider_config.additional_properties = d
        return datastore_provider_config

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
