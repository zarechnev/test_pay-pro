def get_fist_day_of_current_month():
    """
    Возвращает первый день месяца в формате dateTime.
    :return:
    """
    import datetime

    today_date = datetime.date.today()
    if today_date.day > 25:
        today_date += datetime.timedelta(7)

    return today_date.replace(day=1)


def parser_fabric():
    """
    Парсер получает параметры дат начала и конца требуемого отчётного периода.
    :return:
    """
    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', default=datetime.datetime.strftime(get_fist_day_of_current_month(), "%d.%m.%Y"))
    parser.add_argument('-e', '--end', default=datetime.datetime.strftime(datetime.datetime.now(), "%d.%m.%Y"))

    return parser


def main():
    import os
    import sys
    import shutil
    from multiprocessing import cpu_count
    from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
    from datetime import datetime
    from app.main_alg import main_alg
    from app.db import session_fabric, Users

    parser = parser_fabric()
    namespace = parser.parse_args(sys.argv[1:])
    date_start, date_end = datetime.strptime(namespace.start, "%d.%m.%Y"), datetime.strptime(namespace.end, "%d.%m.%Y")

    session = session_fabric()
    # users = session.query(Users).filter_by(contract_received=1).limit(4)

    users = session.query(Users).filter(Users.c.user_id == 113)

    if os.path.exists("./out/"):
        shutil.rmtree("./out/", )

    os.mkdir("./out/")

    if cpu_count() < 4:
        executor = ThreadPoolExecutor(max_workers=4)
    else:
        executor = ProcessPoolExecutor()

    with executor:
        for user in users:
            executor.submit(main_alg, user, date_start, date_end)


if __name__ == '__main__':
    main()
