from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelsMtlsClientCert")


@_attrs_define
class ModelsMtlsClientCert:
    """
    Attributes:
        client_cert (str | Unset): ClientCert is the client certificate PEM string
        client_key (str | Unset): ClientKey is the client private key PEM string
    """

    client_cert: str | Unset = UNSET
    client_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_cert = self.client_cert

        client_key = self.client_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_cert is not UNSET:
            field_dict["client_cert"] = client_cert
        if client_key is not UNSET:
            field_dict["client_key"] = client_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_cert = d.pop("client_cert", UNSET)

        client_key = d.pop("client_key", UNSET)

        models_mtls_client_cert = cls(
            client_cert=client_cert,
            client_key=client_key,
        )

        models_mtls_client_cert.additional_properties = d
        return models_mtls_client_cert

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
