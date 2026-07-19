from enum import Enum


class GetEndpointsDirection(str, Enum):
    NEXT = "next"
    PREV = "prev"

    def __str__(self) -> str:
        return str(self.value)
