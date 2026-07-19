from enum import Enum


class GetSubscriptionsDirection(str, Enum):
    NEXT = "next"
    PREV = "prev"

    def __str__(self) -> str:
        return str(self.value)
