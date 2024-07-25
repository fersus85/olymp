import json
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def load_competitors_from_json(path: str) -> dict[str, dict[str, str]]:
    '''
    Функция для чтения из json файла.
    :param path: str путь к файлу
    :return: список словарей с данными
    '''
    logger.info('Open file with competitors')
    try:
        with open(path, 'r', encoding='utf-8') as file:
            competitors = json.load(file)
        return competitors
    except FileNotFoundError as ex:
        logger.error(f'Error {ex}')
    except json.JSONDecodeError as ex:
        logger.error(f'Error decoding JSON from file: {path} - {ex}')
    except IOError as ex:
        logger.error(f'Error i/a {ex}')


def load_results_from_txt(path: str) -> dict[int, dict[str, datetime]]:
    '''
    Функция для чтения из txt файла.
    :param path: str путь к файлу
    :return: словарь с данными по каждому спортсмену
    '''
    logger.info('Open file with results')
    results = {}
    try:
        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file:
                number, flag, time = line.strip().split()
                number = int(number)
                if flag == 'start':
                    start_time = datetime.strptime(time, "%H:%M:%S,%f")
                    results.setdefault(number, {}).update(start=start_time)
                elif flag == 'finish':
                    fin_time = datetime.strptime(time, "%H:%M:%S,%f")
                    results.setdefault(number, {}).update(finish=fin_time)
        return results
    except FileNotFoundError as ex:
        logger.error(f'Error {ex}')
    except ValueError as ex:
        logger.error(f'Error parsing line in file: {path} - {ex}')
    except IOError as ex:
        logger.error(f'Error i/a {ex}')
