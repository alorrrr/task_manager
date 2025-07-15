from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from schemas.users import UserRolesEnum
from sqlalchemy import String, Integer


class User(Base):
    """
    Model for users.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRolesEnum] = mapped_column(default=UserRolesEnum.user)

    tasks: Mapped[list["Task"]] = relationship(  # noqa: F821 # type: ignore
        "Task",
        back_populates="assignee",
    )
    projects: Mapped[list["ProjectMembership"]] = relationship(  # noqa: F821 # type: ignore
        "ProjectMembership",
        back_populates="user",
        cascade="all, delete-orphan",
    )
