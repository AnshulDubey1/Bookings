from app.infrastructure.database.base import Base
from sqlalchemy import DateTime, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class TrainStation(Base):
    __tablename__="train_stations"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    train_id:Mapped[int]=mapped_column(ForeignKey("trains.id"),nullable=False)
    stations_id:Mapped[int]=mapped_column(ForeignKey("stations.id"),nullable=False)
    stop_order:Mapped[int]=mapped_column(Integer,nullable=False)
    arrival_time:Mapped[datetime]=mapped_column(DateTime)
    departure_time:Mapped[datetime]=mapped_column(DateTime)