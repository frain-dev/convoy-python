from enum import Enum


class DatastoreEncodingType(str, Enum):
    BASE64 = "base64"
    HEX = "hex"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
