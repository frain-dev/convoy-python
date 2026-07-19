from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreCircuitBreakerConfiguration")


@_attrs_define
class DatastoreCircuitBreakerConfiguration:
    """
    Attributes:
        consecutive_failure_threshold (int | Unset):
        error_timeout (int | Unset):
        failure_threshold (int | Unset):
        minimum_request_count (int | Unset):
        observability_window (int | Unset):
        sample_rate (int | Unset):
        success_threshold (int | Unset):
    """

    consecutive_failure_threshold: int | Unset = UNSET
    error_timeout: int | Unset = UNSET
    failure_threshold: int | Unset = UNSET
    minimum_request_count: int | Unset = UNSET
    observability_window: int | Unset = UNSET
    sample_rate: int | Unset = UNSET
    success_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consecutive_failure_threshold = self.consecutive_failure_threshold

        error_timeout = self.error_timeout

        failure_threshold = self.failure_threshold

        minimum_request_count = self.minimum_request_count

        observability_window = self.observability_window

        sample_rate = self.sample_rate

        success_threshold = self.success_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consecutive_failure_threshold is not UNSET:
            field_dict["consecutive_failure_threshold"] = consecutive_failure_threshold
        if error_timeout is not UNSET:
            field_dict["error_timeout"] = error_timeout
        if failure_threshold is not UNSET:
            field_dict["failure_threshold"] = failure_threshold
        if minimum_request_count is not UNSET:
            field_dict["minimum_request_count"] = minimum_request_count
        if observability_window is not UNSET:
            field_dict["observability_window"] = observability_window
        if sample_rate is not UNSET:
            field_dict["sample_rate"] = sample_rate
        if success_threshold is not UNSET:
            field_dict["success_threshold"] = success_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consecutive_failure_threshold = d.pop("consecutive_failure_threshold", UNSET)

        error_timeout = d.pop("error_timeout", UNSET)

        failure_threshold = d.pop("failure_threshold", UNSET)

        minimum_request_count = d.pop("minimum_request_count", UNSET)

        observability_window = d.pop("observability_window", UNSET)

        sample_rate = d.pop("sample_rate", UNSET)

        success_threshold = d.pop("success_threshold", UNSET)

        datastore_circuit_breaker_configuration = cls(
            consecutive_failure_threshold=consecutive_failure_threshold,
            error_timeout=error_timeout,
            failure_threshold=failure_threshold,
            minimum_request_count=minimum_request_count,
            observability_window=observability_window,
            sample_rate=sample_rate,
            success_threshold=success_threshold,
        )

        datastore_circuit_breaker_configuration.additional_properties = d
        return datastore_circuit_breaker_configuration

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
