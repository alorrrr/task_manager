from enum import StrEnum


class UserRolesEnum(StrEnum):
    """
    Enum for user roles in the system.
    """

    user = "user"
    manager = "manager"
    admin = "admin"
