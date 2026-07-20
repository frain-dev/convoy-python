from enum import Enum


class DatastoreProjectType(str, Enum):
    INCOMING = "incoming"
    OUTGOING = "outgoing"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
