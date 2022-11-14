from sqlalchemy import Column, String, Integer, ForeignKey, Identity, DateTime, func, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from KeyIssue import KeyIssue
from Room import Room

class RoomRequest(Base):
    __tablename__ = 'room_requests'
    request_id = Column('request_id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True) # self-generate
    request_time = Column('request_time', DateTime(timezone=True), default=func.now(), nullable=False)
    employee_id = Column('employee_id', Integer, ForeignKey('employees.id'), nullable=False)
    building_name = Column('building_name', String(200), nullable=False)
    room_number = Column('room_number', Integer, nullable=False)
    # building_name = Column('building_name', String(200), ForeignKey('rooms.building_name'), nullable=False)
    # room_number = Column('room_number', Integer, ForeignKey('rooms.room_number'), nullable=False)

    employee = relationship('Employee', back_populates='rooms_list')
    room = relationship('Room', back_populates='employees_list')

    keys_list = relationship('KeyIssue', back_populates='room_request', viewonly=False)

    __table_args__ = (ForeignKeyConstraint((building_name, room_number),
                                           [Room.building_name, Room.room_number]),
                      {})


    def __init__(self, employee, room) -> None:
        self.section_id = employee.id
        # self.building_name = room.building_name
        self.room_number = room.room_number

        self.employee = employee
        self.room = room
        self.keys_list = []
    
    def issue_key(self, key):
        if key in self.keys_list:
            return
        
        key_issue = KeyIssue(self, key)
        print('key number shism', key.key_number)
        key.room_requests_list.append(key_issue)
        self.keys_list.append(key_issue)
        return key_issue