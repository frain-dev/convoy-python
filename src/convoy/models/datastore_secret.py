from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreSecret")


@_attrs_define
class DatastoreSecret:
    """
    Attributes:
        created_at (str | Unset):
        deleted_at (None | str | Unset):
        expires_at (None | str | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        value (str | Unset):
    """

    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    expires_at: None | str | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        uid = self.uid

        updated_at = self.updated_at

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_expires_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        value = d.pop("value", UNSET)

        datastore_secret = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            expires_at=expires_at,
            uid=uid,
            updated_at=updated_at,
            value=value,
        )

        datastore_secret.additional_properties = d
        return datastore_secret

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
