from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from .engine import Session

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = Session()
    try:
        yield session

    finally:
        await session.close()