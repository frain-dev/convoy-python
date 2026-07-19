from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsSignatureVersion")


@_attrs_define
class ModelsSignatureVersion:
    """
    Attributes:
        created_at (str | Unset):
        encoding (str | Unset):
        hash_ (str | Unset):
        uid (str | Unset):
    """

    created_at: str | Unset = UNSET
    encoding: str | Unset = UNSET
    hash_: str | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        encoding = self.encoding

        hash_ = self.hash_

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        encoding = d.pop("encoding", UNSET)

        hash_ = d.pop("hash", UNSET)

        uid = d.pop("uid", UNSET)

        models_signature_version = cls(
            created_at=created_at,
            encoding=encoding,
            hash_=hash_,
            uid=uid,
        )

        models_signature_version.additional_properties = d
        return models_signature_version

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
