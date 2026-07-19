from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_project_config import ModelsProjectConfig


T = TypeVar("T", bound="ModelsCreateProject")


@_attrs_define
class ModelsCreateProject:
    """
    Attributes:
        config (ModelsProjectConfig | Unset):
        logo_url (str | Unset):
        name (str | Unset): Project Name
        type_ (str | Unset): Project Type, supported values are `outgoing`, `incoming`
    """

    config: ModelsProjectConfig | Unset = UNSET
    logo_url: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        logo_url = self.logo_url

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_project_config import ModelsProjectConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: ModelsProjectConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ModelsProjectConfig.from_dict(_config)

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        models_create_project = cls(
            config=config,
            logo_url=logo_url,
            name=name,
            type_=type_,
        )

        models_create_project.additional_properties = d
        return models_create_project

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
