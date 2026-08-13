from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsEndpointPeriodFailureRate")


@_attrs_define
class ModelsEndpointPeriodFailureRate:
    """
    Attributes:
        failure_count (int | Unset):
        period_failure_rate (float | Unset):
        retry_count (int | Unset):
        success_count (int | Unset):
        uid (str | Unset):
    """

    failure_count: int | Unset = UNSET
    period_failure_rate: float | Unset = UNSET
    retry_count: int | Unset = UNSET
    success_count: int | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failure_count = self.failure_count

        period_failure_rate = self.period_failure_rate

        retry_count = self.retry_count

        success_count = self.success_count

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if period_failure_rate is not UNSET:
            field_dict["period_failure_rate"] = period_failure_rate
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if success_count is not UNSET:
            field_dict["success_count"] = success_count
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failure_count = d.pop("failure_count", UNSET)

        period_failure_rate = d.pop("period_failure_rate", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        success_count = d.pop("success_count", UNSET)

        uid = d.pop("uid", UNSET)

        models_endpoint_period_failure_rate = cls(
            failure_count=failure_count,
            period_failure_rate=period_failure_rate,
            retry_count=retry_count,
            success_count=success_count,
            uid=uid,
        )

        models_endpoint_period_failure_rate.additional_properties = d
        return models_endpoint_period_failure_rate

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
