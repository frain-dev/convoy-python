from enum import Enum


class DatastoreStrategyProvider(str, Enum):
    EXPONENTIAL = "exponential"
    LINEAR = "linear"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
