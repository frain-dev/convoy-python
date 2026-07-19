from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_function_response import ModelsFunctionResponse


T = TypeVar("T", bound="PostV1ProjectsProjectIDSourcesTestFunctionResponse200")


@_attrs_define
class PostV1ProjectsProjectIDSourcesTestFunctionResponse200:
    """
    Attributes:
        message (str | Unset):
        status (bool | Unset):
        data (ModelsFunctionResponse | Unset):
    """

    message: str | Unset = UNSET
    status: bool | Unset = UNSET
    data: ModelsFunctionResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status = self.status

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_function_response import ModelsFunctionResponse

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: ModelsFunctionResponse | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ModelsFunctionResponse.from_dict(_data)

        post_v1_projects_project_id_sources_test_function_response_200 = cls(
            message=message,
            status=status,
            data=data,
        )

        post_v1_projects_project_id_sources_test_function_response_200.additional_properties = d
        return post_v1_projects_project_id_sources_test_function_response_200

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
