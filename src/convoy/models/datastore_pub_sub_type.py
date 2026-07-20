from enum import Enum


class DatastorePubSubType(str, Enum):
    AMQP = "amqp"
    GOOGLE = "google"
    KAFKA = "kafka"
    SQS = "sqs"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
