from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,ForeignKey

class CarriageQuota(Base):
    __tablename__="carriage_quota"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    carriage_type_id:Mapped[int]=mapped_column(ForeignKey("carriage_types.id"),nullable=False)
    quota_id:Mapped[int]=mapped_column(ForeignKey("quota.id"),nullable=False)
    seat_count:Mapped[int]=mapped_column(Integer,nullable=False)