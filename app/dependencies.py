from fastapi import Depends, HTTPException, status
from fastapi.security import  OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated
from sqlalchemy.orm import selectinload, joinedload

from app.database import async_session
from app.security import decode_access_token
from sqlalchemy import select
from app.config import settings



async def get_db():
    async with async_session() as session:
        yield session

dbSession = Annotated[AsyncSession, Depends(get_db)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

