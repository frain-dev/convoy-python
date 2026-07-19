from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_bulk_update_filter_request_body import (
        ModelsBulkUpdateFilterRequestBody,
    )
    from ..models.models_bulk_update_filter_request_headers import (
        ModelsBulkUpdateFilterRequestHeaders,
    )
    from ..models.models_bulk_update_filter_request_path import (
        ModelsBulkUpdateFilterRequestPath,
    )
    from ..models.models_bulk_update_filter_request_query import (
        ModelsBulkUpdateFilterRequestQuery,
    )
    from ..models.models_optional_time import ModelsOptionalTime


T = TypeVar("T", bound="ModelsBulkUpdateFilterRequest")


@_attrs_define
class ModelsBulkUpdateFilterRequest:
    """
    Attributes:
        uid (str):
        body (ModelsBulkUpdateFilterRequestBody | Unset):
        enabled_at (ModelsOptionalTime | Unset):
        event_type (str | Unset):
        headers (ModelsBulkUpdateFilterRequestHeaders | Unset):
        path (ModelsBulkUpdateFilterRequestPath | Unset):
        query (ModelsBulkUpdateFilterRequestQuery | Unset):
    """

    uid: str
    body: ModelsBulkUpdateFilterRequestBody | Unset = UNSET
    enabled_at: ModelsOptionalTime | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: ModelsBulkUpdateFilterRequestHeaders | Unset = UNSET
    path: ModelsBulkUpdateFilterRequestPath | Unset = UNSET
    query: ModelsBulkUpdateFilterRequestQuery | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uid = self.uid

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        enabled_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enabled_at, Unset):
            enabled_at = self.enabled_at.to_dict()

        event_type = self.event_type

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uid": uid,
            }
        )
        if body is not UNSET:
            field_dict["body"] = body
        if enabled_at is not UNSET:
            field_dict["enabled_at"] = enabled_at
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bulk_update_filter_request_body import (
            ModelsBulkUpdateFilterRequestBody,
        )
        from ..models.models_bulk_update_filter_request_headers import (
            ModelsBulkUpdateFilterRequestHeaders,
        )
        from ..models.models_bulk_update_filter_request_path import (
            ModelsBulkUpdateFilterRequestPath,
        )
        from ..models.models_bulk_update_filter_request_query import (
            ModelsBulkUpdateFilterRequestQuery,
        )
        from ..models.models_optional_time import ModelsOptionalTime

        d = dict(src_dict)
        uid = d.pop("uid")

        _body = d.pop("body", UNSET)
        body: ModelsBulkUpdateFilterRequestBody | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = ModelsBulkUpdateFilterRequestBody.from_dict(_body)

        _enabled_at = d.pop("enabled_at", UNSET)
        enabled_at: ModelsOptionalTime | Unset
        if isinstance(_enabled_at, Unset):
            enabled_at = UNSET
        else:
            enabled_at = ModelsOptionalTime.from_dict(_enabled_at)

        event_type = d.pop("event_type", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ModelsBulkUpdateFilterRequestHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = ModelsBulkUpdateFilterRequestHeaders.from_dict(_headers)

        _path = d.pop("path", UNSET)
        path: ModelsBulkUpdateFilterRequestPath | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = ModelsBulkUpdateFilterRequestPath.from_dict(_path)

        _query = d.pop("query", UNSET)
        query: ModelsBulkUpdateFilterRequestQuery | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = ModelsBulkUpdateFilterRequestQuery.from_dict(_query)

        models_bulk_update_filter_request = cls(
            uid=uid,
            body=body,
            enabled_at=enabled_at,
            event_type=event_type,
            headers=headers,
            path=path,
            query=query,
        )

        models_bulk_update_filter_request.additional_properties = d
        return models_bulk_update_filter_request

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
