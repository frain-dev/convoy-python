from enum import Enum


class DatastoreSubscriptionType(str, Enum):
    API = "api"
    CLI = "cli"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
