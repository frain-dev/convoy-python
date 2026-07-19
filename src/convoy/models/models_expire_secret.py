from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsExpireSecret")


@_attrs_define
class ModelsExpireSecret:
    """
    Attributes:
        expiration (int | Unset): Amount of time to wait before expiring the old endpoint secret.
            If AdvancedSignatures is turned on for the project, signatures for both secrets will be generated up until
            the old signature is expired.
        secret (str | Unset): New Endpoint secret value.
    """

    expiration: int | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiration = self.expiration

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expiration = d.pop("expiration", UNSET)

        secret = d.pop("secret", UNSET)

        models_expire_secret = cls(
            expiration=expiration,
            secret=secret,
        )

        models_expire_secret.additional_properties = d
        return models_expire_secret

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
