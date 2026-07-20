from enum import Enum


class DatastoreDeviceStatus(str, Enum):
    DISABLED = "disabled"
    OFFLINE = "offline"
    ONLINE = "online"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
