from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_strategy_provider import DatastoreStrategyProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreStrategyConfiguration")


@_attrs_define
class DatastoreStrategyConfiguration:
    """
    Attributes:
        duration (int | Unset):
        retry_count (int | Unset):
        type_ (DatastoreStrategyProvider | Unset):
    """

    duration: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    type_: DatastoreStrategyProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        retry_count = self.retry_count

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreStrategyProvider | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreStrategyProvider(_type_)

        datastore_strategy_configuration = cls(
            duration=duration,
            retry_count=retry_count,
            type_=type_,
        )

        datastore_strategy_configuration.additional_properties = d
        return datastore_strategy_configuration

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
