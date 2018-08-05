def main():
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from app.user_class import User
    from app.main_alg import main_alg


    engine = create_engine("mysql+pymysql://paypro:paypro@localhost/paypro?charset=utf8mb4")
    Session = sessionmaker(bind=engine)

    session = Session()

    users = session.query(User).filter_by(contract_received=1)

    for user in users:
        main_alg(user)


if __name__ == '__main__':
    main()
