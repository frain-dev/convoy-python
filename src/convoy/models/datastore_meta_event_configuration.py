from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_meta_event_type import DatastoreMetaEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_pub_sub_config import DatastorePubSubConfig


T = TypeVar("T", bound="DatastoreMetaEventConfiguration")


@_attrs_define
class DatastoreMetaEventConfiguration:
    """
    Attributes:
        event_type (list[str] | Unset):
        is_enabled (bool | Unset):
        pub_sub (DatastorePubSubConfig | None | Unset):
        secret (str | Unset):
        type_ (DatastoreMetaEventType | Unset):
        url (str | Unset):
    """

    event_type: list[str] | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    pub_sub: DatastorePubSubConfig | None | Unset = UNSET
    secret: str | Unset = UNSET
    type_: DatastoreMetaEventType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_pub_sub_config import DatastorePubSubConfig

        event_type: list[str] | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type

        is_enabled = self.is_enabled

        pub_sub: dict[str, Any] | None | Unset
        if isinstance(self.pub_sub, Unset):
            pub_sub = UNSET
        elif isinstance(self.pub_sub, DatastorePubSubConfig):
            pub_sub = self.pub_sub.to_dict()
        else:
            pub_sub = self.pub_sub

        secret = self.secret

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if pub_sub is not UNSET:
            field_dict["pub_sub"] = pub_sub
        if secret is not UNSET:
            field_dict["secret"] = secret
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_pub_sub_config import DatastorePubSubConfig

        d = dict(src_dict)
        event_type = cast(list[str], d.pop("event_type", UNSET))

        is_enabled = d.pop("is_enabled", UNSET)

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

        secret = d.pop("secret", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreMetaEventType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreMetaEventType(_type_)

        url = d.pop("url", UNSET)

        datastore_meta_event_configuration = cls(
            event_type=event_type,
            is_enabled=is_enabled,
            pub_sub=pub_sub,
            secret=secret,
            type_=type_,
            url=url,
        )

        datastore_meta_event_configuration.additional_properties = d
        return datastore_meta_event_configuration

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
