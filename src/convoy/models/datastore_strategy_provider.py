from enum import Enum


class DatastoreStrategyProvider(str, Enum):
    EXPONENTIAL_STRATEGY_PROVIDER = "exponential"
    LINEAR_STRATEGY_PROVIDER = "linear"

    def __str__(self) -> str:
        return str(self.value)
