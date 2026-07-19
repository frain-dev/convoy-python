from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreGooglePubSubConfig")


@_attrs_define
class DatastoreGooglePubSubConfig:
    """
    Attributes:
        project_id (str | Unset):
        service_account (str | Unset): encoding/json marshals []byte as a base64 string on the wire.
        subscription_id (str | Unset):
    """

    project_id: str | Unset = UNSET
    service_account: str | Unset = UNSET
    subscription_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        service_account = self.service_account

        subscription_id = self.subscription_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if service_account is not UNSET:
            field_dict["service_account"] = service_account
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id", UNSET)

        service_account = d.pop("service_account", UNSET)

        subscription_id = d.pop("subscription_id", UNSET)

        datastore_google_pub_sub_config = cls(
            project_id=project_id,
            service_account=service_account,
            subscription_id=subscription_id,
        )

        datastore_google_pub_sub_config.additional_properties = d
        return datastore_google_pub_sub_config

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
