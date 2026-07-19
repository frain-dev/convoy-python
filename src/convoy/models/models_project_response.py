from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_project_type import DatastoreProjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_project_config import DatastoreProjectConfig
    from ..models.datastore_project_statistics import DatastoreProjectStatistics


T = TypeVar("T", bound="ModelsProjectResponse")


@_attrs_define
class ModelsProjectResponse:
    """
    Attributes:
        config (DatastoreProjectConfig | Unset):
        created_at (str | Unset):
        deleted_at (str | Unset):
        logo_url (str | Unset):
        name (str | Unset):
        organisation_id (str | Unset):
        retained_events (int | Unset):
        statistics (DatastoreProjectStatistics | Unset):
        type_ (DatastoreProjectType | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
    """

    config: DatastoreProjectConfig | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: str | Unset = UNSET
    logo_url: str | Unset = UNSET
    name: str | Unset = UNSET
    organisation_id: str | Unset = UNSET
    retained_events: int | Unset = UNSET
    statistics: DatastoreProjectStatistics | Unset = UNSET
    type_: DatastoreProjectType | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        created_at = self.created_at

        deleted_at = self.deleted_at

        logo_url = self.logo_url

        name = self.name

        organisation_id = self.organisation_id

        retained_events = self.retained_events

        statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        uid = self.uid

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if name is not UNSET:
            field_dict["name"] = name
        if organisation_id is not UNSET:
            field_dict["organisation_id"] = organisation_id
        if retained_events is not UNSET:
            field_dict["retained_events"] = retained_events
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_project_config import DatastoreProjectConfig
        from ..models.datastore_project_statistics import DatastoreProjectStatistics

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: DatastoreProjectConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = DatastoreProjectConfig.from_dict(_config)

        created_at = d.pop("created_at", UNSET)

        deleted_at = d.pop("deleted_at", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        name = d.pop("name", UNSET)

        organisation_id = d.pop("organisation_id", UNSET)

        retained_events = d.pop("retained_events", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: DatastoreProjectStatistics | Unset
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = DatastoreProjectStatistics.from_dict(_statistics)

        _type_ = d.pop("type", UNSET)
        type_: DatastoreProjectType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastoreProjectType(_type_)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        models_project_response = cls(
            config=config,
            created_at=created_at,
            deleted_at=deleted_at,
            logo_url=logo_url,
            name=name,
            organisation_id=organisation_id,
            retained_events=retained_events,
            statistics=statistics,
            type_=type_,
            uid=uid,
            updated_at=updated_at,
        )

        models_project_response.additional_properties = d
        return models_project_response

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
