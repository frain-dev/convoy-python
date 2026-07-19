from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_pagination_data import DatastorePaginationData


T = TypeVar("T", bound="ModelsPagedResponse")


@_attrs_define
class ModelsPagedResponse:
    """
    Attributes:
        content (Any | Unset):
        pagination (DatastorePaginationData | None | Unset):
    """

    content: Any | Unset = UNSET
    pagination: DatastorePaginationData | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_pagination_data import DatastorePaginationData

        content = self.content

        pagination: dict[str, Any] | None | Unset
        if isinstance(self.pagination, Unset):
            pagination = UNSET
        elif isinstance(self.pagination, DatastorePaginationData):
            pagination = self.pagination.to_dict()
        else:
            pagination = self.pagination

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_pagination_data import DatastorePaginationData

        d = dict(src_dict)
        content = d.pop("content", UNSET)

        def _parse_pagination(data: object) -> DatastorePaginationData | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pagination_type_1 = DatastorePaginationData.from_dict(data)

                return pagination_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastorePaginationData | None | Unset, data)

        pagination = _parse_pagination(d.pop("pagination", UNSET))

        models_paged_response = cls(
            content=content,
            pagination=pagination,
        )

        models_paged_response.additional_properties = d
        return models_paged_response

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
