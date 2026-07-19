from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_delivery_mode import DatastoreDeliveryMode
from ..models.datastore_subscription_type import DatastoreSubscriptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_alert_configuration import DatastoreAlertConfiguration
    from ..models.datastore_device import DatastoreDevice
    from ..models.datastore_endpoint import DatastoreEndpoint
    from ..models.datastore_filter_configuration import DatastoreFilterConfiguration
    from ..models.datastore_rate_limit_configuration import (
        DatastoreRateLimitConfiguration,
    )
    from ..models.datastore_retry_configuration import DatastoreRetryConfiguration
    from ..models.datastore_source import DatastoreSource


T = TypeVar("T", bound="ModelsSubscriptionResponse")


@_attrs_define
class ModelsSubscriptionResponse:
    """
    Attributes:
        alert_config (DatastoreAlertConfiguration | Unset):
        created_at (str | Unset):
        deleted_at (str | Unset):
        delivery_mode (DatastoreDeliveryMode | Unset):
        device_metadata (DatastoreDevice | Unset):
        endpoint_metadata (DatastoreEndpoint | Unset):
        filter_config (DatastoreFilterConfiguration | Unset):
        function (str | Unset):
        name (str | Unset):
        project_id (str | Unset):
        rate_limit_config (DatastoreRateLimitConfiguration | Unset):
        retry_config (DatastoreRetryConfiguration | Unset):
        source_metadata (DatastoreSource | Unset):
        type_ (DatastoreSubscriptionType | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
    """

    alert_config: DatastoreAlertConfiguration | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    delivery_mode: DatastoreDeliveryMode | Unset = UNSET
    device_metadata: DatastoreDevice | Unset = UNSET
    endpoint_metadata: DatastoreEndpoint | Unset = UNSET
    filter_config: DatastoreFilterConfiguration | Unset = UNSET
    function: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    rate_limit_config: DatastoreRateLimitConfiguration | Unset = UNSET
    retry_config: DatastoreRetryConfiguration | Unset = UNSET
    source_metadata: DatastoreSource | Unset = UNSET
    type_: DatastoreSubscriptionType | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_config, Unset):
            alert_config = self.alert_config.to_dict()

        created_at = self.created_at

        deleted_at = self.deleted_at

        delivery_mode: str | Unset = UNSET
        if not isinstance(self.delivery_mode, Unset):
            delivery_mode = self.delivery_mode.value

        device_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_metadata, Unset):
            device_metadata = self.device_metadata.to_dict()

        endpoint_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.endpoint_metadata, Unset):
            endpoint_metadata = self.endpoint_metadata.to_dict()

        filter_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_config, Unset):
            filter_config = self.filter_config.to_dict()

        function = self.function

        name = self.name

        project_id = self.project_id

        rate_limit_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit_config, Unset):
            rate_limit_config = self.rate_limit_config.to_dict()

        retry_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_config, Unset):
            retry_config = self.retry_config.to_dict()

        source_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_metadata, Unset):
            source_metadata = self.source_metadata.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_config is not UNSET:
            field_dict["alert_config"] = alert_config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if delivery_mode is not UNSET:
            field_dict["delivery_mode"] = delivery_mode
        if device_metadata is not UNSET:
            field_dict["device_metadata"] = device_metadata
        if endpoint_metadata is not UNSET:
            field_dict["endpoint_metadata"] = endpoint_metadata
        if filter_config is not UNSET:
            field_dict["filter_config"] = filter_config
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if rate_limit_config is not UNSET:
            field_dict["rate_limit_config"] = rate_limit_config
        if retry_config is not UNSET:
            field_dict["retry_config"] = retry_config
        if source_metadata is not UNSET:
            field_dict["source_metadata"] = source_metadata
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_alert_configuration import DatastoreAlertConfiguration
        from ..models.datastore_device import DatastoreDevice
        from ..models.datastore_endpoint import DatastoreEndpoint
        from ..models.datastore_filter_configuration import DatastoreFilterConfiguration
        from ..models.datastore_rate_limit_configuration import (
            DatastoreRateLimitConfiguration,
        )
        from ..models.datastore_retry_configuration import DatastoreRetryConfiguration
        from ..models.datastore_source import DatastoreSource

        d = dict(src_dict)
        _alert_config = d.pop("alert_config", UNSET)
        alert_config: DatastoreAlertConfiguration | Unset
        if isinstance(_alert_config, Unset):
            alert_config = UNSET
        else:
            alert_config = DatastoreAlertConfiguration.from_dict(_alert_config)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        _delivery_mode = d.pop("delivery_mode", UNSET)
        delivery_mode: DatastoreDeliveryMode | Unset
        if isinstance(_delivery_mode, Unset):
            delivery_mode = UNSET
        else:
            delivery_mode = DatastoreDeliveryMode(_delivery_mode)

        _device_metadata = d.pop("device_metadata", UNSET)
        device_metadata: DatastoreDevice | Unset
        if isinstance(_device_metadata, Unset):
            device_metadata = UNSET
        else:
            device_metadata = DatastoreDevice.from_dict(_device_metadata)

        _endpoint_metadata = d.pop("endpoint_metadata", UNSET)
        endpoint_metadata: DatastoreEndpoint | Unset
        if isinstance(_endpoint_metadata, Unset):
            endpoint_metadata = UNSET
        else:
            endpoint_metadata = DatastoreEndpoint.from_dict(_endpoint_metadata)

        _filter_config = d.pop("filter_config", UNSET)
        filter_config: DatastoreFilterConfiguration | Unset
        if isinstance(_filter_config, Unset):
            filter_config = UNSET
        else:
            filter_config = DatastoreFilterConfiguration.from_dict(_filter_config)

        function = d.pop("function", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        _rate_limit_config = d.pop("rate_limit_config", UNSET)
        rate_limit_config: DatastoreRateLimitConfiguration | Unset
        if isinstance(_rate_limit_config, Unset):
            rate_limit_config = UNSET
        else:
            rate_limit_config = DatastoreRateLimitConfiguration.from_dict(
                _rate_limit_config
            )

        _retry_config = d.pop("retry_config", UNSET)
        retry_config: DatastoreRetryConfiguration | Unset
        if isinstance(_retry_config, Unset):
            retry_config = UNSET
        else:
            retry_config = DatastoreRetryConfiguration.from_dict(_retry_config)

        _source_metadata = d.pop("source_metadata", UNSET)
        source_metadata: DatastoreSource | Unset
        if isinstance(_source_metadata, Unset):
            source_metadata = UNSET
        else:
            source_metadata = DatastoreSource.from_dict(_source_metadata)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreSubscriptionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreSubscriptionType(_type_)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        models_subscription_response = cls(
            alert_config=alert_config,
            created_at=created_at,
            deleted_at=deleted_at,
            delivery_mode=delivery_mode,
            device_metadata=device_metadata,
            endpoint_metadata=endpoint_metadata,
            filter_config=filter_config,
            function=function,
            name=name,
            project_id=project_id,
            rate_limit_config=rate_limit_config,
            retry_config=retry_config,
            source_metadata=source_metadata,
            type_=type_,
            uid=uid,
            updated_at=updated_at,
        )

        models_subscription_response.additional_properties = d
        return models_subscription_response

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
