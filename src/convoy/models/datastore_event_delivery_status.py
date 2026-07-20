from enum import Enum


class DatastoreEventDeliveryStatus(str, Enum):
    DISCARDED = "Discarded"
    FAILURE = "Failure"
    PROCESSING = "Processing"
    RETRY = "Retry"
    SCHEDULED = "Scheduled"
    SUCCESS = "Success"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
