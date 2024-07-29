import json
import logging

from .utils import format_timedelta
from .models import ResultDict
from datetime import timedelta


logger = logging.getLogger(__name__)


def display_output(data: list[ResultDict]) -> None:
    """
    Функция для отображения на экране результатов соревнований
    """
    print(
        f"| {'Занятое место':^15} | {'Нагрудный номер':^15} | "
        f"{'Имя':^15} | {'Фамилия':^15} | {'Результат':^15} |"
    )
    print("-" * 91)
    for i, result in enumerate(data, start=1):
        try:
            if isinstance(result["result"], timedelta):
                formatted_time = format_timedelta(result['result'])
                result_str = (
                    f"| {i:^15} | {result['number']:^15} | "
                    f"{result['name']:^15} | "
                    f"{result['surname']:^15} | "
                    f"{formatted_time:^15} |"
                )
                print(result_str)
        except KeyError as ex:
            logger.exception(
                "Key missing trying parse data for displaying: %s", ex)
            continue


def save_results_in_json(results: list[ResultDict], path: str) -> None:
    """
    Функция сохраняет результаты соревнований в json файл
    :param results: список с итоговыми данными
    :param path: str путь для сохранения файла
    """
    logger.info("Save output in file")
    save_dict = {}
    for i, result in enumerate(results, start=1):
        try:
            if isinstance(result["result"], timedelta):
                formatted_time = format_timedelta(result["result"])
                save_dict[str(i)] = {
                    "Нагрудный номер": str(result["number"]),
                    "Имя": result["surname"],
                    "Фамилия": result["name"],
                    "Результат": formatted_time,
                }
        except KeyError as ex:
            logger.warning("Key does not exist: %s", ex)
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(save_dict, file, ensure_ascii=False, indent=4)
    except FileExistsError as ex:
        logger.exception("File already exist: %s", ex)
    except IOError as ex:
        logger.exception("Error i/a: %s", ex)
