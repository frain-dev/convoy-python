from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.datastore_delivery_attempt import DatastoreDeliveryAttempt


T = TypeVar("T", bound="GetDeliveryAttemptsResponse200DataType1")


@_attrs_define
class GetDeliveryAttemptsResponse200DataType1:
    """
    Attributes:
        content (list[DatastoreDeliveryAttempt]):
        next_cursor (str): Pass as before to fetch older attempts. Empty on the last page.
    """

    content: list[DatastoreDeliveryAttempt]
    next_cursor: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = []
        for content_item_data in self.content:
            content_item = content_item_data.to_dict()
            content.append(content_item)

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_delivery_attempt import DatastoreDeliveryAttempt

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:
            content_item = DatastoreDeliveryAttempt.from_dict(content_item_data)

            content.append(content_item)

        next_cursor = d.pop("next_cursor")

        get_delivery_attempts_response_200_data_type_1 = cls(
            content=content,
            next_cursor=next_cursor,
        )

        get_delivery_attempts_response_200_data_type_1.additional_properties = d
        return get_delivery_attempts_response_200_data_type_1

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
