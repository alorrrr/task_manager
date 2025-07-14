from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from config import settings


DATABASE_URL = settings.get_db_url()

engine = create_async_engine(url=DATABASE_URL)

session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


async def get_session():
    async with session_maker() as session:
        yield session
