from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_count_response import ModelsCountResponse


T = TypeVar("T", bound="CountAffectedEventsResponse200")


@_attrs_define
class CountAffectedEventsResponse200:
    """
    Attributes:
        message (str | Unset):
        status (bool | Unset):
        data (ModelsCountResponse | Unset):
    """

    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    data: ModelsCountResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_count_response import ModelsCountResponse

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: ModelsCountResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelsCountResponse.from_dict(_data)

        count_affected_events_response_200 = cls(
            message=message,
            status=status,
            data=data,
        )

        count_affected_events_response_200.additional_properties = d
        return count_affected_events_response_200

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
