from enum import Enum


class DatastoreSourceType(str, Enum):
    DB_CHANGE_STREAM = "db_change_stream"
    HTTP = "http"
    PUB_SUB = "pub_sub"
    REST_API = "rest_api"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
