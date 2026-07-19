from enum import Enum


class ConfigSignatureHeaderProvider(str, Enum):
    DEFAULT_SIGNATURE_HEADER = "X-Convoy-Signature"

    def __str__(self) -> str:
        return str(self.value)
