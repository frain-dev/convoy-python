from enum import Enum


class DatastoreEndpointAuthenticationType(str, Enum):
    API_KEY_AUTHENTICATION = "api_key"
    BASIC_AUTHENTICATION = "basic_auth"
    O_AUTH_2_AUTHENTICATION = "oauth2"

    def __str__(self) -> str:
        return str(self.value)
