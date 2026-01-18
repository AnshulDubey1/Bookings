from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey,Integer
class CarriageTypes(Base):
    __tablename__="carriage_types"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
    class_id=mapped_column(ForeignKey("classes.id"),nullable=False)