from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.datastore_pub_sub_type import DatastorePubSubType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.models_amqp_pub_subconfig import ModelsAmqpPubSubconfig
    from ..models.models_google_pub_sub_config import ModelsGooglePubSubConfig
    from ..models.models_kafka_pub_sub_config import ModelsKafkaPubSubConfig
    from ..models.models_sqs_pub_sub_config import ModelsSQSPubSubConfig


T = TypeVar("T", bound="ModelsPubSubConfig")


@_attrs_define
class ModelsPubSubConfig:
    """
    Attributes:
        amqp (ModelsAmqpPubSubconfig | Unset):
        google (ModelsGooglePubSubConfig | Unset):
        kafka (ModelsKafkaPubSubConfig | Unset):
        sqs (ModelsSQSPubSubConfig | Unset):
        type_ (DatastorePubSubType | Unset):
        workers (int | Unset):
    """

    amqp: ModelsAmqpPubSubconfig | Unset = UNSET
    google: ModelsGooglePubSubConfig | Unset = UNSET
    kafka: ModelsKafkaPubSubConfig | Unset = UNSET
    sqs: ModelsSQSPubSubConfig | Unset = UNSET
    type_: DatastorePubSubType | Unset = UNSET
    workers: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amqp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amqp, Unset):
            amqp = self.amqp.to_dict()

        google: dict[str, Any] | Unset = UNSET
        if not isinstance(self.google, Unset):
            google = self.google.to_dict()

        kafka: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kafka, Unset):
            kafka = self.kafka.to_dict()

        sqs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sqs, Unset):
            sqs = self.sqs.to_dict()

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
        from ..models.models_amqp_pub_subconfig import ModelsAmqpPubSubconfig
        from ..models.models_google_pub_sub_config import ModelsGooglePubSubConfig
        from ..models.models_kafka_pub_sub_config import ModelsKafkaPubSubConfig
        from ..models.models_sqs_pub_sub_config import ModelsSQSPubSubConfig

        d = dict(src_dict)
        _amqp = d.pop("amqp", UNSET)
        amqp: ModelsAmqpPubSubconfig | Unset
        if isinstance(_amqp, Unset):
            amqp = UNSET
        else:
            amqp = ModelsAmqpPubSubconfig.from_dict(_amqp)

        _google = d.pop("google", UNSET)
        google: ModelsGooglePubSubConfig | Unset
        if isinstance(_google, Unset):
            google = UNSET
        else:
            google = ModelsGooglePubSubConfig.from_dict(_google)

        _kafka = d.pop("kafka", UNSET)
        kafka: ModelsKafkaPubSubConfig | Unset
        if isinstance(_kafka, Unset):
            kafka = UNSET
        else:
            kafka = ModelsKafkaPubSubConfig.from_dict(_kafka)

        _sqs = d.pop("sqs", UNSET)
        sqs: ModelsSQSPubSubConfig | Unset
        if isinstance(_sqs, Unset):
            sqs = UNSET
        else:
            sqs = ModelsSQSPubSubConfig.from_dict(_sqs)

        _type_ = d.pop("type", UNSET)
        type_: DatastorePubSubType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatastorePubSubType(_type_)

        workers = d.pop("workers", UNSET)

        models_pub_sub_config = cls(
            amqp=amqp,
            google=google,
            kafka=kafka,
            sqs=sqs,
            type_=type_,
            workers=workers,
        )

        models_pub_sub_config.additional_properties = d
        return models_pub_sub_config

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
