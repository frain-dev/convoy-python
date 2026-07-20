from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        api_key (DatastoreApiKey | None | Unset):
        basic_auth (DatastoreBasicAuth | None | Unset):
        hmac (DatastoreHMac | None | Unset):
        type_ (DatastoreVerifierType | Unset):
    """

    api_key: DatastoreApiKey | None | Unset = UNSET
    basic_auth: DatastoreBasicAuth | None | Unset = UNSET
    hmac: DatastoreHMac | None | Unset = UNSET
    type_: DatastoreVerifierType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_api_key import DatastoreApiKey
        from ..models.datastore_basic_auth import DatastoreBasicAuth
        from ..models.datastore_h_mac import DatastoreHMac

        api_key: dict[str, Any] | None | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        elif isinstance(self.api_key, DatastoreApiKey):
            api_key = self.api_key.to_dict()
        else:
            api_key = self.api_key

        basic_auth: dict[str, Any] | None | Unset
        if isinstance(self.basic_auth, Unset):
            basic_auth = UNSET
        elif isinstance(self.basic_auth, DatastoreBasicAuth):
            basic_auth = self.basic_auth.to_dict()
        else:
            basic_auth = self.basic_auth

        hmac: dict[str, Any] | None | Unset
        if isinstance(self.hmac, Unset):
            hmac = UNSET
        elif isinstance(self.hmac, DatastoreHMac):
            hmac = self.hmac.to_dict()
        else:
            hmac = self.hmac

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

        def _parse_api_key(data: object) -> DatastoreApiKey | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_key_type_1 = DatastoreApiKey.from_dict(data)

                return api_key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreApiKey | None | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_basic_auth(data: object) -> DatastoreBasicAuth | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                basic_auth_type_1 = DatastoreBasicAuth.from_dict(data)

                return basic_auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreBasicAuth | None | Unset, data)

        basic_auth = _parse_basic_auth(d.pop("basic_auth", UNSET))

        def _parse_hmac(data: object) -> DatastoreHMac | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hmac_type_1 = DatastoreHMac.from_dict(data)

                return hmac_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreHMac | None | Unset, data)

        hmac = _parse_hmac(d.pop("hmac", UNSET))

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
