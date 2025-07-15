from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from schemas.users import UserRolesEnum
from sqlalchemy import String


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRolesEnum] = mapped_column(default=UserRolesEnum.user)
