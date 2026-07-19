from enum import Enum


class ConfigRequestIDHeaderProvider(str, Enum):
    DEFAULT_REQUEST_ID_HEADER = "X-Convoy-Idempotency-Key"

    def __str__(self) -> str:
        return str(self.value)
