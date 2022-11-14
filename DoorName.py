from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from orm_base import Base


class DoorName(Base):
    __tablename__ = "door_names"
    name = Column("name", String(100), nullable=False, primary_key=True)

    # door = relationship('Door', back_populates='door_name')

    def __init__(self, name):
        self.name = name
