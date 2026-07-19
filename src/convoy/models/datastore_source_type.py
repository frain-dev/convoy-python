from enum import Enum


class DatastoreSourceType(str, Enum):
    DB_CHANGE_STREAM = "db_change_stream"
    HTTP_SOURCE = "http"
    PUB_SUB_SOURCE = "pub_sub"
    REST_API_SOURCE = "rest_api"

    def __str__(self) -> str:
        return str(self.value)
