from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_o_auth_2_authentication_type import (
    DatastoreOAuth2AuthenticationType,
)
from ..models.datastore_o_auth_2_expiry_time_unit import DatastoreOAuth2ExpiryTimeUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_o_auth_2_field_mapping import DatastoreOAuth2FieldMapping
    from ..models.datastore_o_auth_2_signing_key import DatastoreOAuth2SigningKey


T = TypeVar("T", bound="DatastoreOAuth2")


@_attrs_define
class DatastoreOAuth2:
    """
    Attributes:
        audience (str | Unset):
        authentication_type (DatastoreOAuth2AuthenticationType | Unset):
        client_id (str | Unset):
        client_secret (str | Unset): Encrypted at rest
        expiry_time_unit (DatastoreOAuth2ExpiryTimeUnit | Unset):
        field_mapping (DatastoreOAuth2FieldMapping | Unset):
        grant_type (str | Unset):
        issuer (str | Unset):
        scope (str | Unset):
        signing_algorithm (str | Unset):
        signing_key (DatastoreOAuth2SigningKey | Unset):
        subject (str | Unset):
        url (str | Unset):
    """

    audience: str | Unset = UNSET
    authentication_type: DatastoreOAuth2AuthenticationType | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    expiry_time_unit: DatastoreOAuth2ExpiryTimeUnit | Unset = UNSET
    field_mapping: DatastoreOAuth2FieldMapping | Unset = UNSET
    grant_type: str | Unset = UNSET
    issuer: str | Unset = UNSET
    scope: str | Unset = UNSET
    signing_algorithm: str | Unset = UNSET
    signing_key: DatastoreOAuth2SigningKey | Unset = UNSET
    subject: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience

        authentication_type: str | Unset = UNSET
        if not isinstance(self.authentication_type, Unset):
            authentication_type = self.authentication_type.value

        client_id = self.client_id

        client_secret = self.client_secret

        expiry_time_unit: str | Unset = UNSET
        if not isinstance(self.expiry_time_unit, Unset):
            expiry_time_unit = self.expiry_time_unit.value

        field_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_mapping, Unset):
            field_mapping = self.field_mapping.to_dict()

        grant_type = self.grant_type

        issuer = self.issuer

        scope = self.scope

        signing_algorithm = self.signing_algorithm

        signing_key: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signing_key, Unset):
            signing_key = self.signing_key.to_dict()

        subject = self.subject

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if authentication_type is not UNSET:
            field_dict["authentication_type"] = authentication_type
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if expiry_time_unit is not UNSET:
            field_dict["expiry_time_unit"] = expiry_time_unit
        if field_mapping is not UNSET:
            field_dict["field_mapping"] = field_mapping
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if scope is not UNSET:
            field_dict["scope"] = scope
        if signing_algorithm is not UNSET:
            field_dict["signing_algorithm"] = signing_algorithm
        if signing_key is not UNSET:
            field_dict["signing_key"] = signing_key
        if subject is not UNSET:
            field_dict["subject"] = subject
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_o_auth_2_field_mapping import (
            DatastoreOAuth2FieldMapping,
        )
        from ..models.datastore_o_auth_2_signing_key import DatastoreOAuth2SigningKey

        d = dict(src_dict)
        audience = d.pop("audience", UNSET)

        _authentication_type = d.pop("authentication_type", UNSET)
        authentication_type: DatastoreOAuth2AuthenticationType | Unset
        if isinstance(_authentication_type, Unset):
            authentication_type = UNSET
        else:
            authentication_type = DatastoreOAuth2AuthenticationType(
                _authentication_type
            )

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        _expiry_time_unit = d.pop("expiry_time_unit", UNSET)
        expiry_time_unit: DatastoreOAuth2ExpiryTimeUnit | Unset
        if isinstance(_expiry_time_unit, Unset):
            expiry_time_unit = UNSET
        else:
            expiry_time_unit = DatastoreOAuth2ExpiryTimeUnit(_expiry_time_unit)

        _field_mapping = d.pop("field_mapping", UNSET)
        field_mapping: DatastoreOAuth2FieldMapping | Unset
        if isinstance(_field_mapping, Unset):
            field_mapping = UNSET
        else:
            field_mapping = DatastoreOAuth2FieldMapping.from_dict(_field_mapping)

        grant_type = d.pop("grant_type", UNSET)

        issuer = d.pop("issuer", UNSET)

        scope = d.pop("scope", UNSET)

        signing_algorithm = d.pop("signing_algorithm", UNSET)

        _signing_key = d.pop("signing_key", UNSET)
        signing_key: DatastoreOAuth2SigningKey | Unset
        if isinstance(_signing_key, Unset):
            signing_key = UNSET
        else:
            signing_key = DatastoreOAuth2SigningKey.from_dict(_signing_key)

        subject = d.pop("subject", UNSET)

        url = d.pop("url", UNSET)

        datastore_o_auth_2 = cls(
            audience=audience,
            authentication_type=authentication_type,
            client_id=client_id,
            client_secret=client_secret,
            expiry_time_unit=expiry_time_unit,
            field_mapping=field_mapping,
            grant_type=grant_type,
            issuer=issuer,
            scope=scope,
            signing_algorithm=signing_algorithm,
            signing_key=signing_key,
            subject=subject,
            url=url,
        )

        datastore_o_auth_2.additional_properties = d
        return datastore_o_auth_2

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
