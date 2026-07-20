from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        auth (DatastoreAmqpCredentials | None | Unset):
        binded_exchange (None | str | Unset):
        dead_letter_exchange (None | str | Unset):
        port (str | Unset):
        queue (str | Unset):
        routing_key (str | Unset):
        schema (str | Unset):
        vhost (None | str | Unset):
    """

    host: str | Unset = UNSET
    auth: DatastoreAmqpCredentials | None | Unset = UNSET
    binded_exchange: None | str | Unset = UNSET
    dead_letter_exchange: None | str | Unset = UNSET
    port: str | Unset = UNSET
    queue: str | Unset = UNSET
    routing_key: str | Unset = UNSET
    schema: str | Unset = UNSET
    vhost: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_amqp_credentials import DatastoreAmqpCredentials

        host = self.host

        auth: dict[str, Any] | None | Unset
        if isinstance(self.auth, Unset):
            auth = UNSET
        elif isinstance(self.auth, DatastoreAmqpCredentials):
            auth = self.auth.to_dict()
        else:
            auth = self.auth

        binded_exchange: None | str | Unset
        if isinstance(self.binded_exchange, Unset):
            binded_exchange = UNSET
        else:
            binded_exchange = self.binded_exchange

        dead_letter_exchange: None | str | Unset
        if isinstance(self.dead_letter_exchange, Unset):
            dead_letter_exchange = UNSET
        else:
            dead_letter_exchange = self.dead_letter_exchange

        port = self.port

        queue = self.queue

        routing_key = self.routing_key

        schema = self.schema

        vhost: None | str | Unset
        if isinstance(self.vhost, Unset):
            vhost = UNSET
        else:
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

        def _parse_auth(data: object) -> DatastoreAmqpCredentials | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                auth_type_1 = DatastoreAmqpCredentials.from_dict(data)

                return auth_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreAmqpCredentials | None | Unset, data)

        auth = _parse_auth(d.pop("auth", UNSET))

        def _parse_binded_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        binded_exchange = _parse_binded_exchange(d.pop("bindedExchange", UNSET))

        def _parse_dead_letter_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dead_letter_exchange = _parse_dead_letter_exchange(
            d.pop("deadLetterExchange", UNSET)
        )

        port = d.pop("port", UNSET)

        queue = d.pop("queue", UNSET)

        routing_key = d.pop("routingKey", UNSET)

        schema = d.pop("schema", UNSET)

        def _parse_vhost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vhost = _parse_vhost(d.pop("vhost", UNSET))

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
