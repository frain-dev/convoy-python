from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreSQSPubSubConfig")


@_attrs_define
class DatastoreSQSPubSubConfig:
    """
    Attributes:
        access_key_id (str | Unset):
        default_region (str | Unset):
        endpoint (str | Unset): Optional: for LocalStack testing
        queue_name (str | Unset):
        secret_key (str | Unset):
    """

    access_key_id: str | Unset = UNSET
    default_region: str | Unset = UNSET
    endpoint: str | Unset = UNSET
    queue_name: str | Unset = UNSET
    secret_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key_id = self.access_key_id

        default_region = self.default_region

        endpoint = self.endpoint

        queue_name = self.queue_name

        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["access_key_id"] = access_key_id
        if default_region is not UNSET:
            field_dict["default_region"] = default_region
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if queue_name is not UNSET:
            field_dict["queue_name"] = queue_name
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key_id = d.pop("access_key_id", UNSET)

        default_region = d.pop("default_region", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        queue_name = d.pop("queue_name", UNSET)

        secret_key = d.pop("secret_key", UNSET)

        datastore_sqs_pub_sub_config = cls(
            access_key_id=access_key_id,
            default_region=default_region,
            endpoint=endpoint,
            queue_name=queue_name,
            secret_key=secret_key,
        )

        datastore_sqs_pub_sub_config.additional_properties = d
        return datastore_sqs_pub_sub_config

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
