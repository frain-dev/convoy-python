from enum import Enum


class GetEventDeliveriesPagedDirection(str, Enum):
    NEXT = "next"
    PREV = "prev"

    def __str__(self) -> str:
        return str(self.value)
