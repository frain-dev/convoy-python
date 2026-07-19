from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_meta_event_response import ModelsMetaEventResponse


T = TypeVar("T", bound="ResendMetaEventResponse200")


@_attrs_define
class ResendMetaEventResponse200:
    """
    Attributes:
        message (str | Unset):
        status (bool | Unset):
        data (ModelsMetaEventResponse | Unset):
    """

    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    data: ModelsMetaEventResponse | Unset = UNSET
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
        from ..models.models_meta_event_response import ModelsMetaEventResponse

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: ModelsMetaEventResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelsMetaEventResponse.from_dict(_data)

        resend_meta_event_response_200 = cls(
            message=message,
            status=status,
            data=data,
        )

        resend_meta_event_response_200.additional_properties = d
        return resend_meta_event_response_200

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
