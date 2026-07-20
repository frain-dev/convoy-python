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


T = TypeVar("T", bound="ModelsSourceResponse")


@_attrs_define
class ModelsSourceResponse:
    """
    Attributes:
        body_function (None | str | Unset):
        created_at (str | Unset):
        custom_response (DatastoreCustomResponse | Unset):
        deleted_at (None | str | Unset):
        event_type_location (str | Unset):
        forward_headers (list[str] | Unset):
        header_function (None | str | Unset):
        idempotency_keys (list[str] | Unset):
        is_disabled (bool | Unset):
        mask_id (str | Unset):
        name (str | Unset):
        project_id (str | Unset):
        provider (DatastoreSourceProvider | Unset):
        provider_config (DatastoreProviderConfig | None | Unset):
        pub_sub (DatastorePubSubConfig | None | Unset):
        type_ (DatastoreSourceType | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
        url (str | Unset):
        verifier (DatastoreVerifierConfig | None | Unset):
    """

    body_function: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    custom_response: DatastoreCustomResponse | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    event_type_location: str | Unset = UNSET
    forward_headers: list[str] | Unset = UNSET
    header_function: None | str | Unset = UNSET
    idempotency_keys: list[str] | Unset = UNSET
    is_disabled: bool | Unset = UNSET
    mask_id: str | Unset = UNSET
    name: str | Unset = UNSET
    project_id: str | Unset = UNSET
    provider: DatastoreSourceProvider | Unset = UNSET
    provider_config: DatastoreProviderConfig | None | Unset = UNSET
    pub_sub: DatastorePubSubConfig | None | Unset = UNSET
    type_: DatastoreSourceType | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    url: str | Unset = UNSET
    verifier: DatastoreVerifierConfig | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_provider_config import DatastoreProviderConfig
        from ..models.datastore_pub_sub_config import DatastorePubSubConfig
        from ..models.datastore_verifier_config import DatastoreVerifierConfig

        body_function: None | str | Unset
        if isinstance(self.body_function, Unset):
            body_function = UNSET
        else:
            body_function = self.body_function

        created_at = self.created_at

        custom_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_response, Unset):
            custom_response = self.custom_response.to_dict()

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        event_type_location = self.event_type_location

        forward_headers: list[str] | Unset = UNSET
        if not isinstance(self.forward_headers, Unset):
            forward_headers = self.forward_headers

        header_function: None | str | Unset
        if isinstance(self.header_function, Unset):
            header_function = UNSET
        else:
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

        provider_config: dict[str, Any] | None | Unset
        if isinstance(self.provider_config, Unset):
            provider_config = UNSET
        elif isinstance(self.provider_config, DatastoreProviderConfig):
            provider_config = self.provider_config.to_dict()
        else:
            provider_config = self.provider_config

        pub_sub: dict[str, Any] | None | Unset
        if isinstance(self.pub_sub, Unset):
            pub_sub = UNSET
        elif isinstance(self.pub_sub, DatastorePubSubConfig):
            pub_sub = self.pub_sub.to_dict()
        else:
            pub_sub = self.pub_sub

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        updated_at = self.updated_at

        url = self.url

        verifier: dict[str, Any] | None | Unset
        if isinstance(self.verifier, Unset):
            verifier = UNSET
        elif isinstance(self.verifier, DatastoreVerifierConfig):
            verifier = self.verifier.to_dict()
        else:
            verifier = self.verifier

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

        def _parse_body_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_function = _parse_body_function(d.pop("body_function", UNSET))

        created_at = d.pop("created_at", UNSET)

        _custom_response = d.pop("custom_response", UNSET)
        custom_response: DatastoreCustomResponse | Unset
        if isinstance(_custom_response, Unset):
            custom_response = UNSET
        else:
            custom_response = DatastoreCustomResponse.from_dict(_custom_response)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        event_type_location = d.pop("event_type_location", UNSET)

        forward_headers = cast(list[str], d.pop("forward_headers", UNSET))

        def _parse_header_function(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_function = _parse_header_function(d.pop("header_function", UNSET))

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

        def _parse_provider_config(
            data: object,
        ) -> DatastoreProviderConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_config_type_1 = DatastoreProviderConfig.from_dict(data)

                return provider_config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreProviderConfig | None | Unset, data)

        provider_config = _parse_provider_config(d.pop("provider_config", UNSET))

        def _parse_pub_sub(data: object) -> DatastorePubSubConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pub_sub_type_1 = DatastorePubSubConfig.from_dict(data)

                return pub_sub_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastorePubSubConfig | None | Unset, data)

        pub_sub = _parse_pub_sub(d.pop("pub_sub", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: DatastoreSourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreSourceType(_type_)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        url = d.pop("url", UNSET)

        def _parse_verifier(data: object) -> DatastoreVerifierConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                verifier_type_1 = DatastoreVerifierConfig.from_dict(data)

                return verifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreVerifierConfig | None | Unset, data)

        verifier = _parse_verifier(d.pop("verifier", UNSET))

        models_source_response = cls(
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

        models_source_response.additional_properties = d
        return models_source_response

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
