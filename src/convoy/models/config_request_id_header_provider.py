from enum import Enum


class ConfigRequestIDHeaderProvider(str, Enum):
    VALUE_1 = ""
    X_CONVOY_IDEMPOTENCY_KEY = "X-Convoy-Idempotency-Key"

    def __str__(self) -> str:
        return str(self.value)
