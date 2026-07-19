from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_signature_header_provider import ConfigSignatureHeaderProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_signature_version import DatastoreSignatureVersion


T = TypeVar("T", bound="DatastoreSignatureConfiguration")


@_attrs_define
class DatastoreSignatureConfiguration:
    """
    Attributes:
        header (ConfigSignatureHeaderProvider | Unset):
        versions (list[DatastoreSignatureVersion] | Unset):
    """

    header: ConfigSignatureHeaderProvider | Unset = UNSET
    versions: list[DatastoreSignatureVersion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: str | Unset = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.value

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_signature_version import DatastoreSignatureVersion

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: ConfigSignatureHeaderProvider | Unset
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = ConfigSignatureHeaderProvider(_header)

        _versions = d.pop("versions", UNSET)
        versions: list[DatastoreSignatureVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = DatastoreSignatureVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        datastore_signature_configuration = cls(
            header=header,
            versions=versions,
        )

        datastore_signature_configuration.additional_properties = d
        return datastore_signature_configuration

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
