from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_delivery_attempt import DatastoreDeliveryAttempt
    from ..models.get_delivery_attempts_response_200_data_type_1 import (
        GetDeliveryAttemptsResponse200DataType1,
    )


T = TypeVar("T", bound="GetDeliveryAttemptsResponse200")


@_attrs_define
class GetDeliveryAttemptsResponse200:
    """
    Attributes:
        message (str | Unset):
        status (bool | Unset):
        data (GetDeliveryAttemptsResponse200DataType1 | list[DatastoreDeliveryAttempt] | Unset):
    """

    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    data: (
        GetDeliveryAttemptsResponse200DataType1 | list[DatastoreDeliveryAttempt] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status

        data: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_delivery_attempt import DatastoreDeliveryAttempt
        from ..models.get_delivery_attempts_response_200_data_type_1 import (
            GetDeliveryAttemptsResponse200DataType1,
        )

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        def _parse_data(
            data: object,
        ) -> (
            GetDeliveryAttemptsResponse200DataType1
            | list[DatastoreDeliveryAttempt]
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = DatastoreDeliveryAttempt.from_dict(
                        data_type_0_item_data
                    )

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = GetDeliveryAttemptsResponse200DataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        get_delivery_attempts_response_200 = cls(
            message=message,
            status=status,
            data=data,
        )

        get_delivery_attempts_response_200.additional_properties = d
        return get_delivery_attempts_response_200

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
