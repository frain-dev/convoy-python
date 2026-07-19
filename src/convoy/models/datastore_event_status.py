from enum import Enum


class DatastoreEventStatus(str, Enum):
    FAILURE_STATUS = "Failure"
    PENDING_STATUS = "Pending"
    PROCESSING_STATUS = "Processing"
    RETRY_STATUS = "Retry"
    SUCCESS_STATUS = "Success"

    def __str__(self) -> str:
        return str(self.value)
