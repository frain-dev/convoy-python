from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_api_key_response import DatastoreAPIKeyResponse
    from ..models.models_project_response import ModelsProjectResponse


T = TypeVar("T", bound="ModelsCreateProjectResponse")


@_attrs_define
class ModelsCreateProjectResponse:
    """
    Attributes:
        api_key (DatastoreAPIKeyResponse | None | Unset):
        project (ModelsProjectResponse | None | Unset):
    """

    api_key: DatastoreAPIKeyResponse | None | Unset = UNSET
    project: ModelsProjectResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_api_key_response import DatastoreAPIKeyResponse
        from ..models.models_project_response import ModelsProjectResponse

        api_key: dict[str, Any] | None | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        elif isinstance(self.api_key, DatastoreAPIKeyResponse):
            api_key = self.api_key.to_dict()
        else:
            api_key = self.api_key

        project: dict[str, Any] | None | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, ModelsProjectResponse):
            project = self.project.to_dict()
        else:
            project = self.project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_api_key_response import DatastoreAPIKeyResponse
        from ..models.models_project_response import ModelsProjectResponse

        d = dict(src_dict)

        def _parse_api_key(data: object) -> DatastoreAPIKeyResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                api_key_type_1 = DatastoreAPIKeyResponse.from_dict(data)

                return api_key_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreAPIKeyResponse | None | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_project(data: object) -> ModelsProjectResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                project_type_1 = ModelsProjectResponse.from_dict(data)

                return project_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelsProjectResponse | None | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        models_create_project_response = cls(
            api_key=api_key,
            project=project,
        )

        models_create_project_response.additional_properties = d
        return models_create_project_response

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
