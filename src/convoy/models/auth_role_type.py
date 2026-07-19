from enum import Enum


class AuthRoleType(str, Enum):
    ROLE_API = "api"
    ROLE_BILLING_ADMIN = "billing_admin"
    ROLE_INSTANCE_ADMIN = "instance_admin"
    ROLE_ORGANISATION_ADMIN = "organisation_admin"
    ROLE_PROJECT_ADMIN = "project_admin"
    ROLE_PROJECT_VIEWER = "project_viewer"

    def __str__(self) -> str:
        return str(self.value)
