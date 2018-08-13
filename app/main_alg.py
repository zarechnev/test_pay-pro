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


def _2_3(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    commissions = session.query(Payments.c.commission).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    commissions = commissions.all()

    credit_commissions = session.query(Payments.c.credit_commission).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    credit_commissions = credit_commissions.all()

    ans = 0

    for commission in commissions:
        ans += float(commission.commission)

    for credit_commission in credit_commissions:
        # TODO: ХАК,разобраться как сделать красиво
        add = (float(0) if credit_commission.credit_commission == None else float(credit_commission.credit_commission))
        ans += add

    return str(round(ans, 2))


def _2_3_2(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    commissions = session.query(Payments.c.commission).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0, Payments.c.is_credit == 1).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    commissions = commissions.all()

    credit_commissions = session.query(Payments.c.credit_commission).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0, Payments.c.is_credit == 1 ).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    credit_commissions = credit_commissions.all()

    ans = 0

    for commission in commissions:
        ans += float(commission.commission)

    for credit_commission in credit_commissions:
        # TODO: ХАК,разобраться как сделать красиво
        add = (float(0) if credit_commission.credit_commission == None else float(credit_commission.credit_commission))
        ans += add

    return str(round(ans, 2))


def _2_3_1(user, date_start, date_end) -> str:
    session = session_fabric()

    persons = session.query(Person.c.person_id).\
        filter(Person.c.user_id == user.user_id)

    commissions = session.query(Payments.c.commission).\
        filter(Payments.c.person_id.in_(persons), Payments.c.status_id == 0, Payments.c.is_credit == 0).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    commissions = commissions.all()

    ans = 0

    for commission in commissions:
        ans += float(commission.commission)

    return str(round(ans, 2))


def _2_2_1(user, date_start, date_end) -> str:
    return "0"


def _2_2(user, date_start, date_end) -> str:
    return "0"


def _2_2_1(user, date_start, date_end) -> str:
    return "0"


def _2_2_2(user, date_start, date_end) -> str:
    return "0"


def _3_1_2(user, date_start, date_end) -> str:
    return "0"


def _3_2_1(user, date_start, date_end) -> str:
    return _2_1(user, date_start, date_end)


def _3_2_2(user, date_start, date_end) -> str:
    return _2_3(user, date_start, date_end)


def _3_2_3(user, date_start, date_end) -> str:
    session = session_fabric()

    amounts = session.query(User_tr_log.c.amount).\
        filter(User_tr_log.c.user_id == user.user_id).\
        filter(User_tr_log.c.type == 2).\
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    amounts = amounts.all()

    ans = 0

    for amount in amounts:
        ans += float(amount.amount)

    return str(round(ans, 2))


def _3_1_1(user, date_start, date_end) -> str:
    session = session_fabric()

    amounts = session.query(User_tr_log.c.amount).\
        filter(User_tr_log.c.user_id == user.user_id).\
        filter(User_tr_log.c.type == 1). \
        filter(User_tr_log.c['from'].in_([1, 8])). \
        filter(Payments.c.date_create >= date_start).\
        filter(Payments.c.date_create <= date_end)

    amounts = amounts.all()

    ans = 0

    for amount in amounts:
        ans += float(amount.amount)

    return str(round(ans, 2))


def _3_2(user, date_start, date_end) -> str:
    return str(float(_3_2_1(user, date_start, date_end)) +
               float(_3_2_2(user, date_start, date_end)) +
               float(_3_2_3(user, date_start, date_end)))


def _3_1(user, date_start, date_end) -> str:
    return str(float(_3_1_1(user, date_start, date_end)) +
               float(_3_1_2(user, date_start, date_end)))


def _4_1(user, date_start, date_end) -> str:
    return str(float(_1_1(user, date_start, date_end)) +
               float(_3_1(user, date_start, date_end)) -
               float(_3_2(user, date_start, date_end)))


def _1_1(user, date_start, date_end) -> str:
    return "0"


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
        file.write("1.1.\tОстаток гарантийного фонда\t\t\t\t\t\t= " + _1_1(user, date_start, date_end) + "\n")
        file.write("2.\t\tВ Отчетном периоде\n")
        file.write("2.1.\tПринято платежей\t\t\t\t\t\t\t\t= " + _2_1(user, date_start, date_end) + "\n")
        file.write("2.1.1\tпо предоплатной схеме\t\t\t\t\t\t\t= " + _2_1_1(user, date_start, date_end) + "\n")
        file.write("2.1.2\tпо постоплатной схеме\t\t\t\t\t\t\t= " + _2_1_2(user, date_start, date_end) + "\n")
        file.write("2.2.\tНачислено вознаграждений ПС за приём платежей\t= " + _2_2(user, date_start, date_end) + "\n")
        file.write("2.2.1.\tпо предоплатной схеме\t\t\t\t\t\t\t= " + _2_2_1(user, date_start, date_end) + "\n")
        file.write("2.2.2.\tпо постоплатной схеме\t\t\t\t\t\t\t= " + _2_2_2(user, date_start, date_end) + "\n")
        file.write("2.3.\tНачислено вознаграждений ОПП за приём плитежей\t= " + _2_3(user, date_start, date_end) + "\n")
        file.write("2.3.1.\tпо предоплатной схеме\t\t\t\t\t\t\t= " + _2_3_1(user, date_start, date_end) + "\n")
        file.write("2.3.2.\tпо постоплатной схеме\t\t\t\t\t\t\t= " + _2_3_2(user, date_start, date_end) + "\n")
        file.write("3.\t\tГарантийный фонд\n")
        file.write("3.1.\tУвеличение гарантийного фонда\t\t\t\t\t= " + _3_1(user, date_start, date_end) + "\n")
        file.write("3.1.1.\tавансовые платежи\t\t\t\t\t\t\t\t= " + _3_1_1(user, date_start, date_end) + "\n")
        file.write("3.1.2.\tзачисленное вознаграждение\t\t\t\t\t\t= " + _3_1_2(user, date_start, date_end) + "\n")
        file.write("3.2.\tУменьшение гарантийного фонда\t\t\t\t\t= " + _3_2(user, date_start, date_end) + "\n")
        file.write("3.2.3.\tперевод на сервисный счёт\t\t\t\t\t\t= " + _3_2_3(user, date_start, date_end) + "\n")
        file.write("4.\t\tНа конец отчётного периода\n")
        file.write("4.1.\tОстаток гарантийного фонда\t\t\t\t\t\t= " + _4_1(user, date_start, date_end) + "\n")

    return True
