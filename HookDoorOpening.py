from sqlalchemy import Column, String, Integer, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Door import Door


class HookDoorOpening(Base):
    __tablename__ = 'hook_door_opening'
    hook_number = Column(Integer, ForeignKey('hooks.hook_number'), primary_key=True)
    building_name = Column(String(200), primary_key=True)
    room_number = Column(Integer, primary_key=True)
    door_name = Column(String(100), primary_key=True)

    hook = relationship("Hook", back_populates='doors_list')
    door = relationship('Door', back_populates='hooks_list')

    __table_args__ = (ForeignKeyConstraint((building_name, room_number, door_name),
                                           [Door.building_name, Door.room_number, Door.door_name]),
                      {})

    def __init__(self, hook, door):
        self.hook_number = hook.hook_number
        self.door_name = door.door_name
        self.room_number = door.room_number
        self.building_name = door.building_name
