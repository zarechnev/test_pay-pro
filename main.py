def main():
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from app.user_class import User


    engine = create_engine("mysql+pymysql://paypro:paypro@localhost/paypro?charset=utf8mb4")
    Session = sessionmaker(bind=engine)

    session = Session()

    #myuser = session.query(User).filter(contract_received=1)
    users = session.query(User).all()

    for user in users:
        print(user)


if __name__ == '__main__':
    main()
