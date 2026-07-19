from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_request_id_header_provider import ConfigRequestIDHeaderProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_circuit_breaker_configuration import (
        DatastoreCircuitBreakerConfiguration,
    )
    from ..models.models_meta_event_configuration import ModelsMetaEventConfiguration
    from ..models.models_rate_limit_configuration import ModelsRateLimitConfiguration
    from ..models.models_signature_configuration import ModelsSignatureConfiguration
    from ..models.models_ssl_configuration import ModelsSSLConfiguration
    from ..models.models_strategy_configuration import ModelsStrategyConfiguration


T = TypeVar("T", bound="ModelsProjectConfig")


@_attrs_define
class ModelsProjectConfig:
    """
    Attributes:
        add_event_id_trace_headers (bool | Unset): Controls of the Event ID and Event Delivery ID Headers are added to
            the request when events are dispatched to endpoints
        circuit_breaker (DatastoreCircuitBreakerConfiguration | Unset):
        disable_endpoint (bool | Unset): Controls if the project will disable and endpoint after the retry threshold for
            an event is reached
        max_payload_read_size (int | Unset): Specifies how many bytes and incoming project should read from the ingest
            request, and how many bytes an outgoing project should from the response of your endpoints
            Defaults to 50KB.
        meta_event (ModelsMetaEventConfiguration | Unset):
        multiple_endpoint_subscriptions (bool | Unset): MultipleEndpointSubscriptions is used to configure if multiple
            subscriptions
            can be created for the endpoint in a project
        ratelimit (ModelsRateLimitConfiguration | Unset):
        replay_attacks_prevention_enabled (bool | Unset): Controls if your project will add a timestamp to it's webhook
            signature header to prevent a replay attack, See this blog post[https://getconvoy.io/blog/generating-stripe-
            like-webhook-signatures] for more]
        request_id_header (ConfigRequestIDHeaderProvider | Unset):
        search_policy (str | Unset): Specify the interval in hours for which the event tokenizer runs
        signature (ModelsSignatureConfiguration | Unset):
        ssl (ModelsSSLConfiguration | Unset):
        strategy (ModelsStrategyConfiguration | Unset):
    """

    add_event_id_trace_headers: bool | Unset = UNSET
    circuit_breaker: DatastoreCircuitBreakerConfiguration | Unset = UNSET
    disable_endpoint: bool | Unset = UNSET
    max_payload_read_size: int | Unset = UNSET
    meta_event: ModelsMetaEventConfiguration | Unset = UNSET
    multiple_endpoint_subscriptions: bool | Unset = UNSET
    ratelimit: ModelsRateLimitConfiguration | Unset = UNSET
    replay_attacks_prevention_enabled: bool | Unset = UNSET
    request_id_header: ConfigRequestIDHeaderProvider | Unset = UNSET
    search_policy: str | Unset = UNSET
    signature: ModelsSignatureConfiguration | Unset = UNSET
    ssl: ModelsSSLConfiguration | Unset = UNSET
    strategy: ModelsStrategyConfiguration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_event_id_trace_headers = self.add_event_id_trace_headers

        circuit_breaker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.circuit_breaker, Unset):
            circuit_breaker = self.circuit_breaker.to_dict()

        disable_endpoint = self.disable_endpoint

        max_payload_read_size = self.max_payload_read_size

        meta_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_event, Unset):
            meta_event = self.meta_event.to_dict()

        multiple_endpoint_subscriptions = self.multiple_endpoint_subscriptions

        ratelimit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ratelimit, Unset):
            ratelimit = self.ratelimit.to_dict()

        replay_attacks_prevention_enabled = self.replay_attacks_prevention_enabled

        request_id_header: str | Unset = UNSET
        if not isinstance(self.request_id_header, Unset):
            request_id_header = self.request_id_header.value

        search_policy = self.search_policy

        signature: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        ssl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssl, Unset):
            ssl = self.ssl.to_dict()

        strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_event_id_trace_headers is not UNSET:
            field_dict["add_event_id_trace_headers"] = add_event_id_trace_headers
        if circuit_breaker is not UNSET:
            field_dict["circuit_breaker"] = circuit_breaker
        if disable_endpoint is not UNSET:
            field_dict["disable_endpoint"] = disable_endpoint
        if max_payload_read_size is not UNSET:
            field_dict["max_payload_read_size"] = max_payload_read_size
        if meta_event is not UNSET:
            field_dict["meta_event"] = meta_event
        if multiple_endpoint_subscriptions is not UNSET:
            field_dict["multiple_endpoint_subscriptions"] = (
                multiple_endpoint_subscriptions
            )
        if ratelimit is not UNSET:
            field_dict["ratelimit"] = ratelimit
        if replay_attacks_prevention_enabled is not UNSET:
            field_dict["replay_attacks_prevention_enabled"] = (
                replay_attacks_prevention_enabled
            )
        if request_id_header is not UNSET:
            field_dict["request_id_header"] = request_id_header
        if search_policy is not UNSET:
            field_dict["search_policy"] = search_policy
        if signature is not UNSET:
            field_dict["signature"] = signature
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_circuit_breaker_configuration import (
            DatastoreCircuitBreakerConfiguration,
        )
        from ..models.models_meta_event_configuration import (
            ModelsMetaEventConfiguration,
        )
        from ..models.models_rate_limit_configuration import (
            ModelsRateLimitConfiguration,
        )
        from ..models.models_signature_configuration import ModelsSignatureConfiguration
        from ..models.models_ssl_configuration import ModelsSSLConfiguration
        from ..models.models_strategy_configuration import ModelsStrategyConfiguration

        d = dict(src_dict)
        add_event_id_trace_headers = d.pop("add_event_id_trace_headers", UNSET)

        _circuit_breaker = d.pop("circuit_breaker", UNSET)
        circuit_breaker: DatastoreCircuitBreakerConfiguration | Unset
        if isinstance(_circuit_breaker, Unset):
            circuit_breaker = UNSET
        else:
            circuit_breaker = DatastoreCircuitBreakerConfiguration.from_dict(
                _circuit_breaker
            )

        disable_endpoint = d.pop("disable_endpoint", UNSET)

        max_payload_read_size = d.pop("max_payload_read_size", UNSET)

        _meta_event = d.pop("meta_event", UNSET)
        meta_event: ModelsMetaEventConfiguration | Unset
        if isinstance(_meta_event, Unset):
            meta_event = UNSET
        else:
            meta_event = ModelsMetaEventConfiguration.from_dict(_meta_event)

        multiple_endpoint_subscriptions = d.pop(
            "multiple_endpoint_subscriptions", UNSET
        )

        _ratelimit = d.pop("ratelimit", UNSET)
        ratelimit: ModelsRateLimitConfiguration | Unset
        if isinstance(_ratelimit, Unset):
            ratelimit = UNSET
        else:
            ratelimit = ModelsRateLimitConfiguration.from_dict(_ratelimit)

        replay_attacks_prevention_enabled = d.pop(
            "replay_attacks_prevention_enabled", UNSET
        )

        _request_id_header = d.pop("request_id_header", UNSET)
        request_id_header: ConfigRequestIDHeaderProvider | Unset
        if isinstance(_request_id_header, Unset):
            request_id_header = UNSET
        else:
            request_id_header = ConfigRequestIDHeaderProvider(_request_id_header)

        search_policy = d.pop("search_policy", UNSET)

        _signature = d.pop("signature", UNSET)
        signature: ModelsSignatureConfiguration | Unset
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = ModelsSignatureConfiguration.from_dict(_signature)

        _ssl = d.pop("ssl", UNSET)
        ssl: ModelsSSLConfiguration | Unset
        if isinstance(_ssl, Unset):
            ssl = UNSET
        else:
            ssl = ModelsSSLConfiguration.from_dict(_ssl)

        _strategy = d.pop("strategy", UNSET)
        strategy: ModelsStrategyConfiguration | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = ModelsStrategyConfiguration.from_dict(_strategy)

        models_project_config = cls(
            add_event_id_trace_headers=add_event_id_trace_headers,
            circuit_breaker=circuit_breaker,
            disable_endpoint=disable_endpoint,
            max_payload_read_size=max_payload_read_size,
            meta_event=meta_event,
            multiple_endpoint_subscriptions=multiple_endpoint_subscriptions,
            ratelimit=ratelimit,
            replay_attacks_prevention_enabled=replay_attacks_prevention_enabled,
            request_id_header=request_id_header,
            search_policy=search_policy,
            signature=signature,
            ssl=ssl,
            strategy=strategy,
        )

        models_project_config.additional_properties = d
        return models_project_config

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
