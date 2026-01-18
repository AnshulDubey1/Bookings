from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey,Text,DateTime,func
from datetime import datetime

class Bookings(Base):
    __tablename__="bookings"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False,autoincrement=True)
    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),nullable=False)
    train_id:Mapped[int]=mapped_column(ForeignKey("trains.id"),nullable=False)
    departure_train_stations_id:Mapped[int]=mapped_column(ForeignKey("train_stations.id"),nullable=False)
    arrival_train_stations_id:Mapped[int]=mapped_column(ForeignKey("train_stations.id"),nullable=False)
    class_id:Mapped[int]=mapped_column(ForeignKey("classes.id"),nullable=False)
    booking_status:Mapped[str]=mapped_column(Text,nullable=False)
    booked_at:Mapped[datetime]=mapped_column(DateTime,server_default=func.now())    