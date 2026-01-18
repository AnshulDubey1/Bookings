from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text,func,DateTime,Integer
from datetime import datetime

class Stations(Base):
    __tablename__="stations"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
    station_name:Mapped[str]=mapped_column(Text,nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())