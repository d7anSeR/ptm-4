import json
import logging
import hashlib
from typing import List

"""
В этом модуле обитают функции, необходимые для автоматизированной проверки результатов ваших трудов.
"""


def calculate_checksum(row_numbers: List[int]) -> str:
    """
    Вычисляет md5 хеш от списка целочисленных значений.

    ВНИМАНИЕ, ВАЖНО! Чтобы сумма получилась корректной, считать, что первая строка с данными csv-файла имеет номер 0
    Другими словами: В исходном csv 1я строка - заголовки столбцов, 2я и остальные - данные.
    Соответственно, считаем что у 2 строки файла номер 0, у 3й - номер 1 и так далее.

    Надеюсь, я расписал это максимально подробно.
    Хотя что-то мне подсказывает, что обязательно найдется человек, у которого с этим возникнут проблемы.
    Которому я отвечу, что все написано в докстринге ¯\_(ツ)_/¯

    :param row_numbers: список целочисленных номеров строк csv-файла, на которых были найдены ошибки валидации
    :return: md5 хеш для проверки через github action
    """
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        row_numbers.sort()
        result_str = hashlib.md5(json.dumps(row_numbers).encode('utf-8')).hexdigest()
        logging.info("calculate_checksum: success\n")
        return result_str
    except Exception as e:
        logging.error(
            f"calculate_checksum: there was an error when calculating a hash from a list of integer values: {str(e)}")
        raise Exception("error")


def serialize_result(variant: int, checksum: str) -> None:
    """
    Метод для сериализации результатов лабораторной пишите сами.
    Вам нужно заполнить данными - номером варианта и контрольной суммой - файл, лежащий в корне репозитория.
    Файл называется, очевидно, result.json.

    ВНИМАНИЕ, ВАЖНО! На json натравлен github action, который проверяет корректность выполнения лабораторной.
    Так что не перемещайте, не переименовывайте и не изменяйте его структуру, если планируете успешно сдать лабу.

    :param variant: номер вашего варианта
    :param checksum: контрольная сумма, вычисленная через calculate_checksum()
    """
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        pass
        result = {"variant": str(variant), "checksum": checksum}
        with open("result.json", 'w') as file_name:
            json.dump(result, file_name, indent=3)
        logging.info("serialize_result: success\n")
    except Exception as e:
        logging.error(
            f"serialize_result: there was an error when serializing results: {str(e)}")
        raise Exception("error")
