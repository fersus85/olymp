import logging
from datetime import timedelta, datetime


logger = logging.getLogger(__name__)


def calculate_durations(
        results: dict[int, dict[str, datetime]]) -> dict[int, timedelta]:
    '''
    Функция для вычисления времени прохождения дистанции.
    :param results: dict словарь с результатами спортсменов
    :return: словарь с номером спортсмена и временем прохождения дистанции
    '''
    logger.info('Calculate durations')
    durations = {}
    try:
        for number, times in results.items():
            if 'start' not in times or 'finish' not in times:
                logger.warning(f'Missing start or finish time{number}')
                continue
            duration = times['finish'] - times['start']
            durations[number] = duration
    except KeyError as ex:
        logger.error(f'Error {ex}')
    return durations


def generate_output(competitors: dict[str, dict[str, str]],
                    durations: dict[int, timedelta]) -> list[dict[str, str]]:
    '''
    Функция для генерации выходных данных.
    :param competitors: dict словарь с номером и фио спортсмена
    :param durations: dict словарь с номером и результатом спортсмена
    :return: отсортированный список словарей с финальными данными
    '''
    logger.info('Generate output')
    output = []
    for number, fio in competitors.items():
        try:
            number = int(number.strip('\ufeff'))
        except ValueError as ex:
            logger.warning(f'Error converting number {number} to int: {ex}')
            continue

        try:
            result_time = str(durations[number])
        except KeyError as ex:
            logger.warning(f'Result time not found for competitor: {ex}')
            continue

        try:
            output.append({
                'number': number,
                'name': fio['Name'],
                'surname': fio['Surname'],
                'result': result_time
            })
        except KeyError as ex:
            logger.warning(f'Key missing in competitor data for number {ex}')
    output.sort(key=lambda x: x['result'])
    return output
