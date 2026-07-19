from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreKafkaAuth")


@_attrs_define
class DatastoreKafkaAuth:
    """
    Attributes:
        hash_ (str | Unset):
        password (str | Unset):
        tls (bool | Unset):
        type_ (str | Unset):
        username (str | Unset):
    """

    hash_: str | Unset = UNSET
    password: str | Unset = UNSET
    tls: bool | Unset = UNSET
    type_: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        password = self.password

        tls = self.tls

        type_ = self.type_

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if password is not UNSET:
            field_dict["password"] = password
        if tls is not UNSET:
            field_dict["tls"] = tls
        if type_ is not UNSET:
            field_dict["type"] = type_
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash", UNSET)

        password = d.pop("password", UNSET)

        tls = d.pop("tls", UNSET)

        type_ = d.pop("type", UNSET)

        username = d.pop("username", UNSET)

        datastore_kafka_auth = cls(
            hash_=hash_,
            password=password,
            tls=tls,
            type_=type_,
            username=username,
        )

        datastore_kafka_auth.additional_properties = d
        return datastore_kafka_auth

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
