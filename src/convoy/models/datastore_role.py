from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_role_type import AuthRoleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreRole")


@_attrs_define
class DatastoreRole:
    """
    Attributes:
        app (str | Unset):
        project (str | Unset):
        type_ (AuthRoleType | Unset):
    """

    app: str | Unset = UNSET
    project: str | Unset = UNSET
    type_: AuthRoleType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app

        project = self.project

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app is not UNSET:
            field_dict["app"] = app
        if project is not UNSET:
            field_dict["project"] = project
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app = d.pop("app", UNSET)

        project = d.pop("project", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AuthRoleType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AuthRoleType(_type_)

        datastore_role = cls(
            app=app,
            project=project,
            type_=type_,
        )

        datastore_role.additional_properties = d
        return datastore_role

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
