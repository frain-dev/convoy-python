from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_m import DatastoreM


T = TypeVar("T", bound="ModelsFilterResponse")


@_attrs_define
class ModelsFilterResponse:
    """
    Attributes:
        body (DatastoreM | Unset):
        enabled_at (str | Unset):
        event_type (str | Unset):
        headers (DatastoreM | Unset):
        path (DatastoreM | Unset):
        query (DatastoreM | Unset):
        raw_body (DatastoreM | Unset):
        raw_headers (DatastoreM | Unset):
        raw_path (DatastoreM | Unset):
        raw_query (DatastoreM | Unset):
        subscription_id (str | Unset):
        uid (str | Unset):
    """

    body: DatastoreM | Unset = UNSET
    enabled_at: str | Unset = UNSET
    event_type: str | Unset = UNSET
    headers: DatastoreM | Unset = UNSET
    path: DatastoreM | Unset = UNSET
    query: DatastoreM | Unset = UNSET
    raw_body: DatastoreM | Unset = UNSET
    raw_headers: DatastoreM | Unset = UNSET
    raw_path: DatastoreM | Unset = UNSET
    raw_query: DatastoreM | Unset = UNSET
    subscription_id: str | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        enabled_at = self.enabled_at

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

        raw_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_body, Unset):
            raw_body = self.raw_body.to_dict()

        raw_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_headers, Unset):
            raw_headers = self.raw_headers.to_dict()

        raw_path: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_path, Unset):
            raw_path = self.raw_path.to_dict()

        raw_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw_query, Unset):
            raw_query = self.raw_query.to_dict()

        subscription_id = self.subscription_id

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if raw_body is not UNSET:
            field_dict["raw_body"] = raw_body
        if raw_headers is not UNSET:
            field_dict["raw_headers"] = raw_headers
        if raw_path is not UNSET:
            field_dict["raw_path"] = raw_path
        if raw_query is not UNSET:
            field_dict["raw_query"] = raw_query
        if subscription_id is not UNSET:
            field_dict["subscription_id"] = subscription_id
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_m import DatastoreM

        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: DatastoreM | Unset
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = DatastoreM.from_dict(_body)

        enabled_at = d.pop("enabled_at", UNSET)

        event_type = d.pop("event_type", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: DatastoreM | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = DatastoreM.from_dict(_headers)

        _path = d.pop("path", UNSET)
        path: DatastoreM | Unset
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = DatastoreM.from_dict(_path)

        _query = d.pop("query", UNSET)
        query: DatastoreM | Unset
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = DatastoreM.from_dict(_query)

        _raw_body = d.pop("raw_body", UNSET)
        raw_body: DatastoreM | Unset
        if isinstance(_raw_body, Unset):
            raw_body = UNSET
        else:
            raw_body = DatastoreM.from_dict(_raw_body)

        _raw_headers = d.pop("raw_headers", UNSET)
        raw_headers: DatastoreM | Unset
        if isinstance(_raw_headers, Unset):
            raw_headers = UNSET
        else:
            raw_headers = DatastoreM.from_dict(_raw_headers)

        _raw_path = d.pop("raw_path", UNSET)
        raw_path: DatastoreM | Unset
        if isinstance(_raw_path, Unset):
            raw_path = UNSET
        else:
            raw_path = DatastoreM.from_dict(_raw_path)

        _raw_query = d.pop("raw_query", UNSET)
        raw_query: DatastoreM | Unset
        if isinstance(_raw_query, Unset):
            raw_query = UNSET
        else:
            raw_query = DatastoreM.from_dict(_raw_query)

        subscription_id = d.pop("subscription_id", UNSET)

        uid = d.pop("uid", UNSET)

        models_filter_response = cls(
            body=body,
            enabled_at=enabled_at,
            event_type=event_type,
            headers=headers,
            path=path,
            query=query,
            raw_body=raw_body,
            raw_headers=raw_headers,
            raw_path=raw_path,
            raw_query=raw_query,
            subscription_id=subscription_id,
            uid=uid,
        )

        models_filter_response.additional_properties = d
        return models_filter_response

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
