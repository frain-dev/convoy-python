from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_role import DatastoreRole


T = TypeVar("T", bound="DatastoreAPIKeyResponse")


@_attrs_define
class DatastoreAPIKeyResponse:
    """
    Attributes:
        created_at (str | Unset):
        expires_at (None | str | Unset):
        key (str | Unset):
        key_type (str | Unset):
        name (str | Unset):
        role (DatastoreRole | Unset):
        uid (str | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    key: str | Unset = UNSET
    key_type: str | Unset = UNSET
    name: str | Unset = UNSET
    role: DatastoreRole | Unset = UNSET
    uid: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        key = self.key

        key_type = self.key_type

        name = self.name

        role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.to_dict()

        uid = self.uid

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if key is not UNSET:
            field_dict["key"] = key
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if uid is not UNSET:
            field_dict["uid"] = uid
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_role import DatastoreRole

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        key = d.pop("key", UNSET)

        key_type = d.pop("key_type", UNSET)

        name = d.pop("name", UNSET)

        _role = d.pop("role", UNSET)
        role: DatastoreRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = DatastoreRole.from_dict(_role)

        uid = d.pop("uid", UNSET)

        user_id = d.pop("user_id", UNSET)

        datastore_api_key_response = cls(
            created_at=created_at,
            expires_at=expires_at,
            key=key,
            key_type=key_type,
            name=name,
            role=role,
            uid=uid,
            user_id=user_id,
        )

        datastore_api_key_response.additional_properties = d
        return datastore_api_key_response

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
