from enum import Enum


class ConfigSignatureHeaderProvider(str, Enum):
    VALUE_1 = ""
    X_CONVOY_SIGNATURE = "X-Convoy-Signature"

    def __str__(self) -> str:
        return str(self.value)
