import json
import logging

from config import ROOT_DIR

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(ROOT_DIR + "/logs/read_products_file.log")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_products(path: str) -> list:
    """
    Функция чтения данные json с данными по products и category
    :param path: Путь до файла
    :return: Лист
    """
    if len(path) > 0:
        try:
            with open(path, mode="r", encoding="utf-8") as f:
                data = json.load(f)
            return list(data)
        except FileNotFoundError:
            logger.error("Файл не найден!")
            raise FileNotFoundError("Файл не найден!")
        except Exception as err:
            logger.error(f"Ошибка выполнения функции чтения файла -> {err}")
            raise Exception(f"Ошибка выполнения функции чтения файла -> {err}")
    return []
