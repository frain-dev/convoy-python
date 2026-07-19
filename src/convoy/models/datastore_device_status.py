from enum import Enum


class DatastoreDeviceStatus(str, Enum):
    DEVICE_STATUS_DISABLED = "disabled"
    DEVICE_STATUS_OFFLINE = "offline"
    DEVICE_STATUS_ONLINE = "online"

    def __str__(self) -> str:
        return str(self.value)
