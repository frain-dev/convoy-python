from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_http_header import DatastoreHttpHeader


T = TypeVar("T", bound="DatastoreDeliveryAttempt")


@_attrs_define
class DatastoreDeliveryAttempt:
    """
    Attributes:
        api_version (str | Unset):
        created_at (str | Unset):
        deleted_at (str | Unset):
        endpoint_id (str | Unset):
        error (str | Unset):
        http_status (str | Unset):
        ip_address (str | Unset):
        method (str | Unset):
        msg_id (str | Unset):
        project_id (str | Unset):
        request_http_header (DatastoreHttpHeader | Unset):
        requested_at (str | Unset):
        responded_at (str | Unset):
        response_data (str | Unset):
        response_http_header (DatastoreHttpHeader | Unset):
        status (bool | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    api_version: str | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    error: str | Unset = UNSET
    http_status: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    method: str | Unset = UNSET
    msg_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    request_http_header: DatastoreHttpHeader | Unset = UNSET
    requested_at: str | Unset = UNSET
    responded_at: str | Unset = UNSET
    response_data: str | Unset = UNSET
    response_http_header: DatastoreHttpHeader | Unset = UNSET
    status: bool | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_version = self.api_version

        created_at = self.created_at

        deleted_at = self.deleted_at

        endpoint_id = self.endpoint_id

        error = self.error

        http_status = self.http_status

        ip_address = self.ip_address

        method = self.method

        msg_id = self.msg_id

        project_id = self.project_id

        request_http_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_http_header, Unset):
            request_http_header = self.request_http_header.to_dict()

        requested_at = self.requested_at

        responded_at = self.responded_at

        response_data = self.response_data

        response_http_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_http_header, Unset):
            response_http_header = self.response_http_header.to_dict()

        status = self.status

        uid = self.uid

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_version is not UNSET:
            field_dict["api_version"] = api_version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if error is not UNSET:
            field_dict["error"] = error
        if http_status is not UNSET:
            field_dict["http_status"] = http_status
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if method is not UNSET:
            field_dict["method"] = method
        if msg_id is not UNSET:
            field_dict["msg_id"] = msg_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if request_http_header is not UNSET:
            field_dict["request_http_header"] = request_http_header
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at
        if responded_at is not UNSET:
            field_dict["responded_at"] = responded_at
        if response_data is not UNSET:
            field_dict["response_data"] = response_data
        if response_http_header is not UNSET:
            field_dict["response_http_header"] = response_http_header
        if status is not UNSET:
            field_dict["status"] = status
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_http_header import DatastoreHttpHeader

        d = dict(src_dict)
        api_version = d.pop("api_version", UNSET)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        endpoint_id = d.pop("endpoint_id", UNSET)

        error = d.pop("error", UNSET)

        http_status = d.pop("http_status", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        method = d.pop("method", UNSET)

        msg_id = d.pop("msg_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        _request_http_header = d.pop("request_http_header", UNSET)
        request_http_header: DatastoreHttpHeader | Unset
        if isinstance(_request_http_header, Unset):
            request_http_header = UNSET
        else:
            request_http_header = DatastoreHttpHeader.from_dict(_request_http_header)

        requested_at = d.pop("requested_at", UNSET)

        responded_at = d.pop("responded_at", UNSET)

        response_data = d.pop("response_data", UNSET)

        _response_http_header = d.pop("response_http_header", UNSET)
        response_http_header: DatastoreHttpHeader | Unset
        if isinstance(_response_http_header, Unset):
            response_http_header = UNSET
        else:
            response_http_header = DatastoreHttpHeader.from_dict(_response_http_header)

        status = d.pop("status", UNSET)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        datastore_delivery_attempt = cls(
            api_version=api_version,
            created_at=created_at,
            deleted_at=deleted_at,
            endpoint_id=endpoint_id,
            error=error,
            http_status=http_status,
            ip_address=ip_address,
            method=method,
            msg_id=msg_id,
            project_id=project_id,
            request_http_header=request_http_header,
            requested_at=requested_at,
            responded_at=responded_at,
            response_data=response_data,
            response_http_header=response_http_header,
            status=status,
            uid=uid,
            updated_at=updated_at,
            url=url,
        )

        datastore_delivery_attempt.additional_properties = d
        return datastore_delivery_attempt

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
