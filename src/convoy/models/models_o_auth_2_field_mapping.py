from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsOAuth2FieldMapping")


@_attrs_define
class ModelsOAuth2FieldMapping:
    """
    Attributes:
        access_token (str | Unset): Field name for access token (e.g., "accessToken", "access_token", "token")
        expires_in (str | Unset): Field name for expiry time (e.g., "expiresIn", "expires_in", "expiresAt")
        token_type (str | Unset): Field name for token type (e.g., "tokenType", "token_type")
    """

    access_token: str | Unset = UNSET
    expires_in: str | Unset = UNSET
    token_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        expires_in = self.expires_in

        token_type = self.token_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token", UNSET)

        expires_in = d.pop("expires_in", UNSET)

        token_type = d.pop("token_type", UNSET)

        models_o_auth_2_field_mapping = cls(
            access_token=access_token,
            expires_in=expires_in,
            token_type=token_type,
        )

        models_o_auth_2_field_mapping.additional_properties = d
        return models_o_auth_2_field_mapping

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
