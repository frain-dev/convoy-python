from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_broadcast_event_custom_headers import (
        ModelsBroadcastEventCustomHeaders,
    )
    from ..models.models_broadcast_event_data import ModelsBroadcastEventData


T = TypeVar("T", bound="ModelsBroadcastEvent")


@_attrs_define
class ModelsBroadcastEvent:
    """
    Attributes:
        acknowledged_at (str | Unset):
        custom_headers (ModelsBroadcastEventCustomHeaders | Unset): Specifies custom headers you want convoy to add when
            the event is dispatched to your endpoint
        data (ModelsBroadcastEventData | Unset): Data is an arbitrary JSON value that gets sent as the body of the
            webhook to the endpoints
        event_type (str | Unset): Event Type is used for filtering and debugging e.g invoice.paid
        idempotency_key (str | Unset): Specify a key for event deduplication
    """

    acknowledged_at: str | Unset = UNSET
    custom_headers: ModelsBroadcastEventCustomHeaders | Unset = UNSET
    data: ModelsBroadcastEventData | Unset = UNSET
    event_type: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged_at = self.acknowledged_at

        custom_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_headers, Unset):
            custom_headers = self.custom_headers.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        event_type = self.event_type

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if custom_headers is not UNSET:
            field_dict["custom_headers"] = custom_headers
        if data is not UNSET:
            field_dict["data"] = data
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_broadcast_event_custom_headers import (
            ModelsBroadcastEventCustomHeaders,
        )
        from ..models.models_broadcast_event_data import ModelsBroadcastEventData

        d = dict(src_dict)
        acknowledged_at = d.pop("acknowledged_at", UNSET)

        _custom_headers = d.pop("custom_headers", UNSET)
        custom_headers: ModelsBroadcastEventCustomHeaders | Unset
        if isinstance(_custom_headers, Unset):
            custom_headers = UNSET
        else:
            custom_headers = ModelsBroadcastEventCustomHeaders.from_dict(
                _custom_headers
            )

        _data = d.pop("data", UNSET)
        data: ModelsBroadcastEventData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelsBroadcastEventData.from_dict(_data)

        event_type = d.pop("event_type", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        models_broadcast_event = cls(
            acknowledged_at=acknowledged_at,
            custom_headers=custom_headers,
            data=data,
            event_type=event_type,
            idempotency_key=idempotency_key,
        )

        models_broadcast_event.additional_properties = d
        return models_broadcast_event

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
