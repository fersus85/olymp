import logging
from datetime import timedelta, datetime

from .models import ResultDict

logger = logging.getLogger(__name__)


def calculate_durations(
    results: dict[int, dict[str, datetime]]
) -> dict[int, timedelta]:
    """
    Функция для вычисления времени прохождения дистанции.
    :param results: dict словарь с результатами спортсменов
    :return: словарь с номером спортсмена и временем прохождения дистанции
    """
    logger.info("Calculate durations")
    durations = {}
    try:
        for number, times in results.items():
            if "start" not in times or "finish" not in times:
                logger.warning("Missing start or finish time: %s", number)
                continue
            duration = times["finish"] - times["start"]
            durations[number] = duration
    except KeyError as ex:
        logger.exception("KeyError while calculate duration: %s", ex)
    return durations


def generate_output(
    competitors: dict[str, dict[str, str]], durations: dict[int, timedelta]
) -> list[ResultDict]:
    """
    Функция для генерации выходных данных.
    :param competitors: dict словарь с номером и фио спортсмена
    :param durations: dict словарь с номером и результатом спортсмена
    :return: отсортированный список словарей с финальными данными
    """
    logger.info("Generate output")
    output: list[ResultDict] = []
    for number, fio in competitors.items():
        try:
            number = number.strip("\ufeff")
        except ValueError as ex:
            logger.warning("Error converting number %s to int: %s", number, ex)
            continue

        try:
            result_time = durations[int(number)]
        except KeyError as ex:
            logger.warning("Result time not found for competitor: %s", ex)
            continue

        try:
            output.append(
                {
                    "number": number,
                    "name": fio["Name"],
                    "surname": fio["Surname"],
                    "result": result_time,
                }
            )
        except KeyError as ex:
            logger.warning("Key missing in competitor data for number: %s", ex)
    output.sort(key=lambda x: x["result"])
    return output
