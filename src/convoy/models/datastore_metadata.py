from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_strategy_provider import DatastoreStrategyProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_metadata_data_type_0 import DatastoreMetadataDataType0


T = TypeVar("T", bound="DatastoreMetadata")


@_attrs_define
class DatastoreMetadata:
    """
    Attributes:
        data (DatastoreMetadataDataType0 | None | Unset): Data to be sent to endpoint.
        interval_seconds (int | Unset):
        max_retry_seconds (int | Unset):
        next_send_time (str | Unset):
        num_trials (int | Unset): NumTrials: number of times we have tried to deliver this Event to
            an application
        raw (str | Unset):
        retry_limit (int | Unset):
        strategy (DatastoreStrategyProvider | Unset):
    """

    data: DatastoreMetadataDataType0 | None | Unset = UNSET
    interval_seconds: int | Unset = UNSET
    max_retry_seconds: int | Unset = UNSET
    next_send_time: str | Unset = UNSET
    num_trials: int | Unset = UNSET
    raw: str | Unset = UNSET
    retry_limit: int | Unset = UNSET
    strategy: DatastoreStrategyProvider | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_metadata_data_type_0 import DatastoreMetadataDataType0

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, DatastoreMetadataDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        interval_seconds = self.interval_seconds

        max_retry_seconds = self.max_retry_seconds

        next_send_time = self.next_send_time

        num_trials = self.num_trials

        raw = self.raw

        retry_limit = self.retry_limit

        strategy: str | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if interval_seconds is not UNSET:
            field_dict["interval_seconds"] = interval_seconds
        if max_retry_seconds is not UNSET:
            field_dict["max_retry_seconds"] = max_retry_seconds
        if next_send_time is not UNSET:
            field_dict["next_send_time"] = next_send_time
        if num_trials is not UNSET:
            field_dict["num_trials"] = num_trials
        if raw is not UNSET:
            field_dict["raw"] = raw
        if retry_limit is not UNSET:
            field_dict["retry_limit"] = retry_limit
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_metadata_data_type_0 import DatastoreMetadataDataType0

        d = dict(src_dict)

        def _parse_data(data: object) -> DatastoreMetadataDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = DatastoreMetadataDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMetadataDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        interval_seconds = d.pop("interval_seconds", UNSET)

        max_retry_seconds = d.pop("max_retry_seconds", UNSET)

        next_send_time = d.pop("next_send_time", UNSET)

        num_trials = d.pop("num_trials", UNSET)

        raw = d.pop("raw", UNSET)

        retry_limit = d.pop("retry_limit", UNSET)

        _strategy = d.pop("strategy", UNSET)
        strategy: DatastoreStrategyProvider | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = DatastoreStrategyProvider(_strategy)

        datastore_metadata = cls(
            data=data,
            interval_seconds=interval_seconds,
            max_retry_seconds=max_retry_seconds,
            next_send_time=next_send_time,
            num_trials=num_trials,
            raw=raw,
            retry_limit=retry_limit,
            strategy=strategy,
        )

        datastore_metadata.additional_properties = d
        return datastore_metadata

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
