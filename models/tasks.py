from core.database import Base
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from schemas.tasks import TasksStatusesEnum
from typing import Optional


class Task(Base):
    """
    Model for tasks.
    """

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[TasksStatusesEnum] = mapped_column(default=TasksStatusesEnum.new)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    assignee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    project: Mapped["Project"] = relationship(  # noqa: F821 # type: ignore
        "Project",
        back_populates="tasks",
    )
    assignee: Mapped["User"] = relationship(  # noqa: F821 # type: ignore
        "User",
        back_populates="tasks",
    )
