from infrastructure.database.base import Base
from sqlalchemy import String, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class TrainCarriage(Base):
    __tablename__="train_carriages"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
    train_id:Mapped[int]=mapped_column(ForeignKey("trains.id"),nullable=False)
    carriage_type_id:Mapped[int]=mapped_column(ForeignKey("carriage_types.id"),nullable=False)
    carriage_label:Mapped[str]=mapped_column(String(10),nullable=False)  
    carriage_order:Mapped[int]=mapped_column(Integer,nullable=False)