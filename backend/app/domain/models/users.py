from app.infrastructure.database.base import Base
from sqlalchemy import String, Integer,Text,DateTime,func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    first_name:Mapped[str]=mapped_column(String(100),nullable=False)
    last_name:Mapped[str]=mapped_column(String(100),nullable=False)
    email:Mapped[str]=mapped_column(Text,nullable=False)
    password_hash:Mapped[str]=mapped_column(Text,nullable=False,unique=True)
    address:Mapped[str|None]=mapped_column(Text)
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())