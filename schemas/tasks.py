from enum import StrEnum


class TasksStatusesEnum(StrEnum):
    """
    Enum for tasks statuses.
    """

    new = "new"
    in_progress = "in_progress"
    done = "done"
