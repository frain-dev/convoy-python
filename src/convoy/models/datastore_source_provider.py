from enum import Enum


class DatastoreSourceProvider(str, Enum):
    GITHUB_SOURCE_PROVIDER = "github"
    SHOPIFY_SOURCE_PROVIDER = "shopify"
    TWITTER_SOURCE_PROVIDER = "twitter"

    def __str__(self) -> str:
        return str(self.value)
