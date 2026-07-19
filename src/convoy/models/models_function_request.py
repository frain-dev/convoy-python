from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_function_request_payload import ModelsFunctionRequestPayload


T = TypeVar("T", bound="ModelsFunctionRequest")


@_attrs_define
class ModelsFunctionRequest:
    """
    Attributes:
        function (str | Unset):
        payload (ModelsFunctionRequestPayload | Unset):
        type_ (str | Unset):
    """

    function: str | Unset = UNSET
    payload: ModelsFunctionRequestPayload | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function is not UNSET:
            field_dict["function"] = function
        if payload is not UNSET:
            field_dict["payload"] = payload
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_function_request_payload import (
            ModelsFunctionRequestPayload,
        )

        d = dict(src_dict)
        function = d.pop("function", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: ModelsFunctionRequestPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ModelsFunctionRequestPayload.from_dict(_payload)

        type_ = d.pop("type", UNSET)

        models_function_request = cls(
            function=function,
            payload=payload,
            type_=type_,
        )

        models_function_request.additional_properties = d
        return models_function_request

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
