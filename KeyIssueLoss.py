from sqlalchemy import Column, String, Integer, Identity, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from orm_base import Base

class KeyIssueLoss(Base):
    __tablename__ = "key_issue_losses"
    issue_number = Column('issue_number', Integer, ForeignKey('key_issues.issue_number'), 
                            nullable=False, primary_key=True)
    loss_date = Column('start_time', DateTime(timezone=True), default=func.now(), nullable=False) # self-generate

    key_issue = relationship('KeyIssue', back_populates='key_issue_loss')
