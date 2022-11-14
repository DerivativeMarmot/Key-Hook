from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from orm_base import Base


class Key(Base):
    __tablename__ = "keys"
    hook_number = Column(Integer, ForeignKey('hooks.hook_number'), primary_key=True, nullable=False)
    # key_number = Column('key_number', Integer, primary_key=True, nullable=False)
    key_number = Column('key_number', Integer, Identity(start=1, cycle=True), primary_key=True, nullable=False)

    hook = relationship("Hook", back_populates="keys_list")

    room_requests_list = relationship('KeyIssue', back_populates='key')

    def __init__(self, hook):
        self.hook = hook
        self.hook_number = hook.hook_number
        # self.key_number = key_number

        self.room_requests_list = []
