from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_encoding_type import DatastoreEncodingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreHMac")


@_attrs_define
class DatastoreHMac:
    """
    Attributes:
        encoding (DatastoreEncodingType | Unset):
        hash_ (str | Unset):
        header (str | Unset):
        secret (str | Unset):
    """

    encoding: DatastoreEncodingType | Unset = UNSET
    hash_: str | Unset = UNSET
    header: str | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encoding: str | Unset = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value

        hash_ = self.hash_

        header = self.header

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if header is not UNSET:
            field_dict["header"] = header
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _encoding = d.pop("encoding", UNSET)
        encoding: DatastoreEncodingType | Unset
        if isinstance(_encoding, Unset):
            encoding = UNSET
        else:
            encoding = DatastoreEncodingType(_encoding)

        hash_ = d.pop("hash", UNSET)

        header = d.pop("header", UNSET)

        secret = d.pop("secret", UNSET)

        datastore_h_mac = cls(
            encoding=encoding,
            hash_=hash_,
            header=header,
            secret=secret,
        )

        datastore_h_mac.additional_properties = d
        return datastore_h_mac

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
