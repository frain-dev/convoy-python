from enum import Enum


class DatastorePortalAuthType(str, Enum):
    REFRESH_TOKEN = "refresh_token"
    STATIC_TOKEN = "static_token"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
