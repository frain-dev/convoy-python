from enum import Enum


class DatastoreEndpointStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PAUSED = "paused"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
