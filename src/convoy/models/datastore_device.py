from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_device_status import DatastoreDeviceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreDevice")


@_attrs_define
class DatastoreDevice:
    """
    Attributes:
        created_at (str | Unset):
        deleted_at (str | Unset):
        endpoint_id (str | Unset):
        host_name (str | Unset):
        last_seen_at (str | Unset):
        project_id (str | Unset):
        status (DatastoreDeviceStatus | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
    """

    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    host_name: str | Unset = UNSET
    last_seen_at: str | Unset = UNSET
    project_id: str | Unset = UNSET
    status: DatastoreDeviceStatus | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        deleted_at = self.deleted_at

        endpoint_id = self.endpoint_id

        host_name = self.host_name

        last_seen_at = self.last_seen_at

        project_id = self.project_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        uid = self.uid

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if endpoint_id is not UNSET:
            field_dict["endpoint_id"] = endpoint_id
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        endpoint_id = d.pop("endpoint_id", UNSET)

        host_name = d.pop("host_name", UNSET)

        last_seen_at = d.pop("last_seen_at", UNSET)

        project_id = d.pop("project_id", UNSET)

        _status = d.pop("status", UNSET)
        status: DatastoreDeviceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatastoreDeviceStatus(_status)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        datastore_device = cls(
            created_at=created_at,
            deleted_at=deleted_at,
            endpoint_id=endpoint_id,
            host_name=host_name,
            last_seen_at=last_seen_at,
            project_id=project_id,
            status=status,
            uid=uid,
            updated_at=updated_at,
        )

        datastore_device.additional_properties = d
        return datastore_device

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
