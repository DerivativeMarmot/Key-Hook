from sqlalchemy import Column, String, Integer, Identity, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from orm_base import Base


class KeyIssueLoss(Base):
    __tablename__ = "key_issue_loss"
    issue_number = Column('issue_number', Integer, ForeignKey('key_issue.issue_number'), 
                            nullable=False, primary_key=True)
    loss_date = Column('loss_date', DateTime(timezone=True), nullable=False) # self-generate

    key_issue = relationship('KeyIssue', back_populates='key_issue_loss', cascade="all,delete")

    def __init__(self, key_issue, loss_date=func.now()):
        self.issue_number = key_issue.issue_number
        self.key_issue = key_issue
        self.loss_date = loss_date
