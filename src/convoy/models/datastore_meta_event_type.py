from enum import Enum


class DatastoreMetaEventType(str, Enum):
    HTTP_META_EVENT = "http"
    PUB_SUB_META_EVENT = "pub_sub"

    def __str__(self) -> str:
        return str(self.value)
