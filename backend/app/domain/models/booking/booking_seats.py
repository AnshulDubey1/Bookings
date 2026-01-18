from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,ForeignKey

class BookingSeats(Base):
    __tablename__="booking_seats"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,nullable=False,autoincrement=True)
    booking_id:Mapped[int]=mapped_column(ForeignKey("bookings.id"),nullable=False)
    seat_id:Mapped[int]=mapped_column(ForeignKey("seats.id"),nullable=False)