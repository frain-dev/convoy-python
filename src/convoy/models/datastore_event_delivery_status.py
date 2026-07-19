from enum import Enum


class DatastoreEventDeliveryStatus(str, Enum):
    DISCARDED_EVENT_STATUS = "Discarded"
    FAILURE_EVENT_STATUS = "Failure"
    PROCESSING_EVENT_STATUS = "Processing"
    RETRY_EVENT_STATUS = "Retry"
    SCHEDULED_EVENT_STATUS = "Scheduled"
    SUCCESS_EVENT_STATUS = "Success"

    def __str__(self) -> str:
        return str(self.value)
