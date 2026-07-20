from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.config_request_id_header_provider import ConfigRequestIDHeaderProvider
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_circuit_breaker_configuration import (
        DatastoreCircuitBreakerConfiguration,
    )
    from ..models.datastore_meta_event_configuration import (
        DatastoreMetaEventConfiguration,
    )
    from ..models.datastore_rate_limit_configuration import (
        DatastoreRateLimitConfiguration,
    )
    from ..models.datastore_signature_configuration import (
        DatastoreSignatureConfiguration,
    )
    from ..models.datastore_ssl_configuration import DatastoreSSLConfiguration
    from ..models.datastore_strategy_configuration import DatastoreStrategyConfiguration


T = TypeVar("T", bound="DatastoreProjectConfig")


@_attrs_define
class DatastoreProjectConfig:
    """
    Attributes:
        add_event_id_trace_headers (bool | Unset):
        circuit_breaker (DatastoreCircuitBreakerConfiguration | None | Unset):
        disable_endpoint (bool | Unset):
        max_payload_read_size (int | Unset):
        meta_event (DatastoreMetaEventConfiguration | None | Unset):
        multiple_endpoint_subscriptions (bool | Unset):
        ratelimit (DatastoreRateLimitConfiguration | None | Unset):
        replay_attacks_prevention_enabled (bool | Unset):
        request_id_header (ConfigRequestIDHeaderProvider | Unset):
        search_policy (str | Unset):
        signature (DatastoreSignatureConfiguration | None | Unset):
        ssl (DatastoreSSLConfiguration | None | Unset):
        strategy (DatastoreStrategyConfiguration | None | Unset):
    """

    add_event_id_trace_headers: bool | Unset = UNSET
    circuit_breaker: DatastoreCircuitBreakerConfiguration | None | Unset = UNSET
    disable_endpoint: bool | Unset = UNSET
    max_payload_read_size: int | Unset = UNSET
    meta_event: DatastoreMetaEventConfiguration | None | Unset = UNSET
    multiple_endpoint_subscriptions: bool | Unset = UNSET
    ratelimit: DatastoreRateLimitConfiguration | None | Unset = UNSET
    replay_attacks_prevention_enabled: bool | Unset = UNSET
    request_id_header: ConfigRequestIDHeaderProvider | Unset = UNSET
    search_policy: str | Unset = UNSET
    signature: DatastoreSignatureConfiguration | None | Unset = UNSET
    ssl: DatastoreSSLConfiguration | None | Unset = UNSET
    strategy: DatastoreStrategyConfiguration | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_circuit_breaker_configuration import (
            DatastoreCircuitBreakerConfiguration,
        )
        from ..models.datastore_meta_event_configuration import (
            DatastoreMetaEventConfiguration,
        )
        from ..models.datastore_rate_limit_configuration import (
            DatastoreRateLimitConfiguration,
        )
        from ..models.datastore_signature_configuration import (
            DatastoreSignatureConfiguration,
        )
        from ..models.datastore_ssl_configuration import DatastoreSSLConfiguration
        from ..models.datastore_strategy_configuration import (
            DatastoreStrategyConfiguration,
        )

        add_event_id_trace_headers = self.add_event_id_trace_headers

        circuit_breaker: dict[str, Any] | None | Unset
        if isinstance(self.circuit_breaker, Unset):
            circuit_breaker = UNSET
        elif isinstance(self.circuit_breaker, DatastoreCircuitBreakerConfiguration):
            circuit_breaker = self.circuit_breaker.to_dict()
        else:
            circuit_breaker = self.circuit_breaker

        disable_endpoint = self.disable_endpoint

        max_payload_read_size = self.max_payload_read_size

        meta_event: dict[str, Any] | None | Unset
        if isinstance(self.meta_event, Unset):
            meta_event = UNSET
        elif isinstance(self.meta_event, DatastoreMetaEventConfiguration):
            meta_event = self.meta_event.to_dict()
        else:
            meta_event = self.meta_event

        multiple_endpoint_subscriptions = self.multiple_endpoint_subscriptions

        ratelimit: dict[str, Any] | None | Unset
        if isinstance(self.ratelimit, Unset):
            ratelimit = UNSET
        elif isinstance(self.ratelimit, DatastoreRateLimitConfiguration):
            ratelimit = self.ratelimit.to_dict()
        else:
            ratelimit = self.ratelimit

        replay_attacks_prevention_enabled = self.replay_attacks_prevention_enabled

        request_id_header: str | Unset = UNSET
        if not isinstance(self.request_id_header, Unset):
            request_id_header = self.request_id_header.value

        search_policy = self.search_policy

        signature: dict[str, Any] | None | Unset
        if isinstance(self.signature, Unset):
            signature = UNSET
        elif isinstance(self.signature, DatastoreSignatureConfiguration):
            signature = self.signature.to_dict()
        else:
            signature = self.signature

        ssl: dict[str, Any] | None | Unset
        if isinstance(self.ssl, Unset):
            ssl = UNSET
        elif isinstance(self.ssl, DatastoreSSLConfiguration):
            ssl = self.ssl.to_dict()
        else:
            ssl = self.ssl

        strategy: dict[str, Any] | None | Unset
        if isinstance(self.strategy, Unset):
            strategy = UNSET
        elif isinstance(self.strategy, DatastoreStrategyConfiguration):
            strategy = self.strategy.to_dict()
        else:
            strategy = self.strategy

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
        from ..models.datastore_meta_event_configuration import (
            DatastoreMetaEventConfiguration,
        )
        from ..models.datastore_rate_limit_configuration import (
            DatastoreRateLimitConfiguration,
        )
        from ..models.datastore_signature_configuration import (
            DatastoreSignatureConfiguration,
        )
        from ..models.datastore_ssl_configuration import DatastoreSSLConfiguration
        from ..models.datastore_strategy_configuration import (
            DatastoreStrategyConfiguration,
        )

        d = dict(src_dict)
        add_event_id_trace_headers = d.pop("add_event_id_trace_headers", UNSET)

        def _parse_circuit_breaker(
            data: object,
        ) -> DatastoreCircuitBreakerConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                circuit_breaker_type_1 = DatastoreCircuitBreakerConfiguration.from_dict(
                    data
                )

                return circuit_breaker_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreCircuitBreakerConfiguration | None | Unset, data)

        circuit_breaker = _parse_circuit_breaker(d.pop("circuit_breaker", UNSET))

        disable_endpoint = d.pop("disable_endpoint", UNSET)

        max_payload_read_size = d.pop("max_payload_read_size", UNSET)

        def _parse_meta_event(
            data: object,
        ) -> DatastoreMetaEventConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                meta_event_type_1 = DatastoreMetaEventConfiguration.from_dict(data)

                return meta_event_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMetaEventConfiguration | None | Unset, data)

        meta_event = _parse_meta_event(d.pop("meta_event", UNSET))

        multiple_endpoint_subscriptions = d.pop(
            "multiple_endpoint_subscriptions", UNSET
        )

        def _parse_ratelimit(
            data: object,
        ) -> DatastoreRateLimitConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ratelimit_type_1 = DatastoreRateLimitConfiguration.from_dict(data)

                return ratelimit_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreRateLimitConfiguration | None | Unset, data)

        ratelimit = _parse_ratelimit(d.pop("ratelimit", UNSET))

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

        def _parse_signature(
            data: object,
        ) -> DatastoreSignatureConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_type_1 = DatastoreSignatureConfiguration.from_dict(data)

                return signature_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreSignatureConfiguration | None | Unset, data)

        signature = _parse_signature(d.pop("signature", UNSET))

        def _parse_ssl(data: object) -> DatastoreSSLConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ssl_type_1 = DatastoreSSLConfiguration.from_dict(data)

                return ssl_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreSSLConfiguration | None | Unset, data)

        ssl = _parse_ssl(d.pop("ssl", UNSET))

        def _parse_strategy(
            data: object,
        ) -> DatastoreStrategyConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                strategy_type_1 = DatastoreStrategyConfiguration.from_dict(data)

                return strategy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreStrategyConfiguration | None | Unset, data)

        strategy = _parse_strategy(d.pop("strategy", UNSET))

        datastore_project_config = cls(
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

        datastore_project_config.additional_properties = d
        return datastore_project_config

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
