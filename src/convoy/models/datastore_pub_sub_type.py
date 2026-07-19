from enum import Enum


class DatastorePubSubType(str, Enum):
    AMQP_PUB_SUB = "amqp"
    GOOGLE_PUB_SUB = "google"
    KAFKA_PUB_SUB = "kafka"
    SQS_PUB_SUB = "sqs"

    def __str__(self) -> str:
        return str(self.value)
