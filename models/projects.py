from typing import Optional
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer

from schemas.users import UserRolesEnum


class Project(Base):
    """
    Model for projects.
    """

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))

    tasks: Mapped[list["Task"]] = relationship(  # noqa: F821 # type: ignore
        "Task",
        back_populates="project",
        cascade="all, delete-orphan",
    )
    users: Mapped[list["ProjectMembership"]] = relationship(
        "ProjectMembership",
        back_populates="project",
        cascade="all, delete-orphan",
    )


class ProjectMembership(Base):
    """
    Model, realising many-to-many relationship between projects and users.
    Includes their role in the exact project.
    """

    __tablename__ = "project_memberships"

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role: Mapped[UserRolesEnum] = mapped_column(default=UserRolesEnum.user)

    user: Mapped["User"] = relationship(  # noqa: F821 # type: ignore
        "User",
        back_populates="projects",
    )
    project: Mapped["Project"] = relationship(
        "Project",
        back_populates="users",
    )
