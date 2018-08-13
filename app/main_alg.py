from app.db import session_fabric, Users, Payments, User_tr_log, Person


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


def _2_1_1(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    payments = session.query(Payments.c.amount).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0, Payments.c.is_credit == 0).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    payments = payments.all()

    ans = 0

    for pay in payments:
        ans += pay.amount

    return str(ans)


def _2_1_2(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    payments = session.query(Payments.c.amount).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0, Payments.c.is_credit == 1).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    payments = payments.all()

    ans = 0

    for pay in payments:
        ans += pay.amount

    return str(ans)


def _2_1(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    payments = session.query(Payments.c.amount).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    payments = payments.all()

    ans = 0

    for pay in payments:
        ans += pay.amount

    return str(ans)


def _2_3(user) -> str:
    session = session_fabric()

    payments = session.query(Payments.c.amount).filter(Payments.c.status_id == 0)
    ans = 0
    for pay in payments:
        ans += pay.amount
    return str(ans)


def main_alg(user, date_start, date_end) -> bool:
    """
    Функция реализующая основной алгоритм программы.
    :param user:
    :param date_start:
    :param date_end:
    :return:
    """

    with open(generate_file_name(user), 'w') as file:
        file.write("Клиент: " + user.company + " (" + user.director +")\n\n")
        file.write("За период с " + date_start.strftime("%d.%m.%Y") + " по " + date_end.strftime("%d.%m.%Y") + "\n\n")
        file.write("1.1.\tОстаток гарантийного фонда\t\t= 0\n")
        file.write("2.\t\tВ Отчетном периоде\n")
        file.write("2.1.\tПринято платежей\t\t\t\t= " + _2_1(user, date_start, date_end) + "\n")
        file.write("2.1.1\tпо предоплатной схеме\t\t\t= " + _2_1_1(user, date_start, date_end) + "\n")
        file.write("2.1.2\tпо постоплатной схеме\t\t\t= " + _2_1_2(user, date_start, date_end) + "\n")
        file.write("2.2.\tНачислено вознаграждений ПС за приём платежей\t= 0\n")
        file.write("2.2.1.\tпо предоплатной схеме\t\t\t= 0\n")
        file.write("2.2.2.\tпо постоплатной схеме\t\t\t= 0\n")
        file.write("2.3.\tНачислено вознаграждений ОПП за приём плитежей\t\t= " + _2_3(user) + "\n")

    return True
