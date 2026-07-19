from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_endpoint_authentication_type import (
    DatastoreEndpointAuthenticationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_api_key import ModelsApiKey
    from ..models.models_basic_auth import ModelsBasicAuth
    from ..models.models_o_auth_2 import ModelsOAuth2


T = TypeVar("T", bound="ModelsEndpointAuthentication")


@_attrs_define
class ModelsEndpointAuthentication:
    """
    Attributes:
        api_key (ModelsApiKey | Unset):
        basic_auth (ModelsBasicAuth | Unset):
        oauth2 (ModelsOAuth2 | Unset):
        type_ (DatastoreEndpointAuthenticationType | Unset):
    """

    api_key: ModelsApiKey | Unset = UNSET
    basic_auth: ModelsBasicAuth | Unset = UNSET
    oauth2: ModelsOAuth2 | Unset = UNSET
    type_: DatastoreEndpointAuthenticationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        basic_auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        oauth2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oauth2, Unset):
            oauth2 = self.oauth2.to_dict()

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
        if oauth2 is not UNSET:
            field_dict["oauth2"] = oauth2
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_api_key import ModelsApiKey
        from ..models.models_basic_auth import ModelsBasicAuth
        from ..models.models_o_auth_2 import ModelsOAuth2

        d = dict(src_dict)
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

        _oauth2 = d.pop("oauth2", UNSET)
        oauth2: ModelsOAuth2 | Unset
        if isinstance(_oauth2, Unset):
            oauth2 = UNSET
        else:
            oauth2 = ModelsOAuth2.from_dict(_oauth2)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreEndpointAuthenticationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreEndpointAuthenticationType(_type_)

        models_endpoint_authentication = cls(
            api_key=api_key,
            basic_auth=basic_auth,
            oauth2=oauth2,
            type_=type_,
        )

        models_endpoint_authentication.additional_properties = d
        return models_endpoint_authentication

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
