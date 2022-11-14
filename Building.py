from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint
from sqlalchemy.orm import relationship

from orm_base import Base
from Room import Room


class Building(Base):
    __tablename__ = "buildings"
    name = Column('name', String(200), nullable=False, primary_key=True)

    rooms_list = relationship("Room", back_populates="building", viewonly=False)

    def __init__(self, name):
        self.name = name

    # todo needs fix
    def add_room(self, room_number):
        # for room in self.rooms_list:
        #     if room.room_number == room_number:
        #         return
        room_to_add = Room(self, room_number)
        self.rooms_list.append(room_to_add)
