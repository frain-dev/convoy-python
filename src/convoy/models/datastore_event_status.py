from enum import Enum


class DatastoreEventStatus(str, Enum):
    FAILURE = "Failure"
    PENDING = "Pending"
    PROCESSING = "Processing"
    RETRY = "Retry"
    SUCCESS = "Success"
    VALUE_5 = ""

    def __str__(self) -> str:
        return str(self.value)
