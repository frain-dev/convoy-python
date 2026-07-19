from enum import Enum


class DatastoreSubscriptionType(str, Enum):
    SUBSCRIPTION_TYPE_API = "api"
    SUBSCRIPTION_TYPE_CLI = "cli"

    def __str__(self) -> str:
        return str(self.value)
