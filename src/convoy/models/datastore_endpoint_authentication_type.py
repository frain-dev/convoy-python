from enum import Enum


class DatastoreEndpointAuthenticationType(str, Enum):
    API_KEY = "api_key"
    BASIC_AUTH = "basic_auth"
    OAUTH2 = "oauth2"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
