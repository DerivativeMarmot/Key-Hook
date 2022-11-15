from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from orm_base import Base


class Room(Base):
    __tablename__ = "rooms"
    building_name = Column(String(200), ForeignKey('buildings.name'), primary_key=True, nullable=False)
    # building_name = Column(String(200), ForeignKey('buildings.name'), nullable=False)
    room_number = Column('room_number', Integer, primary_key=True, nullable=False)

    building = relationship("Building", back_populates="rooms_list")
    door = relationship('Door', back_populates='room')

    employees_list = relationship('RoomRequest', back_populates='room')

    def __init__(self, building, room_number):
        self.room_number = room_number
        self.building = building
        self.building_name = building.name

        self.employees_list = []

