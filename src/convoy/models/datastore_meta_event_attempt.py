from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_http_header_type_0 import DatastoreHttpHeaderType0


T = TypeVar("T", bound="DatastoreMetaEventAttempt")


@_attrs_define
class DatastoreMetaEventAttempt:
    """
    Attributes:
        request_http_header (DatastoreHttpHeaderType0 | None | Unset):
        response_data (str | Unset):
        response_http_header (DatastoreHttpHeaderType0 | None | Unset):
    """

    request_http_header: DatastoreHttpHeaderType0 | None | Unset = UNSET
    response_data: str | Unset = UNSET
    response_http_header: DatastoreHttpHeaderType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_http_header_type_0 import DatastoreHttpHeaderType0

        request_http_header: dict[str, Any] | None | Unset
        if isinstance(self.request_http_header, Unset):
            request_http_header = UNSET
        elif isinstance(self.request_http_header, DatastoreHttpHeaderType0):
            request_http_header = self.request_http_header.to_dict()
        else:
            request_http_header = self.request_http_header

        response_data = self.response_data

        response_http_header: dict[str, Any] | None | Unset
        if isinstance(self.response_http_header, Unset):
            response_http_header = UNSET
        elif isinstance(self.response_http_header, DatastoreHttpHeaderType0):
            response_http_header = self.response_http_header.to_dict()
        else:
            response_http_header = self.response_http_header

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_http_header is not UNSET:
            field_dict["request_http_header"] = request_http_header
        if response_data is not UNSET:
            field_dict["response_data"] = response_data
        if response_http_header is not UNSET:
            field_dict["response_http_header"] = response_http_header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_http_header_type_0 import DatastoreHttpHeaderType0

        d = dict(src_dict)

        def _parse_request_http_header(
            data: object,
        ) -> DatastoreHttpHeaderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_http_header_type_0 = (
                    DatastoreHttpHeaderType0.from_dict(data)
                )

                return componentsschemasdatastore_http_header_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreHttpHeaderType0 | None | Unset, data)

        request_http_header = _parse_request_http_header(
            d.pop("request_http_header", UNSET)
        )

        response_data = d.pop("response_data", UNSET)

        def _parse_response_http_header(
            data: object,
        ) -> DatastoreHttpHeaderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasdatastore_http_header_type_0 = (
                    DatastoreHttpHeaderType0.from_dict(data)
                )

                return componentsschemasdatastore_http_header_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreHttpHeaderType0 | None | Unset, data)

        response_http_header = _parse_response_http_header(
            d.pop("response_http_header", UNSET)
        )

        datastore_meta_event_attempt = cls(
            request_http_header=request_http_header,
            response_data=response_data,
            response_http_header=response_http_header,
        )

        datastore_meta_event_attempt.additional_properties = d
        return datastore_meta_event_attempt

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
