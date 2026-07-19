from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_create_event_custom_headers import (
        ModelsCreateEventCustomHeaders,
    )
    from ..models.models_create_event_data import ModelsCreateEventData


T = TypeVar("T", bound="ModelsCreateEvent")


@_attrs_define
class ModelsCreateEvent:
    """
    Attributes:
        app_id (str | Unset): Deprecated but necessary for backward compatibility.
        custom_headers (ModelsCreateEventCustomHeaders | Unset): Specifies custom headers you want convoy to add when
            the event is dispatched to your endpoint
        data (ModelsCreateEventData | Unset): Data is an arbitrary JSON value that gets sent as the body of the
            webhook to the endpoints
        endpoint_id (str | Unset): Specifies the endpoint to send this event to.
        event_type (str | Unset): Event Type is used for filtering and debugging e.g invoice.paid
        idempotency_key (str | Unset): Specify a key for event deduplication
    """

    app_id: str | Unset = UNSET
    custom_headers: ModelsCreateEventCustomHeaders | Unset = UNSET
    data: ModelsCreateEventData | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        custom_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_headers, Unset):
            custom_headers = self.custom_headers.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        endpoint_id = self.endpoint_id

        event_type = self.event_type

        idempotency_key = self.idempotency_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if custom_headers is not UNSET:
            field_dict["custom_headers"] = custom_headers
        if data is not UNSET:
            field_dict["data"] = data
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_create_event_custom_headers import (
            ModelsCreateEventCustomHeaders,
        )
        from ..models.models_create_event_data import ModelsCreateEventData

        d = dict(src_dict)
        app_id = d.pop("app_id", UNSET)

        _custom_headers = d.pop("custom_headers", UNSET)
        custom_headers: ModelsCreateEventCustomHeaders | Unset
        if isinstance(_custom_headers, Unset):
            custom_headers = UNSET
        else:
            custom_headers = ModelsCreateEventCustomHeaders.from_dict(_custom_headers)

        _data = d.pop("data", UNSET)
        data: ModelsCreateEventData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelsCreateEventData.from_dict(_data)

        endpoint_id = d.pop("endpoint_id", UNSET)

        event_type = d.pop("event_type", UNSET)

        idempotency_key = d.pop("idempotency_key", UNSET)

        models_create_event = cls(
            app_id=app_id,
            custom_headers=custom_headers,
            data=data,
            endpoint_id=endpoint_id,
            event_type=event_type,
            idempotency_key=idempotency_key,
        )

        models_create_event.additional_properties = d
        return models_create_event

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
