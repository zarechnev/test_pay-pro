from app.db import session_fabric, Users, Payments, User_tr_log


def generate_file_name(user) -> str:
    """
    Генерирует имя файла, заменяя пробелы и двойные пробелы на "_".
    :param user:
    :return:
    """
    file_name = "out/" + str(user.user_id) + "_" + str(user.company) + ".txt"
    file_name = file_name.replace('  ', ' ')
    file_name = file_name.replace(' ', '_')

    return file_name


def _2_1_1(user) -> str:
    session = session_fabric()
    payments = session.query(Payments.c.amount).filter(Payments.c.is_credit==0, Payments.c.status_id==0)
    ans = 0
    for pay in payments:
        ans += pay.amount
    return str(ans)


def _2_1_2(user) -> str:
    session = session_fabric()
    payments = session.query(Payments.c.amount).filter(Payments.c.is_credit==1, Payments.c.status_id==0)
    ans = 0
    for pay in payments:
        ans += pay.amount
    return str(ans)


def _2_1(user) -> str:
    return str(float(_2_1_1(user)) + float(_2_1_2(user)))


def main_alg(user, date_start, date_end) -> bool:
    """
    Функция реализующая основной алгоритм программы.
    :param user:
    :param date_start:
    :param date_end:
    :return:
    """

    with open(generate_file_name(user), 'w') as file:
        file.write("1.1.\tОстаток гарантийного фонда\t= 0.\n")
        file.write("2.\t\tВ Отчетном периоде.\n")
        file.write("2.1.\tПринято платежей\t\t\t= " + _2_1(user) + "\n")
        file.write("2.1.1\tпо предоплатной схеме\t\t\t= " + _2_1_1(user) + "\n")
        file.write("2.1.2\tпо постоплатной схеме\t\t\t= " + _2_1_2(user) + "\n")

    return True
