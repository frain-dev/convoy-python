from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_kafka_auth import DatastoreKafkaAuth


T = TypeVar("T", bound="DatastoreKafkaPubSubConfig")


@_attrs_define
class DatastoreKafkaPubSubConfig:
    """
    Attributes:
        auth (DatastoreKafkaAuth | None | Unset):
        brokers (list[str] | Unset):
        consumer_group_id (str | Unset):
        topic_name (str | Unset):
    """

    auth: DatastoreKafkaAuth | None | Unset = UNSET
    brokers: list[str] | Unset = UNSET
    consumer_group_id: str | Unset = UNSET
    topic_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_kafka_auth import DatastoreKafkaAuth

        auth: dict[str, Any] | None | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, DatastoreKafkaAuth):
            auth = self.auth.to_dict()
        else:
            auth = self.auth

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
        from ..models.datastore_kafka_auth import DatastoreKafkaAuth

        d = dict(src_dict)

        def _parse_auth(data: object) -> DatastoreKafkaAuth | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_1 = DatastoreKafkaAuth.from_dict(data)

                return auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreKafkaAuth | None | Unset, data)

        auth = _parse_auth(d.pop("auth", UNSET))

        brokers = cast(list[str], d.pop("brokers", UNSET))

        consumer_group_id = d.pop("consumer_group_id", UNSET)

        topic_name = d.pop("topic_name", UNSET)

        datastore_kafka_pub_sub_config = cls(
            auth=auth,
            brokers=brokers,
            consumer_group_id=consumer_group_id,
            topic_name=topic_name,
        )

        datastore_kafka_pub_sub_config.additional_properties = d
        return datastore_kafka_pub_sub_config

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
