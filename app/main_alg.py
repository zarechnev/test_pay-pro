from app.db import session_fabric, Users, Payments, User_tr_log, Person


def generate_file_name(user) -> float:
    """
    Генерирует имя файла, заменяя пробелы и двойные пробелы на "_".
    :param user:
    :return:
    """
    file_name = "out/" + str(user.user_id) + "_" + str(user.company) + ".txt"
    file_name = file_name.replace('  ', ' ')
    file_name = file_name.replace(' ', '_')

    return file_name


def _2_1_1(user, date_start, date_end, session) -> str:
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

    return ans


def _2_1_2(user, date_start, date_end, session) -> float:
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

    return ans


def _2_1(user, date_start, date_end, session) -> float:
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

    return ans


def _2_3(user, date_start, date_end, session) -> float:
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

    return round(ans, 2)


def _2_3_2(user, date_start, date_end, session) -> float:
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

    return round(ans, 2)


def _2_3_1(user, date_start, date_end, session) -> float:
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

    return round(ans, 2)


def _3_2_3(user, date_start, date_end, session) -> float:
    amounts = session.query(User_tr_log.c.amount).\
        filter(User_tr_log.c.user_id == user.user_id).\
        filter(User_tr_log.c.type == 2).\
        filter(User_tr_log.c.date >= date_start).\
        filter(User_tr_log.c.date <= date_end)

    amounts = amounts.all()

    ans = 0

    for amount in amounts:
        ans += float(amount.amount)

    return round(ans, 2)


def _3_1_1(user, date_start, date_end, session) -> float:
    amounts = session.query(User_tr_log.c.amount).\
        filter(User_tr_log.c.user_id == user.user_id).\
        filter(User_tr_log.c.type == 1). \
        filter(User_tr_log.c["from"].in_([1, 8])). \
        filter(User_tr_log.c.date >= date_start).\
        filter(User_tr_log.c.date <= date_end)

    amounts = amounts.all()

    ans = 0

    for amount in amounts:
        ans += float(amount.amount)

    return round(ans, 2)


def main_alg(user, date_start, date_end) -> bool:
    """
    Функция реализующая основной алгоритм программы.
    :param user:
    :param date_start:
    :param date_end:
    :return:
    """
    session = session_fabric()

    p_1_1 = 0
    p_2_1_1 = _2_1_1(user, date_start, date_end, session)
    p_2_1_2 = _2_1_2(user, date_start, date_end, session)
    p_2_1 = _2_1(user, date_start, date_end, session)
    p_2_2 = 0
    p_2_2_1 = 0
    p_2_2_2 = 0
    p_2_3 = _2_3(user, date_start, date_end, session)
    p_2_3_1 = _2_3_1(user, date_start, date_end, session)
    p_2_3_2 = _2_3_2(user, date_start, date_end, session)
    p_3_1_1 = _3_1_1(user, date_start, date_end, session)
    p_3_1_2 = 0
    p_3_1 = p_3_1_1 + p_3_1_2
    p_3_2_1 = p_2_1
    p_3_2_2 = p_2_3
    p_3_2_3 = _3_2_3(user, date_start, date_end, session)
    p_3_2 = round(float(p_3_2_1) + float(p_3_2_2) + float(p_3_2_3), 2)
    p_4_1 = round(p_1_1 + p_3_1 - p_3_2, 2)

    session.close()

    with open(generate_file_name(user), 'w') as file:
        file.write("Клиент: " + user.company + " (" + user.director +")\n\n")
        file.write("За период с " + date_start.strftime("%d.%m.%Y") + " по " + date_end.strftime("%d.%m.%Y") + "\n\n")
        file.write("1.1.\tОстаток гарантийного фонда\t\t\t\t\t\t= "             + str(p_1_1)    + "\n")
        file.write("2.\t\tВ Отчетном периоде\n")
        file.write("2.1.\tПринято платежей\t\t\t\t\t\t\t\t= "                   + str(p_2_1)    + "\n")
        file.write("2.1.1\tпо предоплатной схеме\t\t\t\t\t\t\t= "               + str(p_2_1_1)  + "\n")
        file.write("2.1.2\tпо постоплатной схеме\t\t\t\t\t\t\t= "               + str(p_2_1_2)  + "\n")
        file.write("2.2.\tНачислено вознаграждений ПС за приём платежей\t= "    + str(p_2_2)    + "\n")
        file.write("2.2.1.\tпо предоплатной схеме\t\t\t\t\t\t\t= "              + str(p_2_2_1)  + "\n")
        file.write("2.2.2.\tпо постоплатной схеме\t\t\t\t\t\t\t= "              + str(p_2_2_2)  + "\n")
        file.write("2.3.\tНачислено вознаграждений ОПП за приём плитежей\t= "   + str(p_2_3)    + "\n")
        file.write("2.3.1.\tпо предоплатной схеме\t\t\t\t\t\t\t= "              + str(p_2_3_1)  + "\n")
        file.write("2.3.2.\tпо постоплатной схеме\t\t\t\t\t\t\t= "              + str(p_2_3_2)  + "\n")
        file.write("3.\t\tГарантийный фонд\n")
        file.write("3.1.\tУвеличение гарантийного фонда\t\t\t\t\t= "            + str(p_3_1)    + "\n")
        file.write("3.1.1.\tавансовые платежи\t\t\t\t\t\t\t\t= "                + str(p_3_1_1)  + "\n")
        file.write("3.1.2.\tзачисленное вознаграждение\t\t\t\t\t\t= "           + str(p_3_1_2)  + "\n")
        file.write("3.2.\tУменьшение гарантийного фонда\t\t\t\t\t= "            + str(p_3_2)    + "\n")
        file.write("3.2.1\tпринято платежей\t\t\t\t\t\t\t\t= "                  + str(p_3_2_1)  + "\n")
        file.write("3.2.2\tкомиссия ОПП\t\t\t\t\t\t\t\t\t= "                    + str(p_3_2_2)  + "\n")
        file.write("3.2.3.\tперевод на сервисный счёт\t\t\t\t\t\t= "            + str(p_3_2_3)  + "\n")
        file.write("4.\t\tНа конец отчётного периода\n")
        file.write("4.1.\tОстаток гарантийного фонда\t\t\t\t\t\t= "             + str(p_4_1)    + "\n")

    return True
