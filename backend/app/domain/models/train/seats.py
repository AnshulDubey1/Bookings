from app.infrastructure.database.base import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Seats(Base):
    __tablename__="seats"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    train_carriages_id:Mapped[int]=mapped_column(ForeignKey("train_carriages.id"))
    seat_number:Mapped[str]=mapped_column(String(50))