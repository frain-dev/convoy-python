from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.handlers_stub_type_0 import HandlersStubType0


T = TypeVar("T", bound="ResendEventDeliveryResponse401")


@_attrs_define
class ResendEventDeliveryResponse401:
    """
    Attributes:
        message (str | Unset):
        status (bool | Unset):
        data (HandlersStubType0 | None | Unset):
    """

    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    data: HandlersStubType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.handlers_stub_type_0 import HandlersStubType0

        message = self.message

        status = self.status

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, HandlersStubType0):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.handlers_stub_type_0 import HandlersStubType0

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        def _parse_data(data: object) -> HandlersStubType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemashandlers_stub_type_0 = HandlersStubType0.from_dict(
                    data
                )

                return componentsschemashandlers_stub_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HandlersStubType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        resend_event_delivery_response_401 = cls(
            message=message,
            status=status,
            data=data,
        )

        resend_event_delivery_response_401.additional_properties = d
        return resend_event_delivery_response_401

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
