from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_o_auth_2 import ModelsOAuth2


T = TypeVar("T", bound="ModelsTestOAuth2Request")


@_attrs_define
class ModelsTestOAuth2Request:
    """
    Attributes:
        oauth2 (ModelsOAuth2 | Unset):
    """

    oauth2: ModelsOAuth2 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oauth2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oauth2, Unset):
            oauth2 = self.oauth2.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oauth2 is not UNSET:
            field_dict["oauth2"] = oauth2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_o_auth_2 import ModelsOAuth2

        d = dict(src_dict)
        _oauth2 = d.pop("oauth2", UNSET)
        oauth2: ModelsOAuth2 | Unset
        if isinstance(_oauth2, Unset):
            oauth2 = UNSET
        else:
            oauth2 = ModelsOAuth2.from_dict(_oauth2)

        models_test_o_auth_2_request = cls(
            oauth2=oauth2,
        )

        models_test_o_auth_2_request.additional_properties = d
        return models_test_o_auth_2_request

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
