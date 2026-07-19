from enum import Enum


class DatastoreOAuth2ExpiryTimeUnit(str, Enum):
    EXPIRY_TIME_UNIT_HOURS = "hours"
    EXPIRY_TIME_UNIT_MILLISECONDS = "milliseconds"
    EXPIRY_TIME_UNIT_MINUTES = "minutes"
    EXPIRY_TIME_UNIT_SECONDS = "seconds"

    def __str__(self) -> str:
        return str(self.value)
