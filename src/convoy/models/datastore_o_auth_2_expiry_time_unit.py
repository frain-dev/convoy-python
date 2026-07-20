from enum import Enum


class DatastoreOAuth2ExpiryTimeUnit(str, Enum):
    HOURS = "hours"
    MILLISECONDS = "milliseconds"
    MINUTES = "minutes"
    SECONDS = "seconds"
    VALUE_4 = ""

    def __str__(self) -> str:
        return str(self.value)
