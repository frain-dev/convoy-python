from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_verifier_type import DatastoreVerifierType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_api_key import ModelsApiKey
    from ..models.models_basic_auth import ModelsBasicAuth
    from ..models.models_h_mac import ModelsHMac


T = TypeVar("T", bound="ModelsVerifierConfig")


@_attrs_define
class ModelsVerifierConfig:
    """
    Attributes:
        type_ (DatastoreVerifierType):
        api_key (ModelsApiKey | Unset):
        basic_auth (ModelsBasicAuth | Unset):
        hmac (ModelsHMac | Unset):
    """

    type_: DatastoreVerifierType
    api_key: ModelsApiKey | Unset = UNSET
    basic_auth: ModelsBasicAuth | Unset = UNSET
    hmac: ModelsHMac | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        api_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        basic_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        hmac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hmac, Unset):
            hmac = self.hmac.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth
        if hmac is not UNSET:
            field_dict["hmac"] = hmac

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_api_key import ModelsApiKey
        from ..models.models_basic_auth import ModelsBasicAuth
        from ..models.models_h_mac import ModelsHMac

        d = dict(src_dict)
        type_ = DatastoreVerifierType(d.pop("type"))

        _api_key = d.pop("api_key", UNSET)
        api_key: ModelsApiKey | Unset
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = ModelsApiKey.from_dict(_api_key)

        _basic_auth = d.pop("basic_auth", UNSET)
        basic_auth: ModelsBasicAuth | Unset
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = ModelsBasicAuth.from_dict(_basic_auth)

        _hmac = d.pop("hmac", UNSET)
        hmac: ModelsHMac | Unset
        if isinstance(_hmac, Unset):
            hmac = UNSET
        else:
            hmac = ModelsHMac.from_dict(_hmac)

        models_verifier_config = cls(
            type_=type_,
            api_key=api_key,
            basic_auth=basic_auth,
            hmac=hmac,
        )

        models_verifier_config.additional_properties = d
        return models_verifier_config

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
