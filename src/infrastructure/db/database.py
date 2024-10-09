from typing import AsyncGenerator, Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL, DB_CONNECTOR

Base = declarative_base()


class DatabaseFactory:
    """
    Factory to create synchronous or asynchronous engine and session for psycopg2 and asyncpg connectors.
    """
    @staticmethod
    def create_engine_and_session():
        if DB_CONNECTOR == "psycopg2":
            # Creating synchronous engine and session for psycopg2
            sync_engine = create_engine(DATABASE_URL, echo=False)
            SyncSessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=sync_engine,
            )

            def get_db() -> Generator:
                db = SyncSessionLocal()
                try:
                    yield db
                finally:
                    db.close()

            return SyncSessionLocal, get_db, sync_engine

        elif DB_CONNECTOR == "asyncpg":
            # Creating asynchronous engine and session for asyncpg
            async_engine = create_async_engine(DATABASE_URL, echo=False)
            AsyncSessionLocal = async_sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=async_engine,
                class_=AsyncSession,
                expire_on_commit=False,
            )

            async def get_db() -> AsyncGenerator:
                async with AsyncSessionLocal() as session:
                    yield session

            return AsyncSessionLocal, get_db, async_engine

        else:
            raise ValueError(f"Unsupported DB_CONNECTOR: {DB_CONNECTOR}")


# Creating instances based on DB_CONNECTOR
SessionLocal, get_db, engine = DatabaseFactory.create_engine_and_session()
