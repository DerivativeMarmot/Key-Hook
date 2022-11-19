from sqlalchemy import Column, String, Integer, Identity
from sqlalchemy.orm import relationship
from orm_base import Base
from RoomRequest import RoomRequest

class Employee(Base):
    __tablename__ = "employees"
    id = Column('id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True) # self-generate
    full_name = Column('full_name', String(200), nullable=False)

    rooms_list = relationship('RoomRequest', back_populates='employee', viewonly=False, cascade="all,delete")


    def __init__(self, full_name: String) -> None:
        self.full_name = full_name
        self.rooms_list = []
    
    def request_room(self, room):
        if room in self.rooms_list:
            return
        
        room_request = RoomRequest(self, room)
        room.employees_list.append(room_request)
        self.rooms_list.append(room_request)
        return room_request
    
    def __str__(self) -> str:
        return 'id: ' + str(self.id) + ' ' + 'name: ' + self.full_name
