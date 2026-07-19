from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_encoding_type import DatastoreEncodingType

T = TypeVar("T", bound="ModelsHMac")


@_attrs_define
class ModelsHMac:
    """
    Attributes:
        encoding (DatastoreEncodingType):
        hash_ (str):
        header (str):
        secret (str):
    """

    encoding: DatastoreEncodingType
    hash_: str
    header: str
    secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encoding = self.encoding.value

        hash_ = self.hash_

        header = self.header

        secret = self.secret

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encoding": encoding,
                "hash": hash_,
                "header": header,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encoding = DatastoreEncodingType(d.pop("encoding"))

        hash_ = d.pop("hash")

        header = d.pop("header")

        secret = d.pop("secret")

        models_h_mac = cls(
            encoding=encoding,
            hash_=hash_,
            header=header,
            secret=secret,
        )

        models_h_mac.additional_properties = d
        return models_h_mac

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
