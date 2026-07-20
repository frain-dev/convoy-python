from enum import Enum


class DatastoreDeliveryMode(str, Enum):
    AT_LEAST_ONCE = "at_least_once"
    AT_MOST_ONCE = "at_most_once"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
