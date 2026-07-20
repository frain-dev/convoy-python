from enum import Enum


class DatastoreVerifierType(str, Enum):
    API_KEY = "api_key"
    BASIC_AUTH = "basic_auth"
    HMAC = "hmac"
    NOOP = "noop"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
