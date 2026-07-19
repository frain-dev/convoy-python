from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_test_filter_request_scopes import ModelsTestFilterRequestScopes


T = TypeVar("T", bound="ModelsTestFilterRequest")


@_attrs_define
class ModelsTestFilterRequest:
    """
    Attributes:
        payload (Any | Unset): Sample payload to test against body filter rules. Optional when request scopes are
            supplied.
        request (ModelsTestFilterRequestScopes | Unset):
    """

    payload: Any | Unset = UNSET
    request: ModelsTestFilterRequestScopes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payload = self.payload

        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payload is not UNSET:
            field_dict["payload"] = payload
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_test_filter_request_scopes import (
            ModelsTestFilterRequestScopes,
        )

        d = dict(src_dict)
        payload = d.pop("payload", UNSET)

        _request = d.pop("request", UNSET)
        request: ModelsTestFilterRequestScopes | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = ModelsTestFilterRequestScopes.from_dict(_request)

        models_test_filter_request = cls(
            payload=payload,
            request=request,
        )

        models_test_filter_request.additional_properties = d
        return models_test_filter_request

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
