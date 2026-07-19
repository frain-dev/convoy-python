from enum import Enum


class DatastorePortalAuthType(str, Enum):
    PORTAL_AUTH_TYPE_REFRESH_TOKEN = "refresh_token"
    PORTAL_AUTH_TYPE_STATIC_TOKEN = "static_token"

    def __str__(self) -> str:
        return str(self.value)
