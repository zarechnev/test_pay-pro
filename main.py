def main():
    import os
    import shutil
    from app.main_alg import main_alg
    from app.db import session_fabric, Users

    session = session_fabric()
    users = session.query(Users).filter_by(contract_received=1)

    if os.path.exists("./out/"):
        shutil.rmtree("./out/", )

    os.mkdir("./out/")

    for user in users:
        main_alg(user)


if __name__ == '__main__':
    main()
