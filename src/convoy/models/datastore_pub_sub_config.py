from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_pub_sub_type import DatastorePubSubType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.datastore_amqp_pub_sub_config import DatastoreAmqpPubSubConfig
    from ..models.datastore_google_pub_sub_config import DatastoreGooglePubSubConfig
    from ..models.datastore_kafka_pub_sub_config import DatastoreKafkaPubSubConfig
    from ..models.datastore_sqs_pub_sub_config import DatastoreSQSPubSubConfig


T = TypeVar("T", bound="DatastorePubSubConfig")


@_attrs_define
class DatastorePubSubConfig:
    """
    Attributes:
        amqp (DatastoreAmqpPubSubConfig | None | Unset):
        google (DatastoreGooglePubSubConfig | None | Unset):
        kafka (DatastoreKafkaPubSubConfig | None | Unset):
        sqs (DatastoreSQSPubSubConfig | None | Unset):
        type_ (DatastorePubSubType | Unset):
        workers (int | Unset):
    """

    amqp: DatastoreAmqpPubSubConfig | None | Unset = UNSET
    google: DatastoreGooglePubSubConfig | None | Unset = UNSET
    kafka: DatastoreKafkaPubSubConfig | None | Unset = UNSET
    sqs: DatastoreSQSPubSubConfig | None | Unset = UNSET
    type_: DatastorePubSubType | Unset = UNSET
    workers: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.datastore_amqp_pub_sub_config import DatastoreAmqpPubSubConfig
        from ..models.datastore_google_pub_sub_config import DatastoreGooglePubSubConfig
        from ..models.datastore_kafka_pub_sub_config import DatastoreKafkaPubSubConfig
        from ..models.datastore_sqs_pub_sub_config import DatastoreSQSPubSubConfig

        amqp: dict[str, Any] | None | Unset
        if isinstance(self.amqp, Unset):
            amqp = UNSET
        elif isinstance(self.amqp, DatastoreAmqpPubSubConfig):
            amqp = self.amqp.to_dict()
        else:
            amqp = self.amqp

        google: dict[str, Any] | None | Unset
        if isinstance(self.google, Unset):
            google = UNSET
        elif isinstance(self.google, DatastoreGooglePubSubConfig):
            google = self.google.to_dict()
        else:
            google = self.google

        kafka: dict[str, Any] | None | Unset
        if isinstance(self.kafka, Unset):
            kafka = UNSET
        elif isinstance(self.kafka, DatastoreKafkaPubSubConfig):
            kafka = self.kafka.to_dict()
        else:
            kafka = self.kafka

        sqs: dict[str, Any] | None | Unset
        if isinstance(self.sqs, Unset):
            sqs = UNSET
        elif isinstance(self.sqs, DatastoreSQSPubSubConfig):
            sqs = self.sqs.to_dict()
        else:
            sqs = self.sqs

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        workers = self.workers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amqp is not UNSET:
            field_dict["amqp"] = amqp
        if google is not UNSET:
            field_dict["google"] = google
        if kafka is not UNSET:
            field_dict["kafka"] = kafka
        if sqs is not UNSET:
            field_dict["sqs"] = sqs
        if type_ is not UNSET:
            field_dict["type"] = type_
        if workers is not UNSET:
            field_dict["workers"] = workers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.datastore_amqp_pub_sub_config import DatastoreAmqpPubSubConfig
        from ..models.datastore_google_pub_sub_config import DatastoreGooglePubSubConfig
        from ..models.datastore_kafka_pub_sub_config import DatastoreKafkaPubSubConfig
        from ..models.datastore_sqs_pub_sub_config import DatastoreSQSPubSubConfig

        d = dict(src_dict)

        def _parse_amqp(data: object) -> DatastoreAmqpPubSubConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                amqp_type_1 = DatastoreAmqpPubSubConfig.from_dict(data)

                return amqp_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreAmqpPubSubConfig | None | Unset, data)

        amqp = _parse_amqp(d.pop("amqp", UNSET))

        def _parse_google(data: object) -> DatastoreGooglePubSubConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                google_type_1 = DatastoreGooglePubSubConfig.from_dict(data)

                return google_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreGooglePubSubConfig | None | Unset, data)

        google = _parse_google(d.pop("google", UNSET))

        def _parse_kafka(data: object) -> DatastoreKafkaPubSubConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                kafka_type_1 = DatastoreKafkaPubSubConfig.from_dict(data)

                return kafka_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreKafkaPubSubConfig | None | Unset, data)

        kafka = _parse_kafka(d.pop("kafka", UNSET))

        def _parse_sqs(data: object) -> DatastoreSQSPubSubConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sqs_type_1 = DatastoreSQSPubSubConfig.from_dict(data)

                return sqs_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatastoreSQSPubSubConfig | None | Unset, data)

        sqs = _parse_sqs(d.pop("sqs", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: DatastorePubSubType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastorePubSubType(_type_)

        workers = d.pop("workers", UNSET)

        datastore_pub_sub_config = cls(
            amqp=amqp,
            google=google,
            kafka=kafka,
            sqs=sqs,
            type_=type_,
            workers=workers,
        )

        datastore_pub_sub_config.additional_properties = d
        return datastore_pub_sub_config

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
