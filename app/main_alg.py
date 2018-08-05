from .user_class import User
import os


def generate_file_name(user: User) -> str:
    """
    Генерирует имя файла, заменяя пробелы и двойные пробелы на "_".
    :param user:
    :return:
    """
    file_name = "out/" + str(user.user_id) + "_" + str(user.company) + ".txt"
    file_name = file_name.replace('  ', ' ')
    file_name = file_name.replace(' ', '_')

    return file_name


def main_alg(user: User) -> bool:
    """
    Функция реализующая основной алгоритм программы.
    :param user:
    :return:
    """
    print(user)

    with open(generate_file_name(user), 'w') as file:
        pass

    return True
