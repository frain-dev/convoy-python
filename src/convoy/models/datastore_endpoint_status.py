from enum import Enum


class DatastoreEndpointStatus(str, Enum):
    ACTIVE_ENDPOINT_STATUS = "active"
    INACTIVE_ENDPOINT_STATUS = "inactive"
    PAUSED_ENDPOINT_STATUS = "paused"

    def __str__(self) -> str:
        return str(self.value)
