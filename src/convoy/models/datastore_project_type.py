from enum import Enum


class DatastoreProjectType(str, Enum):
    INCOMING_PROJECT = "incoming"
    OUTGOING_PROJECT = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
