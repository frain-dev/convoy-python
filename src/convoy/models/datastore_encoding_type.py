from enum import Enum


class DatastoreEncodingType(str, Enum):
    BASE_64_ENCODING = "base64"
    HEX_ENCODING = "hex"

    def __str__(self) -> str:
        return str(self.value)
