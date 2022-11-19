from sqlalchemy import Column, String, Integer, ForeignKey, Identity, DateTime, func, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Key import Key
from KeyIssueReturn import KeyIssueReturn
from KeyIssueLoss import KeyIssueLoss


class KeyIssue(Base):
    __tablename__ = 'key_issue'
    issue_number = Column('issue_number', Integer,  Identity(start=1, cycle=True), nullable=False, primary_key=True) # self-generate
    request_id = Column('request_id', Integer, ForeignKey('room_requests.request_id'), nullable=False)
    hook_number = Column('hook_number', Integer, nullable=False)
    key_number = Column('key_number',Integer, nullable=False)
    start_time = Column('start_time', DateTime(timezone=True),nullable=False) # self-generate

    __table_args__ = (ForeignKeyConstraint((hook_number, key_number),
                                           [Key.hook_number, Key.key_number]),{})

    room_request = relationship('RoomRequest', back_populates='keys_list')
    key = relationship('Key', back_populates='room_requests_list')

    key_issue_loss = relationship('KeyIssueLoss', back_populates='key_issue', cascade="all,delete")
    key_issue_return = relationship('KeyIssueReturn', back_populates='key_issue', cascade="all,delete")

    def __init__(self, room_request, key) -> None:
        self.request_id = room_request.request_id
        self.hook_number = key.hook_number
        self.key_number = key.key_number
        self.room_request = room_request
        self.key = key
        self.start_time = func.now()

    def return_key(self):
        # make sure the key isn't already loss / returned
        if len(self.key_issue_loss) + len(self.key_issue_return) > 0:
            return
        key_return = KeyIssueReturn(self)
        self.key_issue_return.append(key_return)
        return key_return

    def loss_key(self):
        # make sure the key isn't already loss / returned
        # if len(self.key_issue_loss) + len(self.key_issue_return) > 0:
        #     return
        key_loss = KeyIssueLoss(self)
        self.key_issue_loss.append(key_loss)
        return key_loss
