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
    parser.add_argument('-s', '--start', default=get_fist_day_of_current_month())
    parser.add_argument('-e', '--end', default=datetime.datetime.now())

    return parser


def main():
    import os
    import sys
    import shutil
    from concurrent.futures import ProcessPoolExecutor
    from app.main_alg import main_alg
    from app.db import session_fabric, Users

    parser = parser_fabric()
    namespace = parser.parse_args(sys.argv[1:])
    date_start, date_end = namespace.start, namespace.end

    session = session_fabric()
    users = session.query(Users).filter_by(contract_received=1)

    if os.path.exists("./out/"):
        shutil.rmtree("./out/", )

    os.mkdir("./out/")

    with ProcessPoolExecutor() as executor:
        for user in users:
            executor.submit(main_alg, user, date_start, date_end)


if __name__ == '__main__':
    main()
