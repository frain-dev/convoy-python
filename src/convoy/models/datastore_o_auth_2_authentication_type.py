from enum import Enum


class DatastoreOAuth2AuthenticationType(str, Enum):
    CLIENT_ASSERTION = "client_assertion"
    SHARED_SECRET = "shared_secret"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
