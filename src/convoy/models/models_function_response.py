from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsFunctionResponse")


@_attrs_define
class ModelsFunctionResponse:
    """
    Attributes:
        log (list[str] | Unset):
        payload (Any | Unset):
    """

    log: list[str] | Unset = UNSET
    payload: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        log: list[str] | Unset = UNSET
        if not isinstance(self.log, Unset):
            log = self.log

        payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log is not UNSET:
            field_dict["log"] = log
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        log = cast(list[str], d.pop("log", UNSET))

        payload = d.pop("payload", UNSET)

        models_function_response = cls(
            log=log,
            payload=payload,
        )

        models_function_response.additional_properties = d
        return models_function_response

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
