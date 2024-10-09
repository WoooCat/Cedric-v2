from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError


@asynccontextmanager
async def transaction_context(db: AsyncSession):
    try:
        yield db
        await db.commit()
    except SQLAlchemyError as e:
        await db.rollback()
        raise e
