from enum import Enum


class DatastoreSourceProvider(str, Enum):
    GITHUB = "github"
    SHOPIFY = "shopify"
    TWITTER = "twitter"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
