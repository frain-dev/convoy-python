from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastorePaginationData")


@_attrs_define
class DatastorePaginationData:
    """
    Attributes:
        has_next_page (bool | Unset):
        has_prev_page (bool | Unset):
        next_page_cursor (str | Unset):
        per_page (int | Unset):
        prev_page_cursor (str | Unset):
        total (int | Unset):
    """

    has_next_page: bool | Unset = UNSET
    has_prev_page: bool | Unset = UNSET
    next_page_cursor: str | Unset = UNSET
    per_page: int | Unset = UNSET
    prev_page_cursor: str | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next_page = self.has_next_page

        has_prev_page = self.has_prev_page

        next_page_cursor = self.next_page_cursor

        per_page = self.per_page

        prev_page_cursor = self.prev_page_cursor

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_next_page is not UNSET:
            field_dict["has_next_page"] = has_next_page
        if has_prev_page is not UNSET:
            field_dict["has_prev_page"] = has_prev_page
        if next_page_cursor is not UNSET:
            field_dict["next_page_cursor"] = next_page_cursor
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_page_cursor is not UNSET:
            field_dict["prev_page_cursor"] = prev_page_cursor
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_next_page = d.pop("has_next_page", UNSET)

        has_prev_page = d.pop("has_prev_page", UNSET)

        next_page_cursor = d.pop("next_page_cursor", UNSET)

        per_page = d.pop("per_page", UNSET)

        prev_page_cursor = d.pop("prev_page_cursor", UNSET)

        total = d.pop("total", UNSET)

        datastore_pagination_data = cls(
            has_next_page=has_next_page,
            has_prev_page=has_prev_page,
            next_page_cursor=next_page_cursor,
            per_page=per_page,
            prev_page_cursor=prev_page_cursor,
            total=total,
        )

        datastore_pagination_data.additional_properties = d
        return datastore_pagination_data

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
