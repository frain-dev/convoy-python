from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_amqp_credentials import DatastoreAmqpCredentials


T = TypeVar("T", bound="DatastoreAmqpPubSubConfig")


@_attrs_define
class DatastoreAmqpPubSubConfig:
    """
    Attributes:
        host (str | Unset):
        auth (DatastoreAmqpCredentials | Unset):
        binded_exchange (str | Unset):
        dead_letter_exchange (str | Unset):
        port (str | Unset):
        queue (str | Unset):
        routing_key (str | Unset):
        schema (str | Unset):
        vhost (str | Unset):
    """

    host: str | Unset = UNSET
    auth: DatastoreAmqpCredentials | Unset = UNSET
    binded_exchange: str | Unset = UNSET
    dead_letter_exchange: str | Unset = UNSET
    port: str | Unset = UNSET
    queue: str | Unset = UNSET
    routing_key: str | Unset = UNSET
    schema: str | Unset = UNSET
    vhost: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        binded_exchange = self.binded_exchange

        dead_letter_exchange = self.dead_letter_exchange

        port = self.port

        queue = self.queue

        routing_key = self.routing_key

        schema = self.schema

        vhost = self.vhost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if auth is not UNSET:
            field_dict["auth"] = auth
        if binded_exchange is not UNSET:
            field_dict["bindedExchange"] = binded_exchange
        if dead_letter_exchange is not UNSET:
            field_dict["deadLetterExchange"] = dead_letter_exchange
        if port is not UNSET:
            field_dict["port"] = port
        if queue is not UNSET:
            field_dict["queue"] = queue
        if routing_key is not UNSET:
            field_dict["routingKey"] = routing_key
        if schema is not UNSET:
            field_dict["schema"] = schema
        if vhost is not UNSET:
            field_dict["vhost"] = vhost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_amqp_credentials import DatastoreAmqpCredentials

        d = dict(src_dict)
        host = d.pop("host", UNSET)

        _auth = d.pop("auth", UNSET)
        auth: DatastoreAmqpCredentials | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = DatastoreAmqpCredentials.from_dict(_auth)

        binded_exchange = d.pop("bindedExchange", UNSET)

        dead_letter_exchange = d.pop("deadLetterExchange", UNSET)

        port = d.pop("port", UNSET)

        queue = d.pop("queue", UNSET)

        routing_key = d.pop("routingKey", UNSET)

        schema = d.pop("schema", UNSET)

        vhost = d.pop("vhost", UNSET)

        datastore_amqp_pub_sub_config = cls(
            host=host,
            auth=auth,
            binded_exchange=binded_exchange,
            dead_letter_exchange=dead_letter_exchange,
            port=port,
            queue=queue,
            routing_key=routing_key,
            schema=schema,
            vhost=vhost,
        )

        datastore_amqp_pub_sub_config.additional_properties = d
        return datastore_amqp_pub_sub_config

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
