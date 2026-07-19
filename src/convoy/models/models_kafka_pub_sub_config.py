from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_kafka_auth import ModelsKafkaAuth


T = TypeVar("T", bound="ModelsKafkaPubSubConfig")


@_attrs_define
class ModelsKafkaPubSubConfig:
    """
    Attributes:
        auth (ModelsKafkaAuth | Unset):
        brokers (list[str] | Unset):
        consumer_group_id (str | Unset):
        topic_name (str | Unset):
    """

    auth: ModelsKafkaAuth | Unset = UNSET
    brokers: list[str] | Unset = UNSET
    consumer_group_id: str | Unset = UNSET
    topic_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        brokers: list[str] | Unset = UNSET
        if not isinstance(self.brokers, Unset):
            brokers = self.brokers

        consumer_group_id = self.consumer_group_id

        topic_name = self.topic_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth is not UNSET:
            field_dict["auth"] = auth
        if brokers is not UNSET:
            field_dict["brokers"] = brokers
        if consumer_group_id is not UNSET:
            field_dict["consumer_group_id"] = consumer_group_id
        if topic_name is not UNSET:
            field_dict["topic_name"] = topic_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_kafka_auth import ModelsKafkaAuth

        d = dict(src_dict)
        _auth = d.pop("auth", UNSET)
        auth: ModelsKafkaAuth | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ModelsKafkaAuth.from_dict(_auth)

        brokers = cast(list[str], d.pop("brokers", UNSET))

        consumer_group_id = d.pop("consumer_group_id", UNSET)

        topic_name = d.pop("topic_name", UNSET)

        models_kafka_pub_sub_config = cls(
            auth=auth,
            brokers=brokers,
            consumer_group_id=consumer_group_id,
            topic_name=topic_name,
        )

        models_kafka_pub_sub_config.additional_properties = d
        return models_kafka_pub_sub_config

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
