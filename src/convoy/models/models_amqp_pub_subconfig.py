from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_amqp_auth import ModelsAmqpAuth
    from ..models.models_amqp_exchange import ModelsAmqpExchange


T = TypeVar("T", bound="ModelsAmqpPubSubconfig")


@_attrs_define
class ModelsAmqpPubSubconfig:
    """
    Attributes:
        host (str | Unset):
        auth (ModelsAmqpAuth | Unset):
        bind_exchange (ModelsAmqpExchange | Unset):
        dead_letter_exchange (str | Unset):
        port (str | Unset):
        queue (str | Unset):
        schema (str | Unset):
        vhost (str | Unset):
    """

    host: str | Unset = UNSET
    auth: ModelsAmqpAuth | Unset = UNSET
    bind_exchange: ModelsAmqpExchange | Unset = UNSET
    dead_letter_exchange: str | Unset = UNSET
    port: str | Unset = UNSET
    queue: str | Unset = UNSET
    schema: str | Unset = UNSET
    vhost: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        bind_exchange: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bind_exchange, Unset):
            bind_exchange = self.bind_exchange.to_dict()

        dead_letter_exchange = self.dead_letter_exchange

        port = self.port

        queue = self.queue

        schema = self.schema

        vhost = self.vhost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if auth is not UNSET:
            field_dict["auth"] = auth
        if bind_exchange is not UNSET:
            field_dict["bindExchange"] = bind_exchange
        if dead_letter_exchange is not UNSET:
            field_dict["deadLetterExchange"] = dead_letter_exchange
        if port is not UNSET:
            field_dict["port"] = port
        if queue is not UNSET:
            field_dict["queue"] = queue
        if schema is not UNSET:
            field_dict["schema"] = schema
        if vhost is not UNSET:
            field_dict["vhost"] = vhost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_amqp_auth import ModelsAmqpAuth
        from ..models.models_amqp_exchange import ModelsAmqpExchange

        d = dict(src_dict)
        host = d.pop("host", UNSET)

        _auth = d.pop("auth", UNSET)
        auth: ModelsAmqpAuth | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = ModelsAmqpAuth.from_dict(_auth)

        _bind_exchange = d.pop("bindExchange", UNSET)
        bind_exchange: ModelsAmqpExchange | Unset
        if isinstance(_bind_exchange, Unset):
            bind_exchange = UNSET
        else:
            bind_exchange = ModelsAmqpExchange.from_dict(_bind_exchange)

        dead_letter_exchange = d.pop("deadLetterExchange", UNSET)

        port = d.pop("port", UNSET)

        queue = d.pop("queue", UNSET)

        schema = d.pop("schema", UNSET)

        vhost = d.pop("vhost", UNSET)

        models_amqp_pub_subconfig = cls(
            host=host,
            auth=auth,
            bind_exchange=bind_exchange,
            dead_letter_exchange=dead_letter_exchange,
            port=port,
            queue=queue,
            schema=schema,
            vhost=vhost,
        )

        models_amqp_pub_subconfig.additional_properties = d
        return models_amqp_pub_subconfig

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
