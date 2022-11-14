from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from Room import Room
from Key import Key


class Door(Base):
    __tablename__ = 'doors'
    building_name = Column(String(200), primary_key=True)
    room_number = Column(Integer, primary_key=True)
    door_name = Column(String(100), ForeignKey('door_names.name'), primary_key=True, nullable=False)

    room = relationship("Room", back_populates='door')
    # door_name = relationship('DoorName', back_populates='door')

    hooks_list = relationship('HookDoorOpening', back_populates='door')

    __table_args__ = (ForeignKeyConstraint((building_name, room_number),
                                           [Room.building_name, Room.room_number]),
                      {})

    # def __init__(self, room):
    def __init__(self, room, door_name):
        self.door_name = door_name.name
        self.room_number = room.room_number
        self.room = room
        self.building_name = room.building_name

        self.hooks_list=[]
