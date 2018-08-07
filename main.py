def main():
    import sys
    import os
    import shutil
    import sqlalchemy as sa
    from sqlalchemy.orm import sessionmaker
    from app.main_alg import main_alg
    from app.db_connect_conf import connect_string


    meta = sa.MetaData()
    engine = sa.create_engine(connect_string)

    Users = sa.Table('users', meta, autoload=True, autoload_with=engine)
    Payments = sa.Table('payments', meta, autoload=True, autoload_with=engine)
    User_tr_log = sa.Table('user_transfer_log', meta, autoload=True, autoload_with=engine)


    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(Users).filter_by(contract_received=1)
    pays = session.query(Payments).count()
    logs = session.query(User_tr_log).count()

    if os.path.exists("./out/"):
        shutil.rmtree("./out/", )
        os.mkdir("./out/")

    print(logs)


if __name__ == '__main__':
    main()
