from app.infrastructure.database.base import Base
from sqlalchemy import DateTime, Integer,TEXT,func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Train(Base):
    __tablename__="trains"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    train_name:Mapped[str]=mapped_column(TEXT,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())