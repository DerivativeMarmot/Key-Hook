from sqlalchemy import Column, String, Integer, ForeignKey, Identity, DateTime, func, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Key import Key

class KeyIssue(Base):
    __tablename__ = 'key_issues'
    issue_id = Column('issue_id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True) # self-generate
    request_id = Column('request_id', Integer, ForeignKey('room_requests.request_id'), nullable=False)
    hook_number = Column('hook_number', Integer, nullable=False)
    # hook_number = Column('hook_number', Integer, ForeignKey('keys.hook_number'), nullable=False)
    key_number = Column('key_number', Integer, nullable=False)
    # key_number = Column('key_number', Integer, ForeignKey('keys.key_number'), nullable=False)
    start_time = Column('start_time', DateTime(timezone=True), default=func.now(), nullable=False) # self-generate

    __table_args__ = (ForeignKeyConstraint((hook_number, key_number),
                                           [Key.hook_number, Key.key_number]),{})

    room_request = relationship('RoomRequest', back_populates='keys_list')
    key = relationship('Key', back_populates='room_requests_list')

    # key_issue_loss = relationship('KeyIssueLoss', back_populates='key_issue')
    # key_issue_return = relationship('KeyIssueReturn', back_populates='key_issue')


    def __init__(self, room_request, key) -> None:
        self.request_id = room_request.request_id
        self.hook_number = key.hook_number
        self.key_number = key.key_number
        
        self.room_request = room_request
        self.key = key