from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_function_request_payload_type_0 import (
        ModelsFunctionRequestPayloadType0,
    )


T = TypeVar("T", bound="ModelsFunctionRequest")


@_attrs_define
class ModelsFunctionRequest:
    """
    Attributes:
        function (str | Unset):
        payload (ModelsFunctionRequestPayloadType0 | None | Unset):
        type_ (str | Unset):
    """

    function: str | Unset = UNSET
    payload: ModelsFunctionRequestPayloadType0 | None | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.models_function_request_payload_type_0 import (
            ModelsFunctionRequestPayloadType0,
        )

        function = self.function

        payload: dict[str, Any] | None | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, ModelsFunctionRequestPayloadType0):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

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
        from ..models.models_function_request_payload_type_0 import (
            ModelsFunctionRequestPayloadType0,
        )

        d = dict(src_dict)
        function = d.pop("function", UNSET)

        def _parse_payload(
            data: object,
        ) -> ModelsFunctionRequestPayloadType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = ModelsFunctionRequestPayloadType0.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsFunctionRequestPayloadType0 | None | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

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
