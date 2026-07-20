from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_event_delivery_status import DatastoreEventDeliveryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_meta_event_attempt import DatastoreMetaEventAttempt
    from ..models.datastore_metadata import DatastoreMetadata


T = TypeVar("T", bound="ModelsMetaEventResponse")


@_attrs_define
class ModelsMetaEventResponse:
    """
    Attributes:
        attempt (DatastoreMetaEventAttempt | None | Unset):
        created_at (str | Unset):
        deleted_at (None | str | Unset):
        event_type (str | Unset):
        metadata (DatastoreMetadata | None | Unset):
        project_id (str | Unset):
        status (DatastoreEventDeliveryStatus | Unset):
        uid (str | Unset):
        updated_at (str | Unset):
    """

    attempt: DatastoreMetaEventAttempt | None | Unset = UNSET
    created_at: str | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    event_type: str | Unset = UNSET
    metadata: DatastoreMetadata | None | Unset = UNSET
    project_id: str | Unset = UNSET
    status: DatastoreEventDeliveryStatus | Unset = UNSET
    uid: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_meta_event_attempt import DatastoreMetaEventAttempt
        from ..models.datastore_metadata import DatastoreMetadata

        attempt: dict[str, Any] | None | Unset
        if isinstance(self.attempt, Unset):
            attempt = UNSET
        elif isinstance(self.attempt, DatastoreMetaEventAttempt):
            attempt = self.attempt.to_dict()
        else:
            attempt = self.attempt

        created_at = self.created_at

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

        event_type = self.event_type

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DatastoreMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        project_id = self.project_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        uid = self.uid

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if status is not UNSET:
            field_dict["status"] = status
        if uid is not UNSET:
            field_dict["uid"] = uid
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_meta_event_attempt import DatastoreMetaEventAttempt
        from ..models.datastore_metadata import DatastoreMetadata

        d = dict(src_dict)

        def _parse_attempt(data: object) -> DatastoreMetaEventAttempt | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attempt_type_1 = DatastoreMetaEventAttempt.from_dict(data)

                return attempt_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMetaEventAttempt | None | Unset, data)

        attempt = _parse_attempt(d.pop("attempt", UNSET))

        created_at = d.pop("created_at", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        event_type = d.pop("event_type", UNSET)

        def _parse_metadata(data: object) -> DatastoreMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = DatastoreMetadata.from_dict(data)

                return metadata_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreMetadata | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        project_id = d.pop("project_id", UNSET)

        _status = d.pop("status", UNSET)
        status: DatastoreEventDeliveryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DatastoreEventDeliveryStatus(_status)

        uid = d.pop("uid", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        models_meta_event_response = cls(
            attempt=attempt,
            created_at=created_at,
            deleted_at=deleted_at,
            event_type=event_type,
            metadata=metadata,
            project_id=project_id,
            status=status,
            uid=uid,
            updated_at=updated_at,
        )

        models_meta_event_response.additional_properties = d
        return models_meta_event_response

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
