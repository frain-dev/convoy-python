from enum import Enum


class AuthRoleType(str, Enum):
    API = "api"
    BILLING_ADMIN = "billing_admin"
    INSTANCE_ADMIN = "instance_admin"
    ORGANISATION_ADMIN = "organisation_admin"
    PROJECT_ADMIN = "project_admin"
    PROJECT_VIEWER = "project_viewer"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
