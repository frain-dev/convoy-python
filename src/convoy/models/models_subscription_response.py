from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        alert_config (DatastoreAlertConfiguration | None | Unset): subscription config
        created_at (str | Unset):
        deleted_at (None | str | Unset):
        delivery_mode (DatastoreDeliveryMode | Unset):
        device_metadata (DatastoreDevice | None | Unset):
        endpoint_metadata (DatastoreEndpoint | None | Unset):
        filter_config (DatastoreFilterConfiguration | None | Unset):
        function (None | str | Unset):
        name (str | Unset):
        project_id (str | Unset):
        rate_limit_config (DatastoreRateLimitConfiguration | None | Unset):
        retry_config (DatastoreRetryConfiguration | None | Unset):
        source_metadata (DatastoreSource | None | Unset):
        type_ (DatastoreSubscriptionType | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
    """

    alert_config: DatastoreAlertConfiguration | None | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    delivery_mode: DatastoreDeliveryMode | Unset = UNSET
    device_metadata: DatastoreDevice | None | Unset = UNSET
    endpoint_metadata: DatastoreEndpoint | None | Unset = UNSET
    filter_config: DatastoreFilterConfiguration | None | Unset = UNSET
    function: None | str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    rate_limit_config: DatastoreRateLimitConfiguration | None | Unset = UNSET
    retry_config: DatastoreRetryConfiguration | None | Unset = UNSET
    source_metadata: DatastoreSource | None | Unset = UNSET
    type_: DatastoreSubscriptionType | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_alert_configuration import DatastoreAlertConfiguration
        from ..models.datastore_device import DatastoreDevice
        from ..models.datastore_endpoint import DatastoreEndpoint
        from ..models.datastore_filter_configuration import DatastoreFilterConfiguration
        from ..models.datastore_rate_limit_configuration import (
            DatastoreRateLimitConfiguration,
        )
        from ..models.datastore_retry_configuration import DatastoreRetryConfiguration
        from ..models.datastore_source import DatastoreSource

        alert_config: dict[str, Any] | None | Unset
        if isinstance(self.alert_config, Unset):
            alert_config = UNSET
        elif isinstance(self.alert_config, DatastoreAlertConfiguration):
            alert_config = self.alert_config.to_dict()
        else:
            alert_config = self.alert_config

        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        delivery_mode: str | Unset = UNSET
        if not isinstance(self.delivery_mode, Unset):
            delivery_mode = self.delivery_mode.value

        device_metadata: dict[str, Any] | None | Unset
        if isinstance(self.device_metadata, Unset):
            device_metadata = UNSET
        elif isinstance(self.device_metadata, DatastoreDevice):
            device_metadata = self.device_metadata.to_dict()
        else:
            device_metadata = self.device_metadata

        endpoint_metadata: dict[str, Any] | None | Unset
        if isinstance(self.endpoint_metadata, Unset):
            endpoint_metadata = UNSET
        elif isinstance(self.endpoint_metadata, DatastoreEndpoint):
            endpoint_metadata = self.endpoint_metadata.to_dict()
        else:
            endpoint_metadata = self.endpoint_metadata

        filter_config: dict[str, Any] | None | Unset
        if isinstance(self.filter_config, Unset):
            filter_config = UNSET
        elif isinstance(self.filter_config, DatastoreFilterConfiguration):
            filter_config = self.filter_config.to_dict()
        else:
            filter_config = self.filter_config

        function: None | str | Unset
        if isinstance(self.function, Unset):
            function = UNSET
        else:
            function = self.function

        name = self.name

        project_id = self.project_id

        rate_limit_config: dict[str, Any] | None | Unset
        if isinstance(self.rate_limit_config, Unset):
            rate_limit_config = UNSET
        elif isinstance(self.rate_limit_config, DatastoreRateLimitConfiguration):
            rate_limit_config = self.rate_limit_config.to_dict()
        else:
            rate_limit_config = self.rate_limit_config

        retry_config: dict[str, Any] | None | Unset
        if isinstance(self.retry_config, Unset):
            retry_config = UNSET
        elif isinstance(self.retry_config, DatastoreRetryConfiguration):
            retry_config = self.retry_config.to_dict()
        else:
            retry_config = self.retry_config

        source_metadata: dict[str, Any] | None | Unset
        if isinstance(self.source_metadata, Unset):
            source_metadata = UNSET
        elif isinstance(self.source_metadata, DatastoreSource):
            source_metadata = self.source_metadata.to_dict()
        else:
            source_metadata = self.source_metadata

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

        def _parse_alert_config(
            data: object,
        ) -> DatastoreAlertConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_config_type_1 = DatastoreAlertConfiguration.from_dict(data)

                return alert_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreAlertConfiguration | None | Unset, data)

        alert_config = _parse_alert_config(d.pop("alert_config", UNSET))

        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        _delivery_mode = d.pop("delivery_mode", UNSET)
        delivery_mode: DatastoreDeliveryMode | Unset
        if isinstance(_delivery_mode, Unset):
            delivery_mode = UNSET
        else:
            delivery_mode = DatastoreDeliveryMode(_delivery_mode)

        def _parse_device_metadata(data: object) -> DatastoreDevice | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_metadata_type_1 = DatastoreDevice.from_dict(data)

                return device_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreDevice | None | Unset, data)

        device_metadata = _parse_device_metadata(d.pop("device_metadata", UNSET))

        def _parse_endpoint_metadata(data: object) -> DatastoreEndpoint | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                endpoint_metadata_type_1 = DatastoreEndpoint.from_dict(data)

                return endpoint_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreEndpoint | None | Unset, data)

        endpoint_metadata = _parse_endpoint_metadata(d.pop("endpoint_metadata", UNSET))

        def _parse_filter_config(
            data: object,
        ) -> DatastoreFilterConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_config_type_1 = DatastoreFilterConfiguration.from_dict(data)

                return filter_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreFilterConfiguration | None | Unset, data)

        filter_config = _parse_filter_config(d.pop("filter_config", UNSET))

        def _parse_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function = _parse_function(d.pop("function", UNSET))

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        def _parse_rate_limit_config(
            data: object,
        ) -> DatastoreRateLimitConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rate_limit_config_type_1 = DatastoreRateLimitConfiguration.from_dict(
                    data
                )

                return rate_limit_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreRateLimitConfiguration | None | Unset, data)

        rate_limit_config = _parse_rate_limit_config(d.pop("rate_limit_config", UNSET))

        def _parse_retry_config(
            data: object,
        ) -> DatastoreRetryConfiguration | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retry_config_type_1 = DatastoreRetryConfiguration.from_dict(data)

                return retry_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreRetryConfiguration | None | Unset, data)

        retry_config = _parse_retry_config(d.pop("retry_config", UNSET))

        def _parse_source_metadata(data: object) -> DatastoreSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_metadata_type_1 = DatastoreSource.from_dict(data)

                return source_metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreSource | None | Unset, data)

        source_metadata = _parse_source_metadata(d.pop("source_metadata", UNSET))

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
