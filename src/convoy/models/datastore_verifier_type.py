from enum import Enum


class DatastoreVerifierType(str, Enum):
    API_KEY_VERIFIER = "api_key"
    BASIC_AUTH_VERIFIER = "basic_auth"
    H_MAC_VERIFIER = "hmac"
    NOOP_VERIFIER = "noop"

    def __str__(self) -> str:
        return str(self.value)
