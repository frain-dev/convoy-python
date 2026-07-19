from enum import Enum


class GetEventsPagedDirection(str, Enum):
    NEXT = "next"
    PREV = "prev"

    def __str__(self) -> str:
        return str(self.value)
