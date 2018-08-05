from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Payments(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    is_credit = Column(Boolean)
    status_id = Column(Boolean)

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.user_id, self.company, self.contract_received)
