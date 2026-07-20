from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_portal_auth_type import DatastorePortalAuthType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_endpoint import DatastoreEndpoint


T = TypeVar("T", bound="DatastorePortalLinkResponse")


@_attrs_define
class DatastorePortalLinkResponse:
    """
    Attributes:
        auth_key (str | Unset):
        auth_type (DatastorePortalAuthType | Unset):
        can_manage_endpoint (bool | Unset):
        created_at (str | Unset):
        deleted_at (None | str | Unset):
        endpoint_count (int | Unset):
        endpoints (list[str] | Unset):
        endpoints_metadata (list[DatastoreEndpoint | None] | Unset):
        name (str | Unset):
        owner_id (str | Unset):
        project_id (str | Unset):
        token (str | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
    """

    auth_key: str | Unset = UNSET
    auth_type: DatastorePortalAuthType | Unset = UNSET
    can_manage_endpoint: bool | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    endpoint_count: int | Unset = UNSET
    endpoints: list[str] | Unset = UNSET
    endpoints_metadata: list[DatastoreEndpoint | None] | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    project_id: str | Unset = UNSET
    token: str | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_endpoint import DatastoreEndpoint

        auth_key = self.auth_key

        auth_type: str | Unset = UNSET
        if not isinstance(self.auth_type, Unset):
            auth_type = self.auth_type.value

        can_manage_endpoint = self.can_manage_endpoint

        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        endpoint_count = self.endpoint_count

        endpoints: list[str] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints

        endpoints_metadata: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.endpoints_metadata, Unset):
            endpoints_metadata = []
            for endpoints_metadata_item_data in self.endpoints_metadata:
                endpoints_metadata_item: dict[str, Any] | None
                if isinstance(endpoints_metadata_item_data, DatastoreEndpoint):
                    endpoints_metadata_item = endpoints_metadata_item_data.to_dict()
                else:
                    endpoints_metadata_item = endpoints_metadata_item_data
                endpoints_metadata.append(endpoints_metadata_item)

        name = self.name

        owner_id = self.owner_id

        project_id = self.project_id

        token = self.token

        uid = self.uid

        updated_at = self.updated_at

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_key is not UNSET:
            field_dict["auth_key"] = auth_key
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if can_manage_endpoint is not UNSET:
            field_dict["can_manage_endpoint"] = can_manage_endpoint
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if endpoint_count is not UNSET:
            field_dict["endpoint_count"] = endpoint_count
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if endpoints_metadata is not UNSET:
            field_dict["endpoints_metadata"] = endpoints_metadata
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if token is not UNSET:
            field_dict["token"] = token
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_endpoint import DatastoreEndpoint

        d = dict(src_dict)
        auth_key = d.pop("auth_key", UNSET)

        _auth_type = d.pop("auth_type", UNSET)
        auth_type: DatastorePortalAuthType | Unset
        if isinstance(_auth_type, Unset):
            auth_type = UNSET
        else:
            auth_type = DatastorePortalAuthType(_auth_type)

        can_manage_endpoint = d.pop("can_manage_endpoint", UNSET)

        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        endpoint_count = d.pop("endpoint_count", UNSET)

        endpoints = cast(list[str], d.pop("endpoints", UNSET))

        _endpoints_metadata = d.pop("endpoints_metadata", UNSET)
        endpoints_metadata: list[DatastoreEndpoint | None] | Unset = UNSET
        if _endpoints_metadata is not UNSET:
            endpoints_metadata = []
            for endpoints_metadata_item_data in _endpoints_metadata:

                def _parse_endpoints_metadata_item(
                    data: object,
                ) -> DatastoreEndpoint | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        endpoints_metadata_item_type_1 = DatastoreEndpoint.from_dict(
                            data
                        )

                        return endpoints_metadata_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(DatastoreEndpoint | None, data)

                endpoints_metadata_item = _parse_endpoints_metadata_item(
                    endpoints_metadata_item_data
                )

                endpoints_metadata.append(endpoints_metadata_item)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        project_id = d.pop("project_id", UNSET)

        token = d.pop("token", UNSET)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        datastore_portal_link_response = cls(
            auth_key=auth_key,
            auth_type=auth_type,
            can_manage_endpoint=can_manage_endpoint,
            created_at=created_at,
            deleted_at=deleted_at,
            endpoint_count=endpoint_count,
            endpoints=endpoints,
            endpoints_metadata=endpoints_metadata,
            name=name,
            owner_id=owner_id,
            project_id=project_id,
            token=token,
            uid=uid,
            updated_at=updated_at,
            url=url,
        )

        datastore_portal_link_response.additional_properties = d
        return datastore_portal_link_response

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
