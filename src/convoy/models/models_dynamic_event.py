from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_dynamic_event_custom_headers_type_0 import (
        ModelsDynamicEventCustomHeadersType0,
    )
    from ..models.models_dynamic_event_data_type_0 import ModelsDynamicEventDataType0


T = TypeVar("T", bound="ModelsDynamicEvent")


@_attrs_define
class ModelsDynamicEvent:
    """
    Attributes:
        custom_headers (ModelsDynamicEventCustomHeadersType0 | None | Unset): Specifies custom headers you want convoy
            to add when the event is dispatched to your endpoint
        data (ModelsDynamicEventDataType0 | None | Unset): Data is an arbitrary JSON value that gets sent as the body of
            the
            webhook to the endpoints
        event_type (str | Unset): Event Type is used for filtering and debugging e.g invoice.paid
        event_types (list[str] | Unset): A list of event types for the subscription filter config
        idempotency_key (str | Unset): Specify a key for event deduplication
        secret (str | Unset): Endpoint's webhook secret. If not provided, Convoy autogenerates one for the endpoint.
        url (str | Unset): URL is the endpoint's URL prefixed with https. non-https urls are currently
            not supported.
    """

    custom_headers: ModelsDynamicEventCustomHeadersType0 | None | Unset = UNSET
    data: ModelsDynamicEventDataType0 | None | Unset = UNSET
    event_type: str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    secret: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.models_dynamic_event_custom_headers_type_0 import (
            ModelsDynamicEventCustomHeadersType0,
        )
        from ..models.models_dynamic_event_data_type_0 import (
            ModelsDynamicEventDataType0,
        )

        custom_headers: dict[str, Any] | None | Unset
        if isinstance(self.custom_headers, Unset):
            custom_headers = UNSET
        elif isinstance(self.custom_headers, ModelsDynamicEventCustomHeadersType0):
            custom_headers = self.custom_headers.to_dict()
        else:
            custom_headers = self.custom_headers

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, ModelsDynamicEventDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        event_type = self.event_type

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        idempotency_key = self.idempotency_key

        secret = self.secret

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_headers is not UNSET:
            field_dict["custom_headers"] = custom_headers
        if data is not UNSET:
            field_dict["data"] = data
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if secret is not UNSET:
            field_dict["secret"] = secret
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_dynamic_event_custom_headers_type_0 import (
            ModelsDynamicEventCustomHeadersType0,
        )
        from ..models.models_dynamic_event_data_type_0 import (
            ModelsDynamicEventDataType0,
        )

        d = dict(src_dict)

        def _parse_custom_headers(
            data: object,
        ) -> ModelsDynamicEventCustomHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_headers_type_0 = ModelsDynamicEventCustomHeadersType0.from_dict(
                    data
                )

                return custom_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsDynamicEventCustomHeadersType0 | None | Unset, data)

        custom_headers = _parse_custom_headers(d.pop("custom_headers", UNSET))

        def _parse_data(data: object) -> ModelsDynamicEventDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ModelsDynamicEventDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsDynamicEventDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        event_type = d.pop("event_type", UNSET)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        idempotency_key = d.pop("idempotency_key", UNSET)

        secret = d.pop("secret", UNSET)

        url = d.pop("url", UNSET)

        models_dynamic_event = cls(
            custom_headers=custom_headers,
            data=data,
            event_type=event_type,
            event_types=event_types,
            idempotency_key=idempotency_key,
            secret=secret,
            url=url,
        )

        models_dynamic_event.additional_properties = d
        return models_dynamic_event

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
