from enum import Enum


class DatastoreOAuth2AuthenticationType(str, Enum):
    CLIENT_ASSERTION_AUTH = "client_assertion"
    SHARED_SECRET_AUTH = "shared_secret"

    def __str__(self) -> str:
        return str(self.value)
