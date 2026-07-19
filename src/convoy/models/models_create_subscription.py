from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_delivery_mode import DatastoreDeliveryMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_alert_configuration import ModelsAlertConfiguration
    from ..models.models_filter_configuration import ModelsFilterConfiguration
    from ..models.models_rate_limit_configuration import ModelsRateLimitConfiguration


T = TypeVar("T", bound="ModelsCreateSubscription")


@_attrs_define
class ModelsCreateSubscription:
    """
    Attributes:
        alert_config (ModelsAlertConfiguration | Unset):
        app_id (str | Unset): Deprecated but necessary for backward compatibility
        delivery_mode (DatastoreDeliveryMode | Unset):
        endpoint_id (str | Unset): Destination endpoint ID
        filter_config (ModelsFilterConfiguration | Unset):
        function (str | Unset): Convoy supports mutating your request payload using a js function. Use this field
            to specify a `transform` function for this purpose. See this[https://docs.getconvoy.io/product-
            manual/subscriptions#functions] for more
        name (str | Unset): Subscription Nme
        rate_limit_config (ModelsRateLimitConfiguration | Unset):
        source_id (str | Unset): Source Id
    """

    alert_config: ModelsAlertConfiguration | Unset = UNSET
    app_id: str | Unset = UNSET
    delivery_mode: DatastoreDeliveryMode | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    filter_config: ModelsFilterConfiguration | Unset = UNSET
    function: str | Unset = UNSET
    name: str | Unset = UNSET
    rate_limit_config: ModelsRateLimitConfiguration | Unset = UNSET
    source_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_config, Unset):
            alert_config = self.alert_config.to_dict()

        app_id = self.app_id

        delivery_mode: str | Unset = UNSET
        if not isinstance(self.delivery_mode, Unset):
            delivery_mode = self.delivery_mode.value

        endpoint_id = self.endpoint_id

        filter_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_config, Unset):
            filter_config = self.filter_config.to_dict()

        function = self.function

        name = self.name

        rate_limit_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit_config, Unset):
            rate_limit_config = self.rate_limit_config.to_dict()

        source_id = self.source_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_config is not UNSET:
            field_dict["alert_config"] = alert_config
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if delivery_mode is not UNSET:
            field_dict["delivery_mode"] = delivery_mode
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if filter_config is not UNSET:
            field_dict["filter_config"] = filter_config
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name
        if rate_limit_config is not UNSET:
            field_dict["rate_limit_config"] = rate_limit_config
        if source_id is not UNSET:
            field_dict["source_id"] = source_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_alert_configuration import ModelsAlertConfiguration
        from ..models.models_filter_configuration import ModelsFilterConfiguration
        from ..models.models_rate_limit_configuration import (
            ModelsRateLimitConfiguration,
        )

        d = dict(src_dict)
        _alert_config = d.pop("alert_config", UNSET)
        alert_config: ModelsAlertConfiguration | Unset
        if isinstance(_alert_config, Unset):
            alert_config = UNSET
        else:
            alert_config = ModelsAlertConfiguration.from_dict(_alert_config)

        app_id = d.pop("app_id", UNSET)

        _delivery_mode = d.pop("delivery_mode", UNSET)
        delivery_mode: DatastoreDeliveryMode | Unset
        if isinstance(_delivery_mode, Unset):
            delivery_mode = UNSET
        else:
            delivery_mode = DatastoreDeliveryMode(_delivery_mode)

        endpoint_id = d.pop("endpoint_id", UNSET)

        _filter_config = d.pop("filter_config", UNSET)
        filter_config: ModelsFilterConfiguration | Unset
        if isinstance(_filter_config, Unset):
            filter_config = UNSET
        else:
            filter_config = ModelsFilterConfiguration.from_dict(_filter_config)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        _rate_limit_config = d.pop("rate_limit_config", UNSET)
        rate_limit_config: ModelsRateLimitConfiguration | Unset
        if isinstance(_rate_limit_config, Unset):
            rate_limit_config = UNSET
        else:
            rate_limit_config = ModelsRateLimitConfiguration.from_dict(
                _rate_limit_config
            )

        source_id = d.pop("source_id", UNSET)

        models_create_subscription = cls(
            alert_config=alert_config,
            app_id=app_id,
            delivery_mode=delivery_mode,
            endpoint_id=endpoint_id,
            filter_config=filter_config,
            function=function,
            name=name,
            rate_limit_config=rate_limit_config,
            source_id=source_id,
        )

        models_create_subscription.additional_properties = d
        return models_create_subscription

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
