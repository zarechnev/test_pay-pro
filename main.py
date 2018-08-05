def main():
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from app.user_class import User
    from app.main_alg import main_alg
    from app.db_connect_conf import connect_string


    engine = create_engine(connect_string)
    Session = sessionmaker(bind=engine)

    session = Session()

    users = session.query(User).filter_by(contract_received=1)

    for user in users:
        main_alg(user)


if __name__ == '__main__':
    main()
