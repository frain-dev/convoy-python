from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_strategy_provider import DatastoreStrategyProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsRetryConfiguration")


@_attrs_define
class ModelsRetryConfiguration:
    """
    Attributes:
        duration (str | Unset): Used to specify a valid Go time duration e.g 10s, 1h3m for how long to wait between
            event delivery retries
        interval_seconds (int | Unset): Used to specify a time in seconds for how long to wait between event delivery
            retries,
        retry_count (int | Unset): Used to specify the max number of retries
        type_ (DatastoreStrategyProvider | Unset):
    """

    duration: str | Unset = UNSET
    interval_seconds: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    type_: DatastoreStrategyProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        interval_seconds = self.interval_seconds

        retry_count = self.retry_count

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration is not UNSET:
            field_dict["duration"] = duration
        if interval_seconds is not UNSET:
            field_dict["interval_seconds"] = interval_seconds
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        interval_seconds = d.pop("interval_seconds", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreStrategyProvider | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreStrategyProvider(_type_)

        models_retry_configuration = cls(
            duration=duration,
            interval_seconds=interval_seconds,
            retry_count=retry_count,
            type_=type_,
        )

        models_retry_configuration.additional_properties = d
        return models_retry_configuration

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
