from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text,Integer

class Classes(Base):
    __tablename__="classes"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
    class_name:Mapped[str]=mapped_column(Text,nullable=False)