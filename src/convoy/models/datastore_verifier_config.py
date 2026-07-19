from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_verifier_type import DatastoreVerifierType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_api_key import DatastoreApiKey
    from ..models.datastore_basic_auth import DatastoreBasicAuth
    from ..models.datastore_h_mac import DatastoreHMac


T = TypeVar("T", bound="DatastoreVerifierConfig")


@_attrs_define
class DatastoreVerifierConfig:
    """
    Attributes:
        api_key (DatastoreApiKey | Unset):
        basic_auth (DatastoreBasicAuth | Unset):
        hmac (DatastoreHMac | Unset):
        type_ (DatastoreVerifierType | Unset):
    """

    api_key: DatastoreApiKey | Unset = UNSET
    basic_auth: DatastoreBasicAuth | Unset = UNSET
    hmac: DatastoreHMac | Unset = UNSET
    type_: DatastoreVerifierType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        basic_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        hmac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hmac, Unset):
            hmac = self.hmac.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth
        if hmac is not UNSET:
            field_dict["hmac"] = hmac
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_api_key import DatastoreApiKey
        from ..models.datastore_basic_auth import DatastoreBasicAuth
        from ..models.datastore_h_mac import DatastoreHMac

        d = dict(src_dict)
        _api_key = d.pop("api_key", UNSET)
        api_key: DatastoreApiKey | Unset
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = DatastoreApiKey.from_dict(_api_key)

        _basic_auth = d.pop("basic_auth", UNSET)
        basic_auth: DatastoreBasicAuth | Unset
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = DatastoreBasicAuth.from_dict(_basic_auth)

        _hmac = d.pop("hmac", UNSET)
        hmac: DatastoreHMac | Unset
        if isinstance(_hmac, Unset):
            hmac = UNSET
        else:
            hmac = DatastoreHMac.from_dict(_hmac)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreVerifierType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreVerifierType(_type_)

        datastore_verifier_config = cls(
            api_key=api_key,
            basic_auth=basic_auth,
            hmac=hmac,
            type_=type_,
        )

        datastore_verifier_config.additional_properties = d
        return datastore_verifier_config

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
