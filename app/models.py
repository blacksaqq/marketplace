from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, text

from app.database import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nickname: Mapped[str] = mapped_column(String(32), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(
        String,
        nullable=False,
        server_default=text(
            "CASE WHEN NOT EXISTS (SELECT 1 FROM users) THEN 'admin' ELSE 'buyer' END"
        ),
    )