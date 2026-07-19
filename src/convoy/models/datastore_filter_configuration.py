from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_filter_schema import DatastoreFilterSchema


T = TypeVar("T", bound="DatastoreFilterConfiguration")


@_attrs_define
class DatastoreFilterConfiguration:
    """
    Attributes:
        event_types (list[str] | Unset):
        filter_ (DatastoreFilterSchema | Unset):
    """

    event_types: list[str] | Unset = UNSET
    filter_: DatastoreFilterSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_filter_schema import DatastoreFilterSchema

        d = dict(src_dict)
        event_types = cast(list[str], d.pop("event_types", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: DatastoreFilterSchema | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = DatastoreFilterSchema.from_dict(_filter_)

        datastore_filter_configuration = cls(
            event_types=event_types,
            filter_=filter_,
        )

        datastore_filter_configuration.additional_properties = d
        return datastore_filter_configuration

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
