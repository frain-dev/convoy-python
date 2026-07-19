from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreProjectStatistics")


@_attrs_define
class DatastoreProjectStatistics:
    """
    Attributes:
        endpoints_exist (bool | Unset):
        events_exist (bool | Unset):
        sources_exist (bool | Unset):
        subscriptions_exist (bool | Unset):
    """

    endpoints_exist: bool | Unset = UNSET
    events_exist: bool | Unset = UNSET
    sources_exist: bool | Unset = UNSET
    subscriptions_exist: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        endpoints_exist = self.endpoints_exist

        events_exist = self.events_exist

        sources_exist = self.sources_exist

        subscriptions_exist = self.subscriptions_exist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoints_exist is not UNSET:
            field_dict["endpoints_exist"] = endpoints_exist
        if events_exist is not UNSET:
            field_dict["events_exist"] = events_exist
        if sources_exist is not UNSET:
            field_dict["sources_exist"] = sources_exist
        if subscriptions_exist is not UNSET:
            field_dict["subscriptions_exist"] = subscriptions_exist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoints_exist = d.pop("endpoints_exist", UNSET)

        events_exist = d.pop("events_exist", UNSET)

        sources_exist = d.pop("sources_exist", UNSET)

        subscriptions_exist = d.pop("subscriptions_exist", UNSET)

        datastore_project_statistics = cls(
            endpoints_exist=endpoints_exist,
            events_exist=events_exist,
            sources_exist=sources_exist,
            subscriptions_exist=subscriptions_exist,
        )

        datastore_project_statistics.additional_properties = d
        return datastore_project_statistics

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
