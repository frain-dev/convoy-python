from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_source_provider import DatastoreSourceProvider
from ..models.datastore_source_type import DatastoreSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_custom_response import ModelsCustomResponse
    from ..models.models_pub_sub_config import ModelsPubSubConfig
    from ..models.models_verifier_config import ModelsVerifierConfig


T = TypeVar("T", bound="ModelsCreateSource")


@_attrs_define
class ModelsCreateSource:
    """
    Attributes:
        body_function (str | Unset): Function is a javascript function used to mutate the payload
            immediately after ingesting an event
        custom_response (ModelsCustomResponse | Unset):
        event_type_location (str | Unset): EventTypeLocation is used to specify where Convoy should read the event type
            from an incoming webhook request.
        header_function (str | Unset): Function is a javascript function used to mutate the headers
            immediately after ingesting an event
        idempotency_keys (list[str] | Unset): IdempotencyKeys are used to specify parts of a webhook request to uniquely
            identify the event in an incoming webhooks project.
        name (str | Unset): Source name.
        provider (DatastoreSourceProvider | Unset):
        pub_sub (ModelsPubSubConfig | Unset):
        type_ (DatastoreSourceType | Unset):
        verifier (ModelsVerifierConfig | Unset):
    """

    body_function: str | Unset = UNSET
    custom_response: ModelsCustomResponse | Unset = UNSET
    event_type_location: str | Unset = UNSET
    header_function: str | Unset = UNSET
    idempotency_keys: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    provider: DatastoreSourceProvider | Unset = UNSET
    pub_sub: ModelsPubSubConfig | Unset = UNSET
    type_: DatastoreSourceType | Unset = UNSET
    verifier: ModelsVerifierConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_function = self.body_function

        custom_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_response, Unset):
            custom_response = self.custom_response.to_dict()

        event_type_location = self.event_type_location

        header_function = self.header_function

        idempotency_keys: list[str] | Unset = UNSET
        if not isinstance(self.idempotency_keys, Unset):
            idempotency_keys = self.idempotency_keys

        name = self.name

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        pub_sub: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pub_sub, Unset):
            pub_sub = self.pub_sub.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        verifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verifier, Unset):
            verifier = self.verifier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_function is not UNSET:
            field_dict["body_function"] = body_function
        if custom_response is not UNSET:
            field_dict["custom_response"] = custom_response
        if event_type_location is not UNSET:
            field_dict["event_type_location"] = event_type_location
        if header_function is not UNSET:
            field_dict["header_function"] = header_function
        if idempotency_keys is not UNSET:
            field_dict["idempotency_keys"] = idempotency_keys
        if name is not UNSET:
            field_dict["name"] = name
        if provider is not UNSET:
            field_dict["provider"] = provider
        if pub_sub is not UNSET:
            field_dict["pub_sub"] = pub_sub
        if type_ is not UNSET:
            field_dict["type"] = type_
        if verifier is not UNSET:
            field_dict["verifier"] = verifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_custom_response import ModelsCustomResponse
        from ..models.models_pub_sub_config import ModelsPubSubConfig
        from ..models.models_verifier_config import ModelsVerifierConfig

        d = dict(src_dict)
        body_function = d.pop("body_function", UNSET)

        _custom_response = d.pop("custom_response", UNSET)
        custom_response: ModelsCustomResponse | Unset
        if isinstance(_custom_response, Unset):
            custom_response = UNSET
        else:
            custom_response = ModelsCustomResponse.from_dict(_custom_response)

        event_type_location = d.pop("event_type_location", UNSET)

        header_function = d.pop("header_function", UNSET)

        idempotency_keys = cast(list[str], d.pop("idempotency_keys", UNSET))

        name = d.pop("name", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: DatastoreSourceProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = DatastoreSourceProvider(_provider)

        _pub_sub = d.pop("pub_sub", UNSET)
        pub_sub: ModelsPubSubConfig | Unset
        if isinstance(_pub_sub, Unset):
            pub_sub = UNSET
        else:
            pub_sub = ModelsPubSubConfig.from_dict(_pub_sub)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreSourceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreSourceType(_type_)

        _verifier = d.pop("verifier", UNSET)
        verifier: ModelsVerifierConfig | Unset
        if isinstance(_verifier, Unset):
            verifier = UNSET
        else:
            verifier = ModelsVerifierConfig.from_dict(_verifier)

        models_create_source = cls(
            body_function=body_function,
            custom_response=custom_response,
            event_type_location=event_type_location,
            header_function=header_function,
            idempotency_keys=idempotency_keys,
            name=name,
            provider=provider,
            pub_sub=pub_sub,
            type_=type_,
            verifier=verifier,
        )

        models_create_source.additional_properties = d
        return models_create_source

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
