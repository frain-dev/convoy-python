from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsTestOAuth2Response")


@_attrs_define
class ModelsTestOAuth2Response:
    """
    Attributes:
        access_token (str | Unset):
        error (str | Unset):
        expires_at (str | Unset):
        message (str | Unset):
        success (bool | Unset):
        token_type (str | Unset):
    """

    access_token: str | Unset = UNSET
    error: str | Unset = UNSET
    expires_at: str | Unset = UNSET
    message: str | Unset = UNSET
    success: bool | Unset = UNSET
    token_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        error = self.error

        expires_at = self.expires_at

        message = self.message

        success = self.success

        token_type = self.token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if error is not UNSET:
            field_dict["error"] = error
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if message is not UNSET:
            field_dict["message"] = message
        if success is not UNSET:
            field_dict["success"] = success
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        error = d.pop("error", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        message = d.pop("message", UNSET)

        success = d.pop("success", UNSET)

        token_type = d.pop("token_type", UNSET)

        models_test_o_auth_2_response = cls(
            access_token=access_token,
            error=error,
            expires_at=expires_at,
            message=message,
            success=success,
            token_type=token_type,
        )

        models_test_o_auth_2_response.additional_properties = d
        return models_test_o_auth_2_response

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
