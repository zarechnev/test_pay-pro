def main():
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from app.user_class import User
    from app.main_alg import main_alg
    from app.db_connect_conf import connect_string
    import sys
    import os


    engine = create_engine(connect_string)
    Session = sessionmaker(bind=engine)

    session = Session()

    users = session.query(User).filter_by(contract_received=1)

    if not os.path.exists("./out/"):
        os.mkdir("./out/")

    try:
        for user in users:
            main_alg(user)
    except Exception as e:
        print("ERROR!!! Exit with:", e)
        sys.exit(1)


if __name__ == '__main__':
    main()
