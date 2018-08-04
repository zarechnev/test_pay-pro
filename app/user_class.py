from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    company = Column(String)
    director = Column(String)
    contract_received = Column(Boolean)

    def __init__(self):
        pass

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.user_id, self.company, self.contract_received)
