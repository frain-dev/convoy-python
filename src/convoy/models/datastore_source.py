from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_source_provider import DatastoreSourceProvider
from ..models.datastore_source_type import DatastoreSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_custom_response import DatastoreCustomResponse
    from ..models.datastore_provider_config import DatastoreProviderConfig
    from ..models.datastore_pub_sub_config import DatastorePubSubConfig
    from ..models.datastore_verifier_config import DatastoreVerifierConfig


T = TypeVar("T", bound="DatastoreSource")


@_attrs_define
class DatastoreSource:
    """
    Attributes:
        body_function (str | Unset):
        created_at (str | Unset):
        custom_response (DatastoreCustomResponse | Unset):
        deleted_at (str | Unset):
        event_type_location (str | Unset):
        forward_headers (list[str] | Unset):
        header_function (str | Unset):
        idempotency_keys (list[str] | Unset):
        is_disabled (bool | Unset):
        mask_id (str | Unset):
        name (str | Unset):
        project_id (str | Unset):
        provider (DatastoreSourceProvider | Unset):
        provider_config (DatastoreProviderConfig | Unset):
        pub_sub (DatastorePubSubConfig | Unset):
        type_ (DatastoreSourceType | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
        verifier (DatastoreVerifierConfig | Unset):
    """

    body_function: str | Unset = UNSET
    created_at: str | Unset = UNSET
    custom_response: DatastoreCustomResponse | Unset = UNSET
    deleted_at: str | Unset = UNSET
    event_type_location: str | Unset = UNSET
    forward_headers: list[str] | Unset = UNSET
    header_function: str | Unset = UNSET
    idempotency_keys: list[str] | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    mask_id: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    provider: DatastoreSourceProvider | Unset = UNSET
    provider_config: DatastoreProviderConfig | Unset = UNSET
    pub_sub: DatastorePubSubConfig | Unset = UNSET
    type_: DatastoreSourceType | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    verifier: DatastoreVerifierConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_function = self.body_function

        created_at = self.created_at

        custom_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_response, Unset):
            custom_response = self.custom_response.to_dict()

        deleted_at = self.deleted_at

        event_type_location = self.event_type_location

        forward_headers: list[str] | Unset = UNSET
        if not isinstance(self.forward_headers, Unset):
            forward_headers = self.forward_headers

        header_function = self.header_function

        idempotency_keys: list[str] | Unset = UNSET
        if not isinstance(self.idempotency_keys, Unset):
            idempotency_keys = self.idempotency_keys

        is_disabled = self.is_disabled

        mask_id = self.mask_id

        name = self.name

        project_id = self.project_id

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        provider_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_config, Unset):
            provider_config = self.provider_config.to_dict()

        pub_sub: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pub_sub, Unset):
            pub_sub = self.pub_sub.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        updated_at = self.updated_at

        url = self.url

        verifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verifier, Unset):
            verifier = self.verifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_function is not UNSET:
            field_dict["body_function"] = body_function
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if custom_response is not UNSET:
            field_dict["custom_response"] = custom_response
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if event_type_location is not UNSET:
            field_dict["event_type_location"] = event_type_location
        if forward_headers is not UNSET:
            field_dict["forward_headers"] = forward_headers
        if header_function is not UNSET:
            field_dict["header_function"] = header_function
        if idempotency_keys is not UNSET:
            field_dict["idempotency_keys"] = idempotency_keys
        if is_disabled is not UNSET:
            field_dict["is_disabled"] = is_disabled
        if mask_id is not UNSET:
            field_dict["mask_id"] = mask_id
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_config is not UNSET:
            field_dict["provider_config"] = provider_config
        if pub_sub is not UNSET:
            field_dict["pub_sub"] = pub_sub
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if verifier is not UNSET:
            field_dict["verifier"] = verifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_custom_response import DatastoreCustomResponse
        from ..models.datastore_provider_config import DatastoreProviderConfig
        from ..models.datastore_pub_sub_config import DatastorePubSubConfig
        from ..models.datastore_verifier_config import DatastoreVerifierConfig

        d = dict(src_dict)
        body_function = d.pop("body_function", UNSET)

        created_at = d.pop("created_at", UNSET)

        _custom_response = d.pop("custom_response", UNSET)
        custom_response: DatastoreCustomResponse | Unset
        if isinstance(_custom_response, Unset):
            custom_response = UNSET
        else:
            custom_response = DatastoreCustomResponse.from_dict(_custom_response)

        deleted_at = d.pop("deleted_at", UNSET)

        event_type_location = d.pop("event_type_location", UNSET)

        forward_headers = cast(list[str], d.pop("forward_headers", UNSET))

        header_function = d.pop("header_function", UNSET)

        idempotency_keys = cast(list[str], d.pop("idempotency_keys", UNSET))

        is_disabled = d.pop("is_disabled", UNSET)

        mask_id = d.pop("mask_id", UNSET)

        name = d.pop("name", UNSET)

        project_id = d.pop("project_id", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: DatastoreSourceProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = DatastoreSourceProvider(_provider)

        _provider_config = d.pop("provider_config", UNSET)
        provider_config: DatastoreProviderConfig | Unset
        if isinstance(_provider_config, Unset):
            provider_config = UNSET
        else:
            provider_config = DatastoreProviderConfig.from_dict(_provider_config)

        _pub_sub = d.pop("pub_sub", UNSET)
        pub_sub: DatastorePubSubConfig | Unset
        if isinstance(_pub_sub, Unset):
            pub_sub = UNSET
        else:
            pub_sub = DatastorePubSubConfig.from_dict(_pub_sub)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreSourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreSourceType(_type_)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        _verifier = d.pop("verifier", UNSET)
        verifier: DatastoreVerifierConfig | Unset
        if isinstance(_verifier, Unset):
            verifier = UNSET
        else:
            verifier = DatastoreVerifierConfig.from_dict(_verifier)

        datastore_source = cls(
            body_function=body_function,
            created_at=created_at,
            custom_response=custom_response,
            deleted_at=deleted_at,
            event_type_location=event_type_location,
            forward_headers=forward_headers,
            header_function=header_function,
            idempotency_keys=idempotency_keys,
            is_disabled=is_disabled,
            mask_id=mask_id,
            name=name,
            project_id=project_id,
            provider=provider,
            provider_config=provider_config,
            pub_sub=pub_sub,
            type_=type_,
            uid=uid,
            updated_at=updated_at,
            url=url,
            verifier=verifier,
        )

        datastore_source.additional_properties = d
        return datastore_source

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
