from enum import Enum


class DatastoreDeliveryMode(str, Enum):
    AT_LEAST_ONCE_DELIVERY_MODE = "at_least_once"
    AT_MOST_ONCE_DELIVERY_MODE = "at_most_once"

    def __str__(self) -> str:
        return str(self.value)
