from enum import Enum


class DatastoreMetaEventType(str, Enum):
    HTTP = "http"
    PUB_SUB = "pub_sub"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
