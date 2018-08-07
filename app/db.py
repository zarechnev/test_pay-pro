import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from app.db_connect_conf import connect_string


meta = sa.MetaData()
engine = sa.create_engine(connect_string)
session_fabric = sessionmaker(bind=engine)

Users = sa.Table('users', meta, autoload=True, autoload_with=engine)
Payments = sa.Table('payments', meta, autoload=True, autoload_with=engine)
User_tr_log = sa.Table('user_transfer_log', meta, autoload=True, autoload_with=engine)
