from app.infrastructure.database.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Text,Integer

class Quota(Base):
    __tablename__="quota"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,nullable=False)
    quota_name:Mapped[str]=mapped_column(Text,nullable=False)