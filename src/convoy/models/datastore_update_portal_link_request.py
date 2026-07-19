from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatastoreUpdatePortalLinkRequest")


@_attrs_define
class DatastoreUpdatePortalLinkRequest:
    """
    Attributes:
        auth_type (str | Unset):
        can_manage_endpoint (bool | Unset): Specify whether endpoint management can be done through the Portal Link UI
        endpoints (list[str] | Unset): Deprecated
            IDs of endpoints in this portal link
        name (str | Unset): Portal Link Name
        owner_id (str | Unset): OwnerID, the portal link will inherit all the endpoints with this owner ID
    """

    auth_type: str | Unset = UNSET
    can_manage_endpoint: bool | Unset = UNSET
    endpoints: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_type = self.auth_type

        can_manage_endpoint = self.can_manage_endpoint

        endpoints: list[str] | Unset = UNSET
        if not isinstance(self.endpoints, Unset):
            endpoints = self.endpoints

        name = self.name

        owner_id = self.owner_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_type is not UNSET:
            field_dict["auth_type"] = auth_type
        if can_manage_endpoint is not UNSET:
            field_dict["can_manage_endpoint"] = can_manage_endpoint
        if endpoints is not UNSET:
            field_dict["endpoints"] = endpoints
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_type = d.pop("auth_type", UNSET)

        can_manage_endpoint = d.pop("can_manage_endpoint", UNSET)

        endpoints = cast(list[str], d.pop("endpoints", UNSET))

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        datastore_update_portal_link_request = cls(
            auth_type=auth_type,
            can_manage_endpoint=can_manage_endpoint,
            endpoints=endpoints,
            name=name,
            owner_id=owner_id,
        )

        datastore_update_portal_link_request.additional_properties = d
        return datastore_update_portal_link_request

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
